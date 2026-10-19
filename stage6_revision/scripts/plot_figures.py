#!/usr/bin/env python3
"""Reproduce six provisional audit figures from the frozen stage-2 JSON files.

Run from any directory: python stage6_revision/scripts/plot_figures.py
No raw workbook or report1 file is modified. No statistical model is fitted.
The JSON source paths are retained alongside each plotting value in CSV files.
"""
from __future__ import annotations

import csv
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.environ.setdefault("MPLCONFIGDIR", "/tmp/hocl-stage2-mplconfig")
os.environ.setdefault("XDG_CACHE_HOME", "/tmp/hocl-stage2-cache")

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch
import numpy as np


DATA = ROOT / "data"
FIGURES = ROOT / "figures"
FIGURES.mkdir(parents=True, exist_ok=True)
COMPLEXES = json.loads((DATA / "complexes.json").read_text(encoding="utf-8"))
PAIRS = json.loads((DATA / "pairs.json").read_text(encoding="utf-8"))
PROVENANCE = json.loads((DATA / "provenance.json").read_text(encoding="utf-8"))
BY_SYSTEM = {r["system"]: r for r in COMPLEXES}
PROV = {(r["system"], r["metric"]): r for r in PROVENANCE}
H_COLOR, CL_COLOR = "#2474AA", "#D67B24"
RED, TEXT, GRID = "#A74448", "#263543", "#E5E9EC"
H_CANDIDATES = {"H-CAACmeSPh2", "H-NHCme", "H-NHCmeSPh2"}
CL_CANDIDATES = {"Cl-NHCme"}
CANDIDATES = H_CANDIDATES | CL_CANDIDATES
EDA_METRICS = ["ES", "EX", "REP", "POL", "ECORR"]
EDA_COLORS = ["#75A8CD", "#8E7BAD", "#BEC3C8", "#76B2A3", "#E5AA6F"]
EXPORTS = []

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 10,
    "axes.titlesize": 12,
    "axes.labelsize": 10,
    "axes.labelcolor": TEXT,
    "text.color": TEXT,
    "xtick.color": TEXT,
    "ytick.color": TEXT,
    "axes.edgecolor": "#798691",
    "axes.spines.right": False,
    "axes.spines.top": False,
    "svg.fonttype": "none",
    "pdf.fonttype": 42,
    "savefig.facecolor": "white",
})


def write_csv(name, records):
    keys = list(dict.fromkeys(k for r in records for k in r))
    with (DATA / name).open("w", encoding="utf-8-sig", newline="") as out:
        writer = csv.DictWriter(out, fieldnames=keys)
        writer.writeheader()
        writer.writerows(records)


def subset_record(row, metrics):
    result = {k: row[k] for k in ("system", "legacy_id", "ligand", "end")}
    for metric in metrics:
        result[metric] = row[metric]
        result[metric + "_source"] = row.get(metric + "_src", "derived; see component sources")
    return result


def prov_source(system, metric):
    r = PROV.get((system, metric))
    return "" if r is None else f"{r['file']}::{r['sheet']}!{r['cell']}"


def clean(ax, xgrid=True, ygrid=False):
    ax.set_axisbelow(True)
    if xgrid:
        ax.grid(axis="x", color=GRID, linewidth=0.7)
    if ygrid:
        ax.grid(axis="y", color=GRID, linewidth=0.7)
    ax.tick_params(length=3)


def foot(fig, lines, x=0.04, y=0.025):
    fig.text(x, y, "\n".join(lines), ha="left", va="bottom", fontsize=8.2,
             linespacing=1.45, color="#586773")


def save(fig, stem):
    for ext in ("png", "svg", "pdf"):
        fig.savefig(FIGURES / f"{stem}.{ext}", dpi=300)
    EXPORTS.append({"figure": stem, "width_inches": float(fig.get_figwidth()),
                    "height_inches": float(fig.get_figheight()),
                    "png_dpi": 300, "formats": "PNG/SVG/PDF"})
    plt.close(fig)


def end_legend(candidate=True, candidate_label="strong-interaction candidate"):
    handles = [Line2D([], [], color=H_COLOR, marker="o", linestyle="none", label="H-end"),
               Line2D([], [], color=CL_COLOR, marker="o", linestyle="none", label="Cl-end")]
    if candidate:
        handles.append(Line2D([], [], color=TEXT, marker="D", linestyle="none",
                              label=candidate_label))
    return handles


