# 全稿参考文献与引文审计

本审计依据用户上传PDF、`report1/参考文献清单.docx`及第一阶段核查报告。已实际打开R01—R11全部PDF，读取书目信息、摘要和下列与本题有关的结果、方法或结论；不宣称逐页核查实验谱图及全部坐标。未联网二次核验、未新增外部文献，未修改原始资料。作者已确认自有数据均独立计算，bess原值保留；文献不能补写本研究缺失的原始数据或计算条件。

机器可读条目见同目录 `references.json`：`references`含R01—R11完整作者、题名、年刊卷页/文章号、DOI、GB/T7714著录候选、页码及可支持/不可支持陈述；`excluded`保存R12—R14不列正式候选的原因。Rxx是跨阶段稳定编号，不能机械当作全稿的顺序编码。正文最终[n]按首次引用次序重排，文内上角标必须与文后表一致。

## 1. 书目核对及正式定位

| 稳定标识 | 题名与作者 | 文件内核实的年刊定位 | DOI与书目限制 |
|---|---|---|---|
| R01 | Li, Shunhua; Zhou, Hangyu; Li, Qingzhong; Scheiner, Steve. *Strong interactions between carbones and halogen atomic centers* | Chemical Science, 2026, 17:14950–14962 | 10.1039/d6sc02210c；正式PDF首页可核对 |
| R02 | Alkorta, Ibon; Blanco, Fernando; Solimannejad, Mohammad; Elguero, José. *Competition of Hydrogen Bonds and Halogen Bonds in Complexes of Hypohalous Acids with Nitrogenated Bases* | The Journal of Physical Chemistry A, 2008, 112:10856–10863 | 10.1021/jp806101t |
| R03 | An, Xiulin; Zhuo, Hongying; Wang, Yingying; Li, Qingzhong. *Competition between hydrogen bonds and halogen bonds in complexes of formamidine and hypohalous acids* | Journal of Molecular Modeling, 2013, 19:4529–4535 | 10.1007/s00894-013-1969-7 |
| R04 | Li, Qingzhong; Zhu, Hongjie; Zhuo, Hongying; Yang, Xin; Li, Wenzuo; Cheng, Jianbo. *Complexes between hypohalous acids and phosphine derivatives. Pnicogen bond versus halogen bond versus hydrogen bond* | Spectrochimica Acta Part A: Molecular and Biomolecular Spectroscopy, 2014；最终卷页未给出 | 10.1016/j.saa.2014.05.001；上传件为Accepted Manuscript，采用[J/OL]+DOI，不编造卷页 |
| R05 | Alkorta, Ibon; Legon, Anthony. *Simple carbenes as hydrogen bond acceptors: ab initio determination of nucleophilicities and reduced nucleophilicities* | Physical Chemistry Chemical Physics, 2025, 27:942–950 | 10.1039/d4cp03894k；在线2024不替代正式卷页年份2025 |
| R06 | Herrmann, Barbara; Svatunek, Dennis. *Directionality of Halogen-Bonds: Insights from 2D Energy Decomposition Analysis* | Chemistry – An Asian Journal, 2024, 19:e202301106 | 10.1002/asia.202301106；文章号不是PDF内部1–8页 |
| R07 | Wieske, Lianne H. E.; Erdélyi, Mate. *Halogen Bonds of Halogen(I) Ions—Where Are We and Where to Go?* | Journal of the American Chemical Society, 2024, 146:3–18 | 10.1021/jacs.3c11449；在线2023，正式卷页2024 |
| R08 | Portela, Susana; Fernández, Israel. *Nature of the Hydrogen Bond Enhanced Halogen Bond* | Molecules, 2021, 26:1885 | 10.3390/molecules26071885；1885为文章号 |
| R09 | Perera, M. D.; Desper, J.; Sinha, A. S.; Aakeröy, C. B. *Impact and importance of electrostatic potential calculations for predicting structural patterns of hydrogen and halogen bonding* | CrystEngComm, 2016, 18:8631–8636 | 10.1039/c6ce02089e；姓名保留上传件明示的缩写，不臆补全名 |
| R10 | Awwadi, Firas F.; Taher, Deeb; Haddad, Salim F.; Turnbull, Mark M. *Competition between Hydrogen and Halogen Bonding Interactions: Theoretical and Crystallographic Studies* | Crystal Growth & Design, 2014, 14:1961–1971 | 10.1021/cg500094b |
| R11 | Abeysekera, Amila M.; Averkiev, Boris B.; Sinha, Abhijeet S.; Le Magueres, Pierre; Aakeröy, Christer B. *Establishing Halogen-Bond Preferences in Molecules with Multiple Acceptor Sites* | ChemPlusChem, 2021, 86；最终页码未给出 | 10.1002/cplu.202100102；页脚明示“These are not the final page numbers”，不得把1–10当正式页码；用[J/OL]+DOI |

