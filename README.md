# python_study
python学习练习仓库  
**黄亮**
>1. day01为第一次课作业。 
>2. day02为第二次作业。约瑟夫环
>3. day03第三次作业，面向对象实现约瑟夫环，文件读取。
>4. day04为第四次作业，实现一个约瑟夫类
>5. day05为第五次作业，实现txt,csv,zip文件读写类，读取文件内容来实现约瑟夫环。
>6. day06为第六次作业，实现文件读取多态。
>7. rent-o-matic为第七次作业，以clean architecture重写约瑟夫环。
>>目录结构(视图-逻辑-实体)：  
>>domain: 存放实体类，与业务流程无关。   
>>adapters: 存放读取文件策略，和约瑟夫策略  
>>use_cases: 机制层，选取对应策略  
>>interface: 提供外部调用接口，供页面调用。  
>>rest: 最外层，存放视图层，只展示页面，不提供逻辑。  
>>common: 公共层，提供公共全局变量