def set_pair_axis(ax, labels=False):
    ax.set_ylim(len(PAIRS) - 0.4, -0.7)
    ax.set_yticks(np.arange(len(PAIRS)))
    if labels:
        ax.set_yticklabels([f"{r['legacy_id']:>3}  {r['ligand']}" for r in PAIRS], fontsize=9)
    else:
        ax.tick_params(axis="y", labelleft=False)


def figure1():
    rows = []
    for p in PAIRS:
        r = dict(p)
        for end in ("H", "Cl"):
            src = BY_SYSTEM[f"{end}-{p['ligand']}"]
            for metric in ("Eb_bess", "Eint_bess"):
                r[f"{end}_{metric}_source"] = src[metric + "_src"]
        rows.append(r)
    write_csv("figure_F1_energy_competition.csv", rows)
    fig, axes = plt.subplots(1, 3, figsize=(15, 11.6), sharey=True,
                             gridspec_kw={"width_ratios": [1.35, 1, 1.1]})
    fig.subplots_adjust(left=.183, right=.975, bottom=.12, top=.86, wspace=.13)
    fig.suptitle("Fig. 2  H-end / Cl-end energy comparison", y=.98, fontsize=16, weight="bold")
    fig.text(.183, .934, "Provisional data audit | 28 matched pairs | 9 ordering reversals highlighted",
             fontsize=10, color=RED)
    for i, p in enumerate(PAIRS):
        if p["ranking_reversal"]:
            for ax in axes:
                ax.axhspan(i - .43, i + .43, color="#F8EDEE", zorder=0)
        axes[0].plot([p["H_Eb"], p["Cl_Eb"]], [i, i], color="#A6ADB3", lw=1.4, zorder=2)
        for end, color in (("H", H_COLOR), ("Cl", CL_COLOR)):
            marker = "D" if f"{end}-{p['ligand']}" in CANDIDATES else "o"
            axes[0].scatter(p[f"{end}_Eb"], i, s=37, marker=marker,
                            color=color, edgecolors="white", linewidths=.45, zorder=3)
        for ax, key in zip(axes[1:], ("delta_Eb_H_minus_Cl", "delta_Eint_H_minus_Cl")):
            val = p[key]
            ax.hlines(i, 0, val, color=H_COLOR if val < 0 else CL_COLOR, lw=1.25)
            ax.scatter(val, i, s=34, marker="D" if p["ranking_reversal"] else "o",
                       color=H_COLOR if val < 0 else CL_COLOR, zorder=3,
                       edgecolors=RED if p["ranking_reversal"] else "white", linewidth=.7)
    titles = ["(a) Workbook $E_b$", "(b) $\\Delta E_b$ = H $-$ Cl", "(c) $\\Delta E_{int}$ = H $-$ Cl"]
    for ax, title in zip(axes, titles):
        set_pair_axis(ax, ax is axes[0])
        clean(ax)
        ax.axvline(0, color="#606F7B", lw=.8)
        ax.set_title(title, pad=12)
    axes[0].set_xlim(-25.5, 2)
    axes[0].set_xlabel("Workbook $E_b$ (kcal mol$^{-1}$)")
    axes[1].set_xscale("symlog", linthresh=1, linscale=1)
    axes[1].set_xlim(-16, 4)
    axes[1].set_xticks([-10, -2, -1, 0, 1, 3])
    axes[1].set_xticklabels(["−10", "−2", "−1", "0", "1", "3"])
    axes[2].set_xscale("symlog", linthresh=1, linscale=1)
    axes[2].set_xlim(-110, 13)
    axes[2].set_xticks([-100, -10, -1, 0, 1, 10])
    axes[2].set_xticklabels(["−100", "−10", "−1", "0", "1", "10"])
    for ax in axes[1:]:
        ax.set_xlabel("H $-$ Cl (kcal mol$^{-1}$)\nsymlog; linear within $\\pm$1")
    fig.legend(handles=end_legend(candidate_label="candidate (panel a)") + [Patch(facecolor="#F8EDEE", label="ordering reversal")],
               loc="upper left", bbox_to_anchor=(.176, .928), ncol=4, frameon=False, fontsize=9)
    foot(fig, ["Negative differences indicate a lower H-end tabulated value; positive differences indicate a lower Cl-end value.",
               "Energy reference states, BSSE/ZPE treatment and cross-configuration computational comparability remain unverified.",
               "Highlighted reversals compare numerical ordering only; they do not establish thermodynamic preference."])
    save(fig, "F1_energy_competition")


