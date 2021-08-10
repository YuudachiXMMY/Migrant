# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

default chapter = "00"

define y = Character("叶雨潇", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define l = Character("梁芷柔", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define loli = Character("小梁芷柔", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define yl = Character("两个人", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define z = Character("老师", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define a = Character("同学A", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define b = Character("同学B", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define c = Character("其他同学", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define e = Character("同学们", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define f = Character("女同学", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define g = Character("同学", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define who = Character("？？？", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define az = Character("医生", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define k = Character("护士", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define d = Character("店员", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define kfc = Character("服务员", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define bird = Character("候鸟", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define narrator = Character(None, ctc_pause="ctc_pause_icon", ctc="ctc_icon")

# 游戏在此开始。

label start:

    stop music
    stop sound

    #取消下面一行代码的注释可以直接进入staff剧情
    # jump staff

#开篇

    $ chapter = "00"

    scene bg title #致十八岁的我们
    with dissolve
    pause 5.0

#高考结束一年后"

    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    scene cg12a #叶雨潇打电话CG-1|CG12a
    with fade
    "漫步河滨，放眼望去，但见河水滔滔，奔流而下，裹挟着泥沙，仿佛要将天地间的一切都染作昏黄。"
    "然而，在这其中，却有一片湿地居于岸边，为这无尽的昏黄，增添了一抹鲜艳的绿色。"
    "数不清的草甸、芦苇，以及槐树、柳树和白杨。"
    "在这个夏末秋初的时节，它们用尽全力展现着自己的活力。"
    "随手捡起一片落叶，仰望天空。"

    scene bg b00 #天空
    with fade

    "湛蓝的青空，如洗的白云。"
    "卷着些许潮湿味道的空气。"
    "江浪声，风声，草木枝叶的哗哗声。"
    "忽然，有一声嘶鸣，自天空响彻四野。"

    scene cg12a1 #叶雨潇打电话CG-1|候鸟|CG12a1
    with fade
    "我抬起头，看到有一道白影，从眼前一晃而过，朝着正南的方向，义无反顾地飞去。"
    "那是一只候鸟。"

    scene bg b00 #天空
    with fade
    pause 1.0
    scene bg b00a #天空|候鸟
    with dissolve
    pause 1.5

    voice "audio/voice/00000a.ogg"
    show text open01 at truecenter
    with dissolve
    pause
    voice "audio/voice/00000b.ogg"
    show text open02 at truecenter
    with dissolve
    pause
    voice "audio/voice/00000c.ogg"
    show text open03 at truecenter
    with dissolve
    pause
    voice "audio/voice/00000d.ogg"
    show text open04 at truecenter
    with dissolve
    pause
    voice "audio/voice/00000e.ogg"
    show text open05 at truecenter
    with dissolve
    pause

    scene bg black #黑屏
    with fade
    voice "audio/voice/00000f.ogg"
    show text open06 at truecenter
    with dissolve
    pause

    scene cg12a2 #叶雨潇打电话CG-1|手机|CG12a2
    with fade
    "掏出手机，打开通讯录。"

    scene cg12a3 #叶雨潇打电话CG-1|手机|通讯录|CG12a3
    "在许许多多的人名中，翻出其中看起来似乎再普通不过的一条。"
    scene cg12a4 #叶雨潇打电话CG-1|手机|通讯录|梁芷柔|CG12a4
    "「梁芷柔」"
    "我凝视着这个名字，片刻。"
    "然后——"

    stop sound fadeout 1.0

#序幕

    scene bg black #黑屏
    with fade
    show text open07 at truecenter
    with dissolve
    pause 3.0

#两年前。
#高二期末考试后。
#7月28日。

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～

    scene bg b01 #教室
    with dissolve
    pause

    "盛夏。"
    "一个热到无以复加的日子。"
    "教室仿佛蒸笼一样，汗水糊满了每个人的身体，出奇地憋闷。"
    "房间内用来降温的就只有一架20年前产的老旧电风扇，现在正半死不活地吊在黑板的左上角，喘出萎靡不振的怪声。"
    "听上去好像在说「快睡吧～快睡吧～」一样。"
    pause 3.0
    "也确实有很多学生抵挡不住这份诱惑倒下了，整个教室都充斥着颓废的气息。"
    "……不过，也有例外的。"
    "比如讲台上的班主任，现在就亢奋得很，正在拼命地朝下面喷着口水。"
    show charaz h01 #老师立绘|夏季|普通
    with dissolve
    voice "audio/voice/010001.ogg"
    z "「……今年！啊，今年咱们县的考生，有42个人考上一本！93个人考上了二本！」"
    voice "audio/voice/010002.ogg"
    z "「啊，这是咱们县这么多年以来最好的成绩了！而这些人有百分之七十以上，都是咱们县一中的！」"
    voice "audio/voice/010003.ogg"
    z "「你们也是县一中的学生，明白吗！一中，是县里最好的学校，你们呢，也是县里最优秀的一批学生！」"
    show charaz h04 #老师立绘|夏季|咆哮
    with dissolve
    voice "audio/voice/010004.ogg"
    z "「明年，就该轮到你们去高考了！目标，只能比往年高，不能比往年低！」"
    voice "audio/voice/010005.ogg"
    z "「不要辜负一中，更不要辜负你们的父母，和你们自己！啊，为了你们将来的前途，你们现在没空放松……」"

    hide chara
    with dissolve

    scene bg b01 #教室
    with fade
    y "「（唉……）」"
    "百无聊赖。"
    "我半坐半靠地倚在座位上，努力寻找一个能让自己舒服一些的姿势。不过无论如何，眼前这幅光景依然让人感到煎熬。"
    "这种正确的废话到底要说多少遍啊……"
    "放眼教室，呼呼大睡者有之，窃窃私语者有之，左顾右盼者有之，不屑一顾者也有之。"
    "……就是没有认真听班主任讲话的。"
    y "「……」"

    scene bg b00b #烈日
    with fade
    "无聊之下，我转过头，透过学校教室的窗户，望向外面的世界。"
    "无垠的天空仿佛刚刚被靛青色的染料洗过一遍似的，举目望去，到处都是纯粹的湛蓝。"
    "万里晴空之上，毫无遮拦的太阳放射出万丈光芒。"
    "说来，这痛苦的高温就是源自它了吧……"
    "由于海拔超过1500米又靠着黄河，我所处的这座县城，往年的夏天一直都还算凉爽。但今年却不知抽的什么疯，气温比往常高了好几度，异常的闷热。"
    y "「……」"
    "灿烂的阳光刺入眼帘，火辣辣的很是不好受。"
    "我微微眯起眼，视线也向下移去少许。"

    scene bg b02 #城区
    with fade
    "大半个城区映入眼帘。"
    "由于学校所处的地势比较高，沿途又没有什么高大的建筑遮挡，县城的模样在这里可以说是一目了然。"
    "这就是我的家乡，一个毫无特色的山区小城。"
    "地处大西北，坐落于黄河流域一处狭长的河谷盆地，全县不过三十万人，没多少物产，交通也不算方便，国家级贫困县的帽子戴了好几十年，直到最近才勉强摘掉。"
    "为此，县里倒也没少想办法。前些年大张旗鼓地进行老旧棚户区改造，还要在老城区的西边扩张新城区，说是吸引投资什么的，最终也没个结果，只留下一大票不知算不算是烂尾的工程。"

    scene bg b01 #教室
    with fade
    "想到这里，目光又转向讲台上仍在兀自嘶吼的班主任。"

    show charaz h04 #老师立绘|夏季|咆哮
    with dissolve
    voice "audio/voice/010006.ogg"
    z "「……总而言之，这两个星期的假期不是给你们玩的。记住要复习，明白吗！这学期我们提前学完了高三的课程……」"
    hide chara
    with dissolve

    "这大概也要算是「没少想办法」的例子之一。"
    "县里一天到晚都在大喊「加强教育」，以期提高人口素质、实现发展，实际上也确实很是下了一番功夫，这些年前前后后新建了好几所初中，把九年义务教育推进了好大一块。"
    "不过，成绩也就仅限于此了。"
    "到了高中这里，每年的大学录取率不过勉强达到五分之一，能考到一本省控线以上的学生更是不足百分之五。虽然每年都说比往年人数增多，但实际上，还是连全省的平均比例都达不到。"
    "不过，也难怪会是这个结果……或者说，不是这个结果的话才比较奇怪。"
    "作为一个马上就要升入高三的学生，我对此有着十分直观且深刻的体会。"
    "毕竟，老师们采取的措施，翻来覆去就只有那一种——"
    "加码、加码、再加码。"
    "……"
    "…………"

    scene bg b01 #教室
    with fade
    "又是十分钟过去了。"
    "随着时间的流逝，教室里的生存环境显得愈发恶劣。"
    "烈日暴晒之下，高温造就出无数个汗流浃背的背影，汗水将衣服紧紧裹在身上，仿佛是在集体蒸桑拿一样。"
    "闷热带来的不止是情绪上的躁动，身体本身也已经到了极限。"
    "感觉再这么下去，等不到下课就要中暑了吧。"
    "记得人类在丧失体重百分之二的水分时就会开始出现脱水的症状。"
    "现在我们这状况……不晓得还能坚持多久。"
    y "「……」"
    "……不行，越是想这种事情，就越感觉到昏昏欲睡。"
    "我的上下眼皮也开始打架了。"
    "低头看了看表，距离下课大约还有不到一刻钟。"
    "再坚持一下比较好。"
    "虽然现在大家的状态普遍不怎么样，但太过肆无忌惮的话，没准就会撞在班主任的枪口上，到时候肯定又会被喷上好久的口水。"
    "还是别去学那几个睡过去的家伙了吧……"
    y "「……」"
    y "「…………」"
    scene bg b01 #教室
    with fade
    y "「呼……」"
    y "「（……不行，不能睡。）」"
    y "「（要振作啊！）」"
    y "「……」"
    scene bg b01 #教室
    with fade
    scene bg b01 #教室
    with fade
    scene bg black #黑屏
    with fade
    y "「zzz……」"
    y "「ZZZzzz……」"
    "……"
    "…………"
    scene bg b01 #教室
    with vpunch
    y "「——！！」"
    "突然之间猛地醒了过来。"
    "由于是突然惊醒，一时间心脏狂跳个不停。"
    "啊……好难受。"
    "虽然难受，不过总算是稍微清醒了一些。"
    y "「（妈的居然一边想着『不要睡！』一边就睡着了。）」"
    y "「（真是……）」"
    "我抹去一把汗水，使劲揉了揉几近迷离的眼睛。"
    "太难熬了……真的有人能在这种环境里坚持下去么？"
    "下意识地环顾四周。"
    y "「……？」"

    scene cg01a #梁芷柔听讲CG-1|标准|CG01a
    with fade
    "忽然发现，在一排排东倒西歪的身影中，还真就有一个另类存在。"
    "一位哪怕是在如此煎熬的环境之中，仍在尽力维持着端正坐姿的少女。"
    "她的座位在我的右前方。由于那一列被讲台向后挤了半个位置，与我的这一列并不平行，不过只隔了一条过道，距离并不算远。"
    "从我的位置，可以清楚地看得到她脸颊和脖子上渗出的细小汗珠。"
    y "「（哇……亏她能撑得住啊。）」"
    "真不愧是学校里出了名的好学生。"

    scene bg b01 #教室
    with fade
    "——梁芷柔。"
    "在这所学校之中……不，在整个县城的教育界，都可以称得上是一位大名鼎鼎的人物。"
    "至于理由，非常简单——学习好。"
    "不是一般的好，据说已经是可以随心所欲地挑选大学的水平。"
    "如之前所述的那样，我们这个县的教育水平一直不怎么样，偶尔哪年有一两个可能考上重点大学的，都会被老师当成大熊猫一样供起来。"
    "不过往昔的那些学霸，和我眼前的这一位相比，就未免显得逊色了。那些我们只闻其名，连做梦都不敢去想的国内顶尖的高等学府，对她而言却如探囊取物一般。"
    "可想而知，她在我们这里有着怎样的待遇。"
    y "「（这就是人比人，气死人吧。）」"
    y "「……」"
    y "「（不过啊……）」"

    scene cg01a #梁芷柔听讲CG-1|标准|CG01a
    with fade
    "就事论事，对于梁芷柔，我是服气的。"
    "有果必有因。她能取得这样的成绩，付出过不知道多少努力。"
    "就比如，哪怕是这样的大热天里，她对自己的要求也并不放松，光是这一份自律，就令人自愧弗如了。"
    y "「……啧。」"
    "反正，我大概是做不到的。"

    scene bg b00b #烈日
    with fade
    "在我看来，她就好像正午的阳光一般，太耀眼了。"
    "那些我们耳熟能详的用来称赞好学生的套话，几乎全都可以原封不动地照搬到梁芷柔的头上。"
    "成绩优秀，品德方面亦无可挑剔，担任着班上的班长兼学习委员，再加上相貌出众，性格也很好，和所有人都融洽相处。"
    "各方面都太完美了。"

    scene bg black #黑屏
    with fade
    "但，也正是因为各方面都太完美了，她显得十分鹤立鸡群。"

    scene cg01a #梁芷柔听讲CG-1|标准|CG01a
    with fade
    "在旁人眼里，她近似于一种不同次元的存在，哪怕近在咫尺，也仿佛毫不相关。"
    "大家对她敬而远之，虽然关系都还好，不过，似乎也没有见过她和谁特别亲密。"
    y "「（不过高考之后，她会到那些大城市去上大学吧？）」"
    y "「（这么一想，也确实不用费那么多心思去处人际关系，反正以后也不见得还能有多少交际……）」"
    y "「……」"
    y "「（大城市啊……）」"

    scene bg b02 #城区
    with fade
    "想到这里，我望向窗外，看着这个我生活了十多年的小县城。"
    "要论对家乡的感情，当然也是十分深厚的，不过内心之中，始终还是存有一种对大城市的向往。"
    "省城距离这里不过几十公里，虽然交通不算方便，偶尔也会过去一趟。"
    "相对于老家这里，省城无疑要繁华得多，而想必东部沿海的那些大城市又会比省城更上一层楼。"
    "对于我们这些穷乡僻壤出身的人来说，那些都市总是很有吸引力的。"
    y "「（不过……唉。）」"
    "只是痴人说梦罢了。"
    "我的成绩，在班上其实还算是不错。虽然只是偶尔才会努一把力，三天打鱼两天晒网的事情没少做，但考试什么的姑且也还排在前面几名。"
    "不过，这种在教育落后的偏远县城中学里还算不错的成绩，放到高考之中，只能勉强摸到二本线。"
    "在省内就读的话，说不定还能照顾一点，但想要往外省考，那就得找不知第几流的学校去了。"

    scene cg01a #梁芷柔听讲CG-1|标准|CG01a
    with fade
    "想到这里，忍不住又把视线转回梁芷柔的身上。"
    "要说起来，和这样优秀的美丽少女同班两年，最开始的时候也不是没有过一些想法。"
    "估计和我抱有相同念头的男生应该不少……只不过，在残酷的现实面前，大家全都深感压力、自惭形秽，最后全都选择了成为呆在优美天鹅身边的沉默的癞蛤蟆。"
    "以我自己而言，除了一些没有营养的打招呼，或者上传下达老师的指令以外，和梁芷柔之间，哪怕连一次值得记忆的对话都没有。"
    "……唉，一把辛酸泪啊。"
    y "「……」"
    "就在这时，我忽然发现了一丝异样。"
    y "「（……咦？）」"
    y "「（那、那是……）」"

    scene cg01c #梁芷柔听讲CG-3|衣服半透|CG01c
    with fade
    "我发现，梁芷柔其实也没少出汗。"
    "也是，就算是意志上能够坚持得住，身体终究不是铁打的。"
    "总之，她也出了一身汗，而我们学校的校服又很薄，被充沛的汗水浸过之后……"
    y "「（噢、噢噢……！）」"

    scene cg01c1 #梁芷柔听讲CG-3|衣服半透|视角拉近|CG01c1
    with fade
    "湿漉漉的校服紧紧趴在梁芷柔的肌肤上。"
    "梁芷柔的头发很长，遮住了一部分后背，不过依然可以看到内衣的轮廓……虽然只是很小的一块。"
    y "「（……啧！）」"
    "我们学校对于女生的头发长短管得很松，而且老师们对梁芷柔这样的特优生还有超常规的优待，只要不是那种染得五彩斑斓的，就没人管。"
    y "「（要是能管得再严一点，起码让她梳个马尾什么的话……）」"
    y "「（……）」"
    "……还是算了。"
    "要是校规真的严格起来，在大饱眼福之前，我们就先要倒大霉了。"
    "不值得，不值得。"
    y "「（……）」"
    "无论如何，这波已经不亏了。"
    "能够看到这样的奇景，看来天气热也不完全是坏事嘛！"
    "作为一只偷窥天鹅的癞蛤蟆，我不禁觉得这种酷暑下的场面若是能再多延续一阵，也未尝不可。"
    y "「（能多看一秒是一秒嘛……嗯？）」"

    scene cg01c2 #梁芷柔听讲CG-3|眼睛向后瞟视|衣服半透|CG01c2
    with fade
    "她瞟了我一眼。"
    "……是察觉到我的目光了吗？"
    "确实，偶尔会有这种第六感一样的感觉。"
    "惨了。盯着她的身体看了半天，结果被她抓了个现行……"

    scene bg b00b #烈日
    with fade
    "我慌慌张张地挪开了视线，装作不经意的样子朝窗外的天空望去。"
    y "「……」"
    y "「…………」"
    "啊……外面的天气真是好啊。"
    y "「……」"
    "我是说真的，不信你看这大太阳？呵呵呵呵呵……"
    y "「……」"

    scene cg01c #梁芷柔听讲CG-3|衣服半透|CG01c
    with fade
    "偷偷回瞄一下……"
    l "「……」"

    scene cg01c2 #梁芷柔听讲CG-3|眼睛向后瞟视|衣服半透|CG01c2
    l "「……」"
    "哎哟还在注意我这边！"

    scene bg b00b #烈日
    "慌忙把头再次扭向窗外。"
    y "「……」"
    "……这就很尴尬了。"
    "在剩下的时间里，我再也不敢把目光投向梁芷柔那一侧，就这么一直煎熬着等到了下课。"

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    play sound "audio/sound/effect06.ogg" noloop
    scene bg b01 #教室
    with fade
    "铃声终于响起。"
    "班主任大概是也看出学生的状态不怎么样，并没有拖堂，只是意犹未尽地总结了两句就离开了。"
    "他前脚刚出门，后面教室里就迸发出一片凄惨的哀嚎。"
    "不少之前阵亡的同学连爬起来的力气都没有了，只是瘫在座位上呻吟。"
    y "「……呼。」"
    "长长地吐出一口气。"
    "要说我的情况也好不到哪去……靠着窗户这一侧，一上午几乎要被晒成人干了。"
    "还好，接下来有两个半小时的午休，虽然不见得能完全恢复，但对于现在的我来说无疑是弥足珍贵的喘息之机。"
    "吃饭去吧……不，先去打水，水壶里装的水在之前就已经喝光了。"
    pause 2.0
    "站起身，准备朝外走。"

    show chara a01a #梁芷柔立绘|夏季校服|普通|正面
    with dissolve
    l "「……」"
    show chara a02 #梁芷柔立绘|夏季校服|皱眉
    with dissolve
    l "「……」"
    y "「呃……」"
    "与梁芷柔的视线相交的那一刻，被她面无表情地瞪了一眼。"
    "所谓做贼心虚，我下意识地缩了一下脖子，迈出一半的脚步也收了回来。"

    hide chara
    with dissolve
    "就这一下犹豫的功夫，后排的人已经拥了过来，塞满了通道。"
    "因为旁边已经没有空间，我只能把身后的桌子推了推，顺着这一点缝隙挤到了队尾的后面。"
    "呜哇……眼前这场面，人满为患啊。"
    "教室的后门是被锁住的，而且后排也被桌椅堵满了，想绕过去非常麻烦，这一侧出去的路只有前面那一条。"
    "结果就是一群人堆在一起，越是着急、抢道，反而越是造成了严重的拥堵。"
    "看这样子，一时半会儿是别想从这边出去了。"
    "要不然翻椅子过去吧……虽然会麻烦点。"
    "这样想着的时候，前面已经有人付诸行动了。"
    "看来大家都等不及了。一帮人油腻腻地互相蹭来蹭去，光是想想就难受。"
    "我也向后稍微退了退，找了个没人的位置准备翻山越岭。"
    "临起步之前，又情不自禁地向梁芷柔那边看了一眼。"

    show chara a01a #梁芷柔立绘|夏季校服|普通|正面
    with dissolve
    l "「……」"
    "她在座位上呆着没动，只是在前后来回地张望着，似乎是打算等人走得差不多了再起身。"
    "确实，对于沉得住气的人来说，这也是一种不错的策略。"
    l "「……」"
    "啊……"
    show chara a02 #梁芷柔立绘|夏季校服|皱眉
    with dissolve
    "在她向后望的时候，我们的视线又对上了。"
    l "「……」"
    show chara a01b #梁芷柔立绘|夏季校服|普通|侧面
    with dissolve
    "梁芷柔的目光在我的身上停顿了一两秒，然后若无其事地转回头向前看去了。"

    hide chara
    with dissolve
    "……她应该是还在介意吧？虽然没表示什么。"
    "真是难堪……算了，事已至此，也没什么办法了，毕竟这种事根本拿不上台面来，哪怕是想要道歉都无从开口。"
    "还是赶快去打水……吧……"
    "就在这时——"

    stop music
    with hpunch
    voice "audio/voice/050001.ogg"
    a "「\[哔——\]！你他妈故意吧？」"
    voice "audio/voice/060001.ogg"
    b "「故你\[哔——\]！滚蛋！」"

    play music "audio/music/bgm06.ogg" fadein 1.5 #悬而未决
    "不知道因为什么事，前面突然吵起来了。"
    "包括我在内，所有人的视线都向争吵的方向集中而去。"
    "嗯……是两个平时就经常惹事的家伙。"
    "现在，这两人正在讲台旁边互相谩骂，把出门的唯一通道给堵得死死的。"
    "看他们似乎一时半会儿完不了事的样子，原本被吸引了注意力的人群又开始涌动，后排的人大多开始选择翻越椅子。"
    "我倒是没急着动身，而是多听了几句。"
    "似乎是因为抢道结果挤在了一起，又互不相让，最后就顶起牛来了。"
    y "「（……要吵到外面吵去啊……）」"
    "我小声嘀咕着。"
    "真是……这俩人明明是为了快点出门，结果却是停留在原地争吵，彻彻底底的本末倒置。"
    "虽然也不是不能理解……大热天的，脾气会暴躁一点，而且最近压力也大，有点冲动也正常。"
    "但是现在眼看着就要放假了啊！你们就非得惹出个事来不可吗？"
    voice "audio/voice/050002.ogg"
    a "「我就\[哔——\]！」"
    voice "audio/voice/060002.ogg"
    b "「你\[哔——\]！」"
    "这两个人还没完没了了，一边骂一边互相推搡起来。"
    "旁边的同学也有想上去劝的，结果被他们粗暴地推开了。"
    y "「（打吧……但愿别连累整个班就好。）」"
    "叹了口气，我摇摇头，准备去翻椅子。"
    "就在这时。"

    stop music
    show chara a02 #梁芷柔立绘|夏季校服|皱眉
    with dissolve
    l "「…………」"
    "梁芷柔站起来了。"
    "不过，她并没有像这一侧其他人那样翻椅子往外走，而是向着正在撕扯的两个人走去。"
    "通道上的人有不少已经去翻山越岭了，剩下的人已经少得多，她得以一路畅通无阻地到达现场。"
    show chara a03 #梁芷柔立绘|夏季校服|生气
    voice "audio/voice/000001.ogg"
    l "「住手！」"
    "那俩人已经在互相揪着脖领子了，这种场面，就算是其他的男生来劝都要担心一下会不会被波及，但梁芷柔却毫不犹豫地上前了。"
    voice "audio/voice/000002.ogg"
    l "「别打了！有什么事不能好好说啊？」"
    "一边嘴上劝阻，一边试图分开两个人。"

    hide chara
    with dissolve
    "她那娇小的身躯，当然没有这么大的力气将两个人硬给掰开。"
    "不过那两个家伙刚才还一幅神挡杀神佛挡杀佛、不打一场誓不罢休的模样，在看到上台劝架的人是梁芷柔的时候，也都迟疑了起来。"
    "其中一个一开始还下意识地想要把「劝架者」给推开，此时伸了一半的手也讪讪地收了回去。"
    voice "audio/voice/050003.ogg"
    a "「不是，班长，我也不想这样。他要不骂我我至于么！」"
    voice "audio/voice/060003.ogg"
    b "「少来这套！你不动手我理你啊？」"
    voice "audio/voice/050004.ogg"
    a "「我他妈动什么手了！」"
    show chara a02 #梁芷柔立绘|夏季校服|皱眉
    with dissolve
    voice "audio/voice/000003.ogg"
    l "「行了行了别吵啦！」"
    show chara a04 #梁芷柔立绘|夏季校服|无奈
    with dissolve
    voice "audio/voice/000004.ogg"
    l "「都少说两句好不好？是不是你们都特别想把郑老师再给招回来呀？」"
    voice "audio/voice/060004.ogg"
    b "「不是，我……」"
    show chara a05a #梁芷柔立绘|夏季校服|苦笑1
    with dissolve
    voice "audio/voice/000005.ogg"
    l "「哎呀，好啦好啦！多大点事啊。」"
    "梁芷柔扯出了我们班主任的虎皮，随即趁着对方气势一挫的机会，挤到了两个人中间，把他们隔开了。"
    hide chara
    with dissolve

    "一般来说男生想要一个人劝这种架不太容易，搞不好就会被夹在中间挨两头打，又或者有意无意地拉了偏架，起到了反效果。"
    "不过，劝架的人是女生的话，一般来说只要不是打疯了，都会有所收敛。"
    "尤其是梁芷柔这样在班上素有威望，各方面都镇得住场子的，处理这种事情是驾轻就熟了。"
    "只能说，不愧是班长。"

    scene bg b01 #教室
    with fade
    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    "三言两语劝开了两个人，原本堵塞的过道终于被打通了。"
    "既然如此，也就没必要去翻椅子了。"
    show chara a01a #梁芷柔立绘|夏季校服|普通|正面
    with dissolve
    voice "audio/voice/000006.ogg"
    l "「啊……」"
    "沿着通道向外走，与返回座位拿东西的梁芷柔打了个照面。"
    show chara a04 #梁芷柔立绘|夏季校服|无奈
    with dissolve
    voice "audio/voice/000007.ogg"
    l "「……」"
    hide chara
    with dissolve
    "错身的时候，听到梁芷柔微微叹了一口气。"
    "似乎也是相当疲惫的样子啊。"
    "难怪，经历了一个难熬的上午以后，还要调解这种狗屁倒灶的破事，换谁都会觉得心力憔悴吧。"
    y "「……」"
    "虽然有点想称赞、鼓励她一下，不过想想刚才我给她留下的不良印象……算了吧，别碍她眼才是真的。"
    y "「（走走走，打水去打水去，快要渴死了！）」"
    "还是走吧——就在我这么想着的时候，刚才打架的两个人之一，靠近我这一侧的家伙，用并不小的声音嘟囔了一句。"

    stop music
    voice "audio/voice/050005.ogg"
    a "「……傻\[哔——\]。」"
    y "「！！」"
    play music "audio/music/bgm06.ogg" fadein 1.5 #悬而未决
    "感觉要糟糕。"
    "最怕的就是这种要打没打起来，好不容易给分开了却又扔下场面话的。"
    voice "audio/voice/050006.ogg"
    a "「你等着，回头再和你——唔噗！」"
    play sound "audio/sound/effect02.ogg" noloop
    with hpunch
    "这一位还在絮絮叨叨地念着什么，那边已经不由分说，直接彪悍地飞起一脚踹过来了。"
    "一声惨叫，前者直接向后摔了出去。"
    y "「喔哟！」"
    "被一个正蹬踹中的那个同学，从我眼前飞过，直接砸进了堆满扫帚和拖把的卫生角里。"
    "这一下着实不轻，但还不足以被秒杀。"
    voice "audio/voice/050007.ogg"
    a "「\[哔——\]！」"
    "他挣扎着爬起身来，随手从身后抄起一把拖把，就这么胡乱朝对方抡去。"
    y "「我去！」"
    "我早就发现不对并且向后退却，但即便如此，拖把的布条还是几乎擦到了我的脸。"
    play sound "audio/sound/effect01.ogg" noloop
    with hpunch
    "「啪——」"
    "最终，抡出去的拖把没有命中他想要的目标，而是造成了一次严重的误伤。"
    "拖把头结结实实地砸在了黑板上面。即使有布头作为缓冲，玻璃材质的黑板还是迸出了一块巨大的碎痕。"
    y "「……」"
    l "「……」"
    c "「……」"
    "一时间，所有还留在教室里的人，除去正在打架的两个以外，全都被惊得呆住了。"
    "这俩人丝毫不在意周围的情形，只管歇斯底里地互殴。"
    "……没人劝，知道劝不住，也不敢上去劝。"
    play sound "audio/sound/effect07.ogg" noloop
    with hpunch
    "「噼里啪啦！！！」"
    play sound "audio/sound/effect08.ogg" noloop
    with vpunch
    "「稀里哗啦！！！」"
    play sound "audio/sound/effect02.ogg" noloop
    with hpunch
    "被拖把戳了几下以后，那位彪悍飞踹的同学也不甘示弱，居然举起了椅子朝对方砸去。"
    y "「（喂喂喂，这下子你们俩可玩大了啊！）」"
    "拖把还好说，那铁腿的椅子要是挨上一下，可不是闹着玩的。"
    "我已经能想象到待会儿班主任的脸色是什么样子了……只能说，但愿别伤人吧。"

    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    voice "audio/voice/000008.ogg"
    l "「你们……你们住手！！」"
    hide chara
    with dissolve
    "突然，梁芷柔从我的身边掠过，随后停留在了战场的外围。"
    "她应该是从震惊之中缓了过来，继而想要接着去劝架。"
    "只不过，她试了好几次，都没能进一步靠近。"
    "两边的械斗进入白热化，已经是什么都不管不顾了，压根就没有她能介入的余地。"
    "而且，这种试图接近的行为也很危险，就比如——"
    voice "audio/voice/050008.ogg"
    a "「你\[哔——\]！」"
    "攻守之间，那两个人的位置是在不断变化的。"
    "这一次抡拖把的向后退了一点，将拖把向后甩，开始蓄力。"
    "「呼——」"
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
    "这一甩的范围，恰好将梁芷柔的位置包含进去。"
    y "「小心！」"
    voice "audio/voice/000009.ogg"
    l "「呀！」"
    "眼看着她因为出乎意料而不及躲避，我顾不上多想，上前一把抓住梁芷柔的胳膊，用力将她向后拽了一步。"
    hide chara
    with dissolve
    play sound "audio/sound/effect07.ogg" noloop
    with hpunch
    "「呼——」"
    "拖把擦着梁芷柔的脸蛋，险险地甩了过去。"
    y "「妈的你们俩看着点！」"
    voice "audio/voice/050009.ogg"
    a "「我\[哔——\]！」"
    voice "audio/voice/060006.ogg"
    b "「你\[哔——\]！」"
    "完全被无视了。"
    "打成这样，就算是班主任来了也不管用了吧……"
    show chara a07b #梁芷柔立绘|夏季校服|消沉2
    with dissolve
    "看了一眼旁边的梁芷柔，她似乎被这一下吓得不轻，一时间又僵在那里，无法动弹了。"
    "虽然平时是气势满满的班长，不过这种时候，她倒是和普通的女孩子别无二致。"
    "说起来，我的手还攥着梁芷柔的胳膊。"
    "明明是非常纤细的手臂，传来的手感却十分柔软，女生果然是……"
    y "「（嗯……不对，我他妈这是在想什么呢？这可不是走神的时候！！）」"
    y "「（还是先接着往后退吧……到一个安全一点的地方……）」"
    y "「（……嗯？）」"
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
    voice "audio/voice/000010.ogg"
    l "「咝——」"
    "才刚刚把乱七八糟的思绪都抛到脑后，就看到梁芷柔倒吸着凉气露出惊恐的表情。"
    y "「怎么了……我\[哔——\]！！」"
    hide chara
    with dissolve
    "顺着她的视线看去，我也吓了一跳。"
    "拿椅子的那一位，似乎是觉得光是上下砸不太方便，索性也抓着椅子背抡了起来。"
    "椅子可比拖把沉多了，面积也大得多，抡起来那叫一个虎虎生风。附近的桌面纷纷惨遭蹂躏，无一幸免。"
    voice "audio/voice/060009.ogg"
    b "「去死！」"
    voice "audio/voice/060008.ogg"
    a "「\[哔——\]！」"
    play sound "audio/sound/effect08.ogg" noloop
    with vpunch
    "结果——"
    "他抡起来的椅子，被拖把挑了一下，改变了方向又没有拿稳，脱手了。"
    "椅子划出了一道夸张的弧线，飞向了——"
    "我们。"

    stop music
    scene bg black #黑屏
    with fade
    "正所谓飞来横祸。"
    "如果被砸中的话，一定会很疼。"
    "破相都是小事了，说不定脑瓜会直接开瓢，砸出个三长两短来也不是没有可能。"
    "如果这只铁椅继续沿着现有的轨迹飞行，肯定会砸中我们两个。"
    "——接住它？"
    "不可能。这玩意又沉又快，徒手去接无异于螳臂当车，挡不住的。"
    "——那，躲开？"
    "也许可以吧？至少我自己应该是能够躲得开的。但是……"
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
    "我突然感觉到，手中攥着的那只柔软的手臂，因为害怕而紧绷了起来。"
    "余光能够看到，那张秀美的脸庞正在因为紧张而变得煞白，整个人吓得连叫都叫不出来了，只能下意识地闭上眼睛。"
    "是的。"
    "还有这样的一个女生，正站在我的身边。"
    hide chara
    with dissolve
    "——身体，下意识地做出了动作。"
    y "「——小心！！！」"
    play sound "audio/sound/effect02.ogg" noloop
    with hpunch
    scene bg black #黑屏
    with fade
    pause
    scene cg02a #梁芷柔被压倒CG-1|标准|视角拉近|CG02a
    with fade
    "勉强睁开眼睛，看到了一张惊慌失措的面孔。"
    "她被我按倒在身旁的桌子上，压在了身下。"
    "我的左手还在抓着她的胳膊，右手则撑在她肩膀旁边。"
    "脸对着脸，距离只有几厘米。"
    "在她的脸上，有几滴鲜红的血液。"
    "而更多的鲜血，还在星星点点地洒向她的脸庞。"
    "那是——我的血吗？"

    scene bg black #黑屏
    with fade
    "深吸一口气。"
    "松开左手、右臂用力地撑起身体，让自己离她的距离稍微远了一些。"

    scene cg02a1 #梁芷柔被压倒CG-1|标准|CG02a1
    with fade
    y "「噫……！」"

    scene bg black #黑屏
    with fade
    "头脑一阵发昏。"
    "原本因为甫遭重击，还没有立即体现出来的疼痛感，全都伴随着这个动作回到了我的身上。"

    scene cg02b #梁芷柔被压倒CG-2|半起身|视角拉远|CG02b
    with fade
    "在最后的那一刻，我把梁芷柔拉到了身后，自己挡在了前面。"
    "椅子的一条铁腿结实地命中了额头，也刮破了侧脸。"
    "现在我整个右脸都热辣辣的，血顺着脑门流下，几乎糊住了眼睛。"
    "不过，梁芷柔也因此得以毫发无损。"

    scene bg b01 #教室
    with fade
    y "「……」"
    y "「怎么样，满意了吧？」"
    "我扭过头，凶神恶煞地瞪着那两个始作俑者。"
    a "「……」"
    b "「……」"
    "不知是被我吓到了，还是也在心生悔意，总之这一眼的效果相当的好，那两个人都默不作声地低下了头。"
    "看起来，战争结束了。"
    "交战双方损害轻微，无辜百姓伤亡惨重。"
    "真是岂有此理……"
    "这个时候，一只温软的小手拉住了我的左臂。"
    voice "audio/voice/000011.ogg"
    l "「你……你还好吗？」"

    scene cg02b1 #梁芷柔被压倒CG-1|标准|担心|CG02b1
    with fade
    "低下头，与梁芷柔的目光相交。"
    "方才还满是惊慌的神色，此时已经变成了关切。"
    y "「嗯……」"
    y "「还好……」"
    "说出了有些违心的话……其实头还是挺晕的。"
    "不过按照英雄救美的模板来说，这个时候别管自己伤成什么德行，也要边摆POSE边说出「我没事」来才对。"
    "不死模式全力全开。这一刻阿诺·施瓦\[哔——\]、西尔维斯特·史\[哔——\]、布鲁斯·威\[哔——\]灵魂附体。"
    y "「应该问题不大吧，待会去医务室看看。」"
    y "「你呢，没受伤吧。」"
    voice "audio/voice/000012.ogg"
    l "「哎？」"
    voice "audio/voice/000013.ogg"
    l "「我……我没事……」"
    voice "audio/voice/000014.ogg"
    l "「我是没事，可是你……」"
    scene bg b01 #教室
    with fade
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
    "梁芷柔一边担心地问着我的情况，一边努力想要把我扶起来。"
    "你看，这种套路虽然烂俗，但自有其道理。"
    "这好感度，刷得蹭蹭的。"
    "但是……"
    y "「啊……」"
    scene bg b01 #教室
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with fade
    scene bg b01 #教室
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with fade
    "突然之间，眩晕感再次变得剧烈。"
    "眼前发黑，视野一片模糊，完全丢失了距离感，也失去了重心。"
    "想要强行支撑住自己，但身体却不听使唤。"
    voice "audio/voice/000015.ogg"
    l "「哎？」"
    voice "audio/voice/000016.ogg"
    l "「叶……叶雨潇？」"
    voice "audio/voice/000017.ogg"
    l "「你怎么了？没事吧？」"
    "想要回答没事，但张了张嘴，却说不出话来。"
    "头脑突然变得好沉，眼前的场景也开始旋转起来。"
    voice "audio/voice/000018.ogg"
    l "「喂！？」"

    #### TODO: 演出效果Check #########################

    ## Note:
    #  1. linear 0.7 zoom 2.0 表示 0.7秒内放大两倍
    #     如想自行修改可以更改0.7的数值和2.0的数值
    #     如有问题欢迎来提出
    #  2. anchor 和 align是修改描点和显示位置，此处
    #     已修改好以达到面对 中下部分的放大效果
    #教室
    scene bg b01:
        anchor(0.5, 1.0) align(0.5, 1.0)
        linear 0.7 zoom 2.0
    #梁芷柔立绘|夏季校服|吃惊
    show chara a06:
        anchor(0.5, 1.0) align(0.5, 1.0)
        linear 0.7 zoom 2.0
    pause 0.5

    ## Note:
    #  1. 此处我用了黑屏结尾，如果需要可以直接删除此段以直接
    #     进入下方的scene bg b01；
    #  2. 还是请无比保留 pause 0.5以维持演出效果（？）或者
    #     也可以直接pause，表示等待点击然后继续进行游戏
    scene bg black
    with fade

    pause 0.5

    #### End TODO: 结束演出效果Check的更改 #################

    "身体直直地扑倒，随即摔在一个柔软的怀抱之中。"
    voice "audio/voice/000019.ogg"
    l "「叶雨潇！！」"
    voice "audio/voice/000020.ogg"
    l "「你怎么了，你醒醒啊！」"
    "眼前一片黑暗。"
    "耳边传来梁芷柔慌乱不已的呼喊声。"
    voice "audio/voice/000021.ogg"
    l "「——！！」"
    "只是，慢慢地，这个声音也变得越来越模糊，直到最后，一切都归于昏暗。"
    "……"
    "…………"

    scene bg indistinct #白色朦胧
    with fade

    "……"
    "…………"

    play sound "audio/sound/ambientnoise02.ogg" fadein 1.5 loop #医院走廊环境噪音
    #医生
    voice "audio/voice/040001.ogg"
    who "「……病人昏迷多长时间了？」"
    #老师
    voice "audio/voice/010007.ogg"
    who "「20分钟，他脑袋被砸了一下，然后晕倒了，我们就立刻把他送过来了，您看……」"
    #医生
    voice "audio/voice/040002.ogg"
    who "「哎哟，这么大一块……被什么东西砸的？」"
    #老师
    voice "audio/voice/010008.ogg"
    who "「一把椅子。」"
    #医生
    voice "audio/voice/040003.ogg"
    who "「哦，来，您让一让……来，把他放床上。」"
    #老师
    voice "audio/voice/010009.ogg"
    who "「大夫，您看他这情况……严重吗？」"
    #医生
    voice "audio/voice/040004.ogg"
    who "「……」"
    #医生
    voice "audio/voice/040005.ogg"
    who "「现在这样看不出来，得先清理一下。」"
    #医生
    voice "audio/voice/040006.ogg"
    who "「来，您先靠边一点。」"
    #老师
    voice "audio/voice/010010.ogg"
    who "「哦、哦……」"

    scene bg indistinct #白色朦胧
    with fade
    #医生
    who "「……」"
    #医生
    who "「…………」"
    #老师
    voice "audio/voice/010011.ogg"
    who "「……大夫？」"
    #医生
    voice "audio/voice/040007.ogg"
    who "「瞳孔正常。」"
    scene bg black #黑屏
    with fade
    #医生
    voice "audio/voice/040008.ogg"
    who "「您别堵在这儿……小李，跟CT说一声，待会儿得拍个片子。」"
    #护士
    voice "audio/voice/070001.ogg"
    who "「哦！」"
    #医生
    who "「……」"
    #医生
    voice "audio/voice/040009.ogg"
    who "「同学，这位同学！」"
    #医生
    voice "audio/voice/040010.ogg"
    who "「你听得见我说话吗？同学！」"
    y "「……」"
    y "「唔……唔…………」"
    #医生
    voice "audio/voice/040011.ogg"
    who "「同学？能听见吗？你能听见我说话吗？同学！」"
    y "「哎……啊……」"
    scene bg indistinct #白色朦胧
    with fade
    #医生
    voice "audio/voice/040012.ogg"
    who "「同学？」"
    #老师
    voice "audio/voice/010012.ogg"
    who "「叶雨潇！」"
    y "「……郑……老师？」"
    voice "audio/voice/010013.ogg"
    z "「对对对！是我呀！哎呀太好了，你可算是醒了！」"
    y "「我这是……」"
    voice "audio/voice/010014.ogg"
    z "「你现在在医院呢。放心，没事的，啊！」"
    y "「啊……」"
    #医生
    voice "audio/voice/040013.ogg"
    who "「你现在感觉怎么样，头疼吗？」"
    y "「……嗯……」"
    #医生
    voice "audio/voice/040014.ogg"
    who "「还有什么感觉没有？」"
    #医生
    voice "audio/voice/040015.ogg"
    who "「能不能看清我？」"
    y "「……」"
    y "「有点模糊……」"
    scene bg indistinct #白色朦胧
    with fade
    y "「……」"
    #医生
    voice "audio/voice/040016.ogg"
    who "「想得起来是因为什么受的伤吗？」"
    y "「我……」"
    y "「……被椅子砸了一下？」"
    scene bg indistinct #白色朦胧
    with fade
    y "「嘶……」"
    #医生
    voice "audio/voice/040017.ogg"
    who "「怎么啦？」"
    scene bg indistinct #白色朦胧
    with fade
    y "「头……头疼……」"
    #医生
    voice "audio/voice/040018.ogg"
    who "「没事，这是正常的！放松一点，没事的，啊！」"
    #医生
    voice "audio/voice/040019.ogg"
    who "「别想事情，放松！要是觉得眼睛睁开难受就别睁了，啊！」"
    #医生
    voice "audio/voice/040020.ogg"
    who "「……好了，送CT。」"
    "……"
    "…………"

    stop sound fadeout 1.5

    scene bg black #黑屏
    with fade
    "脑袋昏昏沉沉的。"
    "只感觉周围乱糟糟的，似乎有很多人来来往往，时不时说些什么，甚至偶尔还会问我几句话。"
    "似乎是下意识地做出了回答……但是被问了什么，又答了什么，我自己一点概念都没有。"
    "再往后就是被人搬来搬去，掰手掰脚，也不知是在做什么检查。"
    "中途也曾尝试着想要让自己清醒一点，然而头很疼，疼到连思考的力气都没有，最后只能闭着眼睛任人摆布了。"
    "……然后，渐渐的，再一次陷入昏睡。"
    "……"
    "…………"

    scene bg indistinct #白色朦胧
    with fade
    "……"
    "…………"
    #梁芷柔
    voice "audio/voice/000022.ogg"
    who "「……啊，郑老师……」"
    #老师
    voice "audio/voice/010015.ogg"
    who "「……咦，你怎么来了？那边已经下课啦……」"
    #梁芷柔
    voice "audio/voice/000023.ogg"
    who "「……嗯，我有点担心，所以过来看看他……」"
    #梁芷柔
    voice "audio/voice/000024.ogg"
    who "「……他情况怎么样啊……」"
    #老师
    voice "audio/voice/010016.ogg"
    who "「……医生说应该问题不大，啊，但是得观察一段时间……」"
    #老师
    voice "audio/voice/010017.ogg"
    who "「……之前醒过一次，现在应该是又睡着了……」"
    #老师
    voice "audio/voice/010018.ogg"
    who "「……让他好好休息吧。你在这儿等着也没用，要不然也先回去吧？……」"
    #梁芷柔
    voice "audio/voice/000025.ogg"
    who "「……嗯……老师，我还是想再等等吧……」"
    "……"
    "…………"

    scene bg indistinct #白色朦胧
    with fade
    "……"
    "…………"
    play sound "audio/sound/effect03.ogg" noloop
    who "「……」"
    stop sound
    #老师
    voice "audio/voice/010019.ogg"
    who "「……喂？……」"
    #老师
    voice "audio/voice/010020.ogg"
    who "「……什么情况啊？……」"
    #老师
    voice "audio/voice/010021.ogg"
    who "「……我现在在医院呢，我们班学生受伤了……」"
    #老师
    voice "audio/voice/010022.ogg"
    who "「……非得我去吗？我哪走得开啊……啊？让老鲁来替我？那行吧，我等他……什么啊，至于这么急吗？……」"
    #老师
    voice "audio/voice/010023.ogg"
    who "「……好好好，我这就回去，你让老鲁快着点啊……」"
    #老师
    who "「…………」"
    #老师
    voice "audio/voice/010024.ogg"
    who "「……哎，真是的……」"
    #梁芷柔
    voice "audio/voice/000026.ogg"
    who "「……郑老师，您有事就先过去吧，我在这里盯着……」"
    #老师
    voice "audio/voice/010025.ogg"
    who "「……唉，也只能这样了。鲁老师呢，一会儿就过来，你帮忙盯一会儿就行，啊。有事给我打电话啊……」"
    "……"
    "…………"

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    play sound "audio/sound/ambientnoise03.ogg" fadein 1.5 loop #傍晚环境噪音
    scene bg b03 #病房
    with fade
    y "「……」"
    y "「…………」"
    "当我再次睁开眼睛的时候，映入眼底的，是一片单一的色彩。"
    "从天花板到窗帘再到床单被罩都被夕阳染成了柔软的橘色。"
    y "「（这里是……）」"
    "四周静悄悄的，空气中弥漫着淡淡的消毒水味道。"
    "微风偶尔从半开的窗口拂进房间，将窗帘轻轻掀起，漏入更多的金色光芒。"
    y "「（……是医院啊。）」"
    "原来如此。"
    "大致上理解了自己的处境。"
    "说到底，我既不是终\[哔——\]者，也不是\[哔——\]博或者麦克莱\[哔——\]，挨了那么重的一下子，晕过去才是比较正常的结果。"
    y "「（不过，这样一来……）」"
    "要完蛋。根本不知道该怎么和爸妈交代。"
    "虽然受伤不是我的错，但不管怎么说都会让父母担惊受怕。"
    "老爸那里应该还好说，但是老妈肯定会先紧张得要死，然后等我没事了之后又大发雷霆咆哮不止吧。"
    y "「（……估计耳朵又要被磨出茧子来了。）」"
    "说起来，现在是什么时候了？"

    y "「……」"
    "病房里没有钟表，看不出具体的时间，只能凭着窗外的光亮判断出天还没有黑。"
    "一个下午不省人事……这大概是我有生以来受的最严重的伤了吧？"
    "啊……如果只是几个小时倒也还好了，就怕像以前听到过的某些故事里说的那样，一次昏迷，醒来之后却发现已经过了三年什么的……"
    y "「……」"
    "不会有那种事的吧。"
    "不过是一个椅子罢了，又不是在电话亭边上被卡车给撞了。"

    y "「（……咦！？）」"
    "当我试图将头转向另一侧的时候，看到了一个意想不到的人。"

    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fade
    l "「……」"
    "梁芷柔。"
    "不知为何，梁芷柔正坐在我病床旁边的椅子上。"

    scene bg b03 #病房
    with fade
    y "「（这是怎么回事？）」"
    "虽然之前自己的神智不算清醒，但隐约记得是班主任老师把我送到医院来的……"
    "然而，醒来以后看到的人却是梁芷柔？"
    "看看周围……似乎病房里就只看到了她一个人。"
    y "「……」"
    "抱着疑惑，我再次望向梁芷柔。"

    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fade
    "梁芷柔正在专心致志地看着书，并没有注意到我的视线。"
    "……真是相当集中的注意力。"
    "从小到大，「全神贯注」、「专心致志」的口号连听带喊了不知多少遍，但实话实说，我从未想到过一个人居然真的可以如此心无旁骛。"
    "说起来，虽然以前在学校的时候也经常能够见到她认真学习的样子，但是现在和那些时候的感觉完全不同。"
    "或许是因为之前我还在昏睡，她身处独自一人的环境吧？此时此刻的梁芷柔，全部的精力都集中在了自己手中的书本上。"
    "除了偶尔翻页以外，几乎没有别的动作。甚至于在很多时候，如果不是她还在眨眼，瞳孔也在随着视线微微移动，我都会以为眼前的少女只是一个人偶。"
    "一个精致无比，而又动人心魄的人偶。"
    "……"
    "…………"

    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fade
    "一个人专注的样子，总是有一种独特的魅力的。"
    "我在不知不觉之间，被梁芷柔的这种魅力所吸引，就这样一直忘我地看着她。"
    "在如此近的距离下，长时间地观察一个女生，这对我来说还是第一次。"
    "越是看得仔细，越是难以自拔。"
    "少女认真的神情与姣美的容颜，搭配出一幅完美的画面。"
    "由于太过完美，反而渐渐生出一种如梦似幻的感觉。"
    "仿佛只要稍稍碰触，眼前这一切便会如同泡沫一般骤然破碎，再也不复存在。"
    "所以，我一动也不敢动。"
    "……"
    "…………"

    scene bg black #黑屏
    with fade
    play sound "audio/sound/effect04.ogg" noloop
    "忽然，一股突如其来的夏风，毫无征兆地挑开了窗帘。"

    scene cg03b #梁芷柔探病CG-2|起风|CG03b
    with fade
    voice "audio/voice/000027.ogg"
    l "「啊……」"
    "整个空间，仿佛都被惊醒了。"
    "夕阳的余晖瞬间铺满了病房的每一个角落，数不清的细碎花瓣从窗外闯入，在半空四散纷飞。"
    "少女的一头青丝随着风的节奏翩然起舞，她伸手轻轻压住一侧，试图拢住散乱的发丝，原本如同象牙般白皙的胳膊被日照抹过，镀上了一层金黄色的光晕，显得华丽而圣洁。"
    y "「……」"

    scene bg black #黑屏
    with fade
    "一瞬间，就好像有一根羽毛在心脏最敏感的地方轻轻划过一般。"
    "在内心的最深处，某些曾经被自己深深掩盖起来的东西，似乎，在这一刻，有了些许松动的迹象。"
    "……"
    "…………"
    voice "audio/voice/000028.ogg"
    l "「……咦？」"
    scene cg03c #梁芷柔探病CG-3|对视|CG03c
    with fade
    y "「哎？……呃。」"
    "回过神来，发现……不知什么时候，梁芷柔的目光已经转移到我这边来了。"
    "于是，四目相对。"
    y "「……」"
    l "「……」"
    "以及，相顾无言。"

    scene cg03c1 #梁芷柔探病CG-3|对视|惊讶|CG03c1
    y "「啊……哈哈。」"
    "梁芷柔惊讶地瞪大了眼睛，而我只能勉强干笑了两声。"
    "……为什么我每次偷看她都会被抓现行？"
    "这就他妈的尴……"
    voice "audio/voice/000029.ogg"
    l "「你醒了！？」"

    play sound "audio/sound/effect05.ogg" noloop
    scene cg03e #梁芷柔探病CG-5|靠近|CG03e
    with vpunch
    "不过，梁芷柔似乎对此并不关心。她反应过来以后，直接一下子扑到我的床边。"
    "由于起身的时候用力过猛，差点连椅子都掀翻了。"
    "她却恍若未闻，只顾翻来覆去地打量着我的脑袋。"
    voice "audio/voice/000030.ogg"
    l "「你感觉怎么样？脑袋难受吗？疼不疼啊？」"
    voice "audio/voice/000031.ogg"
    l "「什么时候醒过来的？还有哪儿不舒服吗？」"
    "随之而来的，还有一大串连珠炮似的问话。"
    y "「啊这……」"
    "不过她似乎也没打算等我回应。"
    voice "audio/voice/000032.ogg"
    l "「你等着，我去叫医生！」"
    "扔下这句话，梁芷柔撒腿就往外跑。"

    scene bg b03 #病房
    with fade
    y "「……」"
    y "「什么鬼。」"
    "留下我一个人，面对着重新安静下来的病房，一头雾水。"
    "……"
    "…………"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    scene bg b03 #病房
    with fade
    voice "audio/voice/040021.ogg"
    az "「……大致就是这样了，有一点脑震荡，问题不算大。」"
    voice "audio/voice/040022.ogg"
    az "「可能之后一段时间会有些头疼、恶心之类的症状，一般过两天就能恢复，保险起见这两天还是留院观察一下比较好……」"
    "……"
    "…………"
    voice "audio/voice/040023.ogg"
    az "「……总之，感觉有不舒服或者其他什么的要及时说。」"
    "在这之后，梁芷柔很快叫来了医生，对我做了个简单地检查。"
    "情况似乎比我预想的要好一些，虽然样子吓人，但还是避开了要害，实际伤害也没有看上去那么重。"
    "最后，医生很淡定地做出了住院观察的结论。"
    "我也是松了一口气。虽然今天灾难连连，不过结果还算是影响不大，至少我高中的最后一个暑假还没有被耽误。"
    "后天出院的话，正好是暑假的第一天。反正就算我毫发无损，那天也肯定是睡到日上三竿再说，所以没啥区别。"
    "不过……"
    show chara la08a #梁芷柔立绘|夏季校服|担心1|近
    with dissolve
    voice "audio/voice/000033.ogg"
    l "「呼……太好了。」"
    voice "audio/voice/000034.ogg"
    l "「没事就好！」"
    "你怎么看上去比我还要多松了一口气啊！"
    "说到底，梁芷柔为什么会在这里，我直到现在都还没搞明白呢。"
    "不只是我在疑惑，医生似乎也受到了误导。"
    voice "audio/voice/040024.ogg"
    az "「啊，对了，你是家属吧？是你弟弟吗？」"
    show chara la06 #梁芷柔立绘|夏季校服|吃惊|近
    with dissolve
    voice "audio/voice/000035.ogg"
    l "「唉？」"
    voice "audio/voice/040025.ogg"
    az "「我知道你很担心他，我也能理解你的心情。」"
    voice "audio/voice/000036.ogg"
    l "「呃……」"
    voice "audio/voice/040026.ogg"
    az "「他现在的情况呢，虽然不严重，但是需要静养。」"
    show chara la02 #梁芷柔立绘|夏季校服|皱眉|近
    with dissolve
    voice "audio/voice/000037.ogg"
    l "「啊……那个……」"
    voice "audio/voice/040027.ogg"
    az "「所以陪护的时候也尽量保持安静，别和病人说太多的话，尽量让他好好休息。」"
    l "「……」"
    show chara la01b #梁芷柔立绘|夏季校服|普通|侧面|近
    with dissolve
    voice "audio/voice/000038.ogg"
    l "「嗯。」"
    voice "audio/voice/040028.ogg"
    az "「如果可能的话，还是让他多睡一会儿……」"
    hide chara
    voice "audio/voice/070002.ogg"
    k "「笮大夫！笮大夫！」"
    voice "audio/voice/040029.ogg"
    az "「怎么了？小李？」"
    voice "audio/voice/070003.ogg"
    k "「有急诊病人，您得过来一下！」"
    voice "audio/voice/040030.ogg"
    az "「好，我知道了。」"
    voice "audio/voice/040031.ogg"
    az "「……我得先离开一下，如果伤情有了反复，随时叫护士。晚上值班室也有人。」"
    voice "audio/voice/000039.ogg"
    l "「好的，谢谢您。」"
    "医生点点头，转身离开了。"
    show chara la01a #梁芷柔立绘|夏季校服|普通|正面|近
    with dissolve
    "梁芷柔朝医生微微鞠躬表示感谢，然后转回头来，似笑非笑的看着我。"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve

    stop music fadeout 1.5

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    y "「……」"
    l "「……」"
    y "「……」"
    l "「……」"
    y "「……看啥啊。」"
    voice "audio/voice/000040.ogg"
    l "「嘻，没事。」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/000041.ogg"
    l "「好好休息吧，弟弟。」"
    y "「……谁啊那是。」"
    voice "audio/voice/000042.ogg"
    l "「不是你吗？」"
    voice "audio/voice/000043.ogg"
    l "「乖，叫姐姐。」"
    y "「……」"
    "对不起，这个时候，我不知道该用什么表情。"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/000044.ogg"
    l "「嘻嘻，我是独生子女啊，偶尔也会想有个弟弟呢。」"
    y "「我也是啊，不过是想要有个妹妹。」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/000045.ogg"
    l "「不不不，我觉得姐弟比较好。」"
    y "「兄妹才是最好的搭配啊！」"
    show chara la03 #梁芷柔立绘|夏季校服|生气|近
    with dissolve
    voice "audio/voice/000046.ogg"
    l "「……妹控！」"
    y "「你好意思说我吗！？还有你是到底是几月的生日啊？」"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/000047.ogg"
    l "「11月啊，10号。」"
    y "「哪年的？」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/000048.ogg"
    l "「和你一样啊！」"
    y "「……」"
    l "「……」"
    y "「那不还是比我小吗！！？」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/000049.ogg"
    l "「啊……哈哈。」"
    y "「哈你个头啊！」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/000050.ogg"
    l "「好啦好啦，要知道我辈同门之间，不以年龄为长，而是以入门先后……不对，成绩高低区分长幼啊！」"
    y "「……喂！」"
    voice "audio/voice/000051.ogg"
    l "「嘻嘻。」"

    stop music
    show chara a11 #梁芷柔立绘|夏季校服|微笑
    with dissolve
    voice "audio/voice/000052.ogg"
    l "「好好休息吧，鲁老师一会儿就过来。啊，你家里也联系上了，叔叔好像下乡去了，现在正在往城里赶，可能得晚一点才能过来。」"
    "的确，老爸今天因为工作要下到乡里，距离县城颇有一段距离。至于老妈，目前人应该在省城，今天是回不来的。"
    y "「哦……说起来我还没搞明白呢，怎么是你在这儿？郑老师呢？我记得好像是他把我送过来的？」"
    show chara a01a #梁芷柔立绘|夏季校服|普通|正面
    with dissolve
    voice "audio/voice/000053.ogg"
    l "「啊，对。郑老师被学校叫回去了，好像是有急事。」"
    voice "audio/voice/000054.ogg"
    l "「至于我呢，其实没过来多久，学校刚放学。」"
    y "「所以说为啥你要过来啊？」"
    show chara a07a #梁芷柔立绘|夏季校服|消沉1
    with dissolve
    voice "audio/voice/000055.ogg"
    l "「这不是……担心你嘛！」"
    voice "audio/voice/000056.ogg"
    l "「毕竟，你是……为了保护我才受的伤。」"
    l "「……」"
    show chara a05b #梁芷柔立绘|夏季校服|苦笑2
    with dissolve
    voice "audio/voice/000057.ogg"
    l "「谢谢你。」"
    "梁芷柔十分郑重地向我道谢。"
    "由于太过正式，反倒是让我有些不知所措起来。"
    y "「啊……不，没什么。」"
    y "「其实我当时也没想那么多，就是下意识地挡了一下……你没受伤就好，你看我这不也没什么大事么……」"
    y "「别弄得这么严肃，怪不好意思的。」"
    #背景左移
    "不知为何突然害羞起来了，忍不住将目光游离到别处。"
    voice "audio/voice/000058.ogg"
    l "「呵。」"
    #背景恢复
    show chara a05a #梁芷柔立绘|夏季校服|苦笑1
    with dissolve
    voice "audio/voice/000059.ogg"
    l "「好吧，总之……」"
    show chara a11 #梁芷柔立绘|夏季校服|微笑
    with dissolve
    voice "audio/voice/000060.ogg"
    l "「……还是得谢谢你。」"
    y "「……」"
    y "「嗯，不客气。」"
    voice "audio/voice/000061.ogg"
    l "「嗯。」"
    l "「……」"
    voice "audio/voice/000062.ogg"
    l "「哎，那个……」"
    y "「嗯？」"
    voice "audio/voice/000063.ogg"
    l "「啊，算了，没事。」"
    voice "audio/voice/000064.ogg"
    l "「你还是好好休息吧，医生说了不让你多说话。」"
    y "「……哦。」"
    "梁芷柔欲言又止。"
    "似乎是想和我多聊两句，但又怕影响到我休息的样子。"
    "……"
    "…………"

    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fade
    "接下来的时间里，梁芷柔又拿起了复习资料去看题，而我则躺在床上发呆。"
    "屋里再一次安静下来。"
    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fade

    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    "窗外传来微风轻拂枝叶的「簌簌」的声响，不时有鸟雀飞过，发出一两声鸣叫。"
    "何等安详的午后……之前中午那一段兵荒马乱的经历，就好像是虚幻的一般，已经完全没有感觉了。"
    "不过，有一些东西，似乎变得不同了。"
    y "「……」"
    l "「……」"
    y "「……」"
    scene cg03c2 #梁芷柔探病CG-3|对视|普通|CG03c2
    with fade
    voice "audio/voice/000065.ogg"
    l "「嗯，怎么了？」"
    "或许是因为才刚开始看书，还没那么投入，梁芷柔很快就注意到了我的目光，随即投来了询问的眼神。"
    y "「啊？啊，没什么。」"
    y "「就是觉得，感觉你好像和以前不太一样。」"
    voice "audio/voice/000066.ogg"
    l "「嗯……？」"
    scene cg03c3 #梁芷柔探病CG-3|对视|微笑|CG03c3
    voice "audio/voice/000067.ogg"
    l "「因为，从同学变成了姐姐？」"
    y "「……喂。」"
    voice "audio/voice/000068.ogg"
    l "「呵呵。」"
    "梁芷柔有些狡黠地笑笑。"
    "……"
    "…………"

    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fade
    "是的，眼前的女生。"
    "一个高入云端，可望而不可即的天骄，在这个午后，突然在我面前展现出了她平常的一面。"
    "不再是那种好学生的样本，而是一个也一样会笑、会怕、会嬉笑打趣、会紧张会担心……的鲜活生动的少女。"
    "我默默地望着读着复习资料的梁芷柔。"
    "看着她那张娟秀的脸。"
    "以前，像许多人一样，我曾经幻想过那种癞蛤蟆吃天鹅肉的故事。"
    "但是，也仅仅是想想罢了。"
    "彼此之间遥不可及的差距，让自认还算是有自知之明的我，从未真正尝试去向前走出过哪怕一步。"

    scene bg black #黑屏
    with fade
    "我不可能做到这种地步。"
    "我不可能站到和她一样的高度。"
    "我不可能……去憧憬与她同样的未来。"

    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fade
    "然而，此时此刻。"
    "在这个午后。"
    "我第一次……心中涌现出一股微小的冲动。"
    "向前迈步的冲动。"

    stop music fadeout 1.5
    scene bg black #黑屏
    with fade

    play sound "audio/sound/transition.ogg" noloop
    scene trans t01 #转场 教室
    with fade
    pause

#01.盛夏篇

    $ chapter = "01"

#次日。
#7月29日。

    scene bg black #黑屏
    with fade
    "第二天中午。"

    play sound "audio/sound/ambientnoise04.ogg" fadein 1.5 loop #白天环境噪音

    scene cg03d #梁芷柔探病CG-4|削苹果|CG03d
    with dissolve
    voice "audio/voice/001001.ogg"
    l "「～～～～」"
    y "「……」"
    voice "audio/voice/001002.ogg"
    l "「～～～～」"
    y "「……喂……」"
    voice "audio/voice/001003.ogg"
    l "「～～～～」"
    with hpunch
    y "「……喂！」"

    scene cg03d2 #梁芷柔探病CG-4|削苹果|对视|微笑|CG03d2
    with dissolve
    voice "audio/voice/001004.ogg"
    l "「嗯？怎么啦？」"
    y "「你这是干什么呢？」"
    voice "audio/voice/001005.ogg"
    l "「嗯？什么干什么？」"
    voice "audio/voice/001006.ogg"
    l "「啊你稍微等一下，马上就削好了，别急，我手笨，别催我。」"

    scene cg03d #梁芷柔探病CG-4|削苹果|CG03d
    with dissolve
    voice "audio/voice/001007.ogg"
    l "「～～～～」"
    y "「……」"
    y "「不是这个问题吧！？」"
    with hpunch
    y "「为什么你要来给我削苹果啊！？」"

    scene cg03d2 #梁芷柔探病CG-4|削苹果|对视|微笑|CG03d2
    with dissolve
    voice "audio/voice/001008.ogg"
    l "「吃水果对身体好哇。」"
    voice "audio/voice/001009.ogg"
    l "「啊，你不爱吃苹果吗？早说啊，还有梨呢。」"
    y "「不，我是说……」"
    voice "audio/voice/001010.ogg"
    l "「不过挑食可不好啊，听话啊，弟弟，乖。」"
    with hpunch
    y "「这个你还没玩够啊！？」"
    "说来这对话根本不在一个频道上吧，梁芷柔你故意的吗？"
    voice "audio/voice/001011.ogg"
    l "「嘻嘻……好啦好啦，不闹了。来，给你。」"

    play audio "audio/sound/effect09.ogg" noloop

    scene cg03f #梁芷柔探病CG-6|递苹果|CG03f
    with dissolve
    y "「……」"
    y "「唉……」"
    y "「谢谢。」"

    play audio "audio/sound/effect09.ogg" noloop

    scene cg03d1 #梁芷柔探病CG-4|削苹果|对视|CG03d1
    with dissolve
    voice "audio/voice/001012.ogg"
    l "「不客气。」"
    y "「所以说……这到底是个什么情况啊？」"
    voice "audio/voice/001013.ogg"
    l "「嗯……」"

    stop sound fadeout 1.0

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～

    scene bg b03a #病房|白天
    with fade
    "我向病房门口望去。"
    "……隐约能听到外面的大人们聊天的声音。"
    "此时此刻，我这间病房堪称门庭若市。"
    "除了本来就在此照顾我的父母以外，梁芷柔、她的父母、我们班的班主任老师，以及学校的一位年级主任也联袂而至。"
    "梁芷柔一家是来正式表示感谢的，而学校的领导和老师除了表达关心，还肩负着消除隐患的职责。"

    scene bg black #黑屏
    with fade
    "毕竟昨天那阵仗，把教室砸得一塌糊涂不说，还有人因此住进了医院，性质可以说是相当恶劣。这种事，一个处理不好就能搞出一个大新闻来，学校也免不了会被上级部门记上一笔、批判一番。"
    "所以学校方面当然是想保住脸面，尽量大事化小、内部消化，不要闹得满城皆知。好在现在梁芷柔毫发未损、我也没什么大事，剩下的就是怎么安抚的问题了。"
    "大人们之间总是要谈一谈的。当然，由于我需要静养，所以谈判的主战场转移到了外面，梁芷柔因为不需要参加，留在了房间里照看我。"

    scene bg b03a #病房|白天
    with fade
    "……也就造成了眼前这种让我甚感尴尬的局面。"

    scene cg03d1 #梁芷柔探病CG-4|削苹果|对视|CG03d1
    with fade
    "大人们……尤其是，双方的父母在外面聊天，单单把梁芷柔扔在这里给我削苹果，看起来简直像是……？"
    voice "audio/voice/001014.ogg"
    l "「怎么了？想什么呢？」"
    with vpunch
    y "「嗯？啊啊啊啊……没事！我走了个神。」"

    scene bg b03a #病房|白天
    with fade
    "我挪了挪身子，让自己坐得更直一些，视线也和梁芷柔平行。借着这一串动作，掩饰了自己的心情。"
    y "「我在想啊，你说付老师、郑老师他们打算怎么安慰我这颗受伤的，嗯，头皮啊？」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/001015.ogg"
    l "「……嘻嘻，这个我还真知道。听老师说，是打算给你一个优秀团员，县级的。」"
    y "「哎哟，听起来不错啊？」"
    show chara la01a #梁芷柔立绘|夏季校服|普通|正面|近
    with dissolve
    voice "audio/voice/001016.ogg"
    l "「嗯……怎么说好呢？马马虎虎吧。」"
    y "「啊，我又不能和你比。你是拿这些奖励拿到手软不在乎了，我可还是第一次呢？」"
    voice "audio/voice/001017.ogg"
    l "「嗯……就是因为你只拿了这一次呀。」"
    show chara la02 #梁芷柔立绘|夏季校服|皱眉|近
    with dissolve
    voice "audio/voice/001018.ogg"
    l "「这种东西吧，你要是拿了好几个，那履历确实会比较漂亮。但就这么一次的话，其实用处不大。」"
    voice "audio/voice/001019.ogg"
    l "「要说咱们学校也真够抠门的，出这么大的事，这么一块鸡肋就把你给打发了……」"
    voice "audio/voice/001020.ogg"
    l "「你还觉得挺好的。真是……惠而不费啊。」"
    y "「……呃。」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/001021.ogg"
    l "「嗯？怎么啦？干嘛用这种眼神看我？」"
    y "「没什么……只是没想到啊。」"
    y "「我还以为你挺看重这种……荣誉啊什么的，结果居然也这么会算计？」"
    show chara la03 #梁芷柔立绘|夏季校服|生气|近
    with dissolve
    voice "audio/voice/001022.ogg"
    l "「喂，什么叫算计呀，怎么跟姐姐说话呢？」"
    y "「喂喂喂没完了啊？」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/001023.ogg"
    l "「……本来就是嘛，不然呢？你以为我不食人间烟火啊？」"
    y "「那倒不是，但总觉得你应该和我这样的凡夫俗子有点不一样？」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/001024.ogg"
    l "「我啊，就是个普通人。」"
    voice "audio/voice/001025.ogg"
    l "「可能因为比较努力，学习成绩好一些，但除此之外，和大家没什么两样。」"
    voice "audio/voice/001026.ogg"
    l "「至于别的感觉……」"
    show chara la05a #梁芷柔立绘|夏季校服|苦笑1|近
    with dissolve
    voice "audio/voice/001027.ogg"
    l "「那就都是你自己的想象了。」"
    "落寞的神情，在梁芷柔的脸上一闪而过。"
    y "「呃——」"
    "但是，当我意识到自己说错话的时候，已经来不及补救了。"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/001028.ogg"
    l "「好啦！一提起学习，我还想起个事来。」"
    y "「嗯？」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    "梁芷柔一边摆出「我想起开心的事情」的笑容，一边从她的书包里拿出了一大摞什么东西。"

    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/001029.ogg"
    l "「……嗯……」"
    hide chara
    with dissolve
    l "「……」"
    show chara a11 #梁芷柔立绘|夏季校服|微笑
    with dissolve
    voice "audio/voice/001030.ogg"
    l "「来，给你！」"
    with hpunch
    y "「哎哟！」"
    "一大塑料袋书本被直接扔在了我的病床上……确切地说，是我的肚子上。"
    y "「这啥？」"

    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/001031.ogg"
    l "「你说呢？」"
    y "「我看看啊，《普通高中课程标准假期作业——语文》……」"
    y "「我的妈呀。」"
    "赤裸裸的报复……我果然惹她不高兴了吧？"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/001032.ogg"
    l "「嘻嘻，任务完成喽。」"
    y "「任务？」"
    voice "audio/voice/001033.ogg"
    l "「对啊，我是班长嘛，给请假的同学带学习资料是职责所在吧？」"
    y "「啊，也对。啧，本来还以为可以逃过去的……」"
    show chara la03 #梁芷柔立绘|夏季校服|生气|近
    with dissolve
    voice "audio/voice/001034.ogg"
    l "「少说废话，记得按时完成啊？别到最后那两天才火烧眉毛似的。」"
    voice "audio/voice/001035.ogg"
    l "「还有啊，不·许·抄·答·案！知道吗！」"
    "哇……突然迸发出班长的气势来了，吓得我直接缩了一下脖子。"
    "……某种意义上，这才是我比较熟悉的梁芷柔，以至于身体形成了条件反射。"
    y "「好好好、好好好，知道啦知道啦。」"
    y "「反正暑假作业老师也不会认真看……」"
    voice "audio/voice/001036.ogg"
    l "「叶！雨！潇！」"
    y "「…………好吧，我错了。」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/001037.ogg"
    l "「……唉。」"
    voice "audio/voice/001038.ogg"
    l "「说实在的，一个暑假作业而已，能有多麻烦啊，你的成绩又不差……多上点心吧，没坏处。」"
    y "「是……」"
    "看来是戳到学霸的逆鳞了，这种时候还是先别犟嘴为好。"
    "当然，具体之后怎么做嘛……"
    voice "audio/voice/001039.ogg"
    l "「……」"
    show chara la02 #梁芷柔立绘|夏季校服|皱眉|近
    with dissolve
    voice "audio/voice/001040.ogg"
    l "「唉……『现在先敷衍过去，反正之后她也管不了我』？」"
    y "「嘎！？」"
    voice "audio/voice/001041.ogg"
    l "「你啊，你这点想法，就差直接拿笔写在脑门上了。」"
    y "「啊，哈、哈哈……」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/001042.ogg"
    l "「你说你，挺聪明的一个人，怎么就老是……哎。」"
    voice "audio/voice/001043.ogg"
    l "「早晚有一天你得后悔！」"
    "看着梁芷柔一脸怒其不争的模样，我忍不住辩解起来。"
    y "「喂喂我冤枉啊，我怎么就聪明啦？我笨着呢，可笨了。」"
    voice "audio/voice/001044.ogg"
    l "「呵。你要是真笨，那早就不是现在这个成绩了。你什么情况你自己不清楚吗？」"
    voice "audio/voice/001045.ogg"
    l "「就你现在这样，还能考到这个分数，你啊，脑袋好着呢。」"
    y "「真不是，我真没那个天赋。初中的时候还好，到了高中就跟不上了。」"
    y "「而且我也不是没努过力啊，要不中考的时候也不可能从三中考过来对不对？」"
    show chara la06 #梁芷柔立绘|夏季校服|吃惊|近
    with dissolve
    voice "audio/voice/001046.ogg"
    l "「喔……你初中是在三中啊？」"
    y "「对啊，我初三的时候可是正儿八经拼了一年的命，本来也就是留校，结果硬是考到一中来了。」"
    voice "audio/voice/001047.ogg"
    l "「那到了高中怎么不继续了？」"
    y "「这你就是冤枉我了啊。我不是没继续，但成绩上不去啊！咱就这水平，你说怎么办？」"
    show chara la02 #梁芷柔立绘|夏季校服|皱眉|近
    with dissolve
    voice "audio/voice/001048.ogg"
    l "「……」"
    "听完我的话，梁芷柔沉默了下来，微微皱眉，似乎在思考什么。"
    voice "audio/voice/001049.ogg"
    l "「看来还不单是心态的问题……」"
    y "「嗯？什么？」"
    voice "audio/voice/001050.ogg"
    l "「嗯……我在想，大概是学习方式有问题吧？」"
    y "「哎哟，那学霸有啥高招，指点一下？」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/001051.ogg"
    l "「嘁，怎么跟你说啊，这又不是三言两语能说得完的。」"
    y "「小气啊，你可还是我姐姐呢，刚才叫了那么半天的弟弟，现在弟弟有难你不救，这可不行啊？」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/001052.ogg"
    l "「嘿、嘿、嘿！这时候知道叫姐姐啦？你说说你……呵呵……」"
    show chara la01b #梁芷柔立绘|夏季校服|普通|侧面|近
    with dissolve
    voice "audio/voice/001053.ogg"
    l "「不过啊，说正经的，咱们班……可能咱们学校都是，跟你的情况差不多，这个问题是通病。」"
    voice "audio/voice/001054.ogg"
    l "「就连我也是，最开始其实也一样，这两年才有点改变。」"
    voice "audio/voice/001055.ogg"
    l "「嗯……至于你，嗯，怎么说呢，我教你当然是可以啊！」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/001056.ogg"
    l "「不过，你可想清楚了，你真的要我教你嘛？」"
    y "「哎？干嘛啊，你有什么阴谋？」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/001057.ogg"
    l "「阴谋是没有啦，不过我可是每天都得开课的，你的暑假大概就泡汤喽？」"
    y "「呃……」"
    y "「为什么每天都要……」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/001058.ogg"
    l "「时间紧，能赶一点是一点嘛！你想想，距离高考也就不到一年了，这时候要是想认真的话，就必须要争分夺秒了。」"
    voice "audio/voice/001059.ogg"
    l "「甚至于，你要真想效果好，那不止暑假了，你整个高三都得搭进去拼命。」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/001060.ogg"
    l "「嘻嘻，怎么样？有没有这个觉悟？」"
    "梁芷柔笑嘻嘻地看着我……是觉得我不会答应吗？"
    "……说实话，我的第一反应也确实是想要拒绝。"
    "毕竟我比上不足比下有余，不愁没有大学上，毫无压力自然也就没有动力。相比之下，或许在这最后的暑假里好好地玩一玩、放松放松，还更吸引我一些。"
    "不过，在我准备开口的时候，脑海中浮现出来的，却是昨天晚上的那一幕。"

    stop music fadeout 1.5

    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fade
    "……"
    "…………"
    y "「就是觉得，感觉你好像和以前不太一样。」"
    voice "audio/voice/001061.ogg"
    l "「嗯……？」"
    scene cg03c3 #梁芷柔探病CG-3|对视|微笑|CG03c3
    voice "audio/voice/001062.ogg"
    l "「因为，从同学变成了姐姐？」"
    y "「……喂。」"
    voice "audio/voice/001063.ogg"
    l "「呵呵。」"

    scene bg black #黑屏
    with fade
    "那一刻。"
    "我第一次涌起冲动，想要向前迈步的那一刻。"
    "我第一次想要尝试去追赶她的步伐、憧憬与她同样的未来的那一刻。"

    scene bg b03a #病房|白天
    with fade
    "尽管，这只是我自己单方面的想法，尽管，我们之间的差距巨大到难以描述，但我知道，自己的这个微小的念头，已经难以磨灭了。"
    y "「（吸——）」"
    y "「……呼。」"

    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
    voice "audio/voice/001064.ogg"
    l "「嗯？」"
    y "「那，我可就真要拜托你啦？会不会给你添麻烦？」"
    show chara la06 #梁芷柔立绘|夏季校服|吃惊|近
    with dissolve
    voice "audio/voice/001065.ogg"
    l "「哎？」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/001066.ogg"
    l "「啊，不会不会，完全不会！你就放心吧！」"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～

    voice "audio/voice/001067.ogg"
    l "「嘻嘻，没想到你还真愿意啊？」"
    y "「是啊，那当然了，这么好的私人家教哪能放过啊。」"
    voice "audio/voice/001068.ogg"
    l "「嗯，很好！我会赌上姐姐的名誉，好好调教你的！」"
    y "「什么调教……不对，什么叫姐姐的名誉啊？还有，我怎么觉得你比我还要开心啊？」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/001069.ogg"
    l "「嗯，对呀，有什么问题吗？」"
    y "「问题挺多的吧……」"
    show chara la01b #梁芷柔立绘|夏季校服|普通|侧面|近
    with dissolve
    voice "audio/voice/001070.ogg"
    l "「嗯……好吧，这么说吧。首先呢，其实是我想要找个机会、找个方式，来感谢你。」"
    show chara la07a #梁芷柔立绘|夏季校服|消沉1|近
    with dissolve
    voice "audio/voice/001071.ogg"
    l "「谢谢你昨天救了我……不管怎么说，虽然现在是比较幸运，你没有什么大事，但是这种事，谁也说不准。我直到现在还在后怕，如果那个椅子砸坏了你，或者砸在我头上，会是一个什么下场……真的，我，还有我爸妈，都非常非常地感谢你。」"
    y "「呃……咳，不是说了嘛，别这样，多不好意思啊。」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/001072.ogg"
    l "「呵……好吧，不过，总之呢，如果有机会，让我能为你做些什么的话，我是很开心的。这是其一。」"
    y "「嗯……」"
    voice "audio/voice/001073.ogg"
    l "「其二呢，就是……我感觉，你和以前的我很像。」"
    y "「以前的你？」"
    show chara la01a #梁芷柔立绘|夏季校服|普通|正面|近
    with dissolve
    voice "audio/voice/001074.ogg"
    l "「嗯。我呢，也不是一开始就学习好的，明明脑子不笨，就是不好好学，尤其是小学的时候，那成绩简直惨不忍睹。」"
    y "「啊？」"
    "感觉听到了一件不可思议的事。"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/001075.ogg"
    l "「怎么啦，没想到？谁都会有点故事嘛。简单来说，在初一的时候，我家里发生了一点事。」"
    show chara la08b #梁芷柔立绘|夏季校服|担心2|近
    with dissolve
    voice "audio/voice/001076.ogg"
    l "「那事，也是一件……让我感到非常后怕的事。我绝不想再重蹈覆辙。」"
    voice "audio/voice/001077.ogg"
    l "「当时真的是很吓人，哪怕到现在已经过了这么久……我都还在后怕。」"
    voice "audio/voice/001078.ogg"
    l "「而这事之所以会发生，究其原因，就是因为我当时学习成绩太差。」"
    voice "audio/voice/001079.ogg"
    l "「我这辈子都不想再重蹈覆辙了。所以，从那以后，我就开始拼命努力，一直到现在。」"
    show chara la05a #梁芷柔立绘|夏季校服|苦笑1|近
    with dissolve
    voice "audio/voice/001080.ogg"
    l "「当然啦，你现在的情况，论成绩是比我那时候要好得多了……但是心态很像。」"
    show chara la01b #梁芷柔立绘|夏季校服|普通|侧面|近
    with dissolve
    voice "audio/voice/001081.ogg"
    l "「所以，如果你愿意积极一点的话，出现我以前那种经历的可能性就会小一些，所以我也很开心。」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/001082.ogg"
    l "「毕竟我也不想让我弟弟放任自流嘛？嘻嘻。」"
    y "「呵……」"
    y "「好吧，那我就不客气了。要杀要剐，悉听尊便。」"
    show chara la01a #梁芷柔立绘|夏季校服|普通|正面|近
    with dissolve
    voice "audio/voice/001083.ogg"
    l "「嗯，很好，那就从你出院以后吧。如果身体没问题的话，中午吃完饭之后，到百货大楼一层的那个连锁快餐店集合，怎么样？」"
    y "「那家啊……我知道了。」"
    "说到连锁品牌的快餐店的话，全县城其实就只有那一家，而且还是去年刚开业的，红呼呼的门脸，绝对找不错，是个很合适的地标。"
    "虽然不知道鸡肉汉堡之类的美式快餐为何要卖到那么贵，不过反正我们又不用在那里吃饭，最多买个饮料，问题不大。"
    y "「不过，这么折腾真的不会影响你吗？还得专门跑出来……」"
    show chara la01b #梁芷柔立绘|夏季校服|普通|侧面|近
    with dissolve
    voice "audio/voice/001084.ogg"
    l "「不会啊，真的。给你讲的同时也可以给我自己重新梳理一遍知识点，一举两得的。而且我也不用专门跑啊，我本来就打算在那里做自习的！」"
    y "「啊？」"
    voice "audio/voice/001085.ogg"
    l "「那儿离我家挺近的，就算没你这事，我下午也会在那里复习的。」"
    y "「啊？为什么啊？」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/001086.ogg"
    l "「嗯……去蹭空调啊。」"
    y "「啥？」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/001087.ogg"
    l "「蹭空调！天这么热，开电扇不管用，家里开空调又浪费电。」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/001088.ogg"
    l "「反正我家离百货大楼也没几分钟的路，就去占个便宜喽。」"
    y "「这样啊……」"
    "还真是……精打细算啊。"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/001089.ogg"
    l "「总之，别想那么多啦，只管来就是了！」"
    y "「……嗯，好。」"
    "我点点头。"

    stop music fadeout 1.5
    scene bg black #黑屏
    with fade
    "这是我迈出的第一步。"
    "虽然只是小小的一步，虽然最终能走多远、会走到哪里，全都一概不知。"
    "毕竟，无论是她，还是她即将前往的那些大城市和知名高校，以前的我都只有在做梦的时候才敢想，就算是现在，也一样没有丝毫底气可言。"
    "但总之，这一步是迈出去了。而这，也仅仅只是个开始。"
    "……"
    "…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t02 #转场 病房
    with fade
    pause

#两天后。
#7月31日。

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音

    scene bg b06 #商业街
    with fade

    y "「唔……」"
    y "「……热死了。」"
    "抹了把汗，轻轻揉了一下额头的纱布。"
    "尽管一路上已经尽量挑了有阴凉的地方走，但汗水还是无可抑制地呼呼往外冒。"
    "没办法，今年的夏天本就难熬得很，更何况现在刚过正午，正是太阳最毒的时候。"

    scene bg b07 #快餐店
    with fade
    play sound "audio/sound/effect04.ogg" noloop
    y "「呼啊！」"
    "钻进快餐店的一瞬间，便感到一股冷气扑面而来。"
    "本已热到打蔫的我，在骤然变化的温差的刺激下，微微打了个哆嗦。"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～

    y "「（吸气）……」"
    y "「（呼气）——！」"
    "用力地做了个深呼吸，将肺腔中的热气吹了出来。"
    y "「……呼！」"
    y "「哎，总算是活过来了。」"
    "感觉多少恢复了一点精神。"
    y "「那么……」"
    "四下环视。"
    y "「……」"
    y "「…………」"
    "并没有看到我想要找的那个身影。"
    "不过也正常，现在距离我们约好的时间还有15分钟左右，是我提前到了。"
    "既然如此，那就先找个地方坐一会儿吧。"

    scene bg b07 #快餐店
    with fade
    voice "audio/voice/151001.ogg"
    kfc "「您好，欢迎光临！」"
    y "「一杯可乐，谢谢。」"
    voice "audio/voice/151002.ogg"
    kfc "「好的，请稍等。」"

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    scene bg b07 #快餐店
    with fade

    "点了一杯饮料，我随便找了个位子坐下。"
    y "「……」"
    y "「（真他妈贵啊……）」"
    "这么小一杯可乐就敢要6块钱……"
    "做好了耐心等待的准备，我一边叼着吸管嘬水喝，一边东张西望。"
    y "「……」"
    y "「倒是都差不多。」"
    "实际上，老家县城里的这家店我也是第一次进来。而在此之前，我只在去省城的时候吃过那么两次。"
    "因为是连锁店的缘故，装潢的设计风格完全是一个模子印出来的，谈不上有多高档，但却是个新鲜玩意儿。"

    scene bg b02 #城区
    with fade
    "——相对于这座城市来说。"
    "这个开遍全国的快餐连锁品牌，直到去年才在我们县开了一家门店，而他家的那些竞争对手，至今依然对我们这种穷乡僻壤不屑一顾。"

    scene bg b07 #快餐店
    with fade
    y "「……」"
    "也难怪，只点了它一杯饮料，我都已经在嫌贵了……"
    "超出了我们本地的消费水平，再加上东西也不见得多好吃，多数人也就是尝个鲜而已，除了最开始那一段日子火爆了一阵以外，回头客是寥寥无几。"
    "就像现在，中午的饭点还没有完全过去，但这里却空空荡荡的，服务员一个个也都无精打采，看不出什么干劲。"
    "这样也好，待会儿我们就算在这里呆上一下午，也不会碍别人的事，应该也不会有谁过来轰我们走。"
    y "「嗯……」"
    stop music fadeout 1.5

    "我用力地吸了一口饮料，开始思索接下来找点什么事来消磨时光……"
    "要不要先做两道暑假作业的题什么的？"
    voice "audio/voice/001090.ogg"
    who "「哟！」"

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    "忽然，肩膀被轻轻拍了一下。"
    with hpunch
    y "「噗啊啊！」"
    "毫无心理准备的情况下，我被吓了一跳，喝到一半的水呛了进去。"
    y "「咳！咳咳！」"
    voice "audio/voice/001091.ogg"
    who "「啊！对不起对不起！」"
    show chara c08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/001092.ogg"
    l "「我就是想和你打个招呼，没想到会这样……」"
    "是梁芷柔。看她的样子，似乎也被我反过来吓到了。"
    y "「不，没事……是我自己的反应过头了……咳咳。」"
    y "「啊，我以为你还要再等一会儿才会过来。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001093.ogg"
    l "「这不是也差不多到时候了吗，没想到你到得更早……等很久了吗？」"
    y "「没有啊，我也是刚刚到，正在走神想事情呢。」"
    "为了把呛在嗓子眼的水咽下去，我又吸了一口饮料。"
    voice "audio/voice/001094.ogg"
    l "「嗯……」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/001095.ogg"
    l "「嘿嘿……」"
    voice "audio/voice/001096.ogg"
    l "「你刚才，该不会是在想，『哎呀，听说女生出门都比较慢，我到这么早该怎么打发时间啊』什么的？」"
    with hpunch
    "——噗！"
    "我刚又吸了一口水还没来得及咽下去，结果一听这话又喷了。"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001097.ogg"
    l "「呀！」"
    "幸亏我及时把嘴巴给捂住了，不然这一下非得全喷在她身上不可。"
    show chara c08b #梁芷柔立绘|夏季私服|担心2
    with dissolve
    voice "audio/voice/001098.ogg"
    l "「……你没事吧？」"
    y "「咳咳……没事，冰可乐汽儿太大，又呛着了。」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001099.ogg"
    l "「真的吗？」"
    y "「真的真的。」"
    voice "audio/voice/001100.ogg"
    l "「嗯……？」"
    "好险好险。"
    "……话说你有超能力啊？难道还会读心不成？"

    stop music fadeout 1.5

    "梁芷柔歪了歪脑袋，有点奇怪地看了看我，不过也并没有继续这个话题。"
    show chara c08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/001101.ogg"
    l "「嗯，你的伤……怎么样了？」"
    y "「啊，这个啊，还好。」"
    "我轻轻按了一下包扎在额头的纱布。"
    "伤口已经结痂了。虽然看起来很吓人，但实际上并不深，恢复得也很快。"
    "虽然医生说最后可能会留下一条很淡的伤疤，但反正我也不是什么白面书生，无所谓。"
    "男人嘛，有道疤不是什么大不了的事，说不定还能显得更彪悍一点。"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001102.ogg"
    l "「嗯……」"
    voice "audio/voice/001103.ogg"
    l "「那么……我们开始吧？」"
    y "「……」"
    y "「哎，好。」"

    play sound "audio/sound/ambientnoise06.ogg" fadein 2.5 loop #快餐店环境噪音
    scene cg04a #梁芷柔快餐店学习CG-1|就坐|CG04a
    with fade
    voice "audio/voice/001104.ogg"
    l "「嗯？怎么啦，怎么一脸的不高兴啊？」"
    y "「不……」"
    y "「我只是觉得，为什么暑假这么短呢？」"
    y "「明明才刚刚开始，感觉就好像已经过去一半了一样……为什么要提前半个月开学啊！？高一那帮崽子们现在玩得好欢啊，再想想去年，呜……」"
    scene cg04a1 #梁芷柔快餐店学习CG-1|就坐|微笑|CG04a1
    with dissolve
    voice "audio/voice/001105.ogg"
    l "「哈哈，好大的怨气……」"
    voice "audio/voice/001106.ogg"
    l "「……不过还是死了这份心吧，毕竟为了高考么，一辈子的事。」"
    y "「唉……干嘛非要考什么大学呢……」"
    "我唉声叹气，小声碎碎念道了一句。"
    "不过也就是说说而已，真要是不让考了，估计我也是不答应的。"
    scene cg04a #梁芷柔快餐店学习CG-1|就坐|CG04a
    with dissolve
    voice "audio/voice/001107.ogg"
    l "「咳咳。」"
    voice "audio/voice/001108.ogg"
    l "「好啦，干正事干正事。」"
    "梁芷柔从自己的书包里拿出了……一大摞习题集。"
    y "「呜哇。」"
    scene cg04a2 #梁芷柔快餐店学习CG-1|就坐|皱眉|CG04a2
    with dissolve
    voice "audio/voice/001109.ogg"
    l "「嗯？」"
    "看到我还是不情不愿的模样，梁芷柔一瞪眼，切换到好学生模式了。"
    voice "audio/voice/001110.ogg"
    l "「有什么问题吗？」"
    y "「呃……」"
    "忍不住先缩了下脖子。"
    "不过……"
    y "「还真有个问题。」"
    scene cg04a #梁芷柔快餐店学习CG-1|就坐|CG04a
    with dissolve
    voice "audio/voice/001111.ogg"
    l "「嗯？」"
    y "「你……拿这么多套题过来是要干什么啊？」"
    voice "audio/voice/001112.ogg"
    l "「做呀？」"
    y "「不不不，我的意思是，这么多……你多久能做完？」"
    "这厚度……给我的话，别说暑假了，就算是在学校全负荷状态的时候，半个月能啃完其中的一小部分就不错了。"
    voice "audio/voice/001113.ogg"
    l "「嗯……这两天吧，也许三天？」"
    y "「啥？」"
    "我知道她很厉害，但如果厉害到这个程度，那就未免非人了吧……"
    voice "audio/voice/001114.ogg"
    l "「嗯？啊，我明白你的意思了。」"
    voice "audio/voice/001115.ogg"
    l "「不是你想的那样，这里面我是挑着做的。」"
    y "「嗯？」"
    voice "audio/voice/001116.ogg"
    l "「嗯……怎么说呢，有的题，看过一眼就能判断出『啊，这道题我会』，这样的题，我是不会再去做的。」"
    voice "audio/voice/001117.ogg"
    l "「我觉得呢，要想提高自己，大量做题还是很有必要的。不过是要做自己没做过的，而不是翻来覆去做一堆相同的题型。」"
    y "「喔喔，原来如此。」"
    voice "audio/voice/001118.ogg"
    l "「但是你现在的情况嘛……嗯，我问你，暑假作业，你做……嗯，你看过了么？」"
    y "「呃……」"
    y "「大概翻了翻，还没仔细看。」"
    scene cg04a3 #梁芷柔快餐店学习CG-1|就坐|无奈|CG04a3
    with dissolve
    voice "audio/voice/001119.ogg"
    l "「唉……」"
    "一种「果然如此」和「怒其不争」混合在一起的表情。"
    "呜……我好有负罪感啊。"
    voice "audio/voice/001120.ogg"
    l "「所以呢，你现在连基础的做题量都没有满足，跟你说这个太早了。」"
    voice "audio/voice/001121.ogg"
    l "「这两天你还是先把作业做完吧，然后再说别的。」"
    y "「好吧，全听你的。」"
    "我认命似的点了点头，开始和万恶的暑假作业进行斗争。"

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    stop sound fadeout 1.5
    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～

    scene bg b07 #快餐店
    with fade
    "时间过去了20分钟。"
    y "「……」"
    y "「…………」"
    y "「………………呜。」"
    "精力……开始涣散了。"
    "说起来，一直以来，对于暑假作业这种东西，我虽然不至于出现那种拖到最后一天才决死冲锋的场面，但也全都是在死线临近的压迫下方才动工。"
    "在暑假刚开始就做作业这种事，有生以来还真是头一遭。"
    "感觉……不习惯啊。"
    "我下意识地去抬头看了看桌子对面的梁芷柔。"
    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with fade
    y "「（呜哇。）」"
    "梁芷柔聚精会神地做着卷子。"
    "她时而思考、时而运笔如飞，迅速地写满了一张A4纸。"
    "这样的A4纸她带了一叠过来，所有的答案都写在了这些纸上，方便在她做完以后，我还可以重复使用这些习题集。"
    y "「（……好认真。）」"
    y "「（而且做题好快！）」"
    "说实在的，以前并没有这种近距离观察她的机会，对她学习水平的印象都是从结果上得出来的，还比较朦胧。但这一次，却是非常直观地让我见识到了她的强大之处。"
    "梁芷柔跳过了很多简单题目，做的多是些大题，但却依然能有这样的速度……而且看了好一会儿，都没见到有哪道题能把她卡住的。"
    "倒也不是强到想都不用想就能写出答案，但是每道题只要经过一段时间的思考，接下来的解题过程就如行云流水一般，非常流畅。"
    "真的是……好厉害。"
    y "「……」"
    y "「（这种水平……我真能赶得上吗？）」"

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    scene bg b07 #快餐店
    with fade
    "又过了一会儿。"
    y "「嗯……」"
    y "「……嗯…………」"
    "解题卡壳了。"
    "有一道明明看起来应该很简单的题，但就是搞不明白。"
    "卡在这里好几分钟了，还完全没有头绪。相比之下，梁芷柔那摧枯拉朽一般的解题速度真是比我高到不知哪里去了。"
    with hpunch
    y "「（啊啊啊，完蛋。）」"
    y "「（这样下去不行啊！）」"
    "本就已经有些浮躁的我，在深切地意识到了自己与目标的巨大差距之后，变得更加心神不宁。"

    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    l "「……」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001122.ogg"
    l "「嗯？怎么了？」"
    "下意识地抬头看了一眼梁芷柔，结果她刚好做完了一篇卷子正在收拾，和我的视线对在了一起。"
    y "「啊，那个……」"
    y "「我有道题弄不太明白。」"
    "算了，求助吧。反正本来就是来向她讨教的，不丢人……应该吧。"
    show chara lc01b #梁芷柔立绘|夏季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/001123.ogg"
    l "「哎？是吗？哪道题？」"
    y "「这一道，是这一道。」"
    voice "audio/voice/001124.ogg"
    l "「我看看……」"
    "梁芷柔把作业向她那边拉了拉，开始审题。"
    voice "audio/voice/001125.ogg"
    l "「嗯……这道题啊。」"
    show chara lc13b #梁芷柔立绘|夏季私服|疑惑2|近
    with dissolve
    voice "audio/voice/001126.ogg"
    l "「嗯？」"
    "看过题后，梁芷柔有些疑惑，抬眼瞄了我一下。"
    voice "audio/voice/001127.ogg"
    l "「这题……你……」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001128.ogg"
    l "「嗯……你先把这道题给我描述一遍。」"
    y "「哦。已知A、B、C为圆O上的三点，AO等于AB加AC的一半，求AB和AC之间的夹角……」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001129.ogg"
    l "「停，我不是让你把题念一遍，是让你把已知的条件描述一遍。」"
    y "「啊？」"
    voice "audio/voice/001130.ogg"
    l "「用你自己的话解释一下，这道题的条件是什么？我们知道什么？」"
    y "「就是说，这儿有个圆，圆心是O，A、B、C都在这个圆上，然后，AB加AC……AB加AC……」"
    y "「啊！」"
    "这不就是个向量和嘛？"
    voice "audio/voice/001131.ogg"
    l "「怎么？」"
    y "「原来如此……我给当成标量和了……」"
    voice "audio/voice/001132.ogg"
    l "「明白啦？」"
    y "「明白了！」"
    voice "audio/voice/001133.ogg"
    l "「那为什么之前不明白啊？」"
    y "「呃……为什么呢？」"
    "我自己也觉得挺奇怪的。现在再看，这种题我闭着眼也应该能做出来，但不知为何当时就是钻了牛角尖。"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001134.ogg"
    l "「因为……你的心思就不在做题上面啊。」"
    y "「呃……」"
    voice "audio/voice/001135.ogg"
    l "「对吧？半个小时了才做了这么点题，还会被这种其实本来会做的题给卡住……除了你精力不集中以外，还有别的原因么？」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001136.ogg"
    l "「说起来，你就这么不想做作业嘛？」"
    y "「呃，这个……那个……」"
    voice "audio/voice/001137.ogg"
    l "「……」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001138.ogg"
    l "「唉，算啦算啦，也不可能一下子就给你扳过来。」"
    voice "audio/voice/001139.ogg"
    l "「正好我这边也告一段落了，先中场休息一会儿吧。」"
    y "「……是。」"

    stop music fadeout 1.5

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    play sound "audio/sound/ambientnoise06.ogg" fadein 2.5 loop #快餐店环境噪音
    scene cg04c #梁芷柔快餐店学习CG-3|饮料|CG04c
    with fade
    y "「来，给你。」"
    voice "audio/voice/001140.ogg"
    l "「谢谢～」"
    "去柜台给梁芷柔点了杯饮料，垂头丧气地端了回来。"
    l "「（吸——）」"
    l "「……」"
    voice "audio/voice/001141.ogg"
    l "「干嘛啊，耷拉着脑袋。」"
    y "「没啥。我在想啊，可能我真不是这块料吧。」"
    y "「说实话，今天一开始的时候，我还真是想要好好学的，结果还是没几分钟就现了原形了。」"
    y "「所以说啊……啧。」"
    voice "audio/voice/001142.ogg"
    l "「嗯……我倒是觉得还可以吧，至少目前来说。」"
    voice "audio/voice/001143.ogg"
    l "「一个人保持专注的时间是有限的，尤其是你的心思不在这上面的时候。所以你刚才这样也算是正常。」"
    voice "audio/voice/001144.ogg"
    l "「说到底还是你对学习没兴趣，注意力全都被别的东西吸引走了。」"
    l "「……」"
    voice "audio/voice/001145.ogg"
    l "「嗯……我能问问你吗？你刚才做题的时候，其实是在想什么？」"
    y "「想什么……这个……」"
    voice "audio/voice/001146.ogg"
    l "「你肯定是在走神，所以我想知道是什么干扰的你。」"
    voice "audio/voice/001147.ogg"
    l "「……嗯……是我打扰你了？」"
    "梁芷柔随口瞎猜了一句。"
    "反问的语气，显然连她自己也没当真。"
    "不过……"

    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with fade
    l "「……」"
    y "「……」"
    l "「……」"

    scene bg black #黑屏
    with fade
    "我还是心虚了一下。"

    scene cg04c #梁芷柔快餐店学习CG-3|饮料|CG04c
    with fade
    "说实话……仔细想想自己刚才的状态，或许还真就是这个原因。"
    "这两天，我的人生经验正在迅速增长，各种以往压根就没想过的场面接踵而至。"
    "而一切改变的根源，则正是眼前的这个女生。"
    "往日只能远远地在一旁憧憬的人，就这样俏生生地被拉近到自己的眼前，甚至还要挤在一张桌子上做卷子。"
    "也不用她主动打扰我，光是维持眼前这种状况就足够让我受到影响的了。"
    y "「……」"
    y "「……那当然不是。」"
    "然而这种事当然不能宣之于口，只好故作镇定地断然否认。"
    voice "audio/voice/001148.ogg"
    l "「所以说啊，到底是因为什么呢？」"
    y "「是啊，为什么呢？」"
    l "「……」"
    y "「……」"
    voice "audio/voice/001149.ogg"
    l "「唉。」"

    scene bg b07 #快餐店
    with fade
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001150.ogg"
    l "「算了，不提这个了。换一个角度来想这个问题。」"
    y "「嗯？」"
    voice "audio/voice/001151.ogg"
    l "「先不说你能不能集中精力了，就说你想不想吧！」"
    voice "audio/voice/001152.ogg"
    l "「换句话说，你想不想好好学啊？」"
    y "「啊……这个呀……」"
    y "「也不能说是……不想吧。」"
    y "「不是，要说起来也确实是没太大动力，怎么说好呢……」"
    y "「主要吧，就像之前说的似的，以前也不是没好好努力过，但是折腾了半天也没什么效果，成绩好不到哪去，然后不那么拼命呢，也没见有多差，高不成低不就的，时间一长就变成这样了。」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001153.ogg"
    l "「高不成低不就……嗬。」"
    y "「你别笑，好歹我也是咱们班第六名呢？」"
    voice "audio/voice/001154.ogg"
    l "「嗯，可你这个第六名啊……」"
    voice "audio/voice/001155.ogg"
    l "「你这次总分是多少来着？差了我得有一百多分呢吧？」"
    y "「那倒是没错，可问题咱们班第二名也一样差了你一百多分啊……」"
    "顺便一提，年级第二名也差了她一百多分。"
    "对我们这些凡夫俗子来说，与她的差距的区别，只是那一百之后的数字是二三十还是四五十、六七十而已。"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001156.ogg"
    l "「唉……」"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    voice "audio/voice/001157.ogg"
    l "「是啊，可他能考上一本，你呢？」"
    y "「二本。」"
    "这个倒是无可辩驳，我直接承认了这个结果。"
    voice "audio/voice/001158.ogg"
    l "「而且可以选择的余地也不大，对吧？」"
    y "「唉，是。」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001159.ogg"
    l "「所以说啊，你不只是跟我有差距，比起咱们学校的其他一些人，你一样差着挺远的呢。」"
    voice "audio/voice/001160.ogg"
    l "「之所以显不出你的问题，不是因为你成绩足够，而是因为咱们断档太厉害。抛开我不说，从第二名到你这个第六名，能差出去好几十分。」"
    show chara lc01b #梁芷柔立绘|夏季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/001161.ogg"
    l "「不过呢……这个差距虽说不算小，但也不是什么遥不可及的事。」"
    voice "audio/voice/001162.ogg"
    l "「我有一个想法。」"
    y "「嗯？」"
    voice "audio/voice/001163.ogg"
    l "「你不是说以前努力过，但是没达到效果吗？我估计啊，这里面有学习方法的问题，也有你自己心态没摆好的问题。」"
    voice "audio/voice/001164.ogg"
    l "「不要一上来就给自己划一道终点线。既然你老说自己笨，那咱们选择一个最简单的笨办法，踏踏实实、一小步一小步的来。」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001165.ogg"
    l "「先定一个能达到的小目标，比方说我先达到一本线！」"
    with hpunch
    y "「噗！」"
    "本来想要一边听一边喝点饮料，这一下差点直接喷出去。"
    y "「姐姐，您这一步还算小啊？」"
    "我们学校今年的毕业生总共还不到30个过一本线的，均摊到各班的话，也就是前三四名希望比较大。"
    "高二这一级……具体到我们班的话，则除了梁芷柔以外，只有两个人在学校自己的摸底测试中基本达到标准，另外还有一个人勉强有戏。"
    "虽然看起来我只需要跨越两三个名次，但实际上就像梁芷柔说的那样，我们之间其实是断档的，几个名次差了二三十分。"
    "而且，这次期末考试还是算我运气比较好、发挥比较出色的一次，平时也不见得每次都能考到这个水平的。"
    "要在发挥出色的基础上，再提高这么大一截……还只是初期的目标，这真不算是搞大跃进么？"
    show chara lc13b #梁芷柔立绘|夏季私服|疑惑2|近
    with dissolve
    voice "audio/voice/001166.ogg"
    l "「这都不行啊？很难吗？三四十分而已啊。」"
    y "「而已……」"
    voice "audio/voice/001167.ogg"
    l "「嗯，而已。你的基础不算差呀，心态调整过来的话，再把学习方式改进一下，只要把一些关键的知识点补牢，这点分数根本是轻而易举的……嗯，到一模吧，应该就差不多了。」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001168.ogg"
    l "「你不信？」"
    y "「呃……」"
    "本来确实是有些不信的，但她说得如此言之凿凿，而且似乎也有道理，我又不禁动摇起来。"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001169.ogg"
    l "「嗯……原来如此。」"
    "看到我的表现，梁芷柔倒是明白了。"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001170.ogg"
    l "「你最大的问题，是太没有自信了。」"
    voice "audio/voice/001171.ogg"
    l "「不是不想，但又没被逼到需要破釜沉舟的份上，以前努力过，失败了，怕重蹈覆辙做无用功，所以呢，畏首畏尾。」"
    l "「……」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001172.ogg"
    l "「哎。」"
    "梁芷柔欲言又止，有些无奈地苦笑了一下。"
    y "「呃……那个。」"
    y "「怎么说啊，我……这个……」"
    "想要说点什么，却又不知该说什么。"
    "自己的问题，自己当然还是知道的，梁芷柔的判断十分准确，没什么可辩解的。"
    "当然，狡辩更是毫无意义，无论我承认与否，问题还是会摆在那里。"
    y "「……唉。」"
    l "「……」"
    "我无话可说，梁芷柔也没有再开口，一时间，场面非常尴尬。"
    "不过，梁芷柔很快打破了沉默。"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001173.ogg"
    l "「哎，没事，就像刚才说的，一步一个脚印，慢慢来呗。」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001174.ogg"
    l "「最起码你肯来找我，那就还是有想法的，对吧？这就已经是进步啦！」"
    y "「啊，哈……」"
    y "「那个，不用安慰我，我也知道自己朽木不可雕……」"
    voice "audio/voice/001175.ogg"
    l "「嘻嘻……可别这么说啊！你不相信自己，还不相信我啊？我都说你有天赋了，相信我，没错的。」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001176.ogg"
    l "「想当年我的情况比你糟多了，现在不也熬过来了？你没问题的，只要肯听我的话。」"
    y "「哦、哦……」"
    "的确，梁芷柔之前说过她并非一直都是学霸，小学时的成绩是十分糟糕的，不过具体的就不知道了。"
    y "「你当年到底是个什么情况？」"
    voice "audio/voice/001177.ogg"
    l "「这个么……秘密。等以后有机会再说吧！」"
    y "「呃？」"
    voice "audio/voice/001178.ogg"
    l "「现在说，你也最多就是当成个故事，满足一下好奇心，听完就完了。」"
    y "「……」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001179.ogg"
    l "「至于眼前嘛……你的情况我也大致了解了，那，就先不考虑主观因素了，我们从技术角度着手吧！先来纠正一下你的坏习惯。」"
    voice "audio/voice/001180.ogg"
    l "「这样的话，虽然还是欠了点，但如果只是为了完成眼前这个小目标的话，应该也差不多够了吧！」"
    y "「啊？真要定这个『小』目标啊？」"
    show chara lc03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/001181.ogg"
    l "「那当然，听话！」"
    y "「呃……」"
    "梁芷柔用理所当然并且不容置疑的语气定下了调子，断绝了我所有的退路。"

    stop sound fadeout 1.5

    y "「……」"
    y "「好。」"
    "虽然我没她那么有信心，但好歹也不至于第一天就临阵脱逃，是死是活，总要拼一把看看再说。"
    "毕竟自己的决心不是白下的，我可不想让自己变成一个笑话。"

    scene bg b02 #城区
    with fade
    "就这样，我的暑假生活——开始了。"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t03 #转场 快餐店
    with fade
    pause

#两天后。
#8月2日。

    scene bg b02 #城区
    with fade
    pause
    scene bg b06 #商业街
    with fade
    pause
    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with fade
    play sound "audio/sound/effect10.ogg" fadein 0.5 loop #写字声
    "沙沙沙……"
    "沙沙沙……"
    y "「……」"
    stop sound fadeout 1.5
    y "「…………」"
    y "「…………………………」"
    with hpunch
    y "「啊啊啊啊啊终于做完了啊啊啊啊啊啊！」"

    scene bg b07 #快餐店
    with fade
    show chara lc13b #梁芷柔立绘|夏季私服|疑惑2|近
    with dissolve
    voice "audio/voice/001182.ogg"
    l "「唉哟，怎么了你，没事吧？」"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～

    y "「哈哈哈，没事。抱歉啊，太激动了。」"
    y "「这辈子从来没有这么早做完暑假作业……第三天啊，第三天就把暑假作业做完了！」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001183.ogg"
    l "「好好好，真了不起。来，给我，我看看。」"
    y "「啊……哦。」"
    "被梁芷柔小小地讽刺了一下以后，我迅速地冷静了下来。"
    "的确是有点得意忘形了……我居然敢在关公面前耍大刀？要知道眼前的这一位，可是当着我的面，只用了三个下午的时间就啃完了厚厚一摞、足够我做上一个月的习题集啊！"
    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with fade
    voice "audio/voice/001184.ogg"
    l "「……嗯……」"
    "梁芷柔飞快地检视着我做完的作业。"
    voice "audio/voice/001185.ogg"
    l "「啊，这里……」"
    voice "audio/voice/001186.ogg"
    l "「嗯……」"
    voice "audio/voice/001187.ogg"
    l "「……还有这里……」"
    "……"
    "…………"
    with fade
    voice "audio/voice/001188.ogg"
    l "「……好啦。」"
    "梁芷柔边看边用铅笔在我的作业上轻轻地打着标记，最后将检查过的作业递还给我。"
    scene cg04b1 #梁芷柔快餐店学习CG-2|讲题|CG04b1
    with dissolve
    voice "audio/voice/001189.ogg"
    l "「这里错了，零点存在性用得不对，答案结果是对的但是过程错了。」"
    y "「哦！」"
    voice "audio/voice/001190.ogg"
    l "「还有这里，换元前后的等价性呢？」"
    y "「哦哦。」"
    voice "audio/voice/001191.ogg"
    l "「然后就是……这儿，斜率的顺序颠倒了。」"
    y "「哦……」"
    "……"
    "…………"
    with fade
    voice "audio/voice/001192.ogg"
    l "「大致上问题就是这些，有哪里不明白吗？」"
    y "「呃……有一点。」"
    voice "audio/voice/001193.ogg"
    l "「嗯？哪儿？我看看。」"
    y "「呃，是这里……」"
    "梁芷柔把作业拉到桌子中间的位置横置，身子稍稍前倾，歪着头看着我指出的题目，随后保持着这个姿势开始给我讲解。"
    "为了看题，我也不得不把头反向歪过来，并且贴近她。"
    "这个姿势似乎稍显暧昧，不过既然梁芷柔并不介意——或者是心无杂念——我自然也没有意见。"
    "实际上，这两天，这种场面也不止一次出现了。"
    "虽然最开始的时候有些慌乱，不过现在已经适应了，甚至精神反而更加容易集中。"
    "没办法，为了压制自己乱七八糟的念头，我不得不强行要求自己认真听讲，结果居然成效显著。"
    with fade
    voice "audio/voice/001194.ogg"
    l "「……就是这样，这次明白了吗？」"
    y "「嗯……明白了！」"
    voice "audio/voice/001195.ogg"
    l "「你自己说一遍。」"
    y "「啊，这里是这样……」"
    "许多我自己原本半懵半懂的知识点，就在这样的讲解过程中融会贯通了。"
    "总觉得她的讲解，比起老师讲的更有用。"
    "这是因为开小灶的缘故？还是因为同是学生，她更清楚我会遇到什么问题？"
    "也许二者兼而有之吧……总之，短短两天时间，我的进步速度出乎意料的快。"
    "如果真能照这样下去的话，也许考个一本确实不是什么不可能的事情？"
    y "「……」"

    scene bg black #黑屏
    with fade
    "……不对。"
    "虽然确实有所进步，不过或许更主要的原因是我的起点相对比较低。"
    "这样的提速能坚持多久呢？我不太确定。"
    "而且，还有更重要的一个问题。"
    scene bg b07 #快餐店
    with fade
    show chara lc01b #梁芷柔立绘|夏季私服|普通|侧面|近
    with dissolve
    l "「……」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001196.ogg"
    l "「……嗯？怎么了？」"
    y "「啊……没事。」"
    scene cg04b1 #梁芷柔快餐店学习CG-2|讲题|CG04b1
    with fade
    "轻轻摇头，试图将杂念甩出头脑。"
    "不过，有些念头，一旦萌生就会在心头扎下根来，很难挥之即去。"
    y "「……」"
    "我学习的目的究竟是什么？"
    scene bg black #黑屏
    with fade
    "在这两天短暂的接触中，我对于自己与她的差距，有了一个更加直接、清晰的感受。"
    "不要说什么缩短距离的可能性了，我甚至连她已经走到了哪一步都不得而知。"
    "尽管我们现在坐在一起，挨得很近，但彼此之间却盘桓着一条令人绝望的鸿沟。"
    "咫尺，天涯。"
    voice "audio/voice/001197.ogg"
    l "「……喂？」"
    voice "audio/voice/001198.ogg"
    l "「喂，叶雨潇？」"

    scene bg b07 #快餐店
    with fade
    with hpunch
    y "「啊？啊，怎么了？」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001199.ogg"
    l "「又走神啦，你怎么搞的？」"
    y "「呃……抱歉。」"
    voice "audio/voice/001200.ogg"
    l "「哎……」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001201.ogg"
    l "「说说，这次又是因为什么？」"
    y "「啊，没什么……没事。」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001202.ogg"
    l "「别没事，你肯定是有心事。」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001203.ogg"
    l "「怎么啦？作业做完了开始纠结了？想去玩？」"
    y "「不是不是，绝对不是。」"
    y "「我只是……」"
    y "「……」"
    y "「我只是在想，还来不来得及。」"
    y "「要是去年这时候的话，可能我还有点信心，但是现在……就剩一年了啊。」"
    voice "audio/voice/001204.ogg"
    l "「呵嗯……」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001205.ogg"
    l "「不错嘛，知道担心时间不够了？」"
    voice "audio/voice/001206.ogg"
    l "「放心吧，所谓好学近乎知嘛！你现在这个水平啊，只要想学，就肯定没问题。」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001207.ogg"
    l "「一本线嘛，小意思，包在姐姐身上。而且，除了这个小目标，如果你还能继续保持努力的话，最后考到百薇也不是不可能的。」"
    y "「哈……」"
    "梁芷柔似乎很高兴……不过会有这样的误会倒也理所当然，毕竟她又不知道我之前的想法。"

    hide chara
    scene bg b02 #城区
    with fade
    "不过……百薇大学啊。"
    "百薇是我们省城的大学，老牌的国家重点，也是本省唯一的985、211。"
    "放眼全国，或许还不敢说多有吸引力，但放在我们这个县里，若是有谁家的孩子考上了百薇，可是足以光宗耀祖的大喜事。"
    scene bg b07 #快餐店
    with fade
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    "该说是她看得起我呢？还是说学霸的境界太妖孽，已经不把凡人的顶点放在眼里了？"
    "感觉这样一来，非但没有获得安慰，反而是更没有信心了……"
    "不知道这样下去，我最后究竟能不能做到……至少可以望其项背啊！"
    "总之，走一步算一步吧。"
    scene bg black #黑屏
    with fade
    "……"
    "…………"

    stop music fadeout 1.5

    scene bg b06 #商业街
    with fade
    y "「哎呀，今天真是谢谢了。」"
    "结束了下午的补习、离开快餐店以后，我照例和她道别，不过……"

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    l "「……」"
    y "「……」"
    l "「……」"
    y "「……喂。」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001208.ogg"
    l "「嗯？怎么啦？」"
    "我停下脚步，看着亦步亦趋地跟在我身后的梁芷柔。"
    y "「什么情况？」"
    voice "audio/voice/001209.ogg"
    l "「没什么啊？」"
    y "「那你跟在我后面干什么……」"
    voice "audio/voice/001210.ogg"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    l "「这个嘛……你猜？」"
    y "「猜得出来才怪！」"
    voice "audio/voice/001211.ogg"
    l "「嘻嘻，你是要回家去吧？」"
    y "「是啊……这都快到饭点了，也没别的地方可去了吧？」"
    voice "audio/voice/001212.ogg"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    l "「对啊。所以呢，我去我弟弟家蹭饭啊！」"
    with vpunch
    y "「哦……啥！？」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    "看她这一脸坏笑的样子，这所谓的「弟弟」分明就是指的我啊！"
    y "「……什么鬼？」"
    show chara c08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/001213.ogg"
    l "「哎～～？不行吗？」"
    "梁芷柔摆出一个伤心的造型。"
    y "「不是，什么行不行的……你就别玩我了，到底是怎么回事？」"
    "她似乎很喜欢这样开玩笑，这两天我也算是身经百战见得多了，丝毫不为所动。"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/001214.ogg"
    l "「就是去你家啊！」"
    y "「说正经的好不好……」"
    show chara c08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/001215.ogg"
    l "「可我就是要去你家啊……」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/001216.ogg"
    l "「……你家边上的书店。」"
    y "「我的妈呀这大喘气。」"
    "果然。果然我早已看穿了一切。不过……"
    y "「嗯？等等，我家边上有书店吗？」"
    y "「还有，你知道我家在哪儿嘛？」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001218.ogg"
    l "「知道呀！当然知道了。」"
    y "「你怎么知道的？」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001219.ogg"
    l "「学校有花名册呀。我好歹也是一班之长嘛，班里同学的基本情况多少还是了解的。」"
    y "「这……所有人的住址你都能记住？」"
    show chara c12a #梁芷柔立绘|夏季私服|羞涩1
    with dissolve
    voice "audio/voice/001220.ogg"
    l "「这个嘛……倒也不是。」"
    voice "audio/voice/001221.ogg"
    l "「你……比较特别嘛。」"
    with hpunch
    y "「……！」"
    "梁芷柔的话让我吓了一跳，一时间心脏都忍不住狂跳了起来。"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001222.ogg"
    l "「之前你昏迷的时候，老师翻名册找你爸妈的联系方式，我也在旁边，看到了，所以印象比较深刻！」"
    y "「……」"
    voice "audio/voice/001223.ogg"
    l "「哈哈哈。」"
    voice "audio/voice/001224.ogg"
    l "「不然你以为呢？」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/001225.ogg"
    l "「我的『弟弟』同学？」"
    "……好吧，我就知道。"
    "梁芷柔这人啊……乍一看是温文尔雅知书达礼，等到和她熟悉了以后就会发现她其实很能闹。以前那种冰山美人什么的性格，根本就是我们距离产生美，胡乱脑补出来的形象。"
    "毕竟平时接触的全都是「身为班长与学霸的梁芷柔」，而「日常生活中的梁芷柔」则难得一见，难免管中窥豹、盲人摸象。"

    stop music fadeout 1.5

    y "「唉……」"
    y "「所以呢？」"

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001226.ogg"
    l "「嗯？什么所以？」"
    y "「我们家附近……哪有书店啊？」"
    y "「要说书店的话，不应该就是在这里么？」"
    hide chara
    with dissolve
    "我指向快餐店所在的百货大楼，这是全县最大的综合性商城，本地唯一的一家新华书店就在那边。"
    "在这个小小的县城里，书店的数量屈指可数，新华书店的规模和质量都算是最好的，本地人如果要买正经的图书，一般来说都会到那里去。"
    "虽然也并不是没有其他书店，但大多是地下作坊一样的小门脸，不止书籍数量有限，而且盗版横行，质量也相当堪忧。"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001227.ogg"
    l "「嗯？嗯……我不去新华书店啊。」"
    y "「啊？」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001228.ogg"
    l "「他们那儿没有我要的书……我现在都是和书店订，让他们进货的时候顺便帮我进一些过来，到时候我过去取，这样省邮费。」"
    "原来如此，这样的话找新华书店当然是不行了。"
    y "「我家边上有这种可以预订的书店吗？」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001229.ogg"
    l "「你不知道吗？就在你家西边一点点，几百米吧，也靠河边，门脸不是很大，但应该挺好找的呀？」"
    y "「西边……哦，那边啊，新城区那边我去的特别少。」"
    y "「那边不是老是施工嘛，土太大，平时不往那边走。」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001230.ogg"
    l "「那倒也是。」"
    scene bg b02 #城区
    with fade
    "我家的小区在黄河北岸边上，紧挨着旧城区西部的边缘，往西走一点就是新城区。"
    "这两年，那边新盖了不少楼，据说还要划出一块工业园区，也不知道有没有人来。"
    "这些新建筑有的已经完工了，但还有不少是半成品或者索性烂尾，总的来说，在多数人眼里，那边就是一片大工地，没事不愿意往过走。"
    "当然，随着旧城区改造的同步实施，老城这边也被拆得不亦乐乎，变成了乌鸦笑猪黑的局面。"
    scene bg b06 #商业街
    with fade
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    "无论如何，这一次是我灯下黑了。"
    y "「那，你是要去订书，还是订的书到了啊？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001231.ogg"
    l "「到货。不过也可以顺便看看有什么别的书吧。」"
    voice "audio/voice/001232.ogg"
    l "「总之，走呗？」"
    y "「好，好。」"
    scene bg black #黑屏
    with fade
    "……"
    "…………"
    scene bg b06 #商业街
    with fade
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001233.ogg"
    l "「说起来啊，你平时都喜欢看什么样的书？」"
    y "「书啊……小说的话，科幻和推理的都还可以。」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001234.ogg"
    l "「嗯～这样啊。」"
    y "「怎么啦？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001235.ogg"
    l "「没什么，怪不得。」"
    y "「怪不得？什么怪不得？」"
    voice "audio/voice/001236.ogg"
    l "「都是很需要思考的书啊！怪不得以你的基础，成绩还能维持在这个水平上，说不定你的逻辑思维能力还真的是很不错呢！」"
    y "「哪有啊，我看的也不是那种纯粹的推理或者硬科幻什么的……」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/001237.ogg"
    l "「但你的考试成绩确实不错嘛，嗯？第六名？」"
    y "「喂喂喂你就别拿这个笑话我了吧？而且你这根本就是赤裸裸地自夸吧？论考试成绩，谁敢跟你比啊！」"
    voice "audio/voice/001238.ogg"
    l "「我可不是这个意思啊。」"
    y "「我也没别的意思，我就是觉得自己没你说的那么聪明……」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001239.ogg"
    l "「看怎么说吧，也许只是你自己都没注意。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001240.ogg"
    l "「你想啊，影响成绩的因素，无外乎学习方法、努力程度和你有多聪明了。」"
    voice "audio/voice/001241.ogg"
    l "「前两项，据我观察，你比其他人顶多是强点有限。所以呢，我高度怀疑你其实很有天赋，只是还没完全发掘出来。」"
    y "「呵呵您可真瞧得起我。」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001242.ogg"
    l "「本来就是嘛，你平时有多努力你自己最清楚了，连这点作业都要叫苦连天的。」"
    "梁芷柔一边说一边朝我装着暑假作业的包呶了呶嘴。"
    voice "audio/voice/001243.ogg"
    l "「至于学习方法，看你们平时动不动就想抄作业的毛病就知道了。还有笔记，虽然我没看过你的笔记本，不过就我看你上课时的状态，一定也没有好好记过笔记。」"
    y "「呜。」"
    "她说得好有道理……我表示无言以对。"
    show chara c03 #梁芷柔立绘|夏季私服|生气
    with dissolve
    voice "audio/voice/001244.ogg"
    l "「所以呢，虽然考试成绩好不好和这个人聪不聪明没有绝对的关系，但套在你的身上的话，那当然就是因为你很聪明呗！」"
    y "「哎。」"
    y "「虽然你是在夸我，可我怎么感觉是被骂了啊……」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001245.ogg"
    l "「你说呢？」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/001246.ogg"
    l "「知·耻·而·后·勇啦！」"

    stop sound fadeout 1.5
    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～

    scene bg b04 #滨河路|夏
    with fade
    "我们一路闲聊着离开了百货大楼所在的商业街，向北过桥，再往西走，就来到了我家小区所在的街道。"
    "这一代的建筑普遍还是六七十年代的风格，看上去有些破旧。不过对于自幼一直住在这里的我来说，更多的还是亲切感。"
    "相比老旧的建筑物来说，道路的状况就要好上很多。毕竟，黄河两岸几乎可以算得上是城区里唯一能够被称为风景的地方了，为了形象，前两年热炒招商引资的时候，南北两侧的滨河路都被认真翻修过，新得很。"
    y "「哎呀，要想富，先修路啊！」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001247.ogg"
    l "「哎？什么先修路？」"
    y "「啊，没事，我自言自语呢。」"
    y "「你看咱们县之前不是嚷嚷了那么半天吗，要吸引投资啊什么的，然后第一件事就是先把我们家门口的这条破路给重新修了。」"
    y "「之后盖那么多楼有没有用我不知道，就只有这条路我觉得最满意了，以前啊，这路难走死了。」"
    y "「要我说，还不如少盖点楼，把全县的路都给修一遍算了。所以说，要想富先修路。」"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/001248.ogg"
    l "「啊哈哈……我觉得这话不是这个意思吧……」"
    y "「我知道啊，我就随便瞎说的。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001249.ogg"
    l "「嘻嘻。你啊……」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001250.ogg"
    l "「不过，要说起来，咱们这里的路啊，确实挺惨。」"
    voice "audio/voice/001251.ogg"
    l "「但是没办法啊，哪有那么多钱翻修啊。你家这条路能修还是沾了湿地公园的光吧？」"
    y "「黄河吧？又不止我们家门口这一段……哎呀无所谓，总之是个面子工程。」"
    voice "audio/voice/001252.ogg"
    l "「嗯～」"
    "梁芷柔不置可否，把视线投向了左侧的黄河。"
    voice "audio/voice/001253.ogg"
    l "「说起来，这公园也修起来了啊？」"
    y "「是啊……」"
    scene bg b05 #湿地公园|夏
    with fade
    "我沿着她的目光望去。"
    "在河道的北侧，有一片自岸边漫延出来的湿地。"
    "从前，这里就是一片天然的芦苇荡，也是我小时候的游乐场之一。不过从去年开始，这里被当作了景点，说是什么「湿地公园自然保护区」，还要申请不知道几A级的国家风景区。"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001254.ogg"
    l "「好久都没有来过了呢，从它要修成公园开始。」"
    y "「一样。别提了，我天天从这儿过，都进不去。」"
    y "「还说是保护区呢，人家各种鸟啊鸭子啊本来住得好好的，这一修公园，老巢被掀了一大堆。」"
    show chara c08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/001255.ogg"
    l "「唉～～～」"
    y "「那阵子，一到大清早就开始施工，又挖又砸的，吵得不行，我都是拿他们当闹铃使的。」"
    y "「之前好不容易修完了，结果没过多久，就前一阵子，上游不是发洪水了吗，这边水位跟着一涨，现在里面全淹了，估计还得重新修。」"
    show chara c02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/001256.ogg"
    l "「那还真是……」"
    show chara c08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/001257.ogg"
    l "「哎，对了，那里面的鸟呢？」"
    y "「还行吧，现在又不是孵化期，应该没大事。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001258.ogg"
    l "「嗯……」"
    y "「也不知道这儿什么时候重新开放……不过还是觉得有点怪啊，不习惯。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001259.ogg"
    l "「这就不习惯啦？明年去省城上大学的时候怎么办啊？」"
    y "「是是是，我就这么一说，让姐姐您操心啦。」"
    voice "audio/voice/001260.ogg"
    l "「嘻嘻。」"

    stop music fadeout 1.5
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    l "「……」"

    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    "梁芷柔微微一笑，却忽然沉默了下来，只是再次把目光投向湿地公园。"
    "一群水鸟，正在波光粼粼的水面上翩然起舞。"
    "对于生活在河边的本地人来说，这是一幕并不罕见的光景，但是梁芷柔不知为何却看得有些入迷，甚至连脚步都渐渐放缓。"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    l "「……」"
    y "「……」"
    y "「怎么了？」"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/001261.ogg"
    l "「啊……」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001262.ogg"
    l "「呵，没事。我们走吧。」"
    y "「哦……」"
    l "「……」"
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve
    voice "audio/voice/001263.ogg"
    l "「……唉。」"
    hide chara
    with dissolve
    "在我们继续前进之前，隐约听到她发出了一声几不可闻的叹息。"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    "然而，等我望向她的时候，却没有看出任何异常之处。"
    y "「……」"
    "……是我的错觉吗？"
    hide chara
    with dissolve

    stop sound fadeout 1.5
    scene bg black #黑屏
    with fade
    "……"
    "…………"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    scene bg b08 #新城区|夏
    with fade
    "新城区。"
    "说是新城，其实也不是什么官方称谓，而是民间约定俗成的叫法。"
    "虽然据说最终的规划甚大，但如今所谓的「新城区」里，能看得见的也就是连成一片的几个新建的小区而已。"
    "……还得是把烂尾的和卖不出去的都算上。"
    y "「一过家门而不入啊。」"
    show chara c13b #梁芷柔立绘|夏季私服|疑惑2
    with dissolve
    voice "audio/voice/001264.ogg"
    l "「啊？」"
    y "「没事。你说的那个书店在哪儿啊？」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001265.ogg"
    l "「嗯，快到了，就在前面。」"
    y "「我说啊，把书店开在这么荒无人烟的地方，他是打算卖给谁去啊？」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001266.ogg"
    l "「哈哈……也许是被开发商给骗来的吧。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001267.ogg"
    l "「不过他们家老板人很好的！而且啊，正因为在这么个地方，生意不好做嘛，所以给的折扣力度也特别大！要不然，我也不会跑这么老远来啊对不对！」"
    y "「亏你能找得到这种店……」"
    y "「不过，要是这么不景气的话，万一他们家回头关门了怎么办啊？」"
    show chara c02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/001268.ogg"
    l "「哎～没那么快吧？他们才刚开没多久，就算要关，也得先熬个一年半载的，再说熬不下去的事吧？」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001269.ogg"
    l "「到那时候咱们也该高考了，考完试哪还管他洪水滔天啊！」"
    y "「这……」"
    y "「不愧是你……」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001270.ogg"
    l "「嘻嘻。」"
    scene bg black #黑屏
    with fade
    "……"
    "…………"
    scene bg b08 #新城区|夏
    with fade
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001271.ogg"
    l "「啊，到了！」"
    y "「哦哦！」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001272.ogg"
    l "「就是这儿啦！」"
    hide chara
    with dissolve
    y "「哎哟，看上去还不错啊！」"
    "出现在眼前的，是位于某个高层住宅小区的底商下的一家门脸很小的书店。"
    "小归小，但是装修颇下了一番功夫，再加上新开店不久，倒是显得蛮精致的。"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001273.ogg"
    l "「嘻嘻，进去吧？」"
    y "「嗯。」"

    stop music fadeout 1.5
    scene bg b09 #书店
    with fade
    play sound "audio/sound/effect11.ogg" noloop
    "推开店门的那一霎，挂在门口的风铃发出了悦耳的碰撞声。"
    y "「啊……好凉快。」"
    play sound "audio/sound/ambientnoise07.ogg" fadein 1.5 loop #书店环境噪音
    "骤然从炎热的室外来到了开着空调的房间里，我忍不住打了个激灵。"
    y "「……」"
    y "「喔哟？」"
    "与在外面时的印象差不多，这家书店的内部装潢也很不错。"
    "而且尤其让我意想不到的是，即便开在这么偏僻的地方，这里也依然并非门可罗雀。"
    "除我们以外的客人还有两三个……虽然不多，但终究也是有了些许人气。"
    show charad lg03 at left #书店店员立绘|笑容|近
    with dissolve
    voice "audio/voice/021001.ogg"
    d "「欢迎！」"
    "很快，有一位身穿制服……并且头发染得非常潇洒的店员迎了上来。"
    y "「啊……」"
    show chara lc10 at right #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001274.ogg"
    l "「嗨！」"
    show charad lg01 #书店店员立绘|普通|近
    with dissolve
    voice "audio/voice/021002.ogg"
    d "「嗨～过来啦？来的还真快啊！」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001275.ogg"
    l "「嗯，这不是迫不及待了嘛，你一打电话说东西寄到，我就赶快跑过来啦。」"
    show charad lg03 #书店店员立绘|笑容|近
    with dissolve
    voice "audio/voice/021003.ogg"
    d "「哈哈，稍微等一下哦，我去给你拿。」"
    hide chara
    hide charad
    with dissolve
    "与第一眼看到我时那标准的商业笑容不同，店员对梁芷柔的态度要亲近得多，看来已经很熟了。"
    show charad g01 at left #书店店员立绘|普通
    show chara lc01b at right  #梁芷柔立绘|夏季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/021004.ogg"
    d "「哎，对了，你们是一起的吧？」"
    voice "audio/voice/001276.ogg"
    l "「是，一起的。」"
    "听到梁芷柔肯定的回答，年轻的女性店员不知怎的突然露出了有些恍然的神色。"
    show charad g04 #书店店员立绘|调戏
    with dissolve
    voice "audio/voice/021005.ogg"
    d "「噢……嗯，他是你的？」"
    show chara c03 at center #梁芷柔立绘|夏季私服|生气
    with dissolve
    voice "audio/voice/001277.ogg"
    l "「是同学啦！」"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/021006.ogg"
    d "「哈哈哈，好的好的。那你们先在里面随便看看吧，马上就好。」"
    "梁芷柔虽然迅速地予以澄清，但对方一脸「你懂的」的表情，看来是完全没有听进去，意味深长地看了我一眼以后，转身跑开了。"
    hide charad
    with dissolve
    "我不由得扭头看了一眼身旁的梁芷柔，却恰好与她四目相对。"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    l "「……」"
    y "「……」"
    hide chara
    with dissolve
    "相顾无言，只好尴尬地挪开了视线。"
    voice "audio/voice/021007.ogg"
    d "「我看看啊……梁芷柔……梁～芷～柔……」"
    voice "audio/voice/021008.ogg"
    d "「啊，在这儿呢。」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/021009.ogg"
    d "「我跟你对一下啊，《最新五年高考真题汇编详解》语文数学英语，《高考数学题型全归纳》理科版，《高考阅读真题分类汇编》英语……」"
    voice "audio/voice/021010.ogg"
    d "「……《全国各省市高考试题汇编全解真题》语数外，《高考必做真题课时练》，《高考阅读真题分类汇编》……」"
    "一长串书名从店员的口中鱼贯而出。"
    y "「（妈呀……换成是我，这些书册别说去买，就是倒找钱我都不想去碰啊！）」"
    "虽然想到了她是来买习题的——之前那厚厚的一大摞已经在我做暑假作业的这几天里消化干净了——但真的听到这些书名的时候我还是忍不住惊叹了一番。"
    "学霸的世界我果然不懂。"
    voice "audio/voice/021011.ogg"
    d "「……《高考现代文阅读专项提分训练》，《没有色彩的多崎作和他的巡礼之年》，《一个人的朝圣》，《眠空》……对吧？」"
    show charad g01 at left #书店店员立绘|普通
    show chara c01a at right #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001278.ogg"
    l "「嗯，没错。」"
    y "「嗯……嗯？」"
    "习惯了一大堆「高考」、「试题」之类的字眼，在听到最后几本书的名字时，我有那么一瞬间没有反应过来。"
    stop sound fadeout 1.5
    "而等我明白过来的时候，则忍不住惊讶地叫出声来。"

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    y "「你你你买了个啥？」"
    hide chara
    hide charad
    with dissolve
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/001279.ogg"
    l "「哎？怎么啦？」"
    y "「不是，你最后那几本书是怎么回事……？」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001280.ogg"
    l "「啊，那个啊。」"
    voice "audio/voice/001281.ogg"
    l "「据说评价都很好的。」"
    "话是这么说没错……都是名家作品，即使是我也多少有所耳闻。"
    y "「没想到你还会买这些书啊？」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001282.ogg"
    l "「嘻嘻，打折啊，很便宜的！」"
    y "「哦……不对不对，重点不是这个吧？」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001283.ogg"
    l "「那是什么？」"
    y "「听开头那一大串名字，我还以为你这次买的全都是参考书啊习题集什么的呢……」"
    show chara lc03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/001284.ogg"
    l "「喂喂喂，我又不是机器人，也需要休息放松的啊！」"
    y "「你还要休息……你找点简单的题做，不就是休息了嘛？」"
    y "「类似那种白的喝多了，来两瓶啤的漱漱口什么的……」"
    l "「……」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001285.ogg"
    l "「唉。」"
    "梁芷柔以手扶额，叹出一口气来，一幅放弃辩解的样子。"
    show chara lc07b #梁芷柔立绘|夏季私服|消沉2|近
    with dissolve
    voice "audio/voice/001286.ogg"
    l "「我的形象有这么可怕吗……姐姐我很伤心啊！」"
    y "「……我开个玩笑啊！真不是那个意思！」"
    show chara lc03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/001287.ogg"
    l "「哼，你不用说了，我已经完全明白了！」"
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve
    voice "audio/voice/001288.ogg"
    l "「『这个书呆子每天就只知道泡在习题堆里，怎么可能这么文艺！』……对吧？」"
    show chara lc03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    with hpunch
    y "「噗！」"
    voice "audio/voice/001289.ogg"
    l "「你看吧，肯定就是。」"
    y "「喂喂喂，你一定要以为我无时无刻不在心里诋毁你吗？」"
    voice "audio/voice/001290.ogg"
    l "「哼！不是吗？」"
    y "「当然不是啊！我只是第一次知道你喜欢什么类型的书，很礼貌地表示一下惊讶而已啊！你不要多想好不好！」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001291.ogg"
    l "「……真的吗？」"
    y "「真的！千真万确啊！」"
    voice "audio/voice/001292.ogg"
    l "「嗯～～～？？」"
    "梁芷柔用怀疑的眼神盯着我看。"
    show chara lc03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/001293.ogg"
    l "「哼，算了。」"
    "梁芷柔瞪了我一眼，轻轻揭过了这个话题。"
    hide chara
    with dissolve
    stop music fadeout 1.5

    "这反而让我有点吃不准她是在故意逗我还是真的有点不高兴了……"
    "不过，我也确实不是在胡说八道蒙混过关。"
    "我真的是对她的兴趣爱好一无所知。从前是没什么接触，这几天虽然关系确实是熟了很多，但话题主要聚焦在学习方面，还没有聊到业余生活这边。"
    "只是……说实话，我也是真没有想到她居然会选择这些书。"
    "倒不是说这些书有什么奇怪的，或者说恰恰相反，是太大众化了，无论谁看都不稀奇。"
    "之前还以为她会看一些更加小众的作品呢……这种凭空瞎猜出来的高冷设定，显然与真实情况相去甚远。"
    show charad sg01 #书店店员立绘|普通|远
    with dissolve
    voice "audio/voice/021012.ogg"
    d "「哎！！」"
    play sound "audio/sound/effect12.ogg" noloop
    with vpunch
    "噗通！"
    play sound "audio/sound/ambientnoise07.ogg" fadein 1.5 loop #书店环境噪音
    show charad g01 #书店店员立绘|普通
    with dissolve
    "在我们说话的期间，店员从摆在角落里的包袱堆中挑出其中一个大号的，连拖带拽地扔在了我们的面前。"
    show charad lg01 #书店店员立绘|普通|近
    with dissolve
    voice "audio/voice/021013.ogg"
    d "「……呼，就是这个啦！」"
    "虽然只走了短短的几步，店员小姐却并不怎么轻松。"
    y "「……」"
    show charad lg01 at left #书店店员立绘|普通|近
    show chara lc06 at right #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    l "「……」"
    y "「看来……挺沉的？」"
    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/001294.ogg"
    l "「啊哈哈……还好啦。」"
    y "「我说你搬得动吗？」"
    voice "audio/voice/001295.ogg"
    l "「还……好啦。哎，姐，钱我微信给你转过去了啊？」"
    "梁芷柔罕见地用了一种不怎么有信心的语气回答，并且还蹩脚地岔开了话题……看来真的是非常沉啊！？"
    "她应该不是第一次在这里买书了，如果以前也是这种情况的话，她是怎么把书搬回去的……"
    show charad lg03 #书店店员立绘|笑容|近
    with dissolve
    voice "audio/voice/021014.ogg"
    d "「嘿嘿，这次总算是学聪明了啊，知道叫男朋友来帮忙啦？」"
    show chara lc03 at center #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/001296.ogg"
    l "「都说了不是男朋友啦！同学！是同学！！」"
    show charad lg04 #书店店员立绘|调戏|近
    with dissolve
    voice "audio/voice/021015.ogg"
    d "「好好好，男同学，男同学行了吧？」"
    voice "audio/voice/001297.ogg"
    l "「你这……哎！」"
    "看上去很是开朗的店员小姐显然对梁芷柔的解释充耳不闻，把后者闹了个大红脸。"
    hide chara
    show charad lg04 at center #书店店员立绘|调戏|近
    with dissolve
    voice "audio/voice/021016.ogg"
    d "「来，这位男同学，过来搭把手。」"
    y "「啊？啊……」"
    with hpunch
    "店员小姐坏笑着把包裹搬起来，然后交到了我的手上。"
    voice "audio/voice/001298.ogg"
    l "「哎！你干什么呀……」"
    show charad lg04 at left #书店店员立绘|调戏|近
    show chara lc03 at right #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/001299.ogg"
    l "「你别给他啊，他就是陪我过来一下，他家就在旁边！」"
    show charad lg02 #书店店员立绘|吃惊|近
    with dissolve
    voice "audio/voice/021017.ogg"
    d "「啊？是吗？」"
    voice "audio/voice/001300.ogg"
    l "「是，真的！」"
    "看到梁芷柔的模样，店员小姐似乎也意识到自己会错了意，不由得尴尬了起来。"
    y "「行了没事，我帮你搬吧。」"
    hide charad
    show chara lc06 at center #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/001301.ogg"
    l "「哎？」"
    y "「这么沉的一大坨……你搬得动嘛？」"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    voice "audio/voice/001302.ogg"
    l "「搬得动！……」"
    y "「得了啊，你别费那个劲了，还是我来吧。」"
    y "「走。」"
    with vpunch
    "我颠了颠怀里的包裹，换了个舒服一点的姿势，不由分说拔腿就走。"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    stop sound fadeout 1.5
    voice "audio/voice/001303.ogg"
    l "「哎你等等我！」"
    hide chara
    with dissolve

    play sound "audio/sound/effect11.ogg" noloop
    "走到门口，我一边用身体挤开大门，一边不忘回头朝店员小姐点头致意。"
    show charad sg02 #书店店员立绘|吃惊|远
    with dissolve
    pause 0.5
    hide charad
    with dissolve
    "虽然只是一个误会……但这也算是给我助攻了吧？"

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音
    scene bg b08 #新城区|夏
    with fade
    y "「哇，好热。」"
    "刚一离开书店，迎面便是一股热浪袭来。"
    show chara c08b #梁芷柔立绘|夏季私服|担心2
    with dissolve
    voice "audio/voice/001304.ogg"
    l "「叶雨潇，没事你别管了，给我吧。」"
    y "「不给。」"
    show chara c03 #梁芷柔立绘|夏季私服|生气
    with dissolve
    voice "audio/voice/001305.ogg"
    l "「你干嘛呀，真的，没问题的，我以前也都是自己搬回去的！」"
    y "「你这么一说我还真是挺好奇的，你怎么搬的啊？你家距离这里也得有三四里地呢吧？」"
    "虽然不知道梁芷柔家的具体位置，但总之是在百货大楼的另一侧，和我家是个对角，大致的距离还是能估算出来的。"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001306.ogg"
    l "「桥东边一点有公交车，直接到我家门口，也没多远……」"
    y "「哦，那儿啊……那不也得有将近一公里呢吗？」"
    show chara c08b #梁芷柔立绘|夏季私服|担心2
    with dissolve
    voice "audio/voice/001307.ogg"
    l "「啊……」"
    y "「行了行了，我知道了，交给我吧。」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001308.ogg"
    l "「哎……」"
    y "「我啊，也不远送，就还是给你送到公交站，好不好？你呢，也别矫情了，全当是我向你交的学费，成吗？」"
    voice "audio/voice/001309.ogg"
    l "「这……哎。好吧。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001310.ogg"
    l "「……谢谢！」"
    y "「呵，客气。」"

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    scene bg b04 #滨河路|夏
    with fade
    "二过家门而不入。"
    "路过我家门口的时候，梁芷柔又一次努力地劝说让我回家，不过当然还是以失败告终。"
    "我继续抱着这一大包的书，吭哧吭哧地往前走。"
    "这玩意是真沉哪……刚开始的时候还不是很明显，走出一段距离以后就变得愈发吃力。"
    y "「说起来啊……」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001311.ogg"
    l "「嗯？」"
    y "「你这样大费周章的，能省多少钱啊？」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001312.ogg"
    l "「嗯……百八十块钱吧！」"
    y "「噢……」"
    "说多不算多，说少也不少。"
    "考虑到梁芷柔做题的速度，这些习题应该也禁不住多久的消耗……这样来算的话，积累起来确实是能省下一笔数量不菲的钱。"
    "但是，相对于自行搬运的路程距离和所需要消耗的体力，我还是有点怀疑它的性价比。"
    y "「我说姐姐啊，您倒是真会过日子……不过你有那么缺钱嘛？这么累自己？」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001313.ogg"
    l "「……唉，缺啊。」"
    "梁芷柔犹豫了一下，大方地承认了。"
    y "「哎？」"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/001314.ogg"
    l "「我穷得很啊，除了必须买的书以外不敢花钱的，现在这样，我好歹还能挤出一点钱来买点别的杂书。」"
    y "「……至于吗？你是独生女吧？你爸妈？」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001315.ogg"
    l "「我爸妈都在上班，家里嘛，倒是就我一个……但是没办法啊，明年要上大学了嘛，只能开始节衣缩食拼命攒钱喽。」"
    y "「大学……上大学有那么贵吗？」"
    "大学的学费确实不算便宜，一年总要有个几千块钱，但如果是父母两人供养一个孩子的话，应该不至于很窘迫吧？"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/001316.ogg"
    l "「那倒不是。但是……」"
    voice "audio/voice/001317.ogg"
    l "「学费是一方面，可还有生活费啊。」"
    y "「哎？」"
    voice "audio/voice/001318.ogg"
    l "「唉……」"
    "梁芷柔并没有直接回应我的疑惑，而是罕见地叹了口气。"
    y "「啊……」"
    "我也明白过来了。"

    stop sound fadeout 1.5
    scene bg b02 #城区
    with fade
    "——生活费。"
    "西北这一带，由于经济条件所限，物价还是相对低廉的。"
    "无论是我们老家这样的县、镇，还是省城那种相对较大的城市，基本的日常开销都算不上很多，以至于我熟视无睹，忽略了这一点。"
    "然而，梁芷柔的未来……却不在这里。"
    "她将来的所在，一定是东部的某一个大城市。"
    "我对那种城市的生活完全没有概念，但想来花销不会很少，至少……相对于老家这边的家庭收入来说，会占用相当可观的一部分。"

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音
    scene bg b04 #滨河路|夏
    with fade
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    y "「……原来如此。」"
    voice "audio/voice/001319.ogg"
    l "「我爸妈上班很辛苦的，为了给我攒钱，还经常要加班啊什么的。我呢，说实话没法帮父母分担什么，只能是尽量别给他们增加负担，别让他们再多操心了。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001320.ogg"
    l "「就是这样啦！所以啊，能省则省嘛！」"
    "说这话的时候，梁芷柔一副理所当然的样子，而若是几天之前的我，听到了也无非会随便感慨一下，然后继续放任自流罢了。"
    "但对于现在的我来说，却是另一种感受。"

    stop sound fadeout 1.5

    scene bg black #黑屏
    with fade
    "这种浑浑噩噩的状态，以前或许还没有什么实感，但在有了对比之后，差距一下子就清晰起来了。"
    "梁芷柔已经在规划那么遥远的事情了……但，我却对自己的未来一直很含糊，在此之前甚至都没有认真想过大学的事，更不要说做什么准备了。"
    "虽然不是不想做出改变，甚至已经冲动着迈出了第一步，但接下来该怎么走，还根本没有概念。"
    "这样下去，我忍不住又要开始怀疑了——"
    "自己现在所做的这一切，真的会有意义吗？"

    scene bg b04 #滨河路|夏
    with fade
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001321.ogg"
    l "「……想什么呢？」"
    y "「……」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001322.ogg"
    l "「喂，喂？」"
    y "「……」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001323.ogg"
    l "「叶雨潇？」"
    with hpunch
    y "「啊？啊……」"
    "不知不觉走神了。"
    "等我回过神来，发现梁芷柔正在旁边看着我轻笑。"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001324.ogg"
    l "「想什么呢？那么认真，跟你说话都不理我。」"
    y "「啊，没…什么……」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001325.ogg"
    l "「没什么是什么啊！」"
    y "「哈哈……我在想啊，姐姐你真是懂事啊，不愧是我姐姐！」"
    "我开了个玩笑，试图蒙混过关。"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001326.ogg"
    l "「嘻嘻，那还用说嘛？弟弟？」"
    l "「……」"
    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/001327.ogg"
    l "「其实呀，我这也是吃过亏，才长的记性。」"
    y "「吃亏？」"
    voice "audio/voice/001328.ogg"
    l "「我之前跟你说过吧，初一的时候，家里出过一件事。」"
    y "「哦哦，对。」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001329.ogg"
    l "「吃一堑长一智，就是这样。」"
    "……所以到底是什么事啊？"
    "虽然好奇，不过过问人家家里的私事终究不太好，我张了张嘴巴，还是把话咽了回去。"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001330.ogg"
    l "「嘻嘻，为了不重蹈姐姐我的覆辙，弟弟你可长点心吧！」"
    y "「……」"
    y "「喂喂喂来劲了啊？说你胖你还真就喘上了！」"
    show chara lc03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/001331.ogg"
    l "「你才胖！不许说我胖！」"
    with hpunch
    y "「哇哇！哇！别掐我啊！书要抱不住了啊！」"
    voice "audio/voice/001332.ogg"
    l "「哼！！！」"
    y "「饶命！饶命啊！！」"
    "我觉得，我首先需要吃一堑长一智的，是以后绝对不能在女人面前提「胖」这个关键词。"

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    scene bg b04 #滨河路|夏
    with fade
    play sound "audio/sound/effect12.ogg" noloop
    y "「呼啊！」"
    "走了大约一刻钟，我们终于到达了公交站。"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001333.ogg"
    l "「谢谢，辛苦你啦！」"
    y "「嘿，还好吧。」"
    "我话虽这么说着，可实际上并不能算是轻松。"
    "天气本来就热，再花了这么多力气，早就汗流浃背了。"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001334.ogg"
    l "「哎呀，出这么多汗！」"
    voice "audio/voice/001335.ogg"
    l "「来……」"
    "梁芷柔翻出一包纸巾递过来。"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    voice "audio/voice/001336.ogg"
    l "「……给。」"
    y "「啊，谢谢。」"
    "我接过纸巾，从里面连抽出两张，胡乱抹了一把脑门，于是纸巾瞬间就吸满了汗水，与手上的灰土混在一起，变得一团花。"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001337.ogg"
    l "「哪里啦，是我谢谢你。」"
    y "「好啦，那就……啊，正好，车来了。」"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/001338.ogg"
    l "「哎，啊，真的，好巧。」"
    y "「挺好，不用在这儿晒太阳了。」"
    hide chara
    with fade
    play sound "audio/sound/effect13.ogg" noloop
    y "「来吧，我帮你搬上去。」"
    with vpunch
    y "「……嘿！」"
    y "「那就这样吧，回去路上小心啊。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001339.ogg"
    l "「嗯，好。」"
    voice "audio/voice/001340.ogg"
    l "「你也是啊，伤口没问题吧？小心别感染了。」"
    y "「嗯，放心吧，没啥大不了的，早好了。」"
    voice "audio/voice/001341.ogg"
    l "「哦……」"
    show chara sc10 #梁芷柔立绘|夏季私服|开心|远
    with dissolve
    voice "audio/voice/001342.ogg"
    l "「那我就走啦，今天真是谢谢你。」"
    y "「不客气，回头见。」"
    show chara sc11 #梁芷柔立绘|夏季私服|微笑|远
    with dissolve
    voice "audio/voice/001343.ogg"
    l "「嗯，拜拜～」"
    hide chara
    with dissolve
    play sound "audio/sound/effect13.ogg" noloop
    "……"
    "…………"
    "我目送梁芷柔乘坐的公交远去。"
    y "「嗯，回去吧。」"

    stop music fadeout 1.5
    scene bg black #黑屏
    with fade
    "……"
    "…………"

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音
    scene bg b04 #滨河路|夏
    with fade
    "独自一人走在回家的路上。"
    y "「……」"
    "下午的太阳依旧火热，我挑着有树荫的地方走，尽量躲避阳光的照晒。"
    "街上没有多少行人，只有知了在无休止境地嘶吼，由于距离很近，愈发显得聒噪。"
    "我有些烦躁地望向河边。"
    scene bg b05 #湿地公园|夏
    with fade
    "湿地公园里还是一片汪洋。"
    "上游洪水造成的冲击尚未恢复，不过，对于水鸟来说，似乎影响并没有那么大。"
    "倒不如说，因为暂时停止对外开放，没有了游客的骚扰，它们反而更乐得自在了。"
    bird "「啾——」"
    "有数只水鸟展开翅膀，凌空而起。"
    scene bg b00a #天空|候鸟
    with fade
    "是雁。"
    y "「斑头雁……么？」"
    "因为从小就生活在河边，这种鸟可以说是司空见惯了，一眼就能认出来。"
    "斑头雁……对我们这里来说属于夏候鸟，算是很常见的种类。"
    "它们号称是世界上飞得最高的鸟，每到深秋，都要成群结队向南迁徙，穿过唐古拉山口、翻过喜马拉雅山脉，一直飞到印度才会停留下来越冬。"
    "等到来年，又原路返回。"
    "不畏艰辛，周而复始。"
    scene bg b05 #湿地公园|夏
    with fade
    y "「……」"
    "它们……是因为什么，才要这样拼命呢？"
    "看看这里的其他候鸟吧，每年同样是要南下，大多数都是往云贵那个方向绕道前往东南亚，却没有几个敢于直面青藏高原的。"
    "如果只是为了生存……为何不去选择一条简单、轻松的道路呢？"

    stop sound fadeout 1.5
    scene bg black #黑屏
    with fade
    "此前，我从未纠结过这种问题。"
    "上学、高考，考上一个能给家里交代得过去的学校，找一个比较容易就业的专业，四年后找份足够糊口的工作，然后开始熬年头，随后在父母的催促中相亲、恋爱、结婚、生子……"
    "我曾以为我的人生大抵如此。"
    "或许平凡，但却轻松。"

    scene bg b00 #天空
    with fade
    play music "audio/music/bgm03.ogg" fadein 1.5 #秋～绯月～
    "勇攀高峰什么的听上去很不错，但所需的付出也不是一星半点。"
    "「憧憬与梁芷柔同样的未来」？"
    "在最初的冲动逐渐平复之后，我反而更加清楚地认识到了现实。"
    "姑且先不管她会不会对我这种单方面的想法有所回应，单只说想要勉强跟随她的步伐——去考一个和她同城的、档次还可以的大学——就已经需要我拿出前所未有的干劲去拼上一整年的命了。"
    "这不是随随便便就能做到的事。"
    "虽然我总说「以前曾经努力过」，但自己其实很清楚，即便是曾经的那种努力，也早已满足不了现在的需求了，何况此时连那时候的程度都还差得远。"
    "而即便真的做到了，最后能否「称心如意」，也还未可知晓。"
    scene bg black #黑屏
    with fade
    "——那么，我该为这个虚无缥缈的想法押上所有筹码吗？"
    #回忆模式
    scene bg b03 #病房
    with fade
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001042.ogg"
    l "「你说你，挺聪明的一个人，怎么就老是……哎。」"
    scene bg b07 #快餐店
    with fade
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001175.ogg"
    l "「嘻嘻……可别这么说啊！你不相信自己，还不相信我啊？我都说你有天赋了，相信我，没错的。」"
    with fade
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001207.ogg"
    l "「一本线嘛，小意思，包在姐姐身上。而且，除了这个小目标，如果你还能继续保持努力的话，最后考到百薇也不是不可能的。」"
    scene bg b06 #商业街
    with fade
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001241-1.ogg"
    l "「所以呢，我高度怀疑你其实很有天赋，只是还没完全发掘出来。」"
    scene bg black #黑屏
    with fade
    "不知为何，在这种时候，我首先想到的是梁芷柔对我的鼓励。"
    "说起来，在学校的时候，或许是老师们对自己的教学质量也有自知之明吧，他们对班上大多数学生的期待，似乎也就是一般般的样子。"
    "甚至就算是我的老爸老妈，也从来没有在这方面对我提过什么太高的标准。"
    "没想到，反倒是梁芷柔……会对我抱有一些期望。"
    "我若轻易放弃，她会因此失望吗？"
    scene bg b05 #湿地公园|夏
    with fade
    stop music fadeout 2.5
    y "「唉！」"
    y "「……」"
    "长叹出一口气来，却丝毫未能变得舒畅。"
    "于是，我索性深深地吸足了气，然后——"
    with vpunch
    y "「——啊啊啊！！！！！！！」"
    "在这个炎炎夏日的午后，用自己的满腔哀怨，惊起一滩鸥鹭。"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t04 #转场 书店
    with fade
    pause

#之后。

    scene bg b02 #城区
    with fade
    "……在那之后。"
    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with fade
    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    y "「……」"
    l "「……」"
    y "「……」"
    l "「……」"
    scene cg04a2 #梁芷柔快餐店学习CG-1|就坐|皱眉|CG04a2
    with dissolve
    voice "audio/voice/001344.ogg"
    l "「你还是先跳过那道题吧。」"
    y "「啊？」"
    voice "audio/voice/001345.ogg"
    l "「嗯……我看你跟那道题上面卡了快十分钟了吧。」"
    y "「啊……」"
    voice "audio/voice/001346.ogg"
    l "「平时倒无所谓，考试的时候遇上这种情况，还是先把它放下，做别的题去比较好。」"
    y "「哦、哦。」"
    scene cg04a3 #梁芷柔快餐店学习CG-1|就坐|无奈|CG04a3
    with dissolve
    voice "audio/voice/001347.ogg"
    l "「考试嘛，本质上是在有限的时间里尽可能拿更多的分，如果题太难大不了这道题的分我不要了还不行么，但至少得把能拿到的分攥住了吧？」"
    voice "audio/voice/001348.ogg"
    l "「要是为了跟一道题较劲，反而把其他的分也给丢掉了，就得不偿失了。」"
    y "「噢！」"
    voice "audio/voice/001349.ogg"
    l "「继续吧，那道题我有印象，待会儿做完了一起给你讲。」"
    y "「好……」"
    stop sound fadeout 1.5

    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with dissolve
    "我们继续着每天的学习会。"
    "之前的暑假作业只能算是开胃小菜，在如今的「正餐」面前不值一提。"
    "那些被她看似十分轻松就解决干净的习题，现在正如同大山一般压到了我的身上。"
    "梁芷柔从其中筛选出难度适合的题目给我，再根据我做的情况进行讲解。她之前已经把这里面的困难题目都做过一遍了，解决我的问题自然也是轻车熟路。"
    "随着她对我的知识结构的进一步了解，题目的针对性也在日渐增强。"
    "虽然时日尚短，却已经能明显地感受到其中的不同之处。只要假以时日，必会大受裨益。"
    scene bg black #黑屏
    with fade
    "……除非是像我现在这样，被自己糟糕无比的状态严重地拖了后腿。"
    "还处在迷茫之中的我，既缺乏一往无前的勇气，又不愿浅尝辄止即放弃，只好就先这样半死不活地继续维持着。"
    "「至少试着朝『小目标』努力一下吧！这样也不算辜负她了。」……我给自己找了这样一个借口。"
    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with fade
    "连自己都知道是借口，这样的说辞当然毫无说服力，然而对于现在的我来说，实在也做不出什么决断。"
    "这样的心态当然也影响到了现实中的状态，我的注意力变得更容易涣散了。"
    "偏偏学习的压力还在加大……结果就是各种莫名其妙的失误频频出现，反过来更加影响心态，几乎要陷入恶性循环之中了。"
    "不过……"

    scene cg04b1 #梁芷柔快餐店学习CG-2|讲题|CG04b1
    with dissolve
    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    voice "audio/voice/001350.ogg"
    l "「基本的东西一定要记住！」"
    voice "audio/voice/001351.ogg"
    l "「所谓『粗心』，永远只是『不会』的借口。理解还不到位就自以为会了，到用的时候自然要出错。」"
    voice "audio/voice/001352.ogg"
    l "「有不会的就要补上，不能拖。越拖就越多，时间长了补都没办法补。」"
    voice "audio/voice/001353.ogg"
    l "「听见了没有！？」"
    stop sound fadeout 1.5

    "梁芷柔却并没有因此而不耐烦。"
    "倒不如说，她对此更加上心了，每次都不厌其烦地把我暴露出来的问题掰开揉碎地讲，还苦口婆心地给我传授她的各种学习心得。"
    "可以感觉得到她是真心希望我的成绩能有所提高的……就不知她这样做是出于「姐姐」的关爱，还是真的认为我是个可造之材了。"
    "无论如何，都可以称得上是仁至义尽，也让我愈发感到羞愧难当。"

    scene bg black #黑屏
    with fade
    "不能……再这样颓废下去了，必须要有所改变。"
    "哪怕微不足道，哪怕最终于事无补。"
    "但至少，我不能让她白费苦心。"
    "……"
    "…………"

#又过了两天。

    scene bg b02 #城区
    with fade
    "又过了两天。"

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.0 loop #街道蝉鸣噪音
    scene bg b06 #商业街
    with fade
    pause
    stop sound fadeout 3.0
    scene bg b07 #快餐店
    with fade
    pause
    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with fade
    play sound "audio/sound/ambientnoise06.ogg" fadein 1.0 loop #快餐店环境噪音
    "……"
    "…………"
    scene bg black #黑屏
    with fade
    voice "audio/voice/001354.ogg"
    l "「……啊啊啊，身子都僵了！」"
    stop sound fadeout 3.0
    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    scene bg b06 #商业街
    with fade
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001355.ogg"
    l "「好啦，我们走吧。」"
    "在学习会结束以后，我们离开了快餐店，而梁芷柔又一次跟在了我的身后。"
    y "「哎？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001356.ogg"
    l "「书店。」"
    y "「哦哦……又有书到了？」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001357.ogg"
    l "「对呀。」"
    y "「这才几天啊……又是习题集？」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001358.ogg"
    l "「不全是吧……还有点小说什么的。」"
    "也就是说大部分都是了……真可怕。"
    y "「这次是谁的书？」"
    voice "audio/voice/001359.ogg"
    l "「乔\[哔——\]丁的，《权力的游戏》……」"
    y "「哎哟？你还爱看这……」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/001360.ogg"
    l "「……的英文版。」"
    y "「噗！」"
    "英文版是什么鬼！你是打算拿来练习阅读理解和词汇量的吗？"
    y "「咳咳咳！老这么大喘气有意思吗？」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001361.ogg"
    l "「哈哈哈，没有啊！我确实很喜欢这小说的。」"
    y "「真的吗？」"
    voice "audio/voice/001362.ogg"
    l "「真的啦，电视剧我也一直在追呢。快走吧！」"
    y "「哎！」"
    scene bg black #黑屏
    with fade
    "……"
    "…………"
    scene bg b04 #滨河路|夏
    with fade
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001363.ogg"
    l "「～～」"
    voice "audio/voice/001364.ogg"
    l "「～～」"
    y "「嗯？怎么哼上歌了？」"
    voice "audio/voice/001365.ogg"
    l "「嘻嘻，没什么呀，就是想哼哼了。」"
    y "「小猪啊？还哼哼。」"
    show chara c03 #梁芷柔立绘|夏季私服|生气
    with dissolve
    voice "audio/voice/001366.ogg"
    l "「呸！你才是猪呢。」"
    show chara c02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/001367.ogg"
    l "「本来挺高兴的，让你这么一搅和，全完蛋了！」"
    voice "audio/voice/001368.ogg"
    l "「哼！」"
    y "「呃……开个玩笑，至于嘛。」"
    y "「说说，什么事这么开心？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001369.ogg"
    l "「没什么呀。」"
    y "「没什么是什么……」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/001370.ogg"
    l "「就是没什么呀。你这个大猪头最近终于开窍了，不行吗？」"
    y "「哈？」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001371.ogg"
    l "「嘿嘿。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001372.ogg"
    l "「你呀，总算是长了点记性了哈！不像最开始那两天似的，每天一大堆低级错误，都快愁死我了。」"
    y "「呃……」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001373.ogg"
    l "「不错，继续保持喔！」"
    voice "audio/voice/001374.ogg"
    l "「～～」"
    y "「……」"
    "正如她所说的那样，经过了一段时间的调整，这两天我总算是稍稍有所起色。"
    "我在强迫自己集中精神……效果还算是马马虎虎，尽管没办法达到自己真正主动的那种效率，但最起码不再是前面那种浑浑噩噩的状态了。"
    "保持这种状态并不是容易的事，不过说到底我也是没什么更好的办法了，只能先这样子把这个暑假硬扛过去——没准扛着扛着就习惯了呢？"
    "至少……在发现自己如此微小的进步，都能被她注意到之后，我感到自己的干劲又提起来了一点。"
    scene bg black #黑屏
    with fade
    "……"
    "…………"
    scene bg b08 #新城区|夏
    with fade
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    "快走到书店的时候，梁芷柔叫了我一下。"
    voice "audio/voice/001375.ogg"
    l "「喂。」"
    y "「嗯……嗯？啊，怎么了？」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001376.ogg"
    l "「倒是没什么事……你自己琢磨什么呢？看你半天没说话。」"
    y "「啊……没什么。」"
    "刚才一直在思考未来，估计又是露出了一脸心事重重的模样。"
    "虽然也确实是如此……但个中缘由就不足与外人道了，此时还是蒙混一下吧。"
    y "「我是在想啊……」"
    y "「你说新城区盖了这么多楼，也没几个人来住，多浪费啊？」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001377.ogg"
    l "「啊……呵呵，这个呀。」"
    voice "audio/voice/001378.ogg"
    l "「这不是才刚盖起来嘛。而且旧的不去新的不来，等旧城区那边的改造再继续一段时间的话，估计总还是会有人往这边来的吧！」"
    y "「也是。不过我是不想往这边搬啊！住惯了自己家的，再看这种楼总觉得怪怪的。」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001379.ogg"
    l "「怪怪的？」"
    y "「嗯……怎么说呢，风格太现代，感觉不像是咱们县了。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001380.ogg"
    l "「啊，这倒也是。」"
    y "「对吧，别说是咱们这儿了，就算是在省城，也就是西区那种新开发的地段，这种风格才比较多吧？」"
    y "「真的……感觉真的是不怎么协调，好像一瞬间扎进了某个大城市，偏偏还是个鬼城。」"
    voice "audio/voice/001381.ogg"
    l "「鬼城……」"
    y "「对啊，到处都是高楼大厦，结果里面人影见不到一两个，不是鬼城是什么。」"
    y "「虽然我是没去过什么大城市，不过反正不会是这个德行吧？」"
    voice "audio/voice/001382.ogg"
    l "「啊，那倒也未必。」"
    y "「呃？」"
    voice "audio/voice/001383.ogg"
    l "「大城市嘛，寸土寸金，市里面的地价很贵的。然后来的人又多，住不下了就只能往原来的郊区扩张，那些地方新建起来的小区，有些也就跟这里差不多荒。」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001384.ogg"
    l "「当然啦，整体上来说还是差得太远了。别说一线，就算和那些二三线的城市比，咱这儿也不是一个档次的。」"
    y "「喔……」"
    y "「你还真是够了解的啊？」"
    "不过，想想也是，铁定要去外地上学的人，自然会对这些事情多关注一些。"
    y "「之前去过哪里嘛？……哎对了，这么一说我记得去年暑假你好像参加了一个外地的比赛来着？」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001385.ogg"
    l "「啊……」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001386.ogg"
    l "「哎，先别说我，你呢？」"
    y "「啊？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001387.ogg"
    l "「你有没有去过哪个大城市啊？以前……啊，省城不算，其他的那些城市，旅游啊什么的，嗯？」"
    y "「这个……」"
    "感觉被强行转移了话题……"
    "虽然有些在意，不过梁芷柔似乎在有意回避，我也不好继续刨根问底。"
    "反正这个话题本来也是我胡扯出来的，不如索性顺着她的话茬说吧。"
    y "「哦，这个呀……上小学以前吧，有一年冬天跟家里去首都旅过一次游。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001388.ogg"
    l "「喔……」"
    y "「不过说实在的，没什么印象了，就记得被我爸妈带着去广场看升旗，因为起得太早，走到一半我就趴在我爸怀里睡着了。」"
    y "「等到睁开眼，国旗已经升到顶了，我当时不干了，哇哇地哭，我妈给我买了根冰糖葫芦，我吃到外面的糖衣，立刻开心了，也不哭了，就在那儿专心致志地舔。」"
    y "「结果后来舔到山楂被酸到了，又开始哭……到了最后，去了这么一趟，记住的就是那根冰糖葫芦。」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001389.ogg"
    l "「噗……」"
    voice "audio/voice/001390.ogg"
    l "「哈哈哈，你个吃货！刚才还好意思说我是小猪！你才是真正的猪呢！」"
    y "「喂喂喂，我好心和你分享自己的经历，你这么嘲笑我我很伤心的好不好？」"
    voice "audio/voice/001391.ogg"
    l "「嘻嘻，好吧好吧，我错了行不行？除此以外呢？还去过哪儿吗？」"
    y "「那就没有了。有一年本来家里说要去长三角那边来个五日游的，结果后来有事，没走成。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001392.ogg"
    l "「这样啊……」"
    y "「对呀，然后我就一直闷在这个小山沟里了。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001393.ogg"
    l "「嗯……」"
    voice "audio/voice/001394.ogg"
    l "「那你有没有想过走出去呢？」"
    y "「走出去……」"
    voice "audio/voice/001395.ogg"
    l "「嗯，走出去。」"
    y "「……」"
    y "「想啊。大城市多好啊，什么都有，机会也多。」"
    y "「可问题是，怎么走啊？毕业以后出去打工吗？」"
    voice "audio/voice/001396.ogg"
    l "「当然不是那个意思，我觉得你完全可以考到那边去读大学嘛！」"
    y "「哎哟我的班长大人啊，您这就是何不食肉糜了。」"
    y "「我这种考二本都费劲的人，往那种地方报不是找死么！我又不是你。」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001397.ogg"
    l "「嘻嘻，以前话是这么说没错，不过现在不是不一样了嘛？」"
    y "「哎？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001398.ogg"
    l "「我说过，有本姐姐帮你补习功课，一本线这个小目标只是个开胃菜！」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001399.ogg"
    l "「而且我还说过，只要你自己努努力，考到百薇也不是不可能，对不对？」"
    y "「……呃，是吧。」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001400.ogg"
    l "「所以呢，如果你能考到那个分数的话，大概也可以在那些大城市里找一个差不多的一本了。」"
    y "「……」"
    voice "audio/voice/001401.ogg"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    l "「对不对？」"
    y "「是……吧。」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001402.ogg"
    l "「要不要考虑考虑？」"
    "梁芷柔故意露出一种奸商一样的笑容，半开玩笑似的对我进行劝诱。"
    y "「……」"
    stop music fadeout 2.5
    "老实说，这个提案让我有些心动。"
    "如果真能做到的话，是不是就代表……我可能……"
    "考到和她相同的城市去上大学？"
    scene cg01a #梁芷柔听讲CG-1|标准|CG01a
    with fade
    "……"
    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fade
    "…………"
    play sound "audio/sound/effect04.ogg" noloop
    scene cg03b #梁芷柔探病CG-2|起风|CG03b
    with dissolve
    "……………………"
    scene bg black #黑屏
    with fade
    y "「……」"
    y "「…………」"
    "……"
    "…………"
    scene bg b08 #新城区|夏
    with fade
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    y "「呼……」"
    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音
    y "「我考虑考虑。」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001403.ogg"
    l "「嗯！」"
    y "「真的……只是先考虑考虑。毕竟现在说这个还是太早了，别说百薇，就您现在这个开胃菜我就已经消化不良了啊！」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001404.ogg"
    l "「哎～～那是你自己的状态没调整好！你看你最近不就很不错嘛。」"
    voice "audio/voice/001405.ogg"
    l "「学习这种事啊，就不是一蹴而就能成的，一点一点来，相信自己啦！」"
    voice "audio/voice/001406.ogg"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    l "「嘻嘻～」"
    hide chara
    with dissolve
    y "「……」"
    y "「……唉。」"
    "我确实有些心动了。"
    "但是……尽管如此，我还是没敢应承下来，只是说了个活话。"
    "心里没底。怕自己做不到，更怕做不到的话，会让自己，以及她……其他人失望。"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001407.ogg"
    l "「～」"
    hide chara
    with dissolve
    "不知道是没注意到还是故意无视我话里的情绪，梁芷柔似乎还蛮高兴的，轻快地走到了前面。"
    y "「（可恶……）」"
    "每到这种时候，就会发现自己的懦弱。"
    "忍不住自我厌恶起来了……如果一直这样下去，我只会一事无成的吧。"
    "「追赶梁芷柔」什么的，就更是痴人说梦了，连宣之于口的资格都不会有。"
    stop sound fadeout 3.0
    scene bg black #黑屏
    with fade
    "我……需要改变。"
    "必须，要改变。"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t03 #转场 快餐店
    with fade
    pause

#七夕。
#8月9日。

    scene bg b02 #城区
    with fade
    "这样的日子又过了两天。"
    "然后，到了「某日」……"

    play sound "audio/sound/ambientnoise06.ogg" fadein 2.5 loop #快餐店环境噪音
    scene cg04d #梁芷柔快餐店学习CG-4|看书|CG04d
    with fade
    y "「……」"
    l "「……」"
    y "「……」"
    voice "audio/voice/001408.ogg"
    l "「……嗯？」"
    y "「……」"
    l "「……？？」"
    voice "audio/voice/001409.ogg"
    l "「哎，问你个事。」"
    y "「嗯？」"
    voice "audio/voice/001410.ogg"
    l "「女孩子看安\[哔——\]宝贝的书很奇怪吗？」"
    y "「完全不奇怪啊。」"
    voice "audio/voice/001411.ogg"
    l "「那你干嘛总是用很奇怪的眼神盯着我看。」"
    y "「因为你居然在看安\[哔——\]宝贝的书啊！」"
    scene cg04d1 #梁芷柔快餐店学习CG-4|看书|青筋暴起|CG04d1
    with dissolve
    voice "audio/voice/001412.ogg"
    l "「喂！？」"
    y "「哈哈哈我错了我错了。」"
    "……"
    "…………"
    scene cg04d #梁芷柔快餐店学习CG-4|看书|CG04d
    with fade
    y "「……」"
    y "「不过说真的，没想到你会看这种书啊。」"
    voice "audio/voice/001413.ogg"
    l "「『这种书』？什么叫『这种书』啊？」"
    y "「啊，就是……我还以为你会看更有深度一些的东西，像你之前看的那个什么来着？总之是一看就很高大上的那种。」"
    y "「反正啊，这种女文青一样的散文，感觉和你重叠不到一块去啊！」"
    scene cg04d1 #梁芷柔快餐店学习CG-4|看书|青筋暴起|CG04d1
    with dissolve
    voice "audio/voice/001414.ogg"
    l "「什么叫女文青……那你什么意思，我是个女汉子吗？」"
    y "「喂喂喂，我可没这么说啊！」"
    voice "audio/voice/001415.ogg"
    l "「不用解释了！解释就是在掩饰！」"
    voice "audio/voice/001416.ogg"
    l "「……哼，看来下半场的题，我得好好地给你筛选一下了。」"
    y "「等等，等等！我的亲姐姐哎！你饶了我吧！」"
    voice "audio/voice/001417.ogg"
    l "「想都别想，你就等死吧！」"
    y "「呜哇……」"
    stop sound fadeout 1.5

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    scene cg04d #梁芷柔快餐店学习CG-4|看书|CG04d
    with fade
    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    "和往常一样，我和梁芷柔在快餐店里开着学习会。"
    "说起来，每天能够和校花泡在一起独处好几个小时，在外人——尤其是我们班上那些男生——看来，或许我应该属于那种遭人羡慕嫉妒恨的家伙？"
    "不过，就是所谓的光看贼吃肉、不见贼挨打了。"
    "能和暗恋的女生近距离接触当然很快乐，然而其中的痛苦也一样不可小觑。"
    "首先是需要拼命去学习。而除此以外，与梁芷柔的接触本身也是一件痛并快乐着的事。"
    "以前和她没有什么交集的时候还好，无论心里怎么想，也只能去单纯地仰望赞叹。"
    "……但现在？"
    "能做的选择似乎倒是多了不少，可仔细想想，一个可行的也没有。"
    "所谓「咫尺天涯」，正是如此。"
    "在五味杂陈的心态中，我迎来了今天这样一个略微特殊的日子。"
    scene bg b07 #快餐店
    with fade
    "……"
    "…………"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001418.ogg"
    l "「喂。」"
    y "「嗯？」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001419.ogg"
    l "「你今天是怎么啦？嗯？」"
    y "「什么怎么了……」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001420.ogg"
    l "「心不在焉啊你，感觉又跟最开始那阵子似的了，不知道满脑子都在想什么呢？」"
    y "「啊？呃，没想什么……」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001421.ogg"
    l "「才怪。你找面镜子自己照照就知道了，就差拿笔直接写在脸上了。」"
    y "「哪有……你也太夸张了吧？」"
    voice "audio/voice/001422.ogg"
    l "「一点都不夸张。」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001423.ogg"
    l "「老实交代，到底是怎么回事？」"
    y "「真的，什么事都没有。」"
    "我一边说谎，一边努力让自己表现出从容的模样。"
    "不过……貌似不大可能蒙混过关……"
    l "「……」"
    y "「……」"
    "在梁芷柔的凝视下，我感到愈发沉不住气。"
    y "「呃……」"
    "好吧。"
    "是的，她说的没错，我确实处在相当烦躁的状态中。"
    "因为今天是……"

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001424.ogg"
    l "「因为今天是七夕，所以想和女朋友去玩，而不是在女汉子这里补习功课？」"
    with vpunch
    y "「噗——」"
    "尽管这种情况已经不是第一次，但我还是忍不住产生了巨大的反应。"
    "梁芷柔对于猜测我的想法乐此不疲，不知道是不是因为每次我这夸张的反应让她觉得很有趣？"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001425.ogg"
    l "「你看，猜中了吧。」"
    y "「咳咳！不对，没有……」"
    "我拼命想要解释……不对，是掩饰。但似乎被梁芷柔毫不犹豫地无视了。"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001426.ogg"
    l "「说起来，都不知道你有没有女朋友呢……」"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/001427.ogg"
    l "「啊，难道真的有？呀，那我把你拖出来这么多天岂不是很糟糕啊？」"
    y "「用膝盖想也知道不可能有了吧？像我这样的人上哪去找女朋友啊？」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001428.ogg"
    l "「那可未必哟？没准有人就喜欢你这个样子的呢？」"
    y "「不可能不可能，这又不是有人喜欢就能有的，喜欢你的人那么多，你不也没有男朋友吗？」"
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve
    voice "audio/voice/001429.ogg"
    l "「才没人喜欢我哪，谁能看得上我这样的女汉子呀！」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    with hpunch
    y "「喂喂喂！」"
    "梁芷柔露出略带狡黠的微笑。"
    "这种程度的玩笑也已经成了常态了。她似乎很喜欢拿这种称呼做文章，每一个都会被用来说上好久。"

    stop music fadeout 2.5

    play sound "audio/sound/ambientnoise06.ogg" fadein 2.5 loop #快餐店环境噪音
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001430.ogg"
    l "「不过，七夕啊……」"
    hide chara
    with dissolve
    "环顾四周，能够轻易发现大批成双成对的情侣。"
    "其中不乏与我们年龄仿佛的年轻身影。"
    y "「……」"
    "是的……这正是我今天烦躁的原因。"
    "今年的七夕来的稍微有些早，居然赶在我们这短暂的暑假期间降临了。"
    "尽管地处偏远，但近年来情人节的概念也终究逐渐流行起来，开始深入人心了。"
    "在学生之间，这种情况更是尤为严重。像我这样有生以来从未谈过恋爱的家伙，每到这种日子，都会如同本能一般，无可抑制地涌出一股莫名的躁动。"
    "然后，就在今年，我的这种躁动，被无限倍地放大了。"
    y "「……」"
    voice "audio/voice/001431.ogg"
    l "「……？」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001432.ogg"
    l "「怎么啦？」"
    y "「没怎么……」"
    voice "audio/voice/001433.ogg"
    l "「那干嘛这么盯着我看……」"
    y "「没看你……」"
    voice "audio/voice/001434.ogg"
    l "「那你在看什么啊？」"
    y "「没看什么……」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001435.ogg"
    l "「……？？？」"
    "梁芷柔被我盯得有些发毛，整个人都忍不住往后缩了缩。"
    y "「……」"
    y "「唉。」"
    hide chara
    with dissolve
    "我他妈在干什么啊？"
    "看得到吃不到的煎熬，让我整个人都有点恍惚了。"
    "虽然明知不可能，但是经过了这么些天的接触，我还是忍不住在这一刻浮想联翩。"
    "不过……"
    "也就仅此而已了。"
    with fade
    with fade
    with hpunch
    "收回视线，喘了口气，眨眨眼，晃晃脑袋。"
    y "「啊，抱歉，突然有点走神。」"
    y "「没事了，咱们继续吧。」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001436.ogg"
    l "「……哈。」"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    l "「……」"
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve
    l "「……」"
    stop sound fadeout 1.5

    "……"
    "…………"

    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    scene cg04c1 #梁芷柔快餐店学习CG-3|做题|饮料|CG04c1
    with fade
    "休息过后，照例的学习时间。"
    "不过，我的心思完全放不到学习上面。"
    l "「……」"
    y "「……」"
    "果然……冷静不下来。"
    "尤其是……在梁芷柔距离我只有一桌之隔的这种情况下，我哪可能做得到心无旁骛？"
    l "「……」"
    "梁芷柔倒是在很专心地写着习题，似乎完全没有受到节日气氛的影响。"
    "说实话，最近这些日子，我没少这样偷偷地看着她……看着这样的她。"
    "她聚精会神的模样，我怎么看也看不够。"
    "然而，今天的我，却无法放平心态去欣赏眼前的光景，反倒是……"
    "总有一种想要破坏掉她这份专注的冲动。"
    y "「……」"
    "为什么会这样呢？"
    "像现在这样，只会让我更加深刻地意识到……盘桓在我们之间的那道巨大的鸿沟。"
    "在这样的日子、这样的气氛里，做一些符合节日氛围的事才对，不是吗？"
    "尽管明知这种想法完全不对，但我还是抱着这样略带卑劣的念头，情不自禁地开口了——"
    y "「喂。」"
    voice "audio/voice/001438.ogg"
    l "「……嗯？」"
    "梁芷柔手中的笔并没有停顿，但是回答的反应……感觉慢了半拍？"
    y "「今天也要做够往常的量么？」"
    voice "audio/voice/001439.ogg"
    l "「……嗯。」"
    y "「太狠了吧，我少做一套好不好？」"
    voice "audio/voice/001440.ogg"
    l "「……嗯。」"
    "「嗯」？"
    "居然答应了？"
    y "「……」"
    "……不对，看这样子，是根本就没听我说什么吧？"
    y "「你在听我说吗？」"
    voice "audio/voice/001441.ogg"
    l "「……嗯。」"
    "还在「嗯」？"
    "果然是没听我说话啊……"
    "虽然佩服她能够如此集中精神，但在这种心态下，遭到无视而生出的不快感被明显放大了。"
    "……也刺激得让我生出一种「一不做二不休」的念头。"
    y "「……」"
    l "「……」"
    "要不要伸手在她眼前挥一挥试试看？"
    "不，那太粗暴了……对了！"
    "机会难得，调戏她一下又会如何呢？"
    y "「待会儿做完题，咱俩一起去玩吧？」"
    voice "audio/voice/001442.ogg"
    l "「…………嗯。」"
    "还真答应了啊……这种操作也可以？"
    "虽然实际上并没有什么用吧，不过那一瞬间的感觉还真是……挺爽的？"
    "应该把刚才这一段录下来给班上那群家伙看看。"
    "……我赌我自己会被打一顿。"
    y "「……」"
    "既然如此，那要是再进一步的话……又会是怎样的场面呢？"
    "在这个念头冒出来的一瞬间，头脑中硕果仅存的少许理智做出了最后的抵抗，想要把这个危险的想法压下去。"
    "然而，在想着「不要」的同时，我的嘴巴却已经不由自主地将之付诸实施了——"
    y "「……做我女朋友好不好？」"
    stop sound fadeout 3.0
    l "「……」"
    y "「……」"
    l "「……」"
    y "「……」"
    play music "audio/music/bgm06.ogg" fadein 1.5 #悬而未决
    "梁芷柔的笔头突然停住了，皱了皱眉。"
    with hpunch
    y "「——！！」"
    "糟、糟糕……玩脱了！"
    l "「……」"
    "短暂……但却无比恐怖的沉默，让我刹那间清醒了过来。"
    "坏了，玩笑开大了。"
    "不，这已经不是一句「玩笑」能解释得过去的事了。这么轻浮的话语，搞不好她可以直接掀桌子的！"
    "心情骤然紧张，叼着吸管吸到一半的饮料都忘了咽下去，只顾屏息静气地看着眼前的女生。"
    l "「……」"
    stop music fadeout 1.5
    "在这个短暂的瞬间过去之后，梁芷柔的眉头舒展开来，手中的笔也继续写了下去。"
    "与此同时的，还有对我刚才那句话的迟来的回应。"
    voice "audio/voice/001443.ogg"
    l "「…………嗯。」"
    with vpunch
    y "「噗！！」"
    "含在嘴里的一大口饮料，混着我的口水，如同一口老血般，呈喷雾状洒满整张桌子。"
    scene cg04c2 #梁芷柔快餐店学习CG-3|做题|饮料|吃惊|CG04c2
    voice "audio/voice/001444.ogg"
    with hpunch
    l "「呀！！」"
    "无论再怎么专心致志，在遭受了如此程度的袭击之后，梁芷柔也终于有了正常的反应。"
    "受到了惊吓的她，慌张……甚至是有些夸张地躲避了一下。"
    with vpunch
    play sound "audio/sound/effect14.ogg" noloop
    "——哗啦。"
    scene cg04c3 #梁芷柔快餐店学习CG-3|做题|饮料倒|CG04c3
    "然后，将放在一边的饮料杯……打翻了。"
    "……"
    "…………"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    scene cg04a #梁芷柔快餐店学习CG-1|就坐|CG04a
    with fade
    "一阵兵荒马乱之后，总算是把桌面收拾干净了。"
    "铺在桌子上的习题集首当其冲，几乎整张卷面都被沾湿了不说，水还渗到了后面几页。"
    "虽然我们本来也不是在上面直接写答案，倒也不至于完全不能用，不过梁芷柔还是想等它完全干燥，于是晾在了一边。"
    "而这还不是最大的问题。"
    "最要命的是她今天带来的那本休息时看的闲书，也被可乐狠狠地泡了一遍。"
    "书页被可乐浸泡以后留下的痕迹……看着应该会很糟心吧。"
    y "「呼……」"
    y "「……唉。」"
    "我真是自己作死啊。"
    scene cg04a1 #梁芷柔快餐店学习CG-1|就坐|微笑|CG04a1
    with dissolve
    voice "audio/voice/001445.ogg"
    l "「呵呵……你刚才到底是怎么了，闹这么大动静。」"
    "貌似，梁芷柔直到被我吓到之前，都在专心致志地做题，对我之前说了什么是一点印象也没有。那个可怕的停顿也只是因为遇到了一个需要思考的难点而已。"
    "结果就是，现在反倒是她更关心我的情况。"
    "真是……万幸之余，也感到十分羞愧。"
    y "「……对不起。」"
    voice "audio/voice/001446.ogg"
    l "「好啦好啦，我又没怨你。」"
    "梁芷柔一边说一边伸了个懒腰。"
    voice "audio/voice/001447.ogg"
    l "「嗯——嗯！」"
    voice "audio/voice/001448.ogg"
    l "「正好我也有点累了，这样歇一会儿也不错。」"
    "她处于暂时无题可做的状况，我则是根本不在状态，索性就再次进入了休息时间。"
    y "「对不起啊，把你的书给弄成这样，回头我赔你一本新的。」"
    voice "audio/voice/001449.ogg"
    l "「哎呀，没事，不用啦，晾干了也一样可以看的嘛。」"
    y "「那哪成啊，肯定得赔。至于这一本就给我呗，也让我拜读一下学霸的课外读物，好陶冶一下情操。」"
    voice "audio/voice/001450.ogg"
    l "「嘻嘻，这么女文青的书，你真读得进去嘛？」"
    "梁芷柔笑吟吟地叼着吸管，有一口没一口地啜着新买的可乐。"
    "与精神集中时的专注神态不同，每当她放松的时候，都会有一些类似的无意识的小动作。"
    "经过了这些天，我已经多少能分辨出一点。于是我紧绷了半天的心也得以稍稍松缓。"
    y "「有什么读不进去的……我的文科可也不差哪，虽然和你比不了。」"
    voice "audio/voice/001451.ogg"
    l "「那又不是说你就能什么书都通吃了。你不是喜欢科幻和推理题材嘛？」"
    y "「随便啦，你就当我有颗纤细的少女心好了。」"
    voice "audio/voice/001452.ogg"
    l "「嗯～？也对，倒不如说更好了，正好和我这个女汉子搭班！嘻嘻。」"
    y "「喂喂。」"
    voice "audio/voice/001453.ogg"
    l "「嗯……说起来啊。」"
    y "「嗯？」"
    voice "audio/voice/001454.ogg"
    l "「真的，都七夕了呢。暑假也过去一半了吧……」"
    y "「哎？」"
    voice "audio/voice/001455.ogg"
    scene cg04a3 #梁芷柔快餐店学习CG-1|就坐|无奈|CG04a3
    with dissolve
    l "「怎么啦，这么惊讶。」"
    y "「我还以为只有我才会感叹这种事呢。对你来说，你有暑假的概念嘛？」"
    voice "audio/voice/001456.ogg"
    l "「怎么没有啊，我也想多放一点假啊！」"
    y "「然后像现在这样，每天开三个小时的学习会？」"
    scene cg04a1 #梁芷柔快餐店学习CG-1|就坐|微笑|CG04a1
    with dissolve
    voice "audio/voice/001457.ogg"
    l "「嘻嘻，这才哪到哪啊，我回家还要再啃一会儿的。」"
    y "「我的妈呀。」"
    voice "audio/voice/001458.ogg"
    l "「呵呵，怎么，又受不了啦？放心啦，现在不会要求你这么做的，你现在这个样子就很不错了。」"
    y "「就算你说也没用，再多了我是真做不到啊……现在这样已经是极限了。」"
    y "「……等等，你说『现在』不要求？」"
    voice "audio/voice/001459.ogg"
    l "「对呀！」"
    y "「那你是打算什么时候……啊？」"
    voice "audio/voice/001460.ogg"
    l "「嗯……如果你能顺利达到『小目标』的话吧。」"
    y "「……我的妈呀。」"
    voice "audio/voice/001461.ogg"
    l "「嘻嘻。」"
    y "「我说……还有整整一年呢吧？有必要现在就这样吗？」"
    scene cg04a3 #梁芷柔快餐店学习CG-1|就坐|无奈|CG04a3
    with dissolve
    voice "audio/voice/001462.ogg"
    l "「哎呀，其实也没那么夸张啦，只是要保持一下自己的状态罢了，又不是在头悬梁锥刺股。」"
    voice "audio/voice/001463.ogg"
    l "「而且，要说时间，在我看来的话……那不是『还』，而是『只』有一年了。」"
    voice "audio/voice/001464.ogg"
    l "「所谓『明日复明日』……就是这个意思了吧！」"
    y "「……唔。」"
    "的确如此。"
    "论起大道理其实谁都明白，但真落到实际上，能做到的却寥寥无几。"
    "知易行难，梁芷柔在这方面比我要坚定得太多了。"
    voice "audio/voice/001465.ogg"
    l "「再说啦，我又不是整天都泡在习题里面。比起在学校的时候，我这已经是够放松的了。」"
    "梁芷柔一边说一边轻轻点了点手边的散文集。"
    y "「喔……」"
    y "「不过，说来说去，也还是在看书啊。你就那么喜欢看书吗？」"
    scene cg04a1 #梁芷柔快餐店学习CG-1|就坐|微笑|CG04a1
    with dissolve
    voice "audio/voice/001466.ogg"
    l "「嘻嘻，喜欢啊。」"
    y "「除了看书以外呢？你还喜欢干什么？」"
    voice "audio/voice/001467.ogg"
    l "「除了看书呀……嗯……」"
    voice "audio/voice/001468.ogg"
    l "「那就是听听轻音乐……」"
    voice "audio/voice/001469.ogg"
    l "「……和逛逛街了吧？」"
    y "「哎哟？」"
    "感觉上似乎平平无奇。这几样爱好……几乎可以称得上是所有女生的标配了。"
    voice "audio/voice/001470.ogg"
    l "「怎么啦，太寻常，和想象中的不一样？」"
    y "「那倒也不是……」"
    voice "audio/voice/001471.ogg"
    l "「在你看来，我该有什么样的兴趣啊？」"
    y "「不知道。虽然是有些意外，不过仔细想想，我其实也没什么概念。」"
    voice "audio/voice/001472.ogg"
    l "「对吧？你没概念，我也没有啊。」"
    voice "audio/voice/001473.ogg"
    l "「……咱们这地方，也没什么稀罕的玩意儿可玩吧。」"
    y "「……」"
    y "「的确。」"
    "一个又落后又封闭的穷乡僻壤，既没有特色又赶不上潮流，生活在其中的我们自然也没什么眼界。"
    "这还是在这些年国家大力建设基础设施，保障了网络通信，而电脑也愈发廉价和普及的情况下……再早几年的时候，我们甚至连上网都还不能保证，更遑论其他。"
    voice "audio/voice/001474.ogg"
    l "「所以说啦～」"
    voice "audio/voice/001475.ogg"
    l "「音乐嘛，我手机耳塞太差，所以一般在家里用电脑听，现在又逛不了街，当然只能看书喽！」"
    y "「说到逛街……你经常来逛嘛？」"
    "在县城里，能称得上可以「逛街」的地方，也只有我们现在所处的这条商业街了。"
    "当然，说是商业街，其实也就是一座百货大楼加上一堆小铺的组合。虽然已经是本地最繁华的地段了，但依旧上不得台面。"
    "其中，相对来说好一点的是百货大楼。前一段时间借着城市改造大潮的东风，百货大楼也把自己的内部重新装修了一番。"
    "重装开业之后，看起来还挺像那么一回事的。"
    voice "audio/voice/001476.ogg"
    l "「嗯……偶尔吧，算不上经常。」"
    scene cg04a3 #梁芷柔快餐店学习CG-1|就坐|无奈|CG04a3
    with dissolve
    voice "audio/voice/001477.ogg"
    l "「毕竟我穷嘛，只能过过眼瘾，不划算啊。」"
    y "「这……」"
    voice "audio/voice/001478.ogg"
    l "「真的呀，你看这一层，哪个我买得起啊？」"
    y "「你故意的吧？这些玩意你倒也得用得着啊？」"
    "快餐店在百货大楼的一层，而这一层主要经营的是品牌化妆品、珠宝首饰及高档服饰。"
    "当然，说是品牌、高档，也就是相对而言。我们这个地方由于经济水平的原因，很难有什么真正的名牌在这里开业。"
    "实际上，就算是这些二、三流品牌，也没能把整个商场一层塞满。"
    "不过，无论如何，学生逛街总是和这一层无缘的。"
    scene cg04a1 #梁芷柔快餐店学习CG-1|就坐|微笑|CG04a1
    with dissolve
    voice "audio/voice/001479.ogg"
    l "「嘻嘻，那你说哪些是我用得到的？」"
    y "「嗯……三楼那个音像店？你不是喜欢音乐吗？我看那里感觉还可以啊。」"
    scene cg04a3 #梁芷柔快餐店学习CG-1|就坐|无奈|CG04a3
    with dissolve
    voice "audio/voice/001480.ogg"
    l "「但我听歌都是从网上下载的呀。那里卖的都是CD，我电脑没光驱哎。」"
    y "「呃……」"
    y "「衣服呢？」"
    scene cg04a1 #梁芷柔快餐店学习CG-1|就坐|微笑|CG04a1
    with dissolve
    voice "audio/voice/001481.ogg"
    l "「淘宝呗。这儿的质量可能还不如淘宝呢，款式就更别说了。」"
    y "「……」"
    voice "audio/voice/001482.ogg"
    l "「所以啦。我一般也就是来逛逛，不买东西的。可是现在哪有那么多时间专门跑过来瞎逛啊……所以最多也就是偶尔来来。」"
    y "「然后还不在这里买书，书都是从我家那边搬过来的，就为了那么一点折扣。」"
    y "「你怎么不索性直接读电子书啊？那不是连书钱都一块省了？」"
    voice "audio/voice/001483.ogg"
    l "「书不一样嘛。书还是得要纸质的读着舒服、有感觉。再说了，有些书也没法用手机看，像那些题，排版全都乱套了。」"
    y "「……好吧，不愧是你。」"
    voice "audio/voice/001484.ogg"
    l "「嘻嘻。」"
    "梁芷柔说得的确有些道理，不过归根结底……应该还是不舍得花钱吧。"
    "……"
    "…………"
    stop music fadeout 1.5

    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with fade
    "在晾干了遭殃的书本之后，我们又继续做了一阵子的题。"
    scene cg04b1 #梁芷柔快餐店学习CG-2|讲题|CG04b1
    with dissolve
    voice "audio/voice/001485.ogg"
    l "「……就是这样，明白了吗？」"
    y "「嗯，明白。」"
    voice "audio/voice/001486.ogg"
    l "「很好！」"
    "之后则是照例的梁老师讲题时间。由于剩下的题本来也不是很多，这两个部分都很快就结束了。"
    "也就是说，今天的学习会，已经到此为止。"
    stop sound fadeout 3.0

    scene bg b06 #商业街
    with fade
    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音
    y "「哎呀，时间还蛮早的嘛，不错。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001487.ogg"
    l "「嗯？怎么啦，你接下来有什么安排吗？」"
    y "「嗯……去书店呗。」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001488.ogg"
    l "「啊？」"
    y "「都说了要赔你的嘛。」"
    y "「既然要赔还是赶早呗，省得耽误你接着看。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001489.ogg"
    l "「啊……我倒是无所谓啦，真的，不用那么急的。」"
    voice "audio/voice/001490.ogg"
    l "「而且你现在过去，那边也未必有现货吧，我上次也是提前预定了才拿到的。」"
    y "「嗯，是啊，所以嘛。」"
    "我指了指旁边的商场。"
    y "「就不舍近求远了，直接在这里买呗。」"
    y "「新华书店的话，应该还是会有的吧！」"
    "毕竟是县城内最大的书店，一些火热的畅销书还是会及时更新上架的。"
    "由于家大业大，不虞积压，想必不会像小书店那样特别精打细算。"
    voice "audio/voice/001491.ogg"
    l "「啊，也是呢，这儿的话说不定还有存货。」"
    y "「是吧。」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001492.ogg"
    l "「的确，上次在这儿看到过，虽然不知道现在有没有卖光吧……不过这里可不打折啊。」"
    y "「没关系，反正又不是天天过来买，仅此一次，也不差那几块钱。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001493.ogg"
    l "「嗯……那倒也是。」"
    "梁芷柔点点头，认同了我的说法。"
    y "「那，你待会儿怎么着？有急事吗？」"
    voice "audio/voice/001494.ogg"
    l "「哎？我啊……我没什么事，回家接着看书吧？」"
    y "「要是……不那么急的话，要不跟我一起上去？要是有货的话就直接给你拿回去了，也省得我拿着来来回回的。」"
    "我稍微犹豫了一下，还是发出了邀请。"
    "仅仅是逛个书店而已，而且目标非常明确，是为了弥补自己过错做出的赔偿，与约会之类的字眼毫不沾边。"
    "应该……不会不可以吧？"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001495.ogg"
    l "「嗯……」"
    l "「……」"
    y "「——！」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001496.ogg"
    l "「……嗯，好呀。」"
    y "「呼……！」"
    hide chara
    with dissolve
    "梁芷柔考虑的时间其实并不长，但是对我来说，却颇有一种度秒如年的感觉。"
    "我也不知道自己在想什么。"
    "即便可以借此在她的身边多呆上那么一小会儿的时间，也并没有什么卵用。"
    "明明对此心知肚明，但却还是忍不住这样做了。"
    "或许，这是每一只待在天鹅身边的癞蛤蟆……的通病？"
    stop sound fadeout 3.0

    "……"
    "…………"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    scene bg b10 #百货商场
    with fade
    y "「……」"
    y "「…………呼。」"
    "当我们并肩迈入书店的那一刻，我居然有种阿姆斯特朗登月时的感受。"
    "从商场门口走到书店，在距离上并没多远，对我来说却是迈出了了不得的一步。"
    "真是紧张得我连冷汗都冒出来了。"
    scene bg black #黑屏
    with fade
    "……"
    "…………"
    scene bg b10 #百货商场
    with fade
    y "「来，给你。」"
    "和预想的一样，我们非常顺利地在这里找到了那本书。"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001497.ogg"
    l "「谢谢～」"
    y "「不用谢啊，是我把你的书给弄坏了，应该是我说对不起才是。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001498.ogg"
    l "「没有啦，真的。其实那也不算弄坏吧，我看书看得比较狠，本来也经常把书弄脏的。」"
    y "「别客气了，再说了，干嘛这么凑合啊？」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001499.ogg"
    l "「呵呵，还好吧。而且不凑合也没办法啊，能省一点是一点对不对。」"
    y "「……」"
    hide chara
    with dissolve
    "这勤俭节约的好习惯还真是被她习惯成自然了啊……"
    "仔细想想，这几天下来，类似的事我也不是第一次见了。"
    "节约每一个铜板，连喜欢的书都不敢随便买。"
    "穿的也都是些再普通不过的大路货，甚至连平时用的文具都是挑的比较廉价的。"
    "不知怎的，觉得有点心疼。"
    "也因此，忽然想到了一件事。"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001500.ogg"
    l "「嗯？怎么了？又发呆。」"
    y "「我在想啊。」"
    voice "audio/voice/001501.ogg"
    l "「嗯？」"
    y "「之前的就不提了，接下来这几天，你再买书的话，我出一半的钱吧。」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001502.ogg"
    l "「哎——！？」"
    voice "audio/voice/001503.ogg"
    l "「不是，等等，你说什么？你要干什么？」"
    y "「我说啊，你再买书的时候，我出其中一半的钱。」"
    voice "audio/voice/001504.ogg"
    l "「那是干嘛啊？不用的，我……」"
    y "「这理所当然的啊？我这几天一直都是在用你买的书做题，出一点买书钱太正常了吧？」"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/001505.ogg"
    l "「这……」"
    y "「之前是我忽略了，其实我早就该想到的。」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001506.ogg"
    l "「不，这个……真的不用的，反正我自己也得买，多一个人用还减少浪费呢，哪能找你要钱啊？」"
    y "「是我自己给你钱，不是你要的好不好？」"
    show chara c02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/001507.ogg"
    l "「那也一样！」"
    y "「那这样行不行，你用完的这些习题，半价卖给我好不好？我拿回去还可以重温一下，加深印象。」"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/001508.ogg"
    l "「这不还是一个意思吗？你干嘛啊，真不用的！别这样。」"
    y "「不不不，你误会了。我这一方面是为了我自己用，毕竟那些题留在你那儿利用率太低，给我复习用就正好；另一方面啊……」"
    y "「也可以给我爸妈看看。」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001509.ogg"
    l "「啊？」"
    y "「这些都是我在好好学习的证据啊，我爸妈肯定特支持，说不定除了书钱，我的零花钱也会增加的。姐姐你一定要帮我这个忙啊！」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001510.ogg"
    l "「这……」"
    "大概是从未见过有如此厚颜无耻之人，梁芷柔居然被我说愣了。"
    "不过，虽然是慷父母之慨，但我说的又不是没有道理……不如说，我直到现在才想到这个问题，已经是很没心没肺了。"
    y "「好不好？」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    l "「……」"
    "梁芷柔有些纠结，似乎觉得这样不太好，但又不知道该怎么拒绝。"
    y "「你就让我掏点书钱吧，学费我都赖掉了，书钱再不给，我于心不安啊！」"
    "我是真的想要掏这笔钱的，一边满嘴跑火车，一边很真诚地看着她。"
    l "「……」"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/001511.ogg"
    l "「……谢谢。」"
    "再三犹豫之后，梁芷柔还是接受了，细若蚊声地道了声谢。"
    hide chara
    with dissolve
    "……"
    "…………"
    with fade
    "新华书店位于商场的三层，由于是老式商场没有直梯，我们需要绕上半圈走扶梯下去。"
    "沿途乱七八糟的小玩意还是挺多的，尤其是七夕这样的日子，说是传统节日，其实更像是商家的大抢节，各种促销宣传晃瞎人眼。"
    "有的时候，梁芷柔的注意力也会被吸引过去，一边放慢脚步，一边扭头去看。"
    y "「要过去看看吗？」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001512.ogg"
    l "「啊？啊……不用！走吧！」"
    "但如果我停下等她，她又会慌慌张张地加快脚步离开。"
    hide chara
    with dissolve
    "短暂的下楼过程中，如此的情况已经反复了两次，果然……其实她还是挺想去逛街的吧？"
    "之前那几天还好说，但在今天这样比较特殊的环境下，内心深处的逛街欲应该很容易被点燃。只是梁芷柔有着相当高强的自制能力，还能管得住自己。"
    "不过，也已经有点岌岌可危的样子了。"
    with fade
    "下到一楼的时候，楼梯口正对着一个卖金银饰品的柜台。"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    l "「……」"
    y "「……这啥咧？」"
    "柜台的前面，立着一面大幅的海报，上面以霹雳字体外加爆炸特效填满了「开业酬宾」、「跳楼甩卖」、「吐血打折」、「抽奖必中」之类夸张的字眼。"
    y "「……话说这里是一楼吧，你在这里跳楼真是一点威慑力都没有啊。」"
    "总而言之，就是这么个只要看一眼就会让人很想要吐槽的海报。"
    "实际上，这个广告的效果也非常存疑。"
    y "「这就是所谓的门可罗雀了吧……」"
    show chara c02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/001513.ogg"
    l "「真的……这是做什么活动哪？」"
    y "「不是说了吗，开业跳楼什么的……」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001514.ogg"
    l "「噗，什么叫开业跳楼啊！」"
    y "「就是啊，你看，又是吐血又是骨折的。」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001515.ogg"
    l "「呸，那是打折，就知道胡扯。」"
    "梁芷柔笑啐了一口，迈开了步子。"
    hide chara
    with dissolve
    "不过她并没有走过柜台，而是……趴在柜台上看了起来。"

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    scene cg05a #梁芷柔看首饰CG-1|观看|CG05a
    with fade
    y "「……」"
    voice "audio/voice/001516.ogg"
    l "「哎～～不错嘛。」"
    y "「……」"
    "终于放弃理智了吗？"
    "都说女人是龙，看到亮晶晶的东西就走不动了，果然诚不我欺，哪怕是梁芷柔也未能幸免。"
    voice "audio/voice/001517.ogg"
    l "「嗯……」"
    "看来是了……她貌似完全没有注意到自己在做什么……"
    "不过，能够在商家们多维度的洗脑下坚持这么久也算是了不起了吧。"
    y "「……」"
    scene cg05a1 #梁芷柔看首饰CG-1|观看|星星眼|CG05a1
    with dissolve
    "话说回来，这样的梁芷柔倒是第一次见到，也算是大饱眼福了。"
    voice "audio/voice/001518.ogg"
    l "「嗯嗯……」"
    y "「哇……」"
    "感觉口水都快留下来了。"
    y "「……有那么想要吗？」"
    "我也凑了上去。"
    l "「……」"
    scene cg05a2 #梁芷柔看首饰CG-1|观看|放大|CG05a2
    with dissolve
    "顺着梁芷柔的视线看去，是一个小挂坠。"
    "羽毛状，看起来有些抽象化，表面经过打磨，亮闪闪的，也不知是什么材质。"
    "看了看价签……"
    y "「……好便宜？」"
    "价格低得出乎意料……不，其实也正常。毕竟摆出这种菜市场般阵仗的地方，又能有什么高端商品。"
    scene cg05a1 #梁芷柔看首饰CG-1|观看|星星眼|CG05a1
    with dissolve
    voice "audio/voice/001519.ogg"
    l "「嗯～～～」"
    "抬头再看看梁芷柔，这位似乎正在以极大的毅力来抵抗诱惑。"
    y "「……」"
    y "「咳。」"
    scene cg05b1 #梁芷柔看首饰CG-2|对视|惊讶|CG05b1
    with hpunch
    voice "audio/voice/001520.ogg"
    l "「……啊？」"
    y "「怎么样，喜欢哪个？」"
    scene cg05b2 #梁芷柔看首饰CG-2|对视|尴尬|CG05b2
    with dissolve
    voice "audio/voice/001521.ogg"
    l "「啊……哈哈。」"
    voice "audio/voice/001522.ogg"
    l "「抱歉啊，下意识就……」"
    y "「是这个吧？」"
    voice "audio/voice/001523.ogg"
    l "「哎？」"
    y "「您好，帮我拿一下这个我看看！」"
    scene cg05b1 #梁芷柔看首饰CG-2|对视|惊讶|CG05b1
    with vpunch
    voice "audio/voice/001524.ogg"
    l "「不不不，不用不用不用！」"
    y "「……对对，就是这个。」"
    voice "audio/voice/001525.ogg"
    l "「你等等啊，我都说了不用啦……」"
    y "「啊？你说啥呢，人太多了我听不清楚，待会儿说。」"
    voice "audio/voice/001526.ogg"
    l "「喂！」"
    "……"
    "…………"

    with fade
    y "「来，试一下？」"
    scene cg05b2 #梁芷柔看首饰CG-2|对视|尴尬|CG05b2
    with dissolve
    voice "audio/voice/001527.ogg"
    l "「你啊……」"
    y "「怎么啦？不喜欢？」"
    scene cg05b #梁芷柔看首饰CG-2|对视|CG05b
    with dissolve
    "梁芷柔轻轻摇摇头。"
    voice "audio/voice/001528.ogg"
    l "「我就是看看，又不买。」"
    y "「没让你买啊，戴一戴试试总成吧？」"
    voice "audio/voice/001529.ogg"
    l "「哎……」"
    scene bg black #黑屏
    with fade
    "……"
    "…………"
    scene cg05c #梁芷柔看首饰CG-3|试戴|CG05c
    with fade
    "虽然一脸被我气得哭笑不得的样子，不过梁芷柔还是接过了挂坠，随即戴上，开始对着台面上的镜子看来看去。"
    "站在她的侧面，还能够看到她的嘴角有意无意地挂着一丝笑意。"
    y "「……」"
    "有句话说得好——"
    "嘴上嚷嚷着不要，但身体还是很诚实的嘛。"
    y "「啧啧，挺不错的嘛。」"
    "挂坠虽然简单，倒也大方，搭配起来的效果意外地好。"
    "当然，也可能是人漂亮了戴什么都好看吧……"
    y "「就是它了。服务员，开票吧。」"
    scene cg05c0 #梁芷柔看首饰CG-3|试戴|惊讶|CG05c0
    with vpunch
    voice "audio/voice/001530.ogg"
    l "「哎！？哎！！！？」"
    scene cg05c1 #梁芷柔看首饰CG-3|试戴|惊讶|对视|CG05c1
    with dissolve
    voice "audio/voice/001531.ogg"
    l "「等等，你给我等等啊！」"
    voice "audio/voice/001532.ogg"
    l "「都说了我不买了啊！」"
    y "「所以说了没让你买啊……你别瞎操心了，这是我给我亲戚买的。」"
    voice "audio/voice/001533.ogg"
    l "「哎？亲戚？」"
    y "「对啊……」"
    "趁着梁芷柔愣神的机会，我抓起小票，如脱兔一般飞奔而去。"
    y "「……给我姐！」"
    voice "audio/voice/001534.ogg"
    l "「喂！」"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    scene bg b10 #百货商场
    with fade
    "等到梁芷柔还回挂坠、再跑出来找我的时候，我已经拿着结完账的小票回来了。"
    y "「你就接受我的好意吧，又不是多贵重的东西。」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001535.ogg"
    l "「可是！」"
    y "「别可是啦，还是说，太便宜了你瞧不上？」"
    show chara c03 #梁芷柔立绘|夏季私服|生气
    with dissolve
    voice "audio/voice/001536.ogg"
    l "「我又不是这个意思！你这人怎么老这样……」"
    y "「我这人怎么样啦？我送我姐姐一个百八十块钱的小玩意有什么问题吗？」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001537.ogg"
    l "「你刚才不是已经送我书了吗？」"
    y "「书不算，那是我赔给你的，这是我送给你的。」"
    show chara c02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/001538.ogg"
    l "「我……这……你……」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001539.ogg"
    l "「唉！！多不合适啊。」"
    y "「有什么不合适的啊？」"
    show chara c08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/001540.ogg"
    l "「本来就是……让你以后帮我出书钱都已经挺不好意思的了……」"
    y "「一码归一码。书钱是算在学习资料里的，这个可是我掏我自己的零花钱买的，不一样。」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001541.ogg"
    l "「所以说为什么啊？干嘛非要送我东西呢……」"
    y "「我嘛，就是赶上了，想要向给我很多帮助的姐姐表达一点心意，结果被弃之如敝屣了。」"
    y "「所以我还想问你呢，干嘛这么排斥我送你东西。」"
    show chara c03 #梁芷柔立绘|夏季私服|生气
    with dissolve
    voice "audio/voice/001542.ogg"
    l "「我哪有！」"
    y "「那就踏踏实实收下呗？哎呀你就别推辞了好不好，你就让我送你点东西聊表谢意呗？」"
    voice "audio/voice/001543.ogg"
    l "「你这……哎！真是的。」"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/001544.ogg"
    l "「其实……真不用的。教你学习本来就是因为我要感谢你，怎么到了最后又变成你要谢谢我了？」"
    y "「刚才我就说了啊，一码归一码。」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/001545.ogg"
    l "「……唉。」"
    "梁芷柔微微无奈地耸了耸肩。"
    voice "audio/voice/001546.ogg"
    l "「好吧好吧，真拿你没办法。」"
    show chara c08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/001547.ogg"
    l "「只此一次，下不为例。再这么干我可要翻脸啦？」"
    y "「噢。」"
    scene bg black #黑屏
    with fade
    "……"
    "…………"
    scene bg b10 #百货商场
    with fade
    "把小票交给售货员，取回了东西。"
    y "「来，给你。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001548.ogg"
    l "「谢谢，我会珍惜它的！」"
    y "「不客气。」"
    "虽然一开始有点担心强送礼物会不会反而惹得她不快……不过现在看起来倒也没那么严重，她应该还是蛮开心的。"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001549.ogg"
    l "「～」"
    "她应该是真的挺喜欢这个挂坠的吧……而且，毕竟只是个小玩意，无伤大雅。"
    y "「接下来……走走走，去抽奖，看看手气怎么样。」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001550.ogg"
    l "「啊？还真有抽奖啊？」"
    y "「是啊，你看。」"
    "我扬了扬手中的小票，指向了商场的另一个角落。"
    "相比起柜台这边的凄凉，那一侧的人数要多得多，排了个长长的队伍。"
    y "「刚才我都问过了，是整个商场都在搞活动，凡是达到一定金额的都可以去抽。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001551.ogg"
    l "「哎～都有什么奖品啊？」"
    y "「那就得过去看了。走呗？」"
    voice "audio/voice/001552.ogg"
    l "「好！」"

    scene bg b10 #百货商场
    with fade
    y "「我看看我看看……」"
    "我们来到了队伍的尾部。虽然隔着一段距离，不过大致上还算能够看清奖品清单。"
    y "「特等奖，苹\[哔——\]笔记本电脑一台。」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001553.ogg"
    l "「喔喔，不错呢！」"
    y "「……」"
    y "「为什么感觉有点不靠谱了呢。」"
    show chara lc13b #梁芷柔立绘|夏季私服|疑惑2|近
    with dissolve
    voice "audio/voice/001554.ogg"
    l "「啊？为什么呀？」"
    y "「你看那些中奖类的诈骗，骗子给出的奖品里面总是会有个苹\[哔——\]的笔记本。」"
    y "「无论奖金多少钱，总要强迫症似的给你搭一个苹\[哔——\]的笔记本……想不要都不行。」"
    y "「所以我现在一看到苹\[哔——\]笔记本，就会产生深深的怀疑。」"
    "而且这个抽奖的门槛本来也就很低……我不禁开始担心起这个活动的可靠性来了。"
    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/001555.ogg"
    l "「啊哈哈……我觉得不至于吧，好歹也是正规的商场啊……」"
    y "「嗯……也是。」"
    y "「继续看继续看，一等奖是……32寸液晶电视？」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001556.ogg"
    l "「这个也不错啊。」"
    y "「嗯嗯，这倒是常见的奖品。」"
    "这个就比较正常了。"
    "不过，感觉和特等奖的价值差距有点大啊。"
    "……这样看起来，那台笔记本或许是用来当做噱头的吧，实际上能不能真的被抽到都要另说吧？"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001557.ogg"
    l "「二等奖是……金项链？」"
    y "「比32寸电视还要便宜的金项链，想必……」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001558.ogg"
    l "「嗯……」"
    y "「果然还是不靠谱啊。」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001559.ogg"
    l "「呵呵……好歹是白送的，如果真能抽得到的话。」"
    y "「是是。三等奖嘛……」"
    hide chara
    with dissolve
    "……"
    "…………"
    with fade
    "这个抽奖的中奖几率是百分之百的必中，而奖品则被分成了好几十个等级，看起来更像是找个借口把长期滞销的商品清理出去的样子。"
    "虽然等候的队伍不算短，不过因为只是抽奖，兑奖还要再到旁边，队伍前进的速度倒是还算快。商量了一下以后，我们决定试一下自己的手气。"
    "在排队期间，我们俩一直在对奖品进行吐槽，借此来消磨时间。不过到了后来基本上就是在讨论如果中了最末等的钥匙链，或者倒数第二等的塑料杯该怎么用。"
    with fade
    y "「哎呀，终于到咱们了。」"
    y "「来来来，姐姐您来？」"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/001560.ogg"
    l "「哎？我吗？」"
    y "「对呀，礼物可是送给你的，赠品当然也由你来决定喽！」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001561.ogg"
    l "「可是这礼物是你送我的呀，不是应该由你决定的吗？」"
    y "「不不不，还是女士优先吧！」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001562.ogg"
    l "「哼哼，真是没有男子气概！」"
    "梁芷柔一边和我拌着毫无意义的嘴，一边轻笑着把手伸进了抽奖箱。"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001563.ogg"
    l "「嗯……就是它啦。」"
    y "「是什么？」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001564.ogg"
    l "「我看看啊，估计是钥匙链吧……」"
    y "「别这么妄自菲薄，我相信您一定可以抽中塑料杯的！」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001565.ogg"
    l "「嘁！」"
    "我们俩凑在一起，拿着手中的奖券和中奖图例进行对比。"
    "真麻烦啊……居然不直接写几等奖，而是画了一大堆图案符号，通过不同的组合来确定中奖等级。"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001566.ogg"
    l "「钥匙链……不是哎。」"
    y "「你看我就说吧……咦？」"
    hide chara
    with dissolve
    "我拿去跟塑料杯的组合对比，发现也不一样。"
    "比塑料杯高一个等级的毛巾……不是。"
    "更高一级的牙刷……不是！"
    "绝大多数的奖券应该都是最低级的几个奖品，结果我们居然不是？"
    y "「难道真中大奖了？」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001567.ogg"
    l "「好像……也不是啊？」"
    "抬头看了看苹\[哔——\]笔记本的兑奖符号，果然不是。"
    y "「那是哪个啊？」"
    "望着这有如天梯一般冗长的图例表，我有种崩溃的感觉。"
    y "「……这什么奇葩抽奖。」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001568.ogg"
    l "「呵呵，至少可以拿到不错的奖品呢。」"
    "是啊，要不是这样我就该直接撕票了。"
    y "「分一下工吧……一人一半，我从上面看，你从下面看。」"
    voice "audio/voice/001569.ogg"
    l "「嗯。」"
    hide chara
    with dissolve
    y "「……」"
    l "「……」"
    y "「…………」"
    l "「…………」"
    with fade
    "经历了N次看花眼、看串行之后，我依然没能找到我们中奖的图案。"
    "不过也差不多该到此为止了，我已经看到很靠中间的位置，想来梁芷柔那边也差不多了吧。那么……"
    y "「嗯？」"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/001570.ogg"
    l "「啊……」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001571.ogg"
    yl "「是这个！」"
    "几乎是同时，我们俩异口同声地喊了出来。"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001572.ogg"
    l "「呵呵……真够难找的！」"
    y "「来来来，看看奖品……」"
    voice "audio/voice/001573.ogg"
    l "「嗯……嗯？」"
    y "「这是……」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001574.ogg"
    l "「当日指定场次的电影票？」"
    y "「……两张？」"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    l "「……」"
    y "「……」"
    "我俩面面相觑，相顾无言。"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……"
    "…………"


    play sound "audio/sound/ambientnoise08.ogg" fadein 1.5 loop #商场环境噪音
    scene bg b10 #百货商场
    with fade
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    y "「……」"
    l "「……」"
    voice "audio/voice/001575.ogg"
    l "「嗯……怎么办好呢？」"
    y "「是啊，怎么办呢？」"
    "从兑奖处取了电影票出来，我和梁芷柔看着手中的电影票发起愁来。"
    "由于是指定场次，我们没有选择电影的余地，偏偏上映时间也已经挨得非常近了。"
    "而且这次给我们的电影票是……"
    y "「是『虹色旋律』啊。」"
    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/001576.ogg"
    l "「嗯……」"
    "最近很有名、在网上形成话题的恋爱电影。短时间内即风靡全国，即便是我们这样的偏远地区，也已经是大名鼎鼎了。"
    y "「导演是那个小新吧……好像说他最近要去日本发展了？」"
    voice "audio/voice/001577.ogg"
    l "「对呀……」"
    y "「这也算是一炮走红了吧？」"
    voice "audio/voice/001578.ogg"
    l "「嗯。」"
    y "「……」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001579.ogg"
    l "「所以……怎么办好呢？」"
    y "「是啊，怎么办呢？」"
    "大眼瞪小眼。"
    y "「你约个谁过来，你们俩一起看呗？」"
    voice "audio/voice/001580.ogg"
    l "「我啊……约谁……我也不知道该约谁啊。」"
    y "「唉？班上的那几个女生呢？」"
    voice "audio/voice/001581.ogg"
    l "「她们好多都已经看过了啊。而且这个时间了，也未必叫得过来吧？」"
    y "「哦……说的也是。」"
    "说起来大家其实都还在放假呢，热门电影一上映，喜欢看的早就已经去看过了，剩下的估计也不见得有兴趣。"
    "何况时间这么紧张……哪怕我们这个县城很小，也不见得都能赶得过来。"
    show chara lc05b #梁芷柔立绘|夏季私服|苦笑2|近
    with dissolve
    voice "audio/voice/001582.ogg"
    l "「你呢？你有谁可以约吗？女朋友什么的？」"
    y "「我哪找女朋友去啊！！哎我说你还记着这事哪？」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001583.ogg"
    l "「呵呵……嗯，那怎么办呀？」"
    y "「你一个人去看呢？」"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    voice "audio/voice/001584.ogg"
    l "「一个人进电影院啊……感觉怪不好意思的。」"
    "……的确，七夕的黄金时段，一位美少女独自一人钻进电影院里看恋爱电影，感觉随便都能脑补出一大堆凄惨的故事来。"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001585.ogg"
    l "「要不你自己试试看？」"
    y "「……姐姐你还是饶了我吧！」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001586.ogg"
    l "「怎么啦，你也害羞？」"
    y "「那倒不是，不过恋爱电影嘛……」"
    "虽然我倒不太介意独自看电影，不过那得是自己喜欢的题材，而恋爱电影显然不在其中。"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001587.ogg"
    l "「这样啊……那怎么办呀……」"
    voice "audio/voice/001588.ogg"
    l "「嗯……」"
    "梁芷柔皱着眉，挠了挠头。"
    y "「那要不然就这么算了？反正也是白来的票。」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001589.ogg"
    l "「……嗯……可是，多可惜啊，我早就想看这个电影了呢！」"
    y "「啊。」"
    "找不到别的伴，自己一个人看不了，又不想放弃，那剩下的选项看来就只有……"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    l "「……」"
    "梁芷柔把视线投向了我。"
    y "「呃……」"
    "我稍稍有些忐忑。虽然看起来结果只有一个了，但梁芷柔真的愿意吗？"
    "要说起来我其实还真没抱多少希望，毕竟刚才的逛街可以说是顺便，但一起去看恋爱电影……那就是另一码事了。"
    "梁芷柔似乎还是比较犹豫，微微皱着眉头。"
    voice "audio/voice/001590.ogg"
    l "「嗯……你又不爱看恋爱电影……」"
    "……咦。"
    "原来她纠结的重点其实是这里吗？"
    y "「不不不，没关系，我虽然谈不上多喜欢，但也不讨厌的。没问题！」"
    "电影题材什么的根本不是重点啊！"
    "有生以来第一次和女生一起看电影，而且对象还是她的话……哪怕是「小\[哔——\]代」我也能给你看下去啊好不好？"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/001591.ogg"
    l "「喔……」"
    show chara lc12a #梁芷柔立绘|夏季私服|羞涩1|近
    with dissolve
    voice "audio/voice/001592.ogg"
    l "「那个，我真的是挺想看这个电影的……」"
    voice "audio/voice/001593.ogg"
    l "「要不，你、你……陪我一下？」"
    y "「哦，我没问题的。」"
    "居然还真可以？"
    "……她到底有多想看这个电影啊。"
    "不过，换句话说，她也确实是冲着电影去的，我最好不要多想。"
    y "「说起来……」"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/001594.ogg"
    l "「哎？」"
    y "「啊，不，没什么事。」"
    "忽然，我想起一件事来，不过话到嘴边又咽了回去。"
    hide chara
    with dissolve
    "我记得……她之前说过，接下来原本是打算回去看书的吧？"
    "现在这样子，大概是已经忘掉这个茬了……我犹豫了一下，还是决定不去提醒她。"
    "一方面是抱着利己主义的想法，想跟她多待一会儿。"
    "另一方面，也是觉得她……是不是压抑自己太久了呢？"
    "明明自己其实很想去逛街，明明有着非常想要看的电影，却一直如同苦行僧一样约束着自己，把精力投入到学习之中去。"
    "到底是因为什么，才会让她有了这么巨大的动力，去贯彻这种行为呢？"
    "我不知道——虽然我很想要知道。"
    "不过，现在，在这个机缘巧合的现在……我更希望，她可以开开心心地放松片刻。"
    "这一次，我可不再是像之前那样抱着拖她后腿的卑鄙念头了，而是真真正正地这么想。"
    "希望……这样的休息，可以对她有好处。"

    scene bg black #黑屏
    with fade
    "……"
    "…………"
    scene bg b10 #百货商场
    with fade
    y "「可乐和爆米花买好喽！」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001595.ogg"
    l "「辛苦啦！」"
    y "「你刚刚看什么呢？」"
    voice "audio/voice/001596.ogg"
    l "「那个哟。」"
    "我顺着梁芷柔指点的方向看去。"
    y "「喔喔，海报啊。」"
    voice "audio/voice/001597.ogg"
    l "「嗯，好漂亮。」"
    y "「不知道实际拍得怎么样啊。」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/001598.ogg"
    l "「呵呵，看了就知道啦，反正我很期待。」"
    y "「好好好。」"
    y "「啊，检票了，咱们进去？」"
    voice "audio/voice/001599.ogg"
    l "「嗯！」"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……"
    "…………"
    voice "audio/voice/001600.ogg"
    l "「啊……」"
    y "「这是……」"
    "当我们按照电影票找到座位时，忍不住都愣住了。"
    with vpunch
    y "「啥啊这是！」"

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    scene cg06a #梁芷柔看电影CG-1|空位|CG06a
    with fade
    "居然……是个双人卡座。"
    "有生以来第一次和女生一起看电影，结果直接上这么高难度的真没问题吗！？"
    "这么说起来，在我们去换电影票的时候，服务员看到我们时那种暧昧的表情就很可疑。"
    "当时虽然注意到了，但是以为只是被误会了关系，倒也没多想……"
    with hpunch
    "原来是这么一回事吗！？"
    l "「……」"
    y "「……」"
    "……怎么办？"
    "这种刚出新手村就要和最终BOSS决战一般的剧本是怎么回事啊？难度太高了吧？虽然这年头满级吊打新手村的类型也是蛮流行的，但我可是如假包换的新手啊！！！"
    "在这一刻，我的大脑里浮现出来的全是这样乱糟糟的念头。"
    "但确实如此——今天一天之间，我和梁芷柔从一起学习到一起逛商场再到一起看电影，最后变成了坐同一个情侣卡座？步子迈得太大，会扯到蛋啊喂！"
    y "「这个……」"
    y "「要不然，还是……」"
    voice "audio/voice/001601.ogg"
    l "「啊，那个……」"
    y "「嗯？」"
    voice "audio/voice/001602.ogg"
    l "「赶快……坐吧。」"
    y "「……哎？」"
    voice "audio/voice/001603.ogg"
    l "「会……影响到别人的。」"
    "的确，我们俩卡在半道上，既阻碍了同一排的其他人入座，也挡住了后排人的视线。"
    with hpunch
    "不过——重点是这个吗！？"
    "这样真的没问题吗？这种设定你也能接受？你真那么想看这个电影啊？"
    scene cg06b #梁芷柔看电影CG-2|入座|CG06b
    with dissolve
    "我俩僵硬地坐下。"
    "我紧紧地贴着自己这一侧座位的边缘，不敢乱动一下；再看梁芷柔，情况似乎也差不多，有意无意地挪到了尽量远的那边。"
    "这为了看一场电影也是蛮拼的了……"
    y "「……」"
    l "「……」"
    "尴尬的沉默。"
    "虽然想要找个话题聊两句，缓解一下气氛，但是脑子里一团浆糊，也不知该说些什么才好。"
    y "「……」"
    y "「啊，对了。」"
    scene cg06b1 #梁芷柔看电影CG-2|爆米花|CG06b1
    with dissolve
    "我把爆米花递给梁芷柔。"
    y "「给。」"
    voice "audio/voice/001604.ogg"
    l "「噢……谢谢。」"
    l "「……」"
    y "「……」"
    scene cg06b #梁芷柔看电影CG-2|入座|CG06b
    with dissolve
    l "「…………」"
    y "「…………」"
    "然后就又沉默了。"
    with vpunch
    y "「（啊啊啊啊……这什么鬼！）」"
    voice "audio/voice/001605.ogg"
    l "「那个……」"
    stop music fadeout 2.5
    y "「哎？」"
    voice "audio/voice/001606.ogg"
    l "「说起来，你看过『虹色旋律』的原作吗？」"
    y "「咦？还有原作啊，我都不知道呢。」"
    voice "audio/voice/001607.ogg"
    l "「对喔，原作也很棒呢，除了改编成电影以外，还有游戏和漫画，嗯，据说都非常不错。」"
    "梁芷柔的声音也有些不自然，似乎也是在努力地寻找话题。"
    "不过，她比我要高到不知哪里去了……最起码，现在我很容易就能接得上话。"
    y "「噢，给我科普一下呗？」"
    voice "audio/voice/001608.ogg"
    l "「嘻嘻，好呀，不过你不怕被剧透吗？」"
    y "「你应该没那么不仗义吧？」"
    voice "audio/voice/001609.ogg"
    l "「那可说不定喔？」"
    y "「那我就只有自求多福了。姐姐您嘴下留情啊！」"
    voice "audio/voice/001610.ogg"
    l "「嘿嘿，我跟你说啊，这个故事呢，说的是男主角在高中的时候回到阔别多年的老家宜清……」"
    "梁芷柔的介绍让我得以对这个电影的背景有了一个大致的了解。"
    "当然，拜此所赐，刚才的尴尬气氛也有所缓解。"
    "……"
    "…………"
    play sound "audio/sound/effect18.ogg" noloop
    scene cg06b2 #梁芷柔看电影CG-2|关灯|CG06b2
    with fade
    y "「啊。」"
    "关灯了。"
    scene cg06b3 #梁芷柔看电影CG-2|开幕|CG06b3
    with dissolve
    "荧幕也亮了起来，开始播放广告。"
    voice "audio/voice/001611.ogg"
    l "「哎呀，终于要开始了。」"
    y "「嗯。」"
    "最难熬的阶段已经过去了。"
    "……"
    "…………"
    play sound "audio/sound/effect15.ogg" noloop

    with fade
    "电影开幕了。"
    "故事有些慢热，各种铺垫徐徐展开，虽然并没有一上来就给人以冲击感，但节奏掌握得很好，也很容易吸引人继续看下去。"
    play sound "audio/sound/effect16.ogg" fadein 1.5 noloop
    l "「……」"
    "梁芷柔看得很专心，表情也随着剧情的进展不断变化。"
    scene cg06b4 #梁芷柔看电影CG-2|放松|CG06b4
    with dissolve
    "刚开始紧绷的身体也渐渐放松下来了。"
    y "「（已经看投入了吗？）」"
    "虽然我这边还多少有一些心猿意马……"
    "不过好歹比之前要强得多了。"
    y "「（别想那么多了，放松、放松……）」"
    "总之……尽可能让自己把注意力集中到电影上面吧。"
    with fade
    "……"
    "…………"
    play sound "audio/sound/effect17.ogg" noloop
    "过了一会儿，电影里出现了一个海啸的场景，女主角要被海水卷走了。"
    voice "audio/voice/001612.ogg"
    l "「啊！」"
    scene cg06c #梁芷柔看电影CG-3|紧张|CG06c
    with dissolve
    "入戏颇深的梁芷柔吃了一惊，轻声低呼了出来。"
    y "「（哈哈，还真会被这样的场面吓到啊，女生还真是……）」"
    y "「（咦？）」"
    scene cg06c1 #梁芷柔看电影CG-3|紧张|抓手|CG06c1
    with vpunch
    "手！我的手！"
    "我的手突然被梁芷柔紧紧地抓住了！"
    "突如其来的状况令我一下子遭受到了远比电影情节强烈一百倍的惊吓。"
    "一瞬间，整个人都变得僵硬了起来。"
    l "「……」"
    y "「……」"
    "梁芷柔紧紧地盯着荧屏，我则是紧紧地盯着她的侧脸。"
    "很快，女主角就被卷入了大海。"
    voice "audio/voice/001613.ogg"
    l "「……啊。」"
    scene cg06d #梁芷柔看电影CG-4|捂嘴|CG06d
    with dissolve
    "梁芷柔用手捂住嘴，尽量压住自己的声音。"
    "手……自然是松开了。"
    y "「……」"
    l "「……」"
    "我看着她的侧脸。"
    "由于灯光昏暗，我看不太清楚她的表情。"
    "不过，感觉上……她应该还是在全神贯注地沉浸在电影的世界中吧。"
    "刚才的那一瞬，应该只是她下意识的举动。或许她自己都没有注意到吧……"
    "这样也好。大概，真要是注意到了反而更麻烦。"
    stop sound fadeout 3.0

    "……"
    "…………"
    scene bg black #黑屏
    with fade
    "……就这样，我以一种混杂着如释重负和微微失落的复杂而奇妙的心情，看完了电影的下半段。"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    scene bg b10 #百货商场
    with fade
    y "「呼啊！」"
    "「重见天日」。"
    "离开放映厅，我脑子里冒出来的第一个词，居然是这个。"
    "……其实电影还是很好看啦，但是电影以外的干扰太过强烈了，直到最后，我的心情也没能平稳下来。"
    "而造成这一切的罪魁祸首……"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001614.ogg"
    l "「哎呀我好开心啊！能来看这场电影真是太好了！」"
    "却没有一丝一毫的罪恶感，正在兴高采烈地大发感慨。"
    voice "audio/voice/001615.ogg"
    l "「中间有一段我还以为会是悲剧呢，没想到后面他们还能在一起！而且几个演员都长得好漂亮～虽然都是新人但是演技真的很不错！」"
    y "「呵呵、呵呵……」"
    "居然一点都没注意自己做了什么吗……果然这丫头一旦陷入紧张状态，就会变得超级迷糊。"
    "算了，她玩得高兴就好。"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/001616.ogg"
    l "「啊，哈哈，抱歉啊。」"
    voice "audio/voice/001617.ogg"
    l "「光顾着我自己高兴了……你是不是觉得特无聊啊，这个电影？」"
    y "「不会啊，我虽然不是很懂，但也大受震撼。」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001618.ogg"
    l "「嗯？」"
    y "「……这就是真正的被水淹没，不知所措吧。」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/001619.ogg"
    l "「什么鬼啦！讨厌！」"
    voice "audio/voice/001620.ogg"
    l "「……呼。」"
    show chara c12a #梁芷柔立绘|夏季私服|羞涩1
    with dissolve
    l "「……」"
    stop music fadeout 1.5

    voice "audio/voice/001621.ogg"
    l "「那个……」"
    play sound "audio/sound/ambientnoise08.ogg" fadein 1.5 loop #商场环境噪音
    y "「嗯？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    l "「……」"
    voice "audio/voice/001622.ogg"
    l "「……谢谢你。」"
    y "「哎？」"
    "梁芷柔突然很郑重其事地对道谢，这让我一下子有些愣神。"
    voice "audio/voice/001623.ogg"
    l "「谢谢你今天陪我，陪我逛街、陪我看电影，还送了我礼物……」"
    voice "audio/voice/001624.ogg"
    l "「我……玩得很开心。」"
    voice "audio/voice/001625.ogg"
    l "「真的，好久好久都没这么开心过了。」"
    voice "audio/voice/001626.ogg"
    l "「所以，谢谢你。」"
    y "「呃……」"
    "我犹豫了一下。"
    "其实我想对她说——"
    "「你干嘛非要把自己逼得那么死呢？」"
    "「连给自己一点放松的时间都这么吝啬？」"
    "但是，看着她清澈的眸子，这些话我全都说不出口。"
    "话到了嘴边，还是换了一句。"
    stop sound fadeout 3.0
    y "「没什么……」"
    y "「……不客气。」"
    scene bg black #黑屏
    with fade
    "我们……终究不一样。"
    "现在的我，根本没有资格去这样问她。"
    "所以，除了这样的话以外，我还能说什么呢？"
    "……"
    "…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t05 #转场 百货商场
    with fade
    pause

#暑假的最后一天。
#8月15日。

    scene bg b02 #城区
    with fade
    "在七夕之后，我们一如既往地继续着每天的学习会，就这样又过了将近一周。"
    "终于，暑假的最后一天到来了。"

    play sound "audio/sound/effect10.ogg" fadein 0.5 loop #写字声
    scene cg04a #梁芷柔快餐店学习CG-1|就坐|CG04a
    with fade
    "尽管这一次的暑假是有生以来最短的，却也是最充实的。"
    "许许多多个有生以来的第一次，都在这个短短的假期中发生了，可以说是极大地丰富了我的人生经验。"
    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with dissolve
    "回过头想想，我都有点佩服自己了……亏我能坚持得下来。"
    "想当年中考的时候，我也就是在最后的备战关头，才开始主动给自己加了加码。而现在明明距离高考还有将近一个学年的时间，我却已经有了当初的那种紧张感。"
    scene cg04b1 #梁芷柔快餐店学习CG-2|讲题|CG04b1
    with dissolve
    "为我带来这种改变的，毫无疑问就是眼前这个陪了我一整个暑假的女生。"
    "我们俩之间有着巨大的差距，大到足以对未来绝望。通过这半个月的交往，我越来越清晰地认清了这个现实。"
    scene bg black #黑屏
    with fade
    "然而，尽管如此，我还是有点不死心。"
    "还是不想放弃。"
    "还是希望，能够找到一个……进一步改变自己、缩短彼此差距的方法。"
    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    scene cg04b1 #梁芷柔快餐店学习CG-2|讲题|CG04b1
    with fade
    voice "audio/voice/001627.ogg"
    l "「……就是这样啦！」"
    y "「嗯嗯。」"
    voice "audio/voice/001628.ogg"
    l "「好。那，今天就到此为止吧。」"
    y "「噢。」"
    voice "audio/voice/001629.ogg"
    l "「嗯～～～」"
    "把最后一个问题讲完，梁芷柔忍不住伸了个大大的懒腰。"
    scene cg04a #梁芷柔快餐店学习CG-1|就坐|CG04a
    with dissolve
    voice "audio/voice/001630.ogg"
    l "「明天就要开学了呢。」"
    y "「嗯，是啊。这个暑假真短。」"
    scene cg04a1 #梁芷柔快餐店学习CG-1|就坐|微笑|CG04a1
    with dissolve
    voice "audio/voice/001631.ogg"
    l "「还都耗在我这儿了。呵呵，有没有后悔呀？」"
    y "「哪能啊？感谢还来不及呢。」"
    y "「辛辛苦苦给我这么笨的人当了半个月的家庭教师。」"
    voice "audio/voice/001632.ogg"
    l "「嘻嘻，都说了你一点也不笨啦。」"
    y "「总之谢谢啦。真的，我这半个月真是受益太多了。」"
    voice "audio/voice/001633.ogg"
    l "「呵呵，很好，有进步就好。」"
    scene bg b07 #快餐店
    with fade
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    l "「……」"
    voice "audio/voice/001634.ogg"
    l "「那个，叶雨潇。」"
    y "「嗯？」"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    voice "audio/voice/001635.ogg"
    l "「接下来，你打算怎么办？」"
    y "「啊？你指什么？」"
    show chara lc08b #梁芷柔立绘|夏季私服|担心2|近
    with dissolve
    voice "audio/voice/001636.ogg"
    l "「一年的时间啊，说短不短，说长也不算长。晃一晃的话，一下子也就过去了。」"
    y "「啊……」"
    show chara lc05b #梁芷柔立绘|夏季私服|苦笑2|近
    with dissolve
    voice "audio/voice/001637.ogg"
    l "「我啊，还是希望……你能努把力试试看。」"
    voice "audio/voice/001638.ogg"
    l "「至少，不会让自己后悔。」"
    y "「……」"
    "「不会让自己后悔。」"
    "是啊……我也不想让自己后悔。"
    "可是……"
    y "「我……能问你一个问题吗？」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001639.ogg"
    l "「嗯？嗯，你问吧。」"
    y "「你说你小学的时候成绩不好。」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001640.ogg"
    l "「嗯。」"
    y "「那到底是怎么回事？后来到底发生了什么啊，能让你变成现在这样？」"
    "之前我也问过梁芷柔这个问题，不过被她避而不答。"
    "如果当时是因为时机不成熟的话……不知道现在的我，是否有些进步了呢？"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001641.ogg"
    l "「这个呀……呵呵。」"
    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/001642.ogg"
    l "「其实呢，我这也是吃了亏，才长的记性。」"
    y "「哦？」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001643.ogg"
    l "「我小的时候是真不好好学习，六年级的时候，语数外三科总共才考了220多分。」"
    y "「……呃？」"
    "虽然说是成绩不好，但我也没想到会是个如此糟糕的分数。"
    "一般来说，小学考试的成绩，一般来说怎么都能维持在80分以上吧……好一点的学生，平均分90以上问题不大。"
    "像我，六年级各科考试成绩就从来没下过90分……"
    "平均分70出头……偏科的话，还有可能有不及格？这真的是梁芷柔能考出来的成绩吗？"
    voice "audio/voice/001644.ogg"
    l "「对……所以毕业的时候，给我分配的学校是就近的十三中。」"
    y "「哦……啥！？」"
    with vpunch
    y "「十三中！？」"
    "要说前面的爆料还能镇定得住，现在这个重磅炸弹可就真的把我给惊到了。"
    "十三中……我知道那个学校，新建没几年，是县里扶贫计划的一部分。"
    "早年间，县城里原本只有两所高中、四所初中，师资力量也很有限，经常是连九年义务教育都做不到。"
    "前几年为了强推义务教育，政府动用扶贫基金，斥资修建了一大批规模较小，但具备基本条件的初中。"
    "十三中也是其中的一所，就在县城里，招收的主要是家住附近的条件较差……或者成绩不怎么好的学生。"
    "那一类学校……感觉上，就好像是在说「反正你们也不打算考、或者考不上高中，不过好歹把九年义务教育念完吧」似的，为了完成任务而建立的。"
    "梁芷柔居然是在这样的学校里上的初中？"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001645.ogg"
    l "「怎么啦，很惊讶吗？」"
    y "「我还以为你是本校直升上来的呢！」"
    "我们学校里包括了完整的初中部，而县一中也是县里排名最好的学校。"
    show chara lc05b #梁芷柔立绘|夏季私服|苦笑2|近
    with dissolve
    voice "audio/voice/001646.ogg"
    l "「呵呵，怎么可能啦，我当时的成绩完全够不上一中的标准的。」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001647.ogg"
    l "「不过嘛，最后我倒是也没去十三中，而是去二中上的初中。」"
    y "「哎？」"
    voice "audio/voice/001648.ogg"
    l "「我妈……托人，花了赞助费，把我送进去了。」"
    y "「啊……」"
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve
    voice "audio/voice/001649.ogg"
    l "「你想，我这个情况，我妈得是费了多大的劲才行啊。」"
    voice "audio/voice/001650.ogg"
    l "「不光是一大笔赞助费，还得到处求爷爷告奶奶的，各个环节都得打点……那阵子，我妈为我上学这事，真是操碎了心了。」"
    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/001651.ogg"
    l "「我家的条件，一般吧。结果这么一折腾，几乎砸锅卖铁了。但是我妈就是死咬着，说必须得上个好点的学校，否则我就彻底完了。」"
    y "「呃……」"
    "这黑历史……我没记错的话，梁芷柔到我们班上的时候就一直稳坐学习成绩第一的宝座，从来没掉下去过，哪想得到还有这么奇葩的过往。"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001652.ogg"
    l "「我家基本上是个慈父严母的情况。我妈呢，是个典型的望女成凤的家长，对我要求很严，小时候我真是没少挨打挨骂。」"
    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/001653.ogg"
    l "「要说起来，我本来也都习惯了。不过，那一段时间真的是……嗯，反正我的日子挺不好过的。」"
    voice "audio/voice/001654.ogg"
    l "「我一开始还不怎么懂事，虽然知道是自己错了，给家里添了麻烦，但就是死咬着不想承认，还在闹。结果在我12岁生日的那一天……」"
    stop sound fadeout 3.0
    voice "audio/voice/001655.ogg"
    l "「我妈晚上刚回到家，就在我的面前，就那么直挺挺地……倒下了。」"

    scene cg07 #赤印梗|小梁芷柔跪地大哭|草图|CG07
    with fade
    voice "audio/voice/001658.ogg"
    loli "「妈妈！你醒醒啊，妈妈！！呜……」"
    voice "audio/voice/001659.ogg"
    loli "「妈妈你别不理我啊！」"
    voice "audio/voice/001660.ogg"
    loli "「妈妈！我再也不挑食了！我再也不在晚上闹腾了！我再不惹你生气了！！」"
    voice "audio/voice/001661.ogg"
    loli "「我会好好学习的！真的！！我以后再也不会让你操心了！妈妈你醒醒啊！！」"
    voice "audio/voice/001662.ogg"
    loli "「呜……呜！哇哇！！！！」"
    "……"
    "…………"
    scene bg b07 #快餐店
    with fade
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve

    voice "audio/voice/001657.ogg"
    l "「当时我妈的脸色，白得跟纸一样，那样子别提有多吓人了。我爸当时也不在家，我又小，也不知道是个什么情况，还以为我妈死了，一下子就傻了，什么都没做，就知道在那儿哇哇的哭。」"
    voice "audio/voice/001656.ogg"
    l "「我是后来才知道的，我妈为了多挣一点加班费，那段时间没少加班……本来她的工作就忙，这么一来，就累垮了。」"
    y "「啊……」"
    voice "audio/voice/001663.ogg"
    l "「……我到现在还记得当时的感觉，就好像全世界都死掉了一样。」"
    y "「那你妈妈后来……？」"

    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/001664.ogg"
    l "「啊，那之后邻居听见动静过来敲门，帮着我把妈妈送到了医院。我妈其实就是疲劳过度，休息了一段时间就好了。」"
    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001665.ogg"
    l "「但是我真的……是不想再体验那种感觉了。」"
    show chara lc05b #梁芷柔立绘|夏季私服|苦笑2|近
    with dissolve
    voice "audio/voice/001666.ogg"
    l "「所以从那以后，我就从一个特别淘气，不好好学习只知道疯玩的傻丫头，变得开始能静下心来认真学点什么、干点什么了。」"
    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/001667.ogg"
    l "「然后呢，学着学着，就发现其实掌握方法以后，学习也不是什么特别痛苦的事，就这样，到了中考的时候，我总算是没再让家里人失望咯。」"
    y "「……」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001668.ogg"
    l "「怎么样，是不是一个挺无聊的故事？」"
    y "「才不是。」"
    hide chara
    with dissolve
    "原来如此。"
    "我多少明白……为什么她会觉得我和她有点「像」了。"
    "因为我的成绩一直还算凑合，我爸我妈倒是没有怎么逼过我，只是……现在想想，父母其实没少投来过期待的目光，却都被我熟视无睹了而已。"
    "哪怕……其实只要自己愿意，明明可以更进一步的。"
    "如果我一直这样蹉跎下去的话，即便没有像小时候的梁芷柔那样吃个大亏，也只能是泯然众人。"
    "正所谓少壮不努力，老大徒伤悲。"
    "长歌行的这句诗，明明早已司空见惯，却在这一刻，突然给予了我无比的实感。"
    "如果不是经历了这一个暑假超越以往极限的自习的话，我是肯定不会真正地认识到这一点的。"
    "不过……"
    y "「那个……」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001669.ogg"
    l "「嗯？」"
    y "「我能再问一个问题吗？」"
    show chara lc13b #梁芷柔立绘|夏季私服|疑惑2|近
    with dissolve
    voice "audio/voice/001670.ogg"
    l "「嗯，你说。」"
    y "「你现在……」"
    y "「……还是在为了家里人的期望而努力吗？」"
    show chara lc01b #梁芷柔立绘|夏季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/001671.ogg"
    l "「嗯，不是了。」"
    y "「那？」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001672.ogg"
    l "「应该说，不只是了吧。我现在呢，更多的，是为了我自己的梦想在努力。」"
    y "「梦想？」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001673.ogg"
    l "「嗯，不过呢，那就是另外一个故事了。」"
    y "「哎？」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001674.ogg"
    l "「嘻嘻，以后有机会再跟你说吧。」"
    y "「……」"
    stop sound fadeout 3.0

    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/001675.ogg"
    l "「也许，如果你能顺利完成那个『小目标』的话……」"
    "梁芷柔轻轻地说着，不过说到一半，就没有再继续。"
    scene bg black #黑屏
    with fade
    "……"
    "…………"

    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    scene bg b04 #滨河路|夏
    with fade
    "就这样，暑假结束了。"
    y "「梦想啊……」"
    "我独自走在回家的路上，思索着梁芷柔的话语。"
    y "「我的梦想又是什么呢？」"
    y "「……」"
    "我想要追赶梁芷柔的脚步。"
    "我想去憧憬与她同样的未来。"
    "这确确实实是我的目标，直到现在也是如此。"
    "……应该是这样的。"
    "然而，这半个月以来，更多的时候却反而是我在被梁芷柔推着前进。"
    "我究竟是怎么想的？"
    "我究竟该怎么做？"
    "我究竟……想怎么做？"
    "……"
    "…………"
    scene bg b00a #天空|候鸟
    with fade
    bird "「啾——」"
    "抬头望天，有大雁正从半空飞过。"
    y "「燕雀……安知鸿鹄之志……吗？」"
    "这批大雁正在进行最后的准备。"
    "半个月后，它们就将飞越艰险的青藏高原，启程向南迁徙。"
    "留给它们的安逸时间，已经不多了。"
    scene bg b05 #湿地公园|夏
    with fade
    "我遥遥望向河边的湿地公园。"
    "看着那些尚在嬉戏的水鸟。"
    "看了许久。"
    stop music fadeout 1.5
    "……"
    "…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t06 #转场 天空
    with fade
    pause

#02.初秋篇

    $ chapter = "02"

#开学。
#8月16日。

    scene bg b02 #城区
    with fade
    "8月，中旬。"

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音

    scene bg b01 #教室
    with fade
    "短短15天的假期如白驹过隙般一晃而过，所有升入高三的学生都被强行拉入了名为「备战高考」的超大型国战副本，提前回到了学校。"
    "老师们早已准备就绪，全都如同打了鸡血一般亢奋不已，憋足了劲准备鞭策学生们好好学习天天向上，争取考出优异成绩，让学校的高考上线率再创新高。"
    "……"
    "其实也不是不能理解。"
    "毕竟我们学校是县内最好的高中，在教育局里是挂了号的，学生的成绩直接决定了他们的前途，以及奖金。"
    "据说有些指标已经被硬性安排好了——真凭实绩当然最好，但即便我们不怎么争气，也会有一个看起来还算「顺眼」的水平。"
    "当然，学校倒是不至于丧尽节操到只会篡改数据，该做的、能做的其实已经是一样不落全做尽了。"
    stop sound fadeout 1.5

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    "只不过……"
    voice "audio/voice/052001.ogg"
    a "「……今年这暑假可真够短的了。」"
    voice "audio/voice/062001.ogg"
    b "「是啊，这才几天啊，感觉还没开始就过去了。」"
    voice "audio/voice/052002.ogg"
    a "「真是的……哎，你作业做了么？」"
    voice "audio/voice/062002.ogg"
    b "「做个毛。妈的我大概是拿了本假作业，答案居然只有结果没有过程。」"
    voice "audio/voice/052003.ogg"
    a "「对啊，这怎么办啊？」"
    voice "audio/voice/062003.ogg"
    b "「凉拌……抄呗！」"
    voice "audio/voice/052004.ogg"
    a "「你知道谁做完了吗？」"
    voice "audio/voice/062004.ogg"
    b "「梁芷柔呗。」"
    voice "audio/voice/052005.ogg"
    a "「滚滚滚，说正经的！」"
    voice "audio/voice/062005.ogg"
    b "「我想想啊……哎，你看，那边那谁是不是正抄着呢！」"
    voice "audio/voice/052006.ogg"
    a "「啊，还真是。」"
    voice "audio/voice/052007.ogg"
    a "「你眼够尖的啊！走走走，赶快先跟他预定去，别待会儿让人给抢了。」"
    voice "audio/voice/062006.ogg"
    b "「哈哈哈，同去同去！」"
    "……"
    stop music fadeout 2.5
    "…………"
    "这就是所谓的「皇上不急太监急」了吧。"

    scene bg b02 #城区
    with fade
    y "「……」"
    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    "望向窗外，可以看到商业街那边的建筑。"
    y "「这帮家伙啊，知足吧……」"
    "他们好歹还踏踏实实地歇了半个月。"
    with vpunch
    "我可是一天都没闲着啊——！！！"
    "甚至于，这个暑假我在学习上投入的精力，比之前在校的时候还要多出一大截呢！"
    "班主任要是知道了，大概会被感动得痛哭流涕吧？"
    "我可是彻彻底底地把他放假前说的「这两个星期的假期不是给你们玩的」落实到了实处啊！"
    "估计全班……不，全年级都算上，几百口人里真正能做到这个份上的，一个巴掌就能数过来。"
    "虽然……"
    "在动机方面，应该和老师期望的有点不一样？"
    "……"
    "…………"
    scene bg b01 #教室
    with fade
    "将视线挪回教室，向那个身影望去。"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/002001.ogg"
    l "「就是说啊，上次我看到的时候也是吓了一跳呢……」"
    "梁芷柔似乎正在和几个女生聊着什么。"
    hide chara
    with dissolve
    "女生之间似乎永远有说不完的话题，只要想聊，总可以聊得热火朝天，不过是不是真的那么亲热，就谁也说不好了。"
    "比方说，现在其中的一个女生，就在别的场合抱怨过梁芷柔「装模作样」。"
    "梁芷柔应该不会不知道，只是……也应该不会在乎这种事吧。"
    "她太清楚自己的目标了，一路奋进只为到达终点，才不会因为这些破事在半途驻足。"
    y "「……唉。」"
    "……这人和人的差距啊！"
    "这样想想，她愿意顺手捎我一程，也是着实难得了。"
    "虽然如此，我这边却还有一个跟不跟得上的问题……"
    stop music fadeout 2.5

    "至于我那点小心思，就更甭提了。"

    scene bg black #黑屏
    with fade
    "……"
    "…………"

    scene bg b01 #教室
    with fade
    show charaz h03 #老师立绘|夏季|皱眉
    with dissolve
    voice "audio/voice/012001.ogg"
    z "「……去年咱们学校的成绩还不错，考上一本的人数再创新高！啊，但是！这是大学扩招所带来的必然结果，是历史的进程！你们赶上了好时候是不假，但并不是说就不需要个人的奋斗了……」"
    show charaz h04 #老师立绘|夏季|咆哮
    with dissolve
    voice "audio/voice/012002.ogg"
    z "「……老师带过很多届高三学生了，啊，什么样的学生我没见过？须知不听老人言吃亏在眼前，你们还年轻！这个时候最重要的目标是提高自己的知识水平，考出好成绩来……」"
    "新学期第一节课，照例是思想动员。"
    "时隔半月，再次见到老师，发现他似乎也休息得不怎么样，声音一如既往的嘶哑，脸上也依旧是一大片的胡茬。"
    hide charaz
    with dissolve
    "再看看身边的同学，大概还都沉浸在假期的感觉之中吧，同样是一个个东倒西歪，左耳朵进右耳朵出，懒散得不成样子。"
    "除了……"

    play sound "audio/sound/effect10.ogg" fadein 1.5 loop
    scene cg01a #梁芷柔听讲CG-1|标准|CG01a
    with fade
    l "「……」"
    y "「（果然。）」"
    "梁芷柔还是那样，无论什么时候都保持着标准的坐姿。"
    "到底是怎么磨炼出来的啊……这么坚韧的意志。"
    y "「（说起来……）」"
    "眼前的这一幕，实在是有点似曾相识。"
    "好像半个月前的时候也是这个样子的……"
    y "「（唔，待会儿不会再有椅子飞过来了吧……）」"
    y "「（嗯？）」"
    stop sound fadeout 3.0

    scene cg01b #梁芷柔听讲CG-2|眼睛向后瞟视|CG01b
    with dissolve
    l "「……」"
    y "「（啊……）」"
    y "「（又被发现了……）」"

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    l "「……」"
    scene cg01b1 #梁芷柔听讲CG-2|瞪眼|CG01b1
    with dissolve
    l "「……」"
    y "「（呃……）」"
    "呜……被狠狠地瞪了一眼。"
    "这是在警告我不要东张西望吗？"
    y "「（好啦好啦，知道啦……）」"
    "我不好意思地讪笑了一下，挠了挠脸，刚想要把视线别开……"
    y "「（……咦？）」"
    scene cg01b2 #梁芷柔听讲CG-2|笑|CG01b2
    with dissolve
    voice "audio/voice/002002.ogg"
    l "「……」"
    y "「（啊……）」"
    "笑、笑了？"
    "不知是因为看到了我的窘相还是别的什么的，梁芷柔露出了狡黠的笑容。"
    y "「……」"
    "总觉得我又被调戏了啊！"
    "不行，不行，这场子必须得找回来！"
    y "「……」"
    y "「（盯——）」"
    "我开始肆无忌惮地盯着她看。"
    scene cg01b #梁芷柔听讲CG-2|眼睛向后瞟视|CG01b
    with dissolve
    l "「……」"
    "察觉到我再一次看过来，梁芷柔似乎稍稍有些疑惑，微微地皱了皱眉头。"
    scene cg01b1 #梁芷柔听讲CG-2|瞪眼|CG01b1
    with dissolve
    l "「……」"
    y "「（啊……又被瞪了。）」"
    y "「（嗯？）」"
    scene cg01b3 #梁芷柔听讲CG-2|笑瞪|CG01b3
    with dissolve
    "不过，这次梁芷柔没坚持住，刚瞪了一眼，自己就先笑场了。"
    y "「……」"
    "好啊，这是较上劲了吧？"
    "谁怕谁啊？不给你点厉害看看，你都不知道马王爷长几只眼！"
    y "「……！」"
    y "「……！！」"
    y "「……！！！」"
    with vpunch
    y "「……！！！！」"
    "接下来的小半段课时里，我俩一直持续着这种大眼瞪小眼的无声交流。"
    stop music fadeout 2.5

    "……"
    "…………"
    scene bg black #黑屏
    with fade
    play sound "audio/sound/effect06.ogg" noloop
    pause
    scene bg b01 #教室
    with fade
    "总算熬到下课了。"
    y "「妈呀。」"
    "先使劲揉了揉眼睛。"
    with fade
    with fade
    "酸得是一塌糊涂……不行了，我需要眼保健操。"
    scene bg black #黑屏
    with fade
    "……"
    "…………"
    voice "audio/voice/002003.ogg"
    l "「……喂。」"
    scene bg b01 #教室
    with fade
    with fade
    y "「啊？」"
    "睁开眼睛，看到梁芷柔笑吟吟地站在我的座位旁边。"
    show chara a09 #梁芷柔立绘|夏季校服|坏笑
    with dissolve
    voice "audio/voice/002004.ogg"
    l "「怎么啦，没事吧？」"
    y "「啊……还好吧。」"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/002005.ogg"
    l "「你这就叫自作自受，谁让你不好好听讲就知道到处瞎瞅的，嗯？」"
    y "「……喂喂喂，你也好意思说这话啊？」"
    "话说回来，这人居然什么事都没有？眼睛是什么材料长的啊？氪金吗？"
    show chara a13a #梁芷柔立绘|夏季校服|疑惑1
    with dissolve
    voice "audio/voice/002006.ogg"
    l "「嘿嘿，我怎么就不好意思啦？」"
    y "「难道你好好听了吗？」"
    show chara a09 #梁芷柔立绘|夏季校服|坏笑
    with dissolve
    voice "audio/voice/002007.ogg"
    l "「哎？你怎么知道我没听啊？」"
    y "「就你那样子，能听得进去才怪呢！」"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/002008.ogg"
    l "「怪什么怪，是你少见多怪吧？要我把老师刚才讲的内容给你重复一遍吗？」"
    y "「……啥？」"
    show chara a02 #梁芷柔立绘|夏季校服|皱眉
    with dissolve
    voice "audio/voice/002009.ogg"
    l "「咳咳！」"
    show chara a01a #梁芷柔立绘|夏季校服|普通|正面
    with dissolve
    voice "audio/voice/002010.ogg"
    l "「老师说啊，这一年是重中之重，每个人都不能掉以轻心。我们之前用一年的时间学了两年的课，目前还有很多的同学不扎实，现在的首要任务是先把前面学完的知识巩固牢了……」"
    y "「……」"
    "这也行？"
    "刚才光顾着和梁芷柔较劲了，至于老师在讲台上说了些什么，我真的是一句都没有听进去，完全当成噪音给屏蔽掉了。"
    "但梁芷柔……居然可以同时一心二用到这个程度吗？这未免非人了吧！？"
    show chara a01b #梁芷柔立绘|夏季校服|普通|侧面
    with dissolve
    voice "audio/voice/002011.ogg"
    l "「怎么样？服不服？」"
    y "「……服了。」"
    show chara a09 #梁芷柔立绘|夏季校服|坏笑
    with dissolve
    voice "audio/voice/002012.ogg"
    l "「嘻嘻。」"
    "梁芷柔露出了得意的笑容。"
    y "「嗯？」"
    y "「……等等。」"
    "从梁芷柔的笑容之中，我突然发现了一丝……狡猾的模样。"
    "如果换成一个不熟悉她的人来看——就好比半个月以前的我——那是肯定是完全看不出来的。"
    "但是现在，虽然还吃不太准，不过已经能够多少有所察觉。"
    show chara a13b #梁芷柔立绘|夏季校服|疑惑2
    with dissolve
    voice "audio/voice/002013.ogg"
    l "「嗯？怎么啦？」"
    y "「……你是在诈我吧？」"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/002014.ogg"
    l "「啊？嘻嘻，我怎么诈你啦？」"
    "果然，没有否认啊！"
    y "「其实你也没有听，刚才说的都是你自己编的吧？」"
    show chara a09 #梁芷柔立绘|夏季校服|坏笑
    with dissolve
    voice "audio/voice/002015.ogg"
    l "「有吗？」"
    y "「有啊。」"
    "刚才这一堆说辞实在是太过高大上或者说假大空了，根本就是套话嘛。"
    "梁芷柔身为班长，班会上没少说过类似的话，早就可以信手拈来了。"
    "……虽然，很有可能老师也确实就是讲了这些内容。"
    show chara a02 #梁芷柔立绘|夏季校服|皱眉
    with dissolve
    voice "audio/voice/002016.ogg"
    l "「嗯……咳咳，你有证据吗？」"
    y "「……欲盖弥彰啊班长，何必呢，至于吗？」"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/002017.ogg"
    l "「哈哈，好吧。」"
    "梁芷柔又笑了起来，不过这次就是纯粹的开心了。"
    show chara a04 #梁芷柔立绘|夏季校服|无奈
    with dissolve
    voice "audio/voice/002018.ogg"
    l "「你说你，新学期第一天就这么涣散，以后可怎么办呀？」"
    y "「那你呢？你不也一样。」"
    show chara a11 #梁芷柔立绘|夏季校服|微笑
    with dissolve
    voice "audio/voice/002019.ogg"
    l "「我这个当然不一样啦，我这叫游刃有余好不好。」"
    y "「好好好……怎么说都是你有理，算我认栽了好吧？」"
    show chara a02 #梁芷柔立绘|夏季校服|皱眉
    with dissolve
    voice "audio/voice/002020.ogg"
    l "「什么叫『算』嘛！」"
    "梁芷柔对我敷衍的态度颇为不满的样子，撅起了小嘴。"
    y "「本来就是嘛，我虽然比不上您老人家，但是比起其他人可能还是要好上不少的吧。」"
    show chara a04 #梁芷柔立绘|夏季校服|无奈
    with dissolve
    voice "audio/voice/002021.ogg"
    l "「是吗？」"
    y "「当然啊，托您的福。」"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/002022.ogg"
    l "「嘻嘻，不客气。」"
    show chara a02 #梁芷柔立绘|夏季校服|皱眉
    with dissolve
    voice "audio/voice/002023.ogg"
    l "「不过你可别放松警惕啊，接下来这一年才是动真格的。『小目标』，知不知道！」"
    y "「好啦好啦，知道啦！」"
    show chara a03 #梁芷柔立绘|夏季校服|生气
    with dissolve
    voice "audio/voice/002024.ogg"
    l "「哼，又敷衍！」"
    y "「喂喂喂，你又冤枉我啊？」"
    show chara a02 #梁芷柔立绘|夏季校服|皱眉
    with dissolve
    voice "audio/voice/002025.ogg"
    l "「我怎么冤枉你啦？」"
    "我翻了个白眼，索性不说话了。不过梁芷柔也没离开，就这么在旁边盯着我，似乎在等我的回话。"
    y "「……」"
    l "「……」"
    "她这一认真起来，还真是让人招架不住啊。不过……"
    y "「……嗯？」"
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
    voice "audio/voice/002026.ogg"
    l "「啊……」"
    "我们俩安静下来以后，周围的声音就一下子显得大起来了。"
    hide chara
    with dissolve
    e "「叽叽喳喳叽叽喳喳……」"
    "不知什么时候，以我的课桌为中心，周围一圈的人都被彻底清空，连我的同桌都不知道跑哪儿去了。"
    "但是人们并没有走远，而是在稍微远一点的位置上散布成一个同心圆的形状。"
    "所有的人全都目不转睛地盯着我……和梁芷柔。"
    e "「叽叽喳喳叽叽喳喳……」"
    "交头接耳的声音络绎不绝。"
    y "「……啥情况？」"

    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
    voice "audio/voice/002027.ogg"
    l "「这个……」"
    "……有什么奇怪的吗？"
    "我有些疑惑地望向梁芷柔，后者也是一脸的茫然。"
    hide chara
    with dissolve
    voice "audio/voice/082001.ogg"
    f "「那个……」"
    y "「嗯？」"
    "一个女生……据我所知是个超级八卦的家伙，似乎终于掩盖不了自己的好奇，壮着胆子凑到了我们的旁边。"
    voice "audio/voice/082002.ogg"
    f "「你们俩……现在是个什么关系？」"
    y "「……啊？」"
    "我呆了一下，有点没搞明白……她在问什么？"
    voice "audio/voice/082003.ogg"
    f "「你看，放暑假之前，咱们班不是打架了吗？」"
    voice "audio/voice/082004.ogg"
    f "「是不是因为你奋不顾身舍命相救，所以梁芷柔就……嗯？」"
    "女生挑着眉毛，一幅欲言又止的模样，不过这个暗示倒是很明白了。"
    voice "audio/voice/002028.ogg"
    yl "「啊？」"
    voice "audio/voice/082005.ogg"
    f "「对吧芷柔？你们俩，现在，到底……？」"
    show chara a03 #梁芷柔立绘|夏季校服|生气
    with dissolve
    voice "audio/voice/002029.ogg"
    l "「什么对不对的！？什么跟什么呀这是……」"
    y "「就是！哎哎哎我跟你说啊你不要凭空污人清白……」"
    voice "audio/voice/082006.ogg"
    f "「哎呀～行啦，不要解释了，对吧？我们明白的！」"
    voice "audio/voice/002030.ogg"
    yl "「——才不对！！！」"
    scene bg black #黑屏
    with fade
    "……"
    "…………"
    scene bg b01 #教室
    with fade
    "一阵兵荒马乱之后，班级里总算是恢复了秩序。"
    voice "audio/voice/002031.ogg"
    l "「唉……」"
    y "「这帮家伙……真是……」"
    "这帮人其实也就是在瞎起哄罢了，真要说起来，怕是他们自己也不相信我们之间会有些什么的。"
    "说起来，还是因为从前的我确实极少和梁芷柔有什么交流吧……这种变化对我而言是连贯的，但在隔了一个暑假未见的同学们的眼里，那就是突如其来的改变。"
    voice "audio/voice/002032.ogg"
    l "「嘻嘻，这可都怪你啊，知道吗？」"
    y "「行。人在座位坐，锅从天上来。不对，椅子从旁边飞过来。」"
    voice "audio/voice/002033.ogg"
    l "「呸，又胡说！是不是还想再挨一次啊？不许再乱说了啊！」"
    play sound "audio/sound/effect06.ogg" noloop
    pause
    voice "audio/voice/002034.ogg"
    l "「啊……」"
    "上课铃响了。"
    voice "audio/voice/002035.ogg"
    l "「上课的时候不许再乱看了，知道吗！」"
    "悄悄撂下这样一句话，梁芷柔匆匆返回了自己的座位。"
    y "「……」"
    y "「好好好。」"
    "我轻声向着她的背影，答复道。"
    scene bg b02 #城区
    with fade
    "就这样，开学的第一天过去了。"
    "说实话，我虽然和梁芷柔一样，极力否认了我俩之间有什么非同寻常的关系，但……其实在内心之中，还是蛮享受这种感觉的。"
    "毕竟，我和她，相比她和别的同学，的确是有了那么一点「不同」的。"
    scene bg b00 #天空
    with fade
    voice "audio/voice/002036.ogg"
    l "「～」"
    "甚至，仿佛有一种时间还停留在我和她的那个暑假之中的感觉。"
    scene bg black #黑屏
    with fade
    "……"
    "…………"
    "然而……"
    "没过多久，我就深刻地意识到了——"
    "高三，已经切切实实地，到来了。"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t01 #转场 教室
    with fade
    pause

#开学后一周左右。

    scene bg b01 #教室
    with fade
    voice "audio/voice/012003.ogg"
    z "「……我看到啊，有些同学的心还没有收回来！我知道，你们暑假没放够，但是这是高三！不是其他的时候！对你们来说时间是不够用的……」"
    "开学已经一周了。"
    "天气依然燥热。"
    "老师依然聒噪。"
    "大多数的学生们依然漫不经心。"
    "然而除此以外，还是有一些东西正在悄然变化。"
    voice "audio/voice/012004.ogg"
    z "「……不要瞧不起早晚自习！学校、老师、家长都在为你们创造条件，为的就是让你们能放下其他的负担，专心搞好学习……」"
    "首先是上课的时间和内容。"
    "上个学期我们已经学完了所有的课程，接下来不会再有新的知识点需要掌握，于是要做的就只剩下复习，复习，再复习。"
    "早自习的时间被提前到7点半，下午则是新加了两节自习。据说这还只是第一阶段，随着时间的推移，还会进一步地提早拉晚。"
    "体育课被压缩到每周一节，勉强维持了一个形式，其他与学习无关的活动更是名存实亡。"
    voice "audio/voice/012005.ogg"
    z "「……现在呀你们不要去想别的，什么都别想！就是专心学习，只有这样呢才对得起你们自己，对得起你们的父母，对得起咱们一中……」"
    "现在的我们，每天都是同一个流程——听老师串讲，发卷子、测试，然后背一筐作业回家。"
    "……"
    "…………"
    with fade
    "上午的课程结束了。"
    y "「……呼。」"
    "啪！"
    "忍不住拍了拍自己的脸颊。"
    y "「不行啊这个。」"
    y "「这才刚开始一个礼拜，后面可怎么办啊……」"
    "我算是稍稍理解梁芷柔为什么老是把「动真格的」挂在嘴边了。"
    "再不把自己的精神状态调整好的话，恐怕后面跟不上节奏的情况会越来越多。"
    y "「……」"
    "朝梁芷柔的方向望去。"
    voice "audio/voice/002037.ogg"
    l "「……嗯啊啊啊～～」"
    "班长大人正在用力地伸着懒腰。"
    "说来也是，她比我用功得多，当然也会更累一些。"
    y "「……」"
    "本来想要找她问个题的，不过现在看到她这个模样，又退缩了回来。"
    "这种时候……还是别给她添麻烦了吧。"
    voice "audio/voice/002038.ogg"
    l "「……嗯？」"
    y "「啊……」"
    "梁芷柔伸完懒腰，将头转向窗户……也就是我这一侧，恰好看到了我一脸欲言又止的模样。"
    voice "audio/voice/002039.ogg"
    l "「怎么啦？」"
    y "「呃，没什么，没事。」"
    voice "audio/voice/002040.ogg"
    l "「嗯？呵……说吧，又哪不明白了？」"
    "虽然不想打扰她了，不过梁芷柔早已看穿了我的想法，反倒是主动问了起来。"
    y "「没事，我自己看吧。」"
    voice "audio/voice/002041.ogg"
    l "「少废话，赶紧的！」"
    y "「呃。」"
    "话说到这份上，再犹豫就矫情了。"
    y "「这道题。」"
#【书本声】
    voice "audio/voice/002042.ogg"
    l "「我看看……」"
    voice "audio/voice/002043.ogg"
    l "「已知抛物线C，y方等于4x的焦点为F，过点K负1，0的直线l与C相交于AB两点，点A关于x轴的对称点为D……第一证明点F在直线BD上，第二设向量AB等于9分之8，求……」"
    voice "audio/voice/002044.ogg"
    l "「具体是哪不明白？」"
    y "「哦，是这样的……」"
    "……"
    "…………"
    voice "audio/voice/002045.ogg"
    l "「这样就明白了？」"
    y "「明白了。」"
    voice "audio/voice/002046.ogg"
    l "「还有别的问题吗？」"
    y "「暂时没有了，多谢班长大人仗义出手，拨冗为在下指点迷津。」"
    "我后退一步，半屈着膝，装模作样地向梁芷柔抱了个拳。"
    voice "audio/voice/002047.ogg"
    l "「……」"
    voice "audio/voice/002048.ogg"
    l "「嘻嘻！」"
    voice "audio/voice/002049.ogg"
    l "「知道就好，本班长的时间是很宝贵滴～」"
    y "「是是是，打扰您饭后休息真是罪该万死。」"
    voice "audio/voice/002050.ogg"
    l "「哈哈。」"
    voice "audio/voice/002051.ogg"
    l "「哎，我说，那你明知该死还来找我是为什么啊？问老师去也可以吧。」"
    y "「这您就明知故问了不是？要能找得到老师我哪会来麻烦您呢。」"
    voice "audio/voice/002052.ogg"
    l "「喔，为什么呀，老师都去哪儿啦？」"
    y "「老师都被您霸占了啊。」"
    voice "audio/voice/002053.ogg"
    l "「嘻嘻……」"
    y "「所以您得对我负责……喂，第二次笑场了啊，还笑个没完，能不能愉快地玩耍了？」"
    voice "audio/voice/002054.ogg"
    l "「哈……谁让你这么贫！以前我怎么没发现你还有这种天赋啊，不说相声可惜了。」"
    y "「这才哪儿到哪儿啊，我一直都是这样的好不好，是你笑点太低了吧？」"
    voice "audio/voice/002055.ogg"
    l "「成成成，都是我不好行了吧。」"
    y "「呵呵呵……」"
    voice "audio/voice/002056.ogg"
    l "「你看，你自己也笑场了好不好？还说我……嘻嘻……」"
    "两个人都笑场了，这一幕当然也就玩不下去了。"
    "我俩偶尔会这样开开玩笑，虽然最初的时候颇是引人注目，不过久而久之，同学们也就司空见惯了。"
    "毕竟暑假前的那件事大家都一清二楚，我和梁芷柔关系会变好并不是什么难理解的事。"
    voice "audio/voice/002057.ogg"
    l "「……呼。」"
    voice "audio/voice/002058.ogg"
    l "「嗯，不闹了，说正经的。」"
    y "「嗯？」"
    voice "audio/voice/002059.ogg"
    l "「真没有别的问题啦？你可别死要面子活受罪啊。」"
    y "「真没了。真的，这我蒙你干什么啊！」"
    voice "audio/voice/002060.ogg"
    l "「嗯～」"
    voice "audio/voice/002061.ogg"
    l "「看来还可以嘛……」"
    y "「嗯？」"
    voice "audio/voice/002062.ogg"
    l "「……嗯，没事。」"
    voice "audio/voice/002063.ogg"
    l "「不错，挺好的，继续努力！」"
    "……"
    "…………"
    scene bg b04 #滨河路|夏
    with fade
    "放学后，急匆匆地踏上回家的道路。"
    "尽管这里的实际时间要比东部地区早1个多小时，但毕竟拖得太晚，到了这个时候，只有西边的天空还残留着最后的一丝余晖。"
    "饭已经在学校吃过了，不过还是想尽量早点赶回家里，这样做完作业以后还可以看一会儿书，也不至于睡得太晚。"
#【手机铃声】
    y "「……嗯？」"
    "手机突然响了。"
    "打开微信一看，是平时经常一起玩的一个班上的哥们。"
    voice "audio/voice/092001.ogg"
    g "「哎，我说，你在哪儿呢！？」"
    "什么情况？还挺着急的……"
    y "「怎么了怎么了？我回家了啊，怎么了？」"
    voice "audio/voice/092002.ogg"
    g "「我～～\[哔——\]！你那么早回去干吗啊？你到哪了？」"
    y "「……我这都过桥了。」"
    voice "audio/voice/092003.ogg"
    g "「完蛋。还说约你一起去网吧五连座吃鸡呢！」"
    y "「那他妈你不早说，再说了吃鸡最多四人联机，你五连座是要干吗？」"
    voice "audio/voice/092004.ogg"
    g "「谁知道你跑那么快！前天就没找着你，有什么事啊你最近，每天都这么急？」"
    y "「这不一大堆作业呢吗？」"
    voice "audio/voice/092005.ogg"
    g "「作业急个屁啊！」"
    y "「还得看会儿书呢！」"
    voice "audio/voice/092006.ogg"
    g "「看！你！妹！」"
    voice "audio/voice/092007.ogg"
    g "「你是不是最近和梁芷柔在一起的时间太长了？学傻了吧？你再怎么学能学成她那样吗？」"
    "扎心了，偏偏我还不知道该怎么才能反驳回去。"
    "就在我绞尽脑汁措辞的时候，那家伙又发消息过来了。"
    voice "audio/voice/092008.ogg"
    g "「哎我\[哔——\]，对了你他妈不是想要追她吧？哈哈哈哈哈哈……」"
    voice "audio/voice/092009.ogg"
    g "「我告诉你你他妈没～戏！快点改邪归正陪我们来开黑啊！」"
    "这……"
    "被说中了。虽然这家伙应该是瞎猜的。"
    "估计也就是随口胡说了一句，自己都不会相信有这种可能性。"
    "不过……"
    y "「……」"
    "……前两天的风言风语才刚平静了一点，再被炒起来就麻烦了……吧。"
    "不管是对老师、同学，还是梁芷柔，都不好交代。"
    y "「……」"
    voice "audio/voice/092010.ogg"
    g "「别废话啊，明天，定死了啊！」"
    y "「……」"
    scene bg black #黑屏
    with fade
    y "「……哦。」"
    "……"
    "…………"
    scene bg b04 #滨河路|夏
    with fade
    y "「……」"
    "心情突然之间变得十分恶劣。"
    "我自认为……我和梁芷柔的关系，比起其他同学和她的关系，是稍有一些不同的。"
    "这让我有了那么一点点的优越感，然而……"
#【看手机|回忆模式】
    voice "audio/voice/092008.ogg"
    g "「哎我\[哔——\]，对了你他妈不是想要追她吧？哈哈哈哈哈哈……」"
    scene bg b04 #滨河路|夏
    with fade
    "其实毫无意义。"
    "别说别人了，我自己都不敢认。"
    "真拿出来说，也只会被当成笑话看吧？"
    "梁芷柔呢？她又会怎么想？"
    "大概是一笑而过吧。"
    scene bg b05 #湿地公园|夏
    with fade
    y "「……真累啊。」"
    "感觉压力越来越大了。"
    "在可以追上梁芷柔的步伐之前，这一切都只能拼命压在心底，不敢有丝毫外露。"
    "然而，我真的有可能追得上吗？"
    y "「……」"
    bird "「啾——」"
    scene bg b00a #天空|候鸟
    with fade
    "仰望天空，可以看到有雁在徘徊。"
    y "「候鸟啊……」"
    scene bg b05 #湿地公园|夏
    with fade
    "不远处的湿地公园里，有工人正在开展清理工作。"
    "看样子之前洪水的影响已经渐渐消除了，正在进入恢复阶段，能够看到有一些本地的鸟类栖息其中。"
    scene bg b00 #天空
    with fade
    "即将远行的候鸟，与驻守栖息的留鸟。"
    "它们各自会有怎样的未来呢？"
    scene bg black #黑屏
    with fade
    "……"
    "…………"

#几天后。
#9月初。

    scene bg b02 #城区
    with fade
    "过了几天。"

    scene bg b01 #教室
    with fade
    "学校依旧枯燥无比。老师们只知道一个劲地给学生加码，搞得我们苦不堪言。尤其是其他两个年级也到了开学的日子，两相对比之下，更是让人难以平衡。"
    "这期间，为了不让自己显得孤立、落人口实，我一定程度地回归到了自己原来的朋友圈子，放学后一起玩了几次。"
    "然而这并不能让我放松心情，反而因为心里面装着事，每次都很不踏实。"
    "这他妈的……以前是学，学不下去，现在是玩，玩不舒服。简直要人命了。"
    y "「……哎！」"
    "感觉自己长吁短叹的时候越来越多了……这样下去会出问题的吧？"
    "下意识地看了看让我整个人都变得不好的始作俑者……"
    y "「嗯？」"
    voice "audio/voice/002064.ogg"
    l "「……呼。」"
    "这一位倒还真是……放松得好彻底啊。"
    "和上课时的样子判若两人，直接脸冲下趴在桌子上了。"
    "说起来也难怪，之前的每次课间，她都忙着东奔西跑，不是帮老师收拾资料，就是帮其他同学解答问题，也几乎没有休息。"
    "不过，现在到了该吃饭的时候，让她这么睡过去似乎也不是个事。"
    "想了一下，我还是走了过去。"
    y "「喂。」"
    voice "audio/voice/002065.ogg"
    l "「……嗯？」"
    y "「别睡啦，该吃饭了。」"
    voice "audio/voice/002066.ogg"
    l "「啊哈哈……我没在睡啦，就趴了一小下而已嘛。」"
    "梁芷柔保持着趴在桌子上的姿势，只是把头稍稍朝我这一侧扭了一点，似乎是想表示一下对说话对象的尊重。"
    y "「怎么搞的啊，累成这样。」"
    voice "audio/voice/002067.ogg"
    l "「『力微任重久神疲，再竭衰庸定不支』……」"
    y "「啥……？」"
    voice "audio/voice/002068.ogg"
    l "「嘻嘻，没事啦，别那么大惊小怪的，你先吃去吧。」"
    "虽然还是闷头趴着没动，但梁芷柔的声音听起来还算精神。"
    "也是，既然还有心情突然念诗玩，那应该问题不大。"
    "不过……果然，即便是梁芷柔，在这种时候也不可能再像之前那样游刃有余了啊。"
    voice "audio/voice/002069.ogg"
    l "「哎对了！」"
    y "「啊？」"
    "刚走了没两步，就听到梁芷柔在后面叫住我。"
    voice "audio/voice/002070.ogg"
    l "「……」"
    voice "audio/voice/002071.ogg"
    l "「算了。」"
    y "「……？」"
    "什么情况？"
    "梁芷柔欲言又止，犹豫反复了一小会儿。"
    l "「……」"
    voice "audio/voice/002072.ogg"
    l "「嗯……我想说啊……」"
    voice "audio/voice/002073.ogg"
    l "「我觉得你最好还是……再多上点心比较好。」"
    y "「呃……」"
    voice "audio/voice/002074.ogg"
    l "「我知道啊，你最近学得比较累。我也累，我明白。但是呢，越是这时候，越是得咬着牙抗过去。」"
    "梁芷柔有些担忧地看着我。"
    voice "audio/voice/002075.ogg"
    l "「所以啊，网吧还是……尽量少去点吧？」"
    y "「……！」"
    voice "audio/voice/002076.ogg"
    l "「我不是要管你啊，但是……」"
    voice "audio/voice/002077.ogg"
    l "「我觉得你还是应该……就是，你要是遇到瓶颈了我可以帮你嘛，你看你这两天都没来找过我。」"
    voice "audio/voice/002078.ogg"
    l "「这刚刚有了点进步，你要是一放弃那就全完了。」"
    voice "audio/voice/002079.ogg"
    l "「啊，好不好？」"
    y "「我……」"
    voice "audio/voice/082007.ogg"
    f "「哎，芷柔，走啊，去吃饭？」"
    "这时候，突然有其他的女生过来招呼梁芷柔。"
    voice "audio/voice/002080.ogg"
    l "「啊……」"
    voice "audio/voice/002081.ogg"
    l "「好，这就去。」"
    y "「……」"
    voice "audio/voice/082008.ogg"
    f "「啊……难道说，我当电灯泡啦？」"
    voice "audio/voice/002082.ogg"
    l "「才没有！」"
    voice "audio/voice/082009.ogg"
    f "「哎哟，那可真是对不起啊……」"
    voice "audio/voice/002083.ogg"
    l "「走走走，去吃饭！八卦不死你……」"
    "梁芷柔似乎有些羞涩，一把抓住那个女生，连拉带拽地把对方拖走了。"
    "路过我旁边的时候，她稍稍停顿了一下。"
    voice "audio/voice/002084.ogg"
    l "「……你再想想吧。」"
    "然后，两个女生头也不回地离开了教室。"
    with fade
    y "「……」"
    "呆在原地目送她们离开教室，我的内心五味杂陈。"
    "——梁芷柔一直在关心着我的情况。"
    "她会为我有所进步感到高兴，也会在我松懈的时候过来劝告。"
    "她是真的对我有所期待……期待我可以考出一个比现在更好的成绩。"
    "然而，当你所期望的，我所能达到的，我真正想要做到的……这一切全都错位的时候。"
    "也就是，对于现在的我来说……"
    "那无疑是一种煎熬。"
    with vpunch
    voice "audio/voice/092011.ogg"
    g "「哟！」"
    "一条胳膊突然搭在了我的肩膀上。转头一看，是班上关系不错的一个男生。"
    voice "audio/voice/092012.ogg"
    g "「怎么，被甩啦？」"
    y "「……」"
    voice "audio/voice/092013.ogg"
    g "「正常！别伤心啦，她嘛！情理之中，呵呵。」"
    y "「……」"
    y "「呵呵你妹。」"
    "有气无力地回了他一句，我用双手抓住这货搭在我身上的胳膊，用力地将他拧得鬼哭狼嚎。"
    scene bg black #黑屏
    with fade

#开学后一个月左右。
#9月中下旬。

    scene bg b01 #教室
    with fade
    "高三生活的头一个月，在各种忙碌之中匆匆而过。"
    "学校开始下狠手了。它就像是一头喜爱玩弄猎物的怪兽，不断地折磨着我们的身体与心灵。"
    "毫无节制可言的拖堂，越来越长的留校自习，永无止境的考试和作业。"
    "每当觉得自己快要适应当前的节奏时，老师们总会将压力再提高一个档次，始终让人疲于奔命。"
    scene bg b04 #滨河路|夏
    with fade
    "离开学校的时候，太阳早已经落山了。"
    "慢慢踱着步子，沿着河边向家走去。"
    "所谓「拖着疲惫的步伐」就是指的这种情况了吧……"
    "不过，其实身体上也没有累到那么严重的程度，更主要的还是精神压力。"
    scene bg black #黑屏
    with fade
    voice "audio/voice/012006.ogg"
    z "「……听说你最近老是缠着梁芷柔？」"
    voice "audio/voice/012007.ogg"
    z "「你哪有那么多问题可问的啊？嗯？还找不到我，我现在是忙，以前呢？前面这两年，你说你主动找过我几次啊？」"
    voice "audio/voice/012008.ogg"
    z "「我可都听说了啊！你小子，对梁芷柔有意思？」"
    voice "audio/voice/012009.ogg"
    z "「哼，我还不知道是没谱的事吗？但这事闹出影响来，你让梁芷柔怎么想啊？我告诉你啊，你给我躲她远点，听见没有！？」"
    voice "audio/voice/012010.ogg"
    z "「其实呢，我也不是批评你，毕竟你最近考得确实不错，看得出来你确实在努力，但是啊……」"
    voice "audio/voice/012011.ogg"
    z "「你得明白，咱们这儿谁掉了链子都不怕，梁芷柔不行。这种事不怕一万，就怕万一……」"
    "……"
    "…………"
    scene bg b04 #滨河路|夏
    with fade
    "老师们的消息渠道似乎有点滞后，直到现在这事都快没人提了，才后知后觉地过来「预防」。"
    "不过，相比起同学之间的传言，这种来自老师的压力无疑更有实质。"
    "虽然，其实我这段时间已经没怎么再麻烦过梁芷柔了……"
    scene bg b05 #湿地公园|夏
    with fade
    y "「……」"
    "夏末秋初，残暑的余温还没有消散，黄河的岸边还满是盎然的绿色，仿佛时间未曾流逝。"
    "之前，自卑如我，只敢远远地仰望着梁芷柔的背影，不敢有丝毫逾越。"
    "如今，我看到了自己的渺小，只能远远地仰望着梁芷柔的背影，无法逾越分毫。"
    "一切……似乎都没有改变。我只是画了个圆，最终回到了起点。"
    y "「……」"
    "没办法吧……"
    "一个月的时间，已经足以让人抚平冲动了。"
    "那么……"
    scene bg black #黑屏
    with fade
    "我该认命吗？"
    "……"
    "…………"
    voice "audio/voice/002085.ogg"
    l "「……咦？」"
    scene bg b05 #湿地公园|夏
    with fade
    "意外的，耳边传来了一个熟悉的声音。"
    voice "audio/voice/002086.ogg"
    l "「叶雨潇？」"
    y "「啊？」"
    voice "audio/voice/002087.ogg"
    l "「真的是你啊？」"
    y "「啊……嗯。」"
    "还真是……说曹操，曹操到。"
    "昏黄的灯光下，梁芷柔独自一人从我迎面的方向走了过来。"
    voice "audio/voice/002088.ogg"
    l "「你怎么这么慢啊，我都往回走了你才过来。」"
    voice "audio/voice/002089.ogg"
    l "「这是又跑哪儿玩去了？」"
    y "「没有没有！」"
    "……下意识地先否认了。"
    "由于反应太快，这一嗓子吼得有点大，几乎是嚷出来的。"
    "随后自己才意识到……我确实没有出去玩啊！"
    "这种意识脱节的情况是怎么回事……"
    y "「……我被郑老师摁住了，训了我半天才放出来。」"
    voice "audio/voice/002090.ogg"
    l "「嗯？真的吗？你又干什么坏事啦？」"
    y "「真没有，老郑这人你比我熟，捕风捉影的功夫登峰造极啊！」"
    "大概是因为我的反应比较奇特，后面的解释看起来根本就是在掩饰，梁芷柔是一脸的不相信。"
    "这可真是冤死了……但又怨不得别人。"
    "说起来……我这是怎么了？累傻了吗？"
    scene bg black #黑屏
    with fade
    "不。"
    "应该是……其实我打心底，不想让她失望吧。"
    "只是，弄巧成拙。"
    "……总是这样。"
#【恢复】
    voice "audio/voice/002091.ogg"
    l "「嗯……好吧。真不是去玩了？」"
    y "「你看我这样子，玩得动才怪……我现在就想睡觉。」"
    y "「倒是你啊，怎么跑这边来了，是去书店了？」"
    voice "audio/voice/002092.ogg"
    l "「对呀，新的书到了。」"
    "梁芷柔抬了抬手。"
    "这时我才注意到，她手中还拎着一个包裹。"
    y "「这次买的是什么啊？嗯，黄冈题库？」"
    voice "audio/voice/002093.ogg"
    l "「哈哈……才不是呢！你再猜猜？」"
    "她扬了扬手里的包裹，并不大，看起来也并不如何沉重。"
    "的确，按照她的做题量，这要是练习题的话大概不够塞牙缝的吧……"
    y "「感觉像是课外读物，不过具体的就没法猜了吧。」"
    voice "audio/voice/002094.ogg"
    l "「嗯，也算对吧。」"
    voice "audio/voice/002095.ogg"
    l "「咳咳，这次呢，买的是《了不起的盖茨比》、《东方快车谋杀案》，还有《枪炮、病菌与钢铁》。」"
    y "「……的英文版吧？」"
    "我已经从这八竿子打不到一起去的分类中察觉到了真相。"
    voice "audio/voice/002096.ogg"
    l "「嘻嘻。」"
    y "「我的妈呀，学霸的世界真可怕。」"
    "一边说，我一边朝她伸出手。"
    voice "audio/voice/002097.ogg"
    l "「哎？」"
    y "「给我，我帮你拿吧。」"
    voice "audio/voice/002098.ogg"
    l "「干什么啊？」"
    y "「我送你一段。」"
    voice "audio/voice/002099.ogg"
    l "「不用啦，又不沉。」"
    y "「顺便嘛。」"
    voice "audio/voice/002100.ogg"
    l "「真不用，别管我了，赶快回家休息吧，你看你都累成这样了……」"
    y "「还是送送你吧，反正也不差这一点了。」"
    voice "audio/voice/002101.ogg"
    l "「嗯……」"
    voice "audio/voice/002102.ogg"
    l "「呵，好吧！」"
    "梁芷柔略微想了一下，点了点头，将包裹递给我，并肩朝桥的方向走去。"
    scene bg b04 #滨河路|夏
    with fade
    voice "audio/voice/002103.ogg"
    l "「……还真巧。」"
    y "「嗯？」"
    voice "audio/voice/002104.ogg"
    l "「嗯，没什么。就是觉得啊，好久没和你一起走这里了。」"
    y "「啊……」"
    voice "audio/voice/002105.ogg"
    l "「对吧？每天放学那么晚，我还得最后一个走，连去个书店的时间都没有！」"
    voice "audio/voice/002106.ogg"
    l "「你看你也给累成这样了……这阵子学校简直是疯了啊！一天到晚的加码，还让不让人活了！」"
    y "「……哈，哈哈。」"
    "听着梁芷柔的抱怨，我忍不住笑了起来。"
    "果然，她还是她。"
    voice "audio/voice/002107.ogg"
    l "「你笑什么啊？」"
    y "「没想到你也会这样喊累啊？」"
    voice "audio/voice/002108.ogg"
    l "「我也是人，当然会累啊！」"
    voice "audio/voice/002109.ogg"
    l "「而且我不是一直在跟你说嘛，学习需要讲效率，可你看咱们现在，呵呵。」"
    y "「这也是没办法吧，又不是所有人都能有那个脑子。」"
    voice "audio/voice/002110.ogg"
    l "「那也不能全指望题海战术往里填鸭啊……」"
    voice "audio/voice/002111.ogg"
    l "「杜甫说得好，『苟能制侵陵，岂在多杀伤』。」"
    voice "audio/voice/002112.ogg"
    l "「哎……」"
    y "「好啦好啦，班长大人您真是辛苦了。」"
    y "「哎，其实我突然想起来，你没必要非得这么晚跑过来一趟啊？跟我说一声我明天早上给你带过去不就行了吗？」"
    voice "audio/voice/002113.ogg"
    l "「我这不是没找到你吗？」"
    "啊……的确，刚下课就被老师抓走了，当时梁芷柔大概在忙别的事，没注意。"
    y "「这个，这是意外吧……你可以给我打电话或者发个消息啊？」"
    voice "audio/voice/002114.ogg"
    l "「嗯……还是算了吧。」"
    voice "audio/voice/002115.ogg"
    l "「毕竟今天过来取，待会儿就可以看了。而且……」"
    voice "audio/voice/002116.ogg"
    l "「都这么累。」"
    y "「啊……」"
    y "「不，其实没事的，举手之劳。像这种事，以后随时找我就行。」"
    voice "audio/voice/002117.ogg"
    l "「可是……」"
    y "「而且啊，天这么黑还一个人走，你也不怕出点什么事，心可真够大的。」"
    voice "audio/voice/002118.ogg"
    l "「这能出什么事啊？」"
    y "「怎么不会啊，你看看周围，黑漆漆的。」"
    "老城区的基础设施相对陈旧，尽管路是重修了，但路灯似乎还沿用着之前的设备，有些已经坏掉了。"
    "别说梁芷柔了，就算是住在这里十几年的我，走的时候也要多加小心才行。"
    "虽不见得会遇到什么坏人，但万一没看清路，磕了碰了也是很麻烦的。"
    voice "audio/voice/002119.ogg"
    l "「哎……好啦，我知道啦！」"
    voice "audio/voice/002120.ogg"
    l "「嘻嘻。」"
    y "「还笑。你啊，还是趁现在开始多长点心眼吧。」"
    y "「这也就是在咱们县，等以后换个大城市，还指不定怎么样呢！」"
    voice "audio/voice/002121.ogg"
    l "「啊……」"
    voice "audio/voice/002122.ogg"
    l "「……也是。」"
    l "「……」"
    voice "audio/voice/002123.ogg"
    l "「是啊……」"
    "梁芷柔轻轻摇了摇头，苦笑了起来。"
    y "「呃……」"
    "不对不对，我才反应过来。"
    "今天脑子简直是一团浆糊，感觉自己现在就是一个傻逼，来回来去说错话。"
    "但是……"
    l "「……」"
    "面对着神色有些黯淡的梁芷柔，我却不知该怎么办，才能将那种疏离感挥散。"
    "……"
    "…………"
    scene bg b06 #商业街
    with fade
    voice "audio/voice/002124.ogg"
    l "「啊，到了。」"
    y "「嗯。」"
    "熬过了沉默的后半段，我将梁芷柔送到南岸的公交站旁。"
    voice "audio/voice/002125.ogg"
    l "「那……今天谢谢你了。」"
    y "「客气什么。」"
    voice "audio/voice/002126.ogg"
    l "「呵呵……你也早点回去吧。」"
    y "「反正都过来了，把你送上车呗。」"
    voice "audio/voice/002127.ogg"
    l "「不用啦，真不用。你看这边这么热闹，出不了事的。」"
    voice "audio/voice/002128.ogg"
    l "「你也赶快回去好好休息吧。」"
    "这边紧挨着商业区，虽然进入夜晚，但总算还有不少人流，也有一些人在车站等车。"
    y "「嗯？真的没问题啦？」"
    voice "audio/voice/002129.ogg"
    l "「真的啦！」"
    y "「嗯，那你路上小心点。」"
    voice "audio/voice/002130.ogg"
    l "「好～」"
    y "「到家给我发个短信。」"
    voice "audio/voice/002131.ogg"
    l "「啊……？」"
    voice "audio/voice/002132.ogg"
    l "「嗯……好。」"
    y "「那，我走啦。」"
    voice "audio/voice/002133.ogg"
    l "「嗯～」"
    "梁芷柔微笑着轻轻朝我挥了挥手。"
    "我也扬了一下手，当做告别的招呼，随即快步离开了。"
    scene bg black #黑屏
    with fade
    "……"
    scene bg b04 #滨河路|夏
    with fade
    "…………"
    scene bg b05 #湿地公园|夏
    with fade
    "………………"
    y "「……」"
    y "「……呼！呼！」"
    "我一路奔跑，直到回到了家的附近才慢下来。"
    "仿佛在逃跑似的。"
    y "「……呼！……」"
    "……"
    "…………"
    scene bg black #黑屏
    with fade
    "我知道。"
    "我知道我自己的弱小。"
    "我知道前路漫漫，遍布荆棘。"
    "我知道我所谓的「目标」几乎是痴人说梦。"
    "只是……"
#【居中】
    "只是，我也知道，我其实……还是不甘心。"
    scene bg b04 #滨河路|夏
    with fade
    "……"
#【手机短信铃声】

    "掏出手机，看到了梁芷柔发来的短信。"
    voice "audio/voice/002134.ogg"
    l "「『安全到达！^_^』」"
    y "「……」"
    "看完短信，抬头向天。"
#【天空】
    "虽然因为身处城市，有光源污染而使得许多星星无法看清……"
    "但即使如此，最为明亮的星星，也依然坚强地闪耀出自己的光芒。"
#【黑屏|居中】
    "是的，其实我知道该做什么，该怎么做。"
#【恢复】
    "我曾以那颗星为指引，向前迈出了第一步，只是……如今却再一次踌躇不前。"
    bird "「啾——」"
    "夜色之中，不远处传来了鸟的鸣叫。"
    "候鸟的迁徙已经开始了一段时间，如斑头雁这样迁徙时间较早的鸟，甚至已经走得七七八八的了。"
    "只有少数，因为各种各样的问题耽搁下来。"
    "如果它们不能及时跟上的话，那么或许就再也走不了了……"
    "到了那时，即使强行起飞，也只会迷失方向，成为迷鸟，根本无法到达自己想要前往的目的地。"
    "而我……又会如何呢？"
    "……"
    "…………"
    scene bg black #黑屏
    with fade
























    return