GB/T7714-2015候选著录见JSON的`gbt7714`。超过3位作者时列前三位加et al.，作者完整数组仍保留以便审校。R04/R11未定卷页是明确书目缺口，不是无法定位或无法阅读；应在审校说明中保留。DOI地址可用作定位链接，但本任务未在线打开出版社或数据库，不能声称完成线上核实。如最终模板要求引用日期，应明确是本稿引用日期，不将其冒充线上访问核验记录。

## 2. 引文—论点对应及证据范围

### R01：直接相关，但研究矩阵与本项目不同

**相关页：** PDF p.1—3（期刊14950—14952）题名、摘要、方法与单体；p.4 Table 2；p.5 Table 3；p.6 Table 4；p.7—8 Fig.5—6、Table 5；p.9—10讨论。

**可支持：** 碳(0)中心可作强Lewis碱；几何形变影响相互作用能与结合能的差别；新旧键几何和拓扑应配对分析；前线轨道孤对特征与NBO的BD供体可以共存。该文用一种碳母体C(NHCMe)₂与29种含卤Lewis酸配对，其中包括ClOH。文献ClOH的C···Cl=2.040 Å、O—Cl=2.049 Å，Eint=−40.24、Eb=−20.39、形变差19.85 kcal/mol，可作显式标注文献对照。

**不可支持：** 不提供本项目28母体×HOCl两端矩阵的偏好；不能倒推本项目计算方法、单位或校正；不能把文献ρ(O—Cl)=0.0949填进自有表；静态终态分析不提供本项目转移路径及势垒。其t参数比较相对于不同孤立参照的伸长量，不是两段实际键长比；20 kcal/mol分组不是通用阈值。

**内部核查事项：** Table3与Table5的ClNC总量不同，避免以该异常行直接作跨表标杆；Table5的Edisp明示包括色散和电子相关，不能改称纯色散。Fig.5实际为ClF/ClNH₂、Fig.6为BrOH，均不是本项目HOCl图。CT正文方向有表达不一致，方向引用应依据p.7明确主通道，而不复制p.6的可疑过渡句。

### R02：HOX两端竞争与NBO能量的边界

**相关页：** p.1摘要；p.2（10857）方法；p.5—6（10860—10861）NBO、Table8、内部键响应；p.7结论。

**可支持：** 在所研究NH₃、N₂、NCH模型中，HOCl/HOBr氢键构型较稳定，HOI两者接近、HOAt偏卤键；受体与卤素改变能影响竞争。NBO通道能在多数样本中大于净相互作用能，排斥等贡献不可忽略。

**不可支持：** 不能将限定模型写成氢键普遍强于卤键；不能将E(2)当结合能；该文p.2称interaction energy的量以优化孤立单体为参照，未用full counterpoise，与R01及本项目Eint名称不能直接等同。

### R03：国内甲脒—HOX研究及次级接触

**相关页：** p.1摘要及烟台大学署名；p.2方法、FA-(Z)-HOX/XOH结构说明；p.5—6取代效应与结论。

**可支持：** 烟台大学团队研究甲脒与HOX，在其模型中Cl/Br氢键构型较有利、I卤键构型较有利；取代基可改变差别。复合物中有主要作用和次级接触，因此构型能差不等于两条孤立键能之差。

**不可支持：** N受体中所得顺序不能直接移作碳(0)配体规律，方法参数只属于文献。p.2静电区域的次级接触文字有可疑表述，不照抄作普遍机制。

### R04：国内HOX—膦衍生物的多构型研究

**相关页：** p.1出版定位；p.2烟台大学署名；p.3摘要；p.5—6研究对象与计算段；p.14—15 NCI与结论。PDF手稿页号比物理页少1。

**可支持：** 主要对象为HOBr:PH₂Y，另以HOCl/HOI:PH₂F对照；存在含磷族键、卤键、氢键及复合作用的多个构型。X、Y及次级作用影响相对稳定性。p.14特定弱接触的NCI特征可在缺少相应AIM键路径时出现，提示不同分析检出的对象未必一一对应。

**不可支持：** 不提供碳(0)—HOCl两端偏好；不将复合作用能当单键能；不把本稿1–30或文件31页作为期刊页码。最终卷页留缺，DOI足以定位。

### R05：carbene不是carbone，异常组应单列

**相关页：** p.1—3模型和方法；p.3（944）§3.1、Fig.4附近；p.7—8结论。