def figure2():
    metrics = ["r_OH", "r_OCl", "dr_OH_recalc", "dr_OCl_recalc"]
    write_csv("figure_F2_internal_bond_response.csv", [
        dict(subset_record(r, metrics), selected_change="dr_OH_recalc" if r["end"] == "H" else "dr_OCl_recalc",
             candidate=r["system"] in CANDIDATES, unit_status="source unit not specified")
        for r in COMPLEXES])
    fig, axes = plt.subplots(1, 3, figsize=(15, 11.6), sharey=True,
                             gridspec_kw={"width_ratios": [1, 1, 1.1]})
    fig.subplots_adjust(left=.183, right=.975, bottom=.13, top=.86, wspace=.15)
    fig.suptitle("Fig. 1  Internal-bond response to complex formation", y=.98, fontsize=16, weight="bold")
    fig.text(.183, .944, "Provisional data audit | distances retain the workbook's unspecified source unit", color=RED)
    for i, p in enumerate(PAIRS):
        h, cl = (BY_SYSTEM[f"{e}-{p['ligand']}"] for e in ("H", "Cl"))
        for ax, r, key, color in [(axes[0], h, "dr_OH_recalc", H_COLOR),
                                  (axes[1], h, "dr_OH_recalc", H_COLOR),
                                  (axes[2], cl, "dr_OCl_recalc", CL_COLOR)]:
            candidate = r["system"] in CANDIDATES
            if ax is axes[1] and candidate:
                ax.text(.174, i, "in panel (a)", ha="right", va="center", fontsize=7.4, color="#929BA2")
                continue
            val = r[key]
            ax.hlines(i, 0, val, color=color, alpha=.55, lw=1.2)
            ax.scatter(val, i, s=49 if candidate else 31, marker="D" if candidate else "o",
                       color=color, edgecolors=RED if candidate else "white", linewidths=.8, zorder=3)
            if candidate:
                ax.annotate(f" {val:.3f}", (val, i), xytext=(5, 0), textcoords="offset points",
                            va="center", fontsize=8.1, color=RED)
    for ax, title in zip(axes, ["(a) H-end: $\\Delta r$(O–H), all 28", "(b) H-end: 25 other systems (zoom)",
                                "(c) Cl-end: $\\Delta r$(O–Cl), all 28"]):
        set_pair_axis(ax, ax is axes[0])
        clean(ax)
        ax.axvline(0, color="#606F7B", lw=.8)
        ax.set_title(title, fontsize=10.5, pad=14)
        ax.set_xlabel("Distance change\n(source unit; not specified)")
    axes[0].set_xlim(-.025, .96)
    axes[1].set_xlim(-.006, .18)
    axes[2].set_xlim(-.012, .415)
    fig.legend(handles=end_legend(), loc="upper left", bbox_to_anchor=(.176, .932),
               frameon=False, ncol=3, fontsize=9)
    foot(fig, ["Changes are recalculated relative to the isolated HOCl entries in Structure data!E59 (O–H) and F59 (O–Cl).",
               "Panel (b) magnifies the 25 H-end systems outside the three highlighted H-end candidates; no points are silently discarded.",
               "Geometry alone does not demonstrate proton transfer, chlorine transfer, or a specific bond category."])
    save(fig, "F2_bond_response")


