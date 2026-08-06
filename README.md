<!-- ╔══════════════════════════════════════════════════════════════╗ -->
<!-- ║  Pengliang Liu (Allen-LPL) · GitHub profile README            ║ -->
<!-- ║  Dark engineering theme — navy #0e1524 / cyan #38bdf8         ║ -->
<!-- ╚══════════════════════════════════════════════════════════════╝ -->

<div align="center">

<!-- [1] HERO — animated typing banner -->
<a href="https://cv.liupengliang.com">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26&pause=1000&color=38BDF8&center=true&vCenter=true&width=760&height=54&lines=Technical+Director+%C2%B7+Full-Stack+Architect;11+years+%C2%B7+Go+%2F+Java+%2F+Python+%2F+PHP+%2F+Android;%E4%BB%8E0%E5%88%B01+%C2%B7+Distributed+%C2%B7+High+Availability+%C2%B7+DevOps;AI+%2F+RAG+%C2%B7+Vector+Search+%C2%B7+Software%E2%80%94Hardware" alt="Technical Director · Full-Stack Architect" />
</a>

<p>
  <img src="https://komarev.com/ghpvc/?username=Allen-LPL&color=38bdf8&style=flat-square&label=Profile+Views" alt="profile views" />
  &nbsp;
  <img src="https://img.shields.io/badge/Experience-11%20years-38bdf8?style=flat-square" alt="11 years" />
  &nbsp;
  <img src="https://img.shields.io/badge/Base-Hangzhou%2C%20China-38bdf8?style=flat-square" alt="Hangzhou" />
  &nbsp;
  <img src="https://img.shields.io/badge/Open%20to-Architecture%20%2F%20CTO-f5b451?style=flat-square" alt="open to" />
</p>

</div>

---

## 👋 About / 关于

```yaml
name:        刘鹏亮 (Pengliang Liu)  ·  "Allen"
role:        技术总监 / 全栈架构师  —  Technical Director / Full-Stack Architect
now:         技术总监 @ 浙江易数时代 (Medical-AI training systems, 软硬件一体化)
focus:       from-0-to-1 product & architecture · distributed high-availability · AI/RAG
superpower:  build the system, harden it under real fire (DDoS/CC, 10T migrations), lead the team
```

- 🏗️ **Architect who ships end-to-end** — 从 0 到 1、从 1 到 100，多款产品与架构落地，兼具软硬件一体化系统开发经验。
- 🤖 **AI-native systems** — enterprise **RAG** dialogue, search & recommendation, large-scale vector retrieval (**ES + Milvus**), recall/ranking strategies.
- ⚡ **High concurrency & HA** — OpenResty 网关限流降级、Redis 削峰、读写分离/分库分表、同步转异步、混合云（阿里云 + IDC）多活容灾。
- 🛡️ **Battle-tested** — 抵御 **600G DDoS + 15G CC** 混合攻击；**10T MongoDB / 550G MySQL** 无感迁移。
- 👥 **Team builder** — 从 0 组建并管理 **10–50 人** 团队，招聘、绩效、流程规范与工程效能。

---

## 🧰 Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=go,java,python,php,lua,typescript,vue,spring,android,kotlin&perline=10" alt="languages" />
<br/>
<img src="https://skillicons.dev/icons?i=mysql,redis,mongodb,elasticsearch,kafka,rabbitmq,docker,kubernetes,nginx,linux&perline=10" alt="data & infra" />
<br/>
<img src="https://skillicons.dev/icons?i=grafana,prometheus,gitlab,git,ansible,aws,tensorflow,pytorch,opengl,cpp&perline=10" alt="devops & ai" />

</div>

<sub>**+ specialties not in the icon set:** OpenResty · gRPC/Protobuf · Nacos · Consul · Milvus · Canal · Zabbix · Hyperf · Beego · Gin · 自研 WAF · UART(RS485/RS232/TTL) · Bluetooth</sub>

| Area | Stack |
| --- | --- |
| **Languages** | Go · Java · Python · PHP · Lua · TypeScript/Vue |
| **Backend / Micro** | Spring Boot · Gin · gRPC · Protobuf · Nacos · Consul · Hyperf · Beego · ThinkPHP |
| **Data / Search** | MySQL · Redis · MongoDB · Elasticsearch · **Milvus** · Kafka · RabbitMQ · Canal |
| **Infra / DevOps** | OpenResty · Nginx · Docker · Kubernetes · GitLab CI · Ansible · Zabbix · Grafana · 自研 WAF |
| **Mobile / Hardware** | Android (Retrofit/OkHttp/AIDL/ijkplayer/OpenGL) · Bluetooth · UART · Socket |
| **AI / Algorithms** | RAG · SSE streaming · CLIP · DINOv2 · Swin Transformer · ResNet50 · DenseNet121 · SIFT/SURF |

---

## 🚀 Key Projects / 核心项目