**可支持：** carbene及同族物可作氢键受体，取代基调节亲核性；具有明显离子对特征的(CH₃)₂C···HCl/HBr/HI被从普通拟合分离。电子态及正解离能De的约定须明确。

**不可支持：** 不把carbene和carbone作为同义词，不将carbene—HX实例视为本研究已完整质子转移的证明，不搬用其正De或取代基趋势。其CH₂计算为单重态而非三重基态。

### R06：方向性与总吸引来源必须区分

**相关页：** p.2形变／相互作用和EDA定义、一致几何比较；p.3二维扫描；p.6—7小卤素与结论。

**可支持：** NH₃···X₂的方向性来源随卤素改变；较大卤素线性偏好可受Pauli降低影响，Cl₂/F₂中轨道与静电更突出。不同平衡距离会同时影响EDA分项；一致几何或路径分析有助减少混杂。

**不可支持：** 本项目没有对应扫描，不能据此声称HOCl—碳(0)方向性由Pauli支配，或终态柱图给出路径／唯一因果。GKS的EX+REP与ETS的Pauli也不能未经定义直接逐值置换。

### R07：三中心四电子框架不能以整体净电荷划界

**相关页：** p.1—2摘要和术语；p.4（期刊6）Fundamentals、Three-Center Bond Character；p.8—9能量参照与转移应用。

**可支持：** 卤素(I)配合物的三中心四电子图景及其卤素转移应用。p.4明确配合物可整体为阳离子、中性或阴离子，取决于两侧Lewis碱。

**不可支持：** 不能写“卤素(I)带电体系与中性HOCl不同”作为模型边界；HOCl中Cl形式氧化态也是+I，不能仅凭此确定三中心模型。当前Cl—NHCme是否适合该图景，仍需明确的片段参照及相应成键证据，近等距离本身不充分。

### R08：氢键增强卤键属于协同背景

**相关页：** p.1摘要；p.2—4 Table1及NOCV；p.6—8取代效应、Table3、方法与结论。

**可支持：** 所研究芳基碘供体与Cl⁻间的卤键可被邻近氢键增强，静电及轨道项同时变化。协同与不同取向竞争需区分。p.8正文完整EDA公式包含Pauli，轨道项含CT与极化。

**不可支持／内部问题：** 不能把其约3 kcal/mol增强当普适值，更不证明HOCl两端顺序。Table1/3注a只列吸引项却标总Eint，不能照抄；Table1部分NOCV通道求和与轨道总项不完全相符；正文优化基组def2-TZVPP与表注def2-SVP不同，QTAIM段也出现D2/D3差异。p.3文字把3/4的能量高低写反，定性增强可依据表内负值和结论，参数与公式不直接迁移。

### R09：MEP提出位点假说，结构验证限定适用范围

**相关页：** p.1书目和摘要；p.3（8633）MEP方法及共晶结果；p.5（8635）结论和局限。

**可支持：** 两种双位点受体的MEP差异与共晶位点选择联系；该特定样本中38和26 kJ/mol差异对应不同选择性。作者承认没有全面多晶型筛选，溶剂等仍待研究。

**不可支持：** 38 kJ/mol不是普适选择性阈值，固态多分子结构结果不直接等于孤立HOCl二聚体自由能，也不能由单体极值推导本项目所有两端能差。摘要“42新共晶”与p.3“42次尝试33个IR阳性”不一致；若需数量，按正文限定而非重复摘要。

### R10：带电晶体模型与几何控制

**相关页：** p.1摘要；p.3（1963）Theoretical Method；p.4晶体结构；p.6理论能量；p.10（1970）结论。

**可支持：** 卤代吡啶鎓四卤合铜晶体中HB/XB共同组织结构；同构系列可减少几何和其他作用混杂。几何图样、带电环境和供受体种类制约竞争结论。

**不可支持：** 该文能量明确含阳离子—阴离子的整体静电及其他作用，且有角度约束，不是纯HB/XB单项能。其“HB总较强”仅限其模型，不提升为普遍定律；不向中性HOCl—碳(0)搬绝对能量或接触阈值。

### R11：多位点共晶选择的样本统计

**相关页：** p.1题名作者、摘要、预排警告；p.2位点设计；p.6样本接触；p.8结论与实验。

**可支持：** 原有氢键是分子内还是分子间、受体位点环境等影响HB/XB共晶竞争。该13个晶体中的26个接触有21个N、4个O、1个π；三个2Pyr保留分子内氢键，其他10个中9个改组原分子间氢键。

**不可支持：** 81%不是普遍N位点亲和概率，卤键不必然替代氢键；不将羰基IR规律直接判为本项目HOCl质子／氯转移；不把预排1–10页写成最终页。仅用DOI与已核实年卷定位。