def figure3():
    chosen = ["CO", "N2CAACme", "PPh3", "NHCme", "CAACmeSPh2"]
    selected = [BY_SYSTEM[f"{end}-{lig}"] for lig in chosen for end in ("H", "Cl")]
    write_csv("figure_F3_EDA_components.csv", [
        dict(subset_record(r, EDA_METRICS + ["EDA_E"]),
             sum_five=r["EDA_sum5"], total_minus_sum=r["EDA_sum_residual"],
             unit_status="kcal/mol explicit only in ES header; common component unit assumed pending verification")
        for r in selected])
    fig, axes_grid = plt.subplots(2, 3, figsize=(15, 9.3))
    axes = axes_grid.ravel()
    fig.subplots_adjust(left=.075, right=.975, bottom=.15, top=.865, wspace=.28, hspace=.43)
    fig.suptitle("Fig. 3  Five-component EDA: stabilization and cancellation", y=.98,
                 fontsize=16, weight="bold")
    fig.text(.075, .93, "Provisional data audit | five reported terms retained | each panel has its own y-scale",
             color=RED, fontsize=10)
    for i, lig in enumerate(chosen):
        ax = axes[i]
        pos, neg = np.zeros(2), np.zeros(2)
        records = [BY_SYSTEM[f"{end}-{lig}"] for end in ("H", "Cl")]
        for metric, color in zip(EDA_METRICS, EDA_COLORS):
            vals = np.array([r[metric] for r in records])
            bottoms = np.where(vals >= 0, pos, neg)
            ax.bar([0, 1], vals, bottom=bottoms, color=color, width=.53,
                   edgecolor="white", linewidth=.6)
            pos += np.maximum(vals, 0)
            neg += np.minimum(vals, 0)
            if metric == "ECORR":
                for j, val in enumerate(vals):
                    if val > 0:
                        ax.text(j, bottoms[j] + val / 2, f"+{val:.2f}", ha="center", va="center",
                                fontsize=8, weight="bold")
        for j, r in enumerate(records):
            ax.scatter(j, r["EDA_E"], marker="D", s=37, color=TEXT,
                       edgecolors="white", linewidths=.5, zorder=5)
            ax.annotate(f" {r['EDA_E']:.2f}", (j, r["EDA_E"]), xytext=(12, 0),
                        textcoords="offset points", fontsize=8.5, va="center", weight="bold")
        ax.axhline(0, color="#65717A", lw=.8)
        ax.set_xticks([0, 1], ["H-end", "Cl-end"])
        ax.get_xticklabels()[0].set_color(H_COLOR)
        ax.get_xticklabels()[1].set_color(CL_COLOR)
        ax.set_xlim(-.65, 1.92)
        span = max(pos) - min(neg)
        ax.set_ylim(min(neg) - span * .06, max(pos) + span * .06)
        ax.set_title(f"({chr(97+i)}) {lig}", fontsize=12)
        ax.set_ylabel("Energy (kcal mol$^{-1}$; see unit caveat)", fontsize=8.7)
        clean(ax, xgrid=False, ygrid=True)
    axes[5].axis("off")
    axes[5].legend(handles=[Patch(facecolor=c, label=m) for m, c in zip(EDA_METRICS, EDA_COLORS)] +
                   [Line2D([], [], color=TEXT, marker="D", linestyle="none", label="reported EDA total")],
                   loc="upper left", frameon=False, fontsize=10, labelspacing=.7)
    axes[5].text(.03, .035, "ES / EX / REP / POL / ECORR are source labels.\n"
                          "No item is omitted or renamed as pure dispersion.\n"
                          "Positive ECORR values are retained.\n"
                          "Compare magnitudes within each labeled scale.",
                 transform=axes[5].transAxes, fontsize=8.5, linespacing=1.5)
    foot(fig, ["Source: HOClxlsx.xlsx, EDA, columns B–G. Only the ES header explicitly states kcal/mol; a shared component unit is assumed here.",
               "EDA method, fragment definitions, and the physical meaning of individual terms require original-output verification.",
               "These stacks visualize the reported cancellation; they are not percentages and do not uniquely establish the mechanism."])
    save(fig, "F3_eda_components")


