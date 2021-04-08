# simulate

本项目由python开发，采用元胞自动机的思路，对新冠疫情做了模拟，模拟的区域是个开放的空地，任何人可以进行随机移动，开始会

进行随机生成若干人，人群分为未感染者，感染者与痊愈者三种类型人，痊愈者感染病毒的概率相比未感染者会相当小。模拟开始后会

所有人群可能会进行上下左右随机移动然后根据感染者周围的情况根据概率进行感染，每个未感染者都有极小的几率变异变成感染者。

感染者每次模拟会有一定几率痊愈变成痊愈者。


疫情控制分别有两种防控方式：戴口罩，隔离。戴口罩会将感染几率降低，隔离则会限制人群的移动。

最终经过多轮的模拟判断当前疫情的情况。

运行的结果如下（蓝色字体第二列表示从未被感染过的，第三列表示目前已感染的，第四列表示感染后痊愈的）：

未戴口罩，未隔离：


<img width="300" alt="未戴口罩未隔离" src="https://user-images.githubusercontent.com/37739385/113983675-c72e5080-987c-11eb-806e-2b2e88c1c620.png">


<img width="198" alt="未戴口罩未隔离2" src="https://user-images.githubusercontent.com/37739385/113983690-cc8b9b00-987c-11eb-8cb7-05ca97b6319a.png">

其中第50波后未被感染的只有23人

戴口罩，未隔离：


<img width="479" alt="戴口罩未隔离" src="https://user-images.githubusercontent.com/37739385/113983806-f0e77780-987c-11eb-80b3-ad27bec4c450.png">

<img width="211" alt="戴口罩未隔离2" src="https://user-images.githubusercontent.com/37739385/113983834-f6dd5880-987c-11eb-8ad3-580576b8f4d5.png">

其中第50波后未被感染的只有137人

未戴口罩，隔离：


<img width="476" alt="隔离" src="https://user-images.githubusercontent.com/37739385/113983923-1a080800-987d-11eb-98b5-647193a86dea.png">

<img width="174" alt="隔离2" src="https://user-images.githubusercontent.com/37739385/113983944-1f655280-987d-11eb-9cfc-3c725c221490.png">

其中第50波后未被感染的只有120人

戴口罩，隔离：


<img width="481" alt="隔离且戴口罩" src="https://user-images.githubusercontent.com/37739385/113983860-0197ed80-987d-11eb-8cab-6957e27ab120.png">

<img width="184" alt="隔离且戴口罩2" src="https://user-images.githubusercontent.com/37739385/113983882-0bb9ec00-987d-11eb-8428-37da615811b6.png">

其中第50波后未被感染的只有174人