| Project | What it is | Stack highlights | Link |
| --- | --- | --- | --- |
| **时刻体育** · Moment Sports | 从 0→1 体育社区平台（小程序 / H5 / APP），高并发、灰度发布、混合云多活 | Spring Boot · Nacos · ES · Redis · RabbitMQ · Vue3 · Uniapp · OpenResty | — |
| **AI 论文/图像查重** · Similarity Check | RAG + **5M** 小图向量检索的科研查重系统（篇内/策略/全库三种模式，专家三级审核） | Milvus · CLIP · DINOv2 · Swin · ResNet50 · Spring Boot · Vue3 | [demo](https://seven.weilantech.com) · [code](https://github.com/Allen-LPL/seven-server) |
| **CPR AI 训练与考核系统** | 医疗急救 **软硬件一体化**：Android 平板 ↔ 模拟人/AED，多协议通信 + AI 数字人对话 | Android · Spring Boot · BLE/UART/Socket · OpenGL · 讯飞/腾讯云 SDK | — |
| **Mydesign** · Cross-border DTC | 跨境电商独立站出海，AWS 部署、千人千面搜索/推荐、跨境数据同步与加速 | Spring Boot · ES · AWS · Vue3 · Python | — |

<sub>More open source → <a href="https://github.com/Allen-LPL/Captcha-Pic">Captcha-Pic</a> (Go 拼图验证) · <a href="https://github.com/Allen-LPL/Laradock">Laradock 二开</a> (生产级 Docker 编排) · <a href="https://github.com/Allen-LPL/webCron">webCron</a> (Beego 分布式定时任务)</sub>

---

## 🤖 AI Systems & Tooling

**What I build with AI / 用 AI 构建的系统**

- **RAG & vector search** — enterprise retrieval over **ElasticSearch + Milvus**, recall → filter → rerank; 500 万小图向量索引与检索工程化落地。
- **Multimodal & real-time** — 大模型 **SSE 流式对话** + 逐句 TTS，**OpenGL 透明通道数字人** 口型同步，讯飞语音唤醒 + 腾讯云 ASR/TTS 全链路。
- **Computer vision** — 图像相似度：CLIP / DINOv2 / Swin Transformer / ResNet50 / DenseNet121，SIFT·SURF 特征点匹配。

**AI-native dev workflow / 日常 AI 工具栈**

<p>
  <img src="https://img.shields.io/badge/Claude_Code-MAX%20%2B%20API-D97757?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code MAX + API" />
  <img src="https://img.shields.io/badge/ChatGPT-Pro%20%2F%20Plus%20%2B%20API-10A37F?style=for-the-badge&logo=openai&logoColor=white" alt="ChatGPT Pro/Plus + API" />
  <img src="https://img.shields.io/badge/GitHub_Copilot-active-24292f?style=for-the-badge&logo=githubcopilot&logoColor=white" alt="GitHub Copilot" />
  <img src="https://img.shields.io/badge/Figma-design-F24E1E?style=for-the-badge&logo=figma&logoColor=white" alt="Figma" />
</p>

<sub>Daily driver: **Claude Code (MAX + API)** for agentic coding & architecture. Also **ChatGPT Pro/Plus + API** and **Copilot** for breadth, **Figma** for design. 全流程 AI 辅助研发。</sub>

---

## 📊 GitHub Stats

<div align="center">

<img height="165" src="https://github-readme-stats.vercel.app/api?username=Allen-LPL&show_icons=true&count_private=true&hide_border=true&title_color=38bdf8&icon_color=38bdf8&text_color=c9d4e5&bg_color=0e1524" alt="stats" />
<img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Allen-LPL&layout=compact&langs_count=8&hide_border=true&title_color=38bdf8&text_color=c9d4e5&bg_color=0e1524" alt="top langs" />

<br/>

<img src="https://github-readme-streak-stats.herokuapp.com/?user=Allen-LPL&hide_border=true&background=0e1524&stroke=1f2b45&ring=38bdf8&fire=f5b451&currStreakLabel=38bdf8&sideLabels=c9d4e5&dates=64748b&currStreakNum=c9d4e5&sideNums=c9d4e5&dayLabels=c9d4e5&titleColor=38bdf8" alt="streak" />

<br/>

<img src="https://github-profile-trophy.vercel.app/?username=Allen-LPL&theme=onedark&no-frame=true&no-bg=true&column=7&margin-w=8&margin-h=8" alt="trophies" />

</div>

---

## 🐍 Contribution Snake

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Allen-LPL/Allen-LPL/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Allen-LPL/Allen-LPL/output/github-contribution-grid-snake.svg" />
  <img alt="contribution snake" src="https://raw.githubusercontent.com/Allen-LPL/Allen-LPL/output/github-contribution-grid-snake.svg" />
</picture>

</div>

---

## 🔗 Connect

<div align="center">

<a href="https://www.liupengliang.com">
  <img src="https://img.shields.io/badge/Blog-liupengliang.com-38bdf8?style=for-the-badge&logo=hugo&logoColor=white" alt="blog" />
</a>
<a href="https://cv.liupengliang.com">
  <img src="https://img.shields.io/badge/Online%20CV-cv.liupengliang.com-f5b451?style=for-the-badge&logo=readdotcv&logoColor=white" alt="online cv" />
</a>

</div>

<div align="center"><sub>⚙️ Architected end-to-end · shipped under real load · 从代码到团队</sub></div>