def figure4():
    metrics = ["r_CH", "r_OH", "r_CCl", "r_OCl"]
    write_csv("figure_F4_geometry_screening.csv", [
        dict(subset_record(r, metrics), candidate=r["system"] in CANDIDATES,
             unit_status="source unit not specified") for r in COMPLEXES])
    fig, axes = plt.subplots(1, 2, figsize=(13, 7.6))
    fig.subplots_adjust(left=.085, right=.975, bottom=.2, top=.80, wspace=.26)
    fig.suptitle("Fig. 4  Geometry screening of strongly reorganized candidates", y=.98,
                 fontsize=15, weight="bold")
    fig.text(.085, .926, "Provisional data audit | 28 H-end + 28 Cl-end geometries | no transfer assignment",
             color=RED, fontsize=10)
    for ax, end, xkey, ykey, color in [(axes[0], "H", "r_CH", "r_OH", H_COLOR),
                                      (axes[1], "Cl", "r_CCl", "r_OCl", CL_COLOR)]:
        selected = [r for r in COMPLEXES if r["end"] == end]
        for r in selected:
            cand = r["system"] in CANDIDATES
            ref = r["ligand"] == "CO"
            ax.scatter(r[xkey], r[ykey], marker="D" if cand else ("s" if ref else "o"),
                       s=72 if cand else (58 if ref else 35), color=color,
                       edgecolors=RED if cand else "white", linewidths=1 if cand else .5,
                       alpha=1 if cand or ref else .65, zorder=4 if cand or ref else 2)
        clean(ax, xgrid=True, ygrid=True)
        ax.set_xlabel(f"{xkey.replace('r_', 'r(').replace('CH', 'C–H)').replace('CCl', 'C–Cl)')}\n(source unit; not specified)")
        ax.set_ylabel(f"{ykey.replace('r_', 'r(').replace('OH', 'O–H)').replace('OCl', 'O–Cl)')}\n(source unit; not specified)")
        ax.set_title("(a) H-end" if end == "H" else "(b) Cl-end", color=color, pad=13)
    label_offsets = {"H-CAACmeSPh2": (12, 1), "H-NHCmeSPh2": (12, 17),
                     "H-NHCme": (12, -7), "H-CO": (12, 17),
                     "Cl-NHCme": (13, 2), "Cl-CO": (-12, 17)}
    for system, offset in label_offsets.items():
        r = BY_SYSTEM[system]
        ax = axes[0] if r["end"] == "H" else axes[1]
        xkey, ykey = ("r_CH", "r_OH") if r["end"] == "H" else ("r_CCl", "r_OCl")
        ax.annotate(f"{r['legacy_id']} {system}", (r[xkey], r[ykey]), xytext=offset,
                    textcoords="offset points", fontsize=8.3, color=RED if system in CANDIDATES else TEXT,
                    ha="left" if offset[0] > 0 else "right",
                    arrowprops={"arrowstyle": "-", "color": "#84919B", "lw": .7})
    axes[0].set_xlim(1.02, 2.49); axes[0].set_ylim(.94, 1.84)
    axes[1].set_xlim(1.98, 3.26); axes[1].set_ylim(1.69, 2.08)
    fig.legend(handles=end_legend() + [Line2D([], [], color=TEXT, marker="s", linestyle="none", label="CO reference")],
               loc="upper left", bbox_to_anchor=(.075, .9), frameon=False, ncol=4, fontsize=9)
    foot(fig, ["All geometry values are source-table entries; atomic correspondence and distance units await optimized coordinates.",
               "Highlighted candidates combine short external contacts with elongated internal bonds; they remain a screening class.",
               "A transfer assignment additionally requires matched old/new-bond electronic evidence and, for a pathway claim, further calculations."])
    save(fig, "F4_geometry_candidates")