## 3. 国内外研究归纳的边界

若全稿仍区分国内外进展，依据上传件机构署名而不是作者姓名推断国别。R03和R04可明确写“烟台大学团队”；R01为国内团队与国外研究者合作，不宜硬分为纯国内或纯国外。R02、R05—R11的作用主要是不同模型的背景和方法限制，不要求把所有文献都塞入结果章节。

文献归纳应说明“在所研究模型与条件下”，避免把HOX卤素序列、带电晶体、邻近氢键协同、不同酸分子的比较，混成“同一HOCl两端的碳(0)配体效应”。本项目的具体28对排序必须引用自有表格。

## 4. 剔除正式引用候选但保留可读资料

- **R12，`Comparison Between Hydrogen and Halogen Bonds in Complexes of 6-O.pdf`**：实际标题为 *Competition between Hydrogen and Halogen Bonds in Complexes of 6-OX-Fulvene with Pnicogen and Chalcogen Electron Donors*；上传件有编辑／DOI占位符，文件内不能核实正式出版书目，不列正式候选。可读且可作思路记录，这不是对其科学内容的否定。它比较不同酸分子的HB/XB，也不等于同一HOCl两端。
- **R13，`cs3c01131_si_001.pdf`**：仅SI，父文献正文和完整书目未核实；不从文件名推导DOI，不声称读过未上传的父文献。
- **R14，`ja0c12084_si_001.pdf`**：仅SI，父文献书目未核实，且研究重元素类似物；不作为本研究碳(0)结果。保留可读记录但不充数引用。

## 5. 全稿最后审校的判定项目

1. 所有[n]与文后题名、DOI和首次出现顺序对应，Rxx仅作内部稳定标识。
2. 文献数字始终明示为文献，未进入本研究56条总表或补缺列；自有定量结论有文件、表、体系、列／单元格依据。
3. Eint/Eb定义与校正未核实处仍保留条件，g=Eb−Eint仅称表列差量；不把电子能排序直接转换自由能、丰度或速率。
4. GKS/ETS/NBO不同能量不相加；ECORR不自动等于纯色散；EX不省略；NOCV Energy未定义不称轨道总能。
5. 大E(2)、单条距离或BCP符号不作为完整质子／氯转移的充分证据；没有路径计算就不写势垒或反应步骤。
6. R07保留整体中性配合物的准确范围，R01保留“一种碳母体×29酸”的矩阵范围，R05保留carbene/carbone区别。
7. R04/R11缺卷页不编造；R12—R14不提升为未经核实的正式引用。

## 6. 第四阶段全稿复核结论

已只读审查`final_paper/论文_正文.md`及`data/citation_map.json`，逐项检查正文引用与本文件证据范围的对应。初次全稿审查版本正文SHA-256为`57b24a81759b6a1158af2bd429118beb81be9abfc201b9128b73e04680f97ee5`。之后仅将NOCV字段的“只有一列”修正为“单一数值字段，分别列出两端记录”，以准确区分字段含义与两端记录的表格布局；该非引文修订未改变数值、证据限制或文献陈述，复核仍通过。最新审查版本SHA-256为`07d3486df1341e2ed597f51b6ad215b127d031125989103da44453cce5856182`。没有修改论文、原始数据或源PDF。

正文共35组文献上角标，首次出现依次为[1]—[11]，复合标注内部均升序、无重复，文后11项均被引用，未遗留`{{Rxx}}`占位符；DOI与已核条目一致。最终对应为：[1]R02、[2]R04、[3]R06、[4]R01、[5]R10、[6]R09、[7]R11、[8]R08、[9]R03、[10]R05、[11]R07。R04/R11采用[J/OL]及DOI，正文文后未补造最终卷页；阅览日期为本稿引用日期，不代表已在线二次核验。

科研措辞复核结果：文献ClOH数值与自有Cl—NHCme数值明确分开，没有文献旧键指标补入自有空缺；原大纲方法仅作待核实声明，未被写成已验证的运行条件；Eint/Eb、g、EDA分项及NOCV字段仍保留定义与参照限制；强结构重排仅以候选讨论，未据静态终态给出完整转移、路径或势垒；R01一种碳母体×29酸的研究范围、R05 carbene/carbone区别及R07整体中性三中心模型均保留。绪论与NH₃的比较已准确用“相互作用”，没有将R01 Table6的Eint比较改称Eb比较。

**本次未发现必须修改的引文支持、编号或科学限制问题。** 该结论限于上述审查版本，不等于确认缺失的原始量子化学作业、完整成键分类或全部数值计算已完成验证；数值逐项复算另见数值审计，缺失参数及最小补充资料继续作为作者待确认项保留。