def supplementary1():
    metrics = EDA_METRICS + ["EDA_E", "Eint_bess"]
    records = []
    for r in COMPLEXES:
        d = subset_record(r, metrics)
        d.update(sum_five=r["EDA_sum5"], EDA_total_minus_sum=r["EDA_sum_residual"],
                 EDA_total_minus_bess=r["EDA_minus_bess_Eint"],
                 sum_rounding_bound=.03, cross_table_rounding_bound=.01,
                 sum_exceeds_bound=abs(r["EDA_sum_residual"]) > .03 + 1e-9,
                 cross_table_exceeds_bound=abs(r["EDA_minus_bess_Eint"]) > .01 + 1e-9)
        records.append(d)
    write_csv("figure_S1_energy_audit.csv", records)
    fig, axes = plt.subplots(1, 2, figsize=(13, 11.6), sharey=True)
    fig.subplots_adjust(left=.215, right=.975, bottom=.135, top=.84, wspace=.17)
    fig.suptitle("S1  Numerical audit of EDA sums and cross-table values", y=.98,
                 fontsize=15, weight="bold")
    fig.text(.215, .935, "Provisional data audit | all 56 records | source values preserved", color=RED)
    for ax, key, bound, title in [
            (axes[0], "EDA_sum_residual", .03, "(a) EDA total $-$ five-term sum"),
            (axes[1], "EDA_minus_bess_Eint", .01, "(b) EDA total $-$ bess $E_{int}$")]:
        ax.axvspan(-bound, bound, color="#EDF1F4", zorder=0)
        ax.axvline(-bound, color=RED, ls="--", lw=.8)
        ax.axvline(bound, color=RED, ls="--", lw=.8)
        ax.axvline(0, color="#6C7780", lw=.7)
        for i, p in enumerate(PAIRS):
            for end, color, dodge in (("H", H_COLOR, -.14), ("Cl", CL_COLOR, .14)):
                r = BY_SYSTEM[f"{end}-{p['ligand']}"]
                value = r[key]
                anomaly = abs(value) > bound + 1e-9
                ax.scatter(value, i + dodge, s=47 if anomaly else 22, marker="D" if anomaly else "o",
                           color=color, edgecolors=RED if anomaly else "white", linewidths=.6, zorder=3)
                if anomaly:
                    ax.annotate(f"{end}: +{value:.2f}", (value, i + dodge), xytext=(6, -1),
                                textcoords="offset points", va="center", fontsize=8, color=RED)
        set_pair_axis(ax, ax is axes[0])
        clean(ax)
        ax.set_xscale("symlog", linthresh=.015, linscale=1)
        ax.set_title(title, fontsize=11, pad=15)
        ax.set_xlabel("Difference (kcal mol$^{-1}$; unit caveat as F3)\nsymlog; linear within $\\pm$0.015")
    axes[0].set_xlim(-.055, .42)
    axes[0].set_xticks([-.03, -.01, 0, .01, .03, .1, .3])
    axes[0].set_xticklabels(["−.03", "−.01", "0", ".01", ".03", ".1", ".3"])
    axes[1].set_xlim(-.025, 1.2)
    axes[1].set_xticks([-.01, 0, .01, .03, .1, .5, 1])
    axes[1].set_xticklabels(["−.01", "0", ".01", ".03", ".1", ".5", "1"])
    fig.legend(handles=end_legend(False) + [Patch(facecolor="#EDF1F4", label="rounding envelope")],
               loc="upper left", bbox_to_anchor=(.208, .92), frameon=False, ncol=3, fontsize=9)
    foot(fig, ["Panel (a): EDA total − (ES + EX + REP + POL + ECORR). A conservative 0.03 envelope covers six independently rounded 0.01 entries.",
               "Panel (b): the 0.01 envelope covers two independently rounded 0.01 entries, assuming a shared unit and identical definitions.",
               "Envelopes test arithmetic rounding only. Values within them do not verify methods, reference states, or physical consistency."])
    save(fig, "S1_energy_audit")


def supplementary2():
    records = []
    for p in PAIRS:
        r = dict(p)
        r.update(MEP_B_source=prov_source(p["ligand"], "MEP_B"),
                 MEP_C_source=prov_source(p["ligand"], "MEP_C"),
                 included_in_plot=p["MEP_B"] is not None,
                 exclusion_reason="" if p["MEP_B"] is not None else "MEP exists only in column C; unit/comparability unverified")
        records.append(r)
    write_csv("figure_S2_MEP_exploratory.csv", records)
    chosen = [p for p in PAIRS if p["MEP_B"] is not None]
    fig, axes = plt.subplots(1, 2, figsize=(13, 7.6))
    fig.subplots_adjust(left=.075, right=.975, bottom=.21, top=.82, wspace=.2)
    fig.suptitle("S2  Exploratory MEP and paired-energy comparison", y=.98, fontsize=15, weight="bold")
    fig.text(.075, .93, "Provisional data audit | 24 column-B values only | four column-C-only systems excluded", color=RED, fontsize=10)
    for ax in axes:
        for p in chosen:
            if ax is axes[1] and p["delta_Eb_H_minus_Cl"] < -2:
                continue
            cand = f"H-{p['ligand']}" in H_CANDIDATES
            color = H_COLOR if p["delta_Eb_H_minus_Cl"] < 0 else CL_COLOR
            ax.scatter(p["MEP_B"], p["delta_Eb_H_minus_Cl"], s=57 if cand else 34,
                       marker="D" if cand else "o", color=color,
                       edgecolors=RED if cand else "white", linewidths=.7, zorder=3)
        ax.axhline(0, color="#6F7C87", lw=.8)
        ax.set_xlim(-47, 9)
        ax.set_xlabel("MEP, column B (kcal mol$^{-1}$)\nsurface definition remains unverified")
        clean(ax, xgrid=True, ygrid=True)
    axes[0].set_title("(a) All 24 same-field entries", fontsize=11)
    axes[0].set_ylim(-13.7, 3.4)
    axes[0].set_ylabel("$\\Delta E_b$ = H $-$ Cl (kcal mol$^{-1}$)")
    axes[1].set_title("(b) Expanded range: 21 visible entries", fontsize=11)
    axes[1].set_ylim(-2, 3.4)
    axes[1].set_ylabel("$\\Delta E_b$ = H $-$ Cl (kcal mol$^{-1}$)")
    for p in chosen:
        if p["ligand"] in ["CAACmeSPh2", "NHCme", "NHCmeSPh2", "CO", "CS", "NHCmeCAACme"]:
            offset = (7, -14) if p["ligand"] == "NHCme" else (7, 6)
            axes[0].annotate(f"{p['legacy_id']} {p['ligand']}", (p["MEP_B"], p["delta_Eb_H_minus_Cl"]),
                             xytext=offset, textcoords="offset points", fontsize=7.9)
    # Fixed offsets keep the crowded local comparison reproducible without a fitting step.
    offsets = {"L1": (5, 6), "L2": (5, 5), "L4": (-16, -13), "L5": (5, -13),
               "L6": (5, -13), "L7": (5, 6), "L8": (5, 6), "L10": (-24, -12),
               "L11": (-21, 8), "L12": (-20, -12), "L14": (5, 6), "L15": (-20, 6),
               "L17": (5, -14), "L18": (5, 6), "L19": (-23, 6), "L20": (-23, 5),
               "L21": (5, 4), "L22": (5, 5), "L23": (-20, 6), "L27": (5, -13), "L28": (5, 6)}
    for p in chosen:
        if -2 <= p["delta_Eb_H_minus_Cl"] <= 3.4:
            axes[1].annotate(p["legacy_id"], (p["MEP_B"], p["delta_Eb_H_minus_Cl"]),
                             xytext=offsets.get(p["legacy_id"], (5, 5)), textcoords="offset points", fontsize=7.8)
    legend = [Line2D([], [], color=H_COLOR, marker="o", linestyle="none", label="H-end $E_b$ numerically lower"),
              Line2D([], [], color=CL_COLOR, marker="o", linestyle="none", label="Cl-end $E_b$ numerically lower"),
              Line2D([], [], color=TEXT, marker="D", linestyle="none", label="H-end candidate")]
    fig.legend(handles=legend, loc="upper left", bbox_to_anchor=(.065, .91), frameon=False, ncol=3, fontsize=9)
    foot(fig, ["Excluded column-C-only systems: N2CS (L9), SCCAACme (L24), SCNHCme (L25), SCPPh3 (L26). No cross-column conversion is made.",
               "Panel (b) changes only the displayed y-range; H-CAACmeSPh2, H-NHCme and H-NHCmeSPh2 remain visible in panel (a).",
               "This is a descriptive co-variation view. No regression, causal relation, or intrinsic donor-strength ranking is asserted."])
    save(fig, "S2_mep_competition")


def main():
    assert len(COMPLEXES) == 56 and len(PAIRS) == 28
    assert sum(p["ranking_reversal"] for p in PAIRS) == 9
    assert len([p for p in PAIRS if p["MEP_B"] is not None]) == 24
    for r in COMPLEXES:
        assert abs(sum(r[m] for m in EDA_METRICS) - r["EDA_sum5"]) < 1e-8
    for plot in (figure1, figure2, figure3, figure4, supplementary1, supplementary2):
        plot()
    (FIGURES / "figure_manifest.json").write_text(json.dumps(EXPORTS, indent=2), encoding="utf-8")
    print(json.dumps(EXPORTS, indent=2))


if __name__ == "__main__":
    main()
