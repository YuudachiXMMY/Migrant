# 游戏的脚本可置于此文件中。

# # Gallery
# Music
init python:
    mr = MusicRoom(fadeout=1.0, loop=True, shuffle=False)

    mr.add("audio/music/themepiano.ogg", always_unlocked=True)
    mr.add("audio/music/theme.ogg", always_unlocked=True)
    mr.add("audio/music/bgm01.ogg", always_unlocked=True)
    mr.add("audio/music/bgm02.ogg", always_unlocked=True)
    mr.add("audio/music/bgm03.ogg", always_unlocked=True)
    mr.add("audio/music/bgm04.ogg", always_unlocked=True)
    mr.add("audio/music/bgm05.ogg", always_unlocked=True)
    mr.add("audio/music/bgm06.ogg", always_unlocked=True)
    mr.add("audio/music/bgm07.ogg", always_unlocked=True)
    mr.add("audio/music/bgm08.ogg", always_unlocked=True)
    mr.add("audio/music/bgm09.ogg", always_unlocked=True)
    mr.add("audio/music/bgm10.ogg", always_unlocked=True)
    mr.add("audio/music/bgm11.ogg", always_unlocked=True)
    mr.add("audio/music/bgm12.ogg", always_unlocked=True)
    mr.add("audio/music/bgm13.ogg", always_unlocked=True)
    # mr.add("audio/music/bgm14.ogg", always_unlocked=True)
    mr.add("audio/music/bgm15.ogg", always_unlocked=True)

# 游戏通关次数
# 在"我抬起头....义无反顾地飞去。" "那是一只候鸟。" 后+1
default persistent.game_clear_times = 0

# CG Flags
default persistent.cg_1_1_flag = False
default persistent.cg_1_2_flag = False
default persistent.cg_1_3_flag = False
default persistent.cg_1_4_flag = False

default persistent.cg_2_1_flag = False
default persistent.cg_2_2_flag = False
default persistent.cg_2_3_flag = False
default persistent.cg_2_4_flag = False

default persistent.cg_3_1_flag = False
default persistent.cg_3_2_flag = False
default persistent.cg_3_3_flag = False
default persistent.cg_3_4_flag = False


# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

default chapter = "00"

define y = Character("叶雨潇", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define l = Character("梁芷柔", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define loli = Character("小梁芷柔", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define yl = Character("两个人", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define z = Character("老师", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define a = Character("同学A", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define b = Character("同学B", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define ab = Character("同学A&B", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
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
define j = Character("李金凡", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define h = Character("工作人员", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define i = Character("保安", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define bird2 = Character("海鸟", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define m = Character("广播", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define narrator = Character(None, ctc_pause="ctc_pause_icon", ctc="ctc_icon")
define nvl_narrator = Character(None, kind=nvl, ctc_pause="ctc_pause_icon", ctc="ctc_icon")

# 转场特效
define fadehold = Fade(0.5, 2.0, 0.5)
define fadeslow = Fade(0.5, 1.0, 3.0)

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

    "青空如洗，白云如练。"
    "空气中卷着些许潮湿的味道。"
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
    stop sound fadeout 2.0

    pause 1.5

    show textblack
    with dissolve

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

    play sound "audio/sound/ambientnoise01.ogg" fadein 3.5 loop #河边环境噪音
    scene cg12a2 #叶雨潇打电话CG-1|手机|CG12a2
    with fade
    "掏出手机，打开通讯录。"

    scene cg12a3 #叶雨潇打电话CG-1|手机|通讯录|CG12a3
    with dissolve
    "在许许多多的人名中，翻出其中看起来似乎再普通不过的一条。"
    scene cg12a4 #叶雨潇打电话CG-1|手机|通讯录|梁芷柔|CG12a4
    with dissolve
    "「梁芷柔」"
    "我凝视着这个名字，片刻。"
    "然后——"

    stop sound fadeout 1.0

#序幕

    scene bg black #黑屏
    with fade
    pause 1.5
    show text open07 at truecenter
    with dissolve
    pause 3.0
    scene bg black #黑屏
    with fade
    pause 1.5

#两年前。
#高二期末考试后。
#7月28日。

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～

    $ persistent.cg_2_2_flag = True

    scene bg b01 #教室
    with dissolve
    pause 1.5

    "盛夏。"
    "一个热到无以复加的日子。"
    "教室仿佛蒸笼一样，汗水糊满了每个人的身体，出奇地憋闷。"
    "房间内用来降温的就只有一架20年前产的老旧电风扇，现在正半死不活地挂在墙边，喘出萎靡不振的怪声。"
    "听上去好像在说「快睡吧～快睡吧～」一样。"
    "……{w=1.0}……{w=1.0}……………………………………………………"
    "也确实有很多学生抵挡不住这份诱惑倒下了，整个教室都充斥着颓废的气息。"
    "……不过，也有例外的。"
    "比如讲台上的班主任，现在就亢奋得很，正在拼命地朝下面喷着口水。"
    show charaz h01 #老师立绘|夏季|普通
    with dissolve
    voice "audio/voice/010001.ogg"
    z "「……今年！啊，今年咱们县的考生，有42个人考上一本！有93个人考上了二本！」"
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
    "我半坐半躺地倚在座位上，努力寻找一个能让自己舒服一些的姿势。不过无论如何，眼前这幅光景依然让人感到煎熬。"
    "这种正确的废话到底要说多少遍啊……"
    "放眼教室，呼呼大睡者有之，窃窃私语者有之，左顾右盼者有之，不屑一顾者也有之。"
    "……就是没有认真听班主任讲话的。"
    y "「……」"

    stop music fadeout 3.0

    $ persistent.cg_1_2_flag = True

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音

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

    stop sound fadeout 3.0
    play music "audio/music/bgm11.ogg" fadein 1.5 #风轻云淡

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
    "加码、{w}加码、{w}再加码。"
    "……{p}…………"
    stop music fadeout 4.0

    play sound "audio/sound/ambientnoise10.ogg" fadein 2.0 loop #安静学习环境噪音
    scene bg b01 #教室
    with fadehold
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
    stop sound fadeout 3.0
    "……{p}…………"
    scene bg b01 #教室
    with vpunch
    y "「——！！」"
    play sound "audio/sound/effect23.ogg" noloop
    "突然之间猛地醒了过来。"
    "由于是突然惊醒，一时间心脏狂跳个不停。"
    "啊……好难受。"
    stop sound fadeout 3.0

    "虽然难受，不过总算是稍微清醒了一些。"
    play sound "audio/sound/ambientnoise10.ogg" fadein 2.0 loop #安静学习环境噪音
    y "「（妈的居然一边想着『不要睡！』一边就睡着了。）」"
    y "「（真是……）」"
    "我抹去一把汗水，使劲揉了揉几近迷离的眼睛。"
    "太难熬了……真的有人能在这种环境里坚持下去么？"
    "抱着这种疑问，我下意识地环顾四周。"
    y "「……？」"
    stop sound fadeout 3.0

    ##需追加BGM：梁芷柔印象曲
    play music "audio/music/bgm09.ogg" fadein 1.5 #梁芷柔印象曲

    $ persistent.cg_1_1_flag = True

    scene cg01a #梁芷柔听讲CG-1|标准|CG01a
    with fade
    "忽然发现，在一排排东倒西歪的身影中，还真就有一个另类存在。"
    "一位哪怕是在如此煎熬的环境之中，仍在尽力维持着端正坐姿的少女。"
    "她的座位在我的右前方。由于那一列被讲台向后挤了半个位置，与我的这一列并不平行，不过只隔了一条过道，距离并不算远。"
    "从我的位置，可以清楚地看得到她脸颊和脖子上渗出的细小汗珠。"
    y "「（哇……亏她能撑得住啊。）」"
    y "「（真不愧是学校里出了名的好学生。）」"
    scene cg01a #梁芷柔听讲CG-1|标准|CG01a
    with dissolve
    nvl show
    nvl_narrator "——梁芷柔。"
    nvl_narrator "在这所学校之中……{w=1.0}不，在整个县城的教育界，{w=1.0}都可以称得上是一位大名鼎鼎的人物。"
    nvl_narrator "至于理由，非常简单——{w}学习好。"
    nvl_narrator "不是一般的好，据说已经是可以随心所欲地挑选大学的水平。"
    nvl clear
    nvl_narrator "如之前所述的那样，我们这个县的教育水平一直不怎么样，偶尔哪年有一两个可能考上重点大学的，都会被老师当成大熊猫一样供起来。"
    nvl_narrator "不过往昔的那些学霸，和我眼前的这一位相比，就未免显得逊色了。那些我们只闻其名，连做梦都不敢去想的国内顶尖的高等学府，对她而言却如探囊取物一般。"
    nvl_narrator "可想而知，她在我们这里有着怎样的待遇。"
    nvl clear
    nvl hide
    with dissolve

    y "「（这就是人比人，气死人吧。）」"
    y "「……」"
    y "「（不过啊……）」"
    "就事论事，对于梁芷柔，我是服气的。"
    "有果必有因。她能取得这样的成绩，付出过不知道多少努力。"
    "就比如，哪怕是这样的大热天里，她对自己的要求也并不放松，光是这一份自律，就令人自愧弗如了。"
    y "「……啧。」"
    "反正……{w=1.0}我大概是做不到的。"

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
    y "「（这么一想，她也确实不用费那么多心思去处人际关系，反正以后也不见得还能有多少交际……）」"
    y "「……」"
    y "「（大城市啊……）」"

    scene bg b02 #城区
    with fade
    "想到这里，我望向窗外，看着这个我生活了十多年的小县城。"
    "要论对家乡的感情，当然也是十分深厚的，不过内心之中，始终还是存有一种对大城市的向往。"
    "省城距离这里不过几十公里，虽然交通不算方便，偶尔也会过去一趟。"
    "相对于老家这里，省城无疑要繁华得多，而想必东部沿海的那些大城市又会比省城更上一层楼。"
    "对于我们这些穷乡僻壤出身的人来说，那些都市总是很有吸引力的。"
    y "「（不过…{cps=2}…唉{/cps}。）」"
    "只是痴人说梦罢了。"
    "我的成绩，在班上其实还算是不错。虽然只是偶尔才会努一把力，三天打鱼两天晒网的事情没少做，但考试什么的姑且也还排在前面几名。"
    "不过，这种在教育落后的偏远县城中学里还算不错的成绩，放到高考之中，只能勉强摸到二本线。"
    "在省内就读的话，说不定还能照顾一点，但想要往外省考，那就得找不知第几流的学校去了。"

    scene cg01a #梁芷柔听讲CG-1|标准|CG01a
    with fade
    "想到这里，忍不住又把视线转回梁芷柔的身上。"
    "要说起来，和这样优秀的美丽少女同班两年，最开始的时候也不是没有过一些想法。"
    "估计和我抱有相同念头的男生应该不少……{w}只不过，在残酷的现实面前，大家全都深感压力、自惭形秽，最后全都选择了成为呆在优美天鹅身边的沉默的癞蛤蟆。"
    "以我自己为例，除了一些没有营养的打招呼，或者上传下达老师的指令以外，和梁芷柔之间，哪怕连一次值得记忆的对话都没有。"
    "……唉，{w=1.0}一把辛酸泪啊。"
    y "「……」"

    stop music fadeout 3.0
    "就在这时，我忽然发现了一丝异样。"
    y "「（……咦？）」"
    y "「（那、那是……）」"

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷

    scene cg01c #梁芷柔听讲CG-3|衣服半透|CG01c
    with fade
    "我发现，梁芷柔其实也没少出汗。"
    "也是，就算是意志上能够坚持得住，身体终究不是铁打的。"
    "总之，她也出了一身汗，而我们学校的校服又很薄，被充沛的汗水浸过之后……"
    with hpunch
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
    y "「（不对…{cps=2}…完{/cps}蛋了！）」"

    scene bg b00b #烈日
    with hpunch
    "我慌慌张张地挪开了视线，装作不经意的样子朝窗外的天空望去。"
    y "「……」"
    "盯着她的身体看了半天，结果被她抓了个现行……"
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
    with hpunch
    "慌忙把头再次扭向窗外。"
    y "「……」"
    "……这就很尴尬了。"
    "在剩下的时间里，我再也不敢把目光投向梁芷柔那一侧，就这么一直煎熬着等到了下课。"

    stop music fadeout 2.5
    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/effect06.ogg" noloop
    scene bg b01 #教室
    with fade
    "铃声终于响起。"
    "班主任大概是也看出学生的状态不怎么样，并没有拖堂，只是意犹未尽地总结了两句就离开了。"
    play music "audio/music/bgm11.ogg" fadein 1.5 #风轻云淡
    "他前脚刚出门，后面教室里就迸发出一片凄惨的哀嚎。"
    "不少之前阵亡的同学连爬起来的力气都没有了，只是瘫在座位上呻吟。"
    y "「……呼。」"
    "长长地吐出一口气。"
    "要说我的情况也好不到哪去……靠着窗户这一侧，一上午几乎要被晒成人干了。"
    "还好，接下来有两个半小时的午休，虽然不见得能完全恢复，但对于现在的我来说无疑是弥足珍贵的喘息之机。"
    "吃饭去吧…{cps=2}…不{/cps}，先去打水，水壶里装的水在之前就已经喝光了。"
    play sound "audio/sound/effect09.ogg" noloop
    with vpunch
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
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
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
    "真是难堪…{cps=2}…算{/cps}了，事已至此，也没什么办法了，毕竟这种事根本拿不上台面来，哪怕是想要道歉都无从开口。"
    "还是赶快打水去吧……"
    stop music fadeout 0.5
    "就在我这么想的时候——"

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
    "…{cps=2}…………{/cps}…"
    "似乎是因为抢道结果挤在了一起，又互不相让，最后就顶起牛来了。"
    y "「要吵到外面吵去啊……」"
    "我小声嘀咕着。"
    "真是……这俩人明明是为了快点出门，结果却是停留在原地争吵，彻彻底底的本末倒置。"
    "虽然也不是不能理解…{cps=2}…大{/cps}热天的，脾气会暴躁一点，而且最近压力也大，有点冲动也正常。"
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
    with dissolve
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

    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音

    "一般来说男生想要一个人劝这种架不太容易，搞不好就会被夹在中间挨两头打，又或者有意无意地拉了偏架，起到了反效果。"
    "不过，劝架的人是女生的话，一般来说只要不是打疯了，都会有所收敛。"
    "尤其是梁芷柔这样在班上素有威望，各方面都镇得住场子的，处理这种事情是驾轻就熟了。"
    "只能说，不愧是班长。"

    with fade
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
    "难怪，经历了一个难熬的上午以后，还要调解这种狗屁倒灶的破事，换谁都会觉得心力交瘁吧。"
    y "「……」"
    "虽然有点想称赞、鼓励她一下，不过想想刚才我给她留下的不良印象……算了吧，别碍她眼才是真的。"
    y "「（走走走，打水去打水去，快要渴死了！）」"
    "还是走吧——就在我这么想着的时候，刚才打架的两个人之一，靠近我这一侧的家伙，用并不小的声音嘟囔了一句。"

    stop sound fadeout 3.0

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
    "噼里啪啦！！！"
    play sound "audio/sound/effect08.ogg" noloop
    with vpunch
    "稀里哗啦！！！"
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
    play sound "audio/sound/effect35.ogg" noloop
    "呼——"
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
    "这一甩的范围，恰好将梁芷柔的位置包含进去。"
    y "「小心！」"
    voice "audio/voice/000009.ogg"
    l "「呀！」"
    "眼看着她因为出乎意料而不及躲避，我顾不上多想，上前一把抓住梁芷柔的胳膊，用力将她向后拽了一步。"
    play sound "audio/sound/effect35.ogg" noloop
    hide chara
    with dissolve
    play sound "audio/sound/effect07.ogg" noloop
    with hpunch
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
    play sound "audio/sound/effect35.ogg" noloop
    "椅子划出了一道夸张的弧线，飞向了——"
    stop music fadeout 1.0
    "我们。"

    scene bg b01 #教室
    with dissolve
    nvl show
    nvl clear
    nvl_narrator "正所谓飞来横祸。"
    nvl_narrator "如果这只铁椅继续沿着现有的轨迹飞行，肯定会砸中我们两个。"
    nvl_narrator "如果被砸中的话，一定会很疼。"
    nvl_narrator "破相都是小事了，说不定脑瓜会直接开瓢，砸出个三长两短来也不是没有可能。"
    nvl clear
    nvl_narrator "——接住它？"
    nvl_narrator "不可能。"
    nvl_narrator "这玩意又沉又快，徒手去接无异于螳臂当车，挡不住的。"
    nvl clear
    nvl_narrator "——那，躲开？"
    nvl_narrator "也许可以吧？"
    nvl_narrator "至少我自己应该是能够躲得开的。{w}但是……"
    nvl clear
    nvl hide
    with dissolve

    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
    "我突然感觉到，手中攥着的那只柔软的手臂，因为害怕而紧绷了起来。"
    "余光能够看到，那张秀美的脸庞正在因为紧张而变得煞白，整个人吓得连叫都叫不出来了，只能下意识地闭上眼睛。"
    scene bg black #黑屏
    with fade
    "是的。"
    "还有这样的一个女生，正站在我的身边。"
    "——身体，下意识地做出了动作。"
    with hpunch
    y "「——小心！！！」"
    play sound "audio/sound/effect02.ogg" noloop
    scene bg black #黑屏
    with fade
    pause 5.0

    $ persistent.cg_2_1_flag = True

    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音

    scene cg02a #梁芷柔被压倒CG-1|标准|视角拉近|CG02a
    with fadeslow
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
    with vpunch
    y "「噫……！」"

    scene bg black #黑屏
    with fade
    "头脑一阵发昏。"
    "原本因为甫遭重击，还没有立即体现出来的疼痛感，全都伴随着这个动作回到了我的身上。"

    scene cg02b #梁芷柔被压倒CG-2|半起身|视角拉远|CG02b
    with fade
    nvl show
    nvl clear
    nvl_narrator "在最后的那一刻，我把梁芷柔拉到了身后，自己挡在了前面。"
    nvl_narrator "椅子的一条铁腿结实地命中了我的额头，也刮破了侧脸。"
    nvl_narrator "现在我整个右脸都热辣辣的，血顺着脑门流下，几乎糊住了眼睛。"
    nvl_narrator "不过，梁芷柔也因此得以毫发无损。"
    nvl clear

    scene bg b01 #教室
    with fade
    nvl hide
    y "「……」"
    y "「怎么样，满意了吧？」"
    "我扭过头，凶神恶煞地瞪着那两个始作俑者。"
    a "「……」"
    b "「……」"
    stop sound fadeout 3.0

    "不知是被我吓到了，还是也在心生悔意，总之这一眼的效果相当的好，那两个人都默不作声地低下了头。"
    "看起来，战争结束了。"
    "交战双方损害轻微，无辜百姓伤亡惨重。"
    "真是岂有此理……"
    "这个时候，一只温软的小手拉住了我的左臂。"
    voice "audio/voice/000011.ogg"
    l "「你……你还好吗？」"

    play music "audio/music/bgm09.ogg" fadein 1.5 #梁芷柔印象曲

    scene cg02b1 #梁芷柔被压倒CG-1|标准|担心|CG02b1
    with fade
    "低下头，与梁芷柔的目光相交。"
    "方才还满是惊慌的神色，此时已经变成了关切。"
    y "「嗯……」"
    y "「还好……」"
    "说出了有些违心的话……其实头还是挺晕的。"
    "不过按照英雄救美的模板来说，这个时候别管自己伤成什么德行，也要不死模式全力全开，边摆POSE边说出「我没事」来才对。"
    y "「……应该问题不大吧，待会去医务室看看。」"
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
    "你看，模板起效了。"
    "套路虽然烂俗，但既成经典，自然有其道理。"
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
    stop music fadeout 2.5

    ## TODO: 演出效果Check #############

    # Note:
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

    # Note:
    #  1. 此处我用了黑屏结尾，如果需要可以直接删除此段以直接
    #     进入下方的scene bg b01；
    #  2. 还是请无比保留 pause 0.5以维持演出效果（？）或者
    #     也可以直接pause，表示等待点击然后继续进行游戏
    scene bg black
    with fade
    play sound "audio/sound/effect12.ogg" noloop

    pause 0.5

    ## End TODO: 结束演出效果Check的更改 #########

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
    "……{p}…………"

    scene bg indistinct #白色朦胧
    with fade

    "……{p}…………"

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
    who "「大夫，您看他这个情况……严重吗？」"
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
    with fadehold
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
    y "「唔……{w=1.0}唔…………」"
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
    y "「我…{cps=2}…被{/cps}椅子砸了一下？」"
    scene bg indistinct #白色朦胧
    with fade
    y "「嘶……」"
    #医生
    voice "audio/voice/040017.ogg"
    who "「怎么啦？」"
    scene bg indistinct #白色朦胧
    with fade
    y "「头…{cps=2}…头{/cps}疼……」"
    #医生
    voice "audio/voice/040018.ogg"
    who "「没事，这是正常的！放松一点，没事的，啊！」"
    #医生
    voice "audio/voice/040019.ogg"
    who "「别想事情，放松！要是觉得眼睛睁开难受就别睁了，啊！」"
    #医生
    voice "audio/voice/040020.ogg"
    who "「……好了，送CT。」"
    "……{p}…………"

    stop sound fadeout 1.5

    scene bg black #黑屏
    with fade
    "脑袋昏昏沉沉的。"
    "只感觉周围乱糟糟的，似乎有很多人来来往往，时不时说些什么，甚至偶尔还会问我几句话。"
    "似乎是下意识地做出了回答……但是被问了什么，又答了什么，我自己一点概念都没有。"
    "再往后就是被人搬来搬去，掰手掰脚，也不知是在做什么检查。"
    "中途也曾尝试着想要让自己清醒一点，然而头很疼，疼到连思考的力气都没有，最后只能闭着眼睛任人摆布了。"
    "然后，渐渐的，再一次陷入昏睡。"
    "……{p}…………"

    scene bg indistinct #白色朦胧
    with fade
    "……{p}…………"
    #梁芷柔
    voice "audio/voice/000022.ogg"
    who "「……郑老师……」"
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
    "……{p}…………"

    scene bg indistinct #白色朦胧
    with fade
    "……{p}…………"
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
    "……{p}…………"

    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/ambientnoise03.ogg" fadein 1.5 loop #傍晚环境噪音

    $ persistent.cg_3_2_flag = True

    scene bg b03 #病房
    with fadeslow
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
    "毕竟不是在拍电影，挨了那么重的一下子，晕过去才是比较正常的结果。"
    y "「（不过，这样一来……）」"
    with hpunch
    "要完蛋。"
    "要完蛋。{fast}根本不知道该怎么和爸妈交代。"
    "虽然受伤不是我的错，但不管怎么说都会让父母担惊受怕。"
    "老爸那里应该还好说，但是老妈肯定会先紧张得要死，然后等我没事了之后又大发雷霆咆哮不止吧。"
    y "「（……估计耳朵又要被磨出茧子来了。）」"
    y "「……」"
    "说起来，现在是什么时候了？"
    "病房里没有钟表，看不出具体的时间，只能凭着窗外的光亮判断出天还没有黑。"
    "一个下午不省人事……这大概是我有生以来受的最严重的伤了吧？"
    "啊……如果只是几个小时倒也还好了，就怕像以前听到过的某些故事里说的那样，一次昏迷，醒来之后却发现已经过了三年什么的……"
    y "「……」"
    "不会有那种事的吧。"
    "不过是一个椅子罢了，又不是在电话亭边上被卡车给撞了。"
    y "「嗯…{cps=2}……咦{/cps}！？」"
    "当我试图将头转向另一侧的时候，看到了一个意想不到的人。"

    $ persistent.cg_3_1_flag = True

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
    stop sound fadeout 3.0
    "抱着疑惑，我再次望向梁芷柔。"

    play music "audio/music/bgm09.ogg" fadein 2.5 #梁芷柔印象曲

    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fade
    "梁芷柔正在专心致志地看着书，并没有注意到我的视线。"
    "这份注意力真是相当厉害了。"
    "从小到大，「全神贯注」、「专心致志」的口号连听带喊了不知多少遍，但实话实说，我从未想到过一个人居然真的可以如此心无旁骛。"
    "说起来，虽然以前在学校的时候也经常能够见到她认真学习的样子，但是现在和那些时候的感觉完全不同。"
    "或许是因为之前我还在昏睡，她身处独自一人的环境吧？此时此刻的梁芷柔，全部的精力都集中在了自己手中的书本上。"
    "除了偶尔翻页以外，几乎没有别的动作。甚至于在很多时候，如果不是她还在眨眼，瞳孔也在随着视线微微移动，我都会以为眼前的少女只是一个人偶。"
    "一个精致无比，而又动人心魄的人偶。"
    "……{p}…………"

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
    "……{p}…………"
    stop music fadeout 1.5

    scene bg black #黑屏
    with fade
    play sound "audio/sound/effect04.ogg" noloop
    "忽然，一股突如其来的夏风，毫无征兆地挑开了窗帘。"

    scene cg03b #梁芷柔探病CG-2|起风|CG03b
    with fade
    voice "audio/voice/000027.ogg"
    l "「啊……」"
    play music "audio/music/bgm09.ogg" fadein 2.5 #梁芷柔印象曲
    "一瞬间，仿佛整个空间都被惊醒了。"
    "夕阳的余晖瞬间铺满了病房的每一个角落，数不清的细碎花瓣从窗外闯入，在半空四散纷飞。"
    "少女的一头青丝随着风的节奏翩然起舞，她伸手轻轻压住一侧，试图拢住散乱的发丝，原本如同象牙般白皙的胳膊被日照抹过，镀上了一层金黄色的光晕，显得华丽而圣洁。"
    y "「……」"

    scene bg black #黑屏
    with fade
    "就好像有一根羽毛在心脏最敏感的地方轻轻划过一般。"
    "在内心的最深处，某些曾经被自己深深掩盖起来的东西，似乎，在这一刻，有了些许松动的迹象。"
    "……{p}…………"
    stop music fadeout 1.5
    voice "audio/voice/000028.ogg"
    l "「……咦？」"
    play sound "audio/sound/ambientnoise03.ogg" fadein 1.5 loop #傍晚环境噪音
    scene cg03c #梁芷柔探病CG-3|对视|CG03c
    with fade
    y "「哎？……呃。」"
    "回过神来，发现……不知什么时候，梁芷柔的目光已经转移到我这边来了。"
    "于是，四目相对。"
    y "「……」"
    l "「……」"
    "以及，相顾无言。"

    scene cg03c1 #梁芷柔探病CG-3|对视|惊讶|CG03c1
    with dissolve
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
    "……{p}…………"

    play music "audio/music/bgm11.ogg" fadein 1.5 #风轻云淡
    scene bg b03 #病房
    with fade
    voice "audio/voice/040021.ogg"
    az "「……大致就是这样了，有一点脑震荡，问题不算大。」"
    voice "audio/voice/040022.ogg"
    az "「可能之后一段时间会有些头疼、恶心之类的症状，一般过两天就能恢复，保险起见这两天还是留院观察一下比较好……」"
    "……{p}…………"
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
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/000034.ogg"
    l "「没事就好！」"
    with hpunch
    "你怎么看上去比我还要多松了一口气啊！"
    "说到底，梁芷柔为什么会在这里，我直到现在都还没搞明白呢。"
    "不只是我在疑惑，医生似乎也受到了误导。"
    stop music fadeout 3.0

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
    with dissolve
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
    show chara la01b #梁芷柔立绘|夏季校服|普通|侧面|近
    with dissolve
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
    with vpunch
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
    stop music fadeout 1.0
    voice "audio/voice/000051.ogg"
    l "「嘻嘻。」"

    play sound "audio/sound/ambientnoise03.ogg" fadein 1.5 loop #傍晚环境噪音

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
    show chara a13a #梁芷柔立绘|夏季校服|疑惑1
    with dissolve
    voice "audio/voice/000062.ogg"
    l "「哎，那个……」"
    y "「嗯？」"
    show chara a11 #梁芷柔立绘|夏季校服|微笑
    with dissolve
    voice "audio/voice/000063.ogg"
    l "「啊，算了，没事。」"
    voice "audio/voice/000064.ogg"
    l "「你还是好好休息吧，医生说了不让你多说话。」"
    y "「……哦。」"
    "梁芷柔欲言又止。"
    "似乎是想和我多聊两句，但又怕影响到我休息的样子。"
    "……{p}…………"

    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    with fadeslow
    "接下来的时间里，梁芷柔又拿起了复习资料去看题，而我则躺在床上发呆。"
    "屋里再一次安静下来。"
    "窗外传来微风轻拂枝叶的「簌簌」的声响，不时有鸟雀飞过，发出一两声鸣叫。"
    stop sound fadeout 3.0

    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    "何等安详的午后……之前中午那一段兵荒马乱的经历，就好像是虚幻的一般，已经完全没有感觉了。"
    "不过，有一些东西，似乎变得不同了。"
    y "「……」"
    l "「……」"
    y "「……」"
    scene cg03c2 #梁芷柔探病CG-3|对视|普通|CG03c2
    with dissolve
    voice "audio/voice/000065.ogg"
    l "「嗯，怎么了？」"
    "或许是因为才刚开始看书，还没那么投入，梁芷柔很快就注意到了我的目光，随即投来了询问的眼神。"
    y "「啊？啊，没什么。」"
    y "「就是觉得，感觉你好像和以前不太一样。」"
    voice "audio/voice/000066.ogg"
    l "「嗯……？」"
    scene cg03c3 #梁芷柔探病CG-3|对视|微笑|CG03c3
    with dissolve
    voice "audio/voice/000067.ogg"
    l "「因为，从同学变成了姐姐？」"
    y "「……喂。」"
    voice "audio/voice/000068.ogg"
    l "「呵呵。」"
    "梁芷柔有些狡黠地笑笑。"
    "……{p}…………"

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
    l "「♩～～～～」"
    y "「……」"
    voice "audio/voice/001002.ogg"
    l "「♪～～～～」"
    y "「……喂……」"
    voice "audio/voice/001003.ogg"
    l "「♫～～～～」"
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
    l "「♬～～～～」"
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

    play music "audio/music/bgm10.ogg" fadein 1.5 #梁芷柔～allegro vivace ver.

    scene bg b03a #病房|白天
    with fade
    "我向病房门口望去。"
    "……隐约能听到外面的大人们聊天的声音。"
    "此时此刻，我这间病房堪称门庭若市。"
    "除了我的父母以外，梁芷柔、她的父母、我们班的班主任老师，以及学校的一位年级主任也联袂而至。"
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
    play sound "audio/sound/effect12.ogg" noloop
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
    "话说回来，这样的梁芷柔才反而是我印象中的那个…{cps=2}…以{/cps}至于身体都形成了条件反射。"
    y "「好好好、好好好，知道啦知道啦。」"
    y "「反正暑假作业老师也不会认真看……」"
    voice "audio/voice/001036.ogg"
    l "「叶！雨！潇！」"
    y "「……」"
    y "「……{fast}我错了。」"
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
    with hpunch
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
    show chara la02 #梁芷柔立绘|夏季校服|皱眉|近
    with dissolve
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
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
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
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
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
    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
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
    show memories #回忆滤镜
    with fade
    "……{p}…………"
    y "「就是觉得，感觉你好像和以前不太一样。」"
    voice "audio/voice/001061.ogg"
    l "「嗯……？」"
    scene cg03c3 #梁芷柔探病CG-3|对视|微笑|CG03c3
    show memories #回忆滤镜
    with dissolve
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

    play music "audio/music/bgm10.ogg" fadein 1.5 #梁芷柔～allegro vivace ver.

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
    show chara la08b #梁芷柔立绘|夏季校服|担心2|近
    with dissolve
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
    y "「喂。」"
    y "「……」"
    "虽然梁芷柔这话说得有些语焉不详…{cps=2}…不{/cps}过也正常，我们之间毕竟还远没有亲密到可以无话不谈。"
    "然而，我也能感受得到，她是真心实意地想要以她的方式来报答……或者说是帮助我。"
    "再纠结的话，就显得是我矫情了。"
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
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
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
    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t02 #转场 病房
    with fade
    pause

#两天后。
#7月31日。

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音

    $ persistent.cg_2_4_flag = True

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
    with hpunch
    y "「呼啊！」"
    "钻进快餐店的一瞬间，便感到一股冷气扑面而来。"
    "本已热到打蔫的我，在骤然变化的温差的刺激下，微微打了个哆嗦。"

    play music "audio/music/bgm12.ogg" fadein 1.5 #快马加鞭

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

    with fade
    voice "audio/voice/151001.ogg"
    kfc "「您好，欢迎光临！」"
    y "「一杯可乐，谢谢。」"
    voice "audio/voice/151002.ogg"
    kfc "「好的，请稍等。」"

    scene bg black #黑屏
    with fade
    "……{p}…………"

    scene bg b07 #快餐店
    with fade

    "点了一杯饮料，我随便找了个位子坐下。"
    y "「……」"
    y "「（真他妈贵啊……）」"
    "这么小一杯可乐就敢要6块钱……"
    "做好了耐心等待的准备，我一边叼着吸管嘬水喝，一边开始东张西望。"
    y "「……」"
    y "「装修得倒是都差不多。」"
    "实际上，老家县城里的这家店我也是第一次进来。而在此之前，他家我只在去省城的时候吃过那么两次。"
    "因为是连锁店的缘故，装潢的设计风格完全是一个模子印出来的，谈不上有多高档，但却是个新鲜玩意儿。"

    scene bg b02 #城区
    with fade
    "——相对于这座城市来说。"
    "这个开遍全国的快餐连锁品牌，直到去年才在我们县开了一家门店，而他家的那些竞争对手，至今依然对我们这种穷乡僻壤不屑一顾。"

    scene bg b07 #快餐店
    with fade
    y "「……」"
    "也难怪。毕竟我只点了它一杯饮料，都已经在嫌贵了……"
    "超出了我们本地的消费水平，再加上东西也不见得多好吃，多数人也就是尝个鲜而已，除了最开始那一段日子火爆了一阵以外，回头客是寥寥无几。"
    "就像现在，中午的饭点还没有完全过去，但这里却空空荡荡的，服务员一个个也都无精打采，看不出什么干劲。"
    "这样也好，待会儿我们就算在这里呆上一下午，也不会碍别人的事，应该也不会有谁过来轰我们走。"
    y "「嗯……」"
    stop music fadeout 1.5

    "我用力地吸了一口饮料，开始思索接下来找点什么事来消磨时光……"
    "要不要先做两道暑假作业的题什么的？"
    #梁芷柔
    voice "audio/voice/001090.ogg"
    who "「哟！」"

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    "忽然，肩膀被轻轻拍了一下。"
    with hpunch
    y "「噗啊啊！」"
    "毫无心理准备的情况下，我被吓了一跳，喝到一半的水呛了进去。"
    y "「咳！咳咳！」"
    #梁芷柔
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
    "……话说你有超能力啊？{w}难道还会读心不成？"

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
    "见我恢复得还不错，梁芷柔也终于放下心来。"
    voice "audio/voice/001103.ogg"
    l "「那么……我们开始吧？」"
    y "「……」"
    y "「哎，好。」"

    play sound "audio/sound/ambientnoise06.ogg" fadein 2.5 loop #快餐店环境噪音

    $ persistent.cg_1_3_flag  = True

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
    y "「唉…{cps=2}…干{/cps}嘛非要考什么大学呢……」"
    "我唉声叹气，小声碎碎念道了一句。"
    "不过也就是说说而已。{w}真要是不让考了，估计我也是不答应的。"
    scene cg04a #梁芷柔快餐店学习CG-1|就坐|CG04a
    with dissolve
    voice "audio/voice/001107.ogg"
    l "「咳咳。」"
    voice "audio/voice/001108.ogg"
    l "「好啦，干正事干正事。」"
    "梁芷柔从自己的书包里拿出了…{cps=2}…一{/cps}大摞习题集。"
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
    y "「你…{cps=2}…拿{/cps}这么多套题过来是要干什么啊？」"
    voice "audio/voice/001112.ogg"
    l "「做呀？」"
    y "「不不不，我的意思是，这么多…{cps=2}…你{/cps}多久能做完？」"
    "这厚度…{cps=2}…给{/cps}我的话，别说暑假了，就算是在学校全负荷状态的时候，半个月能啃完其中的一小部分就不错了。"
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
    l "「但是你现在的情况嘛……嗯，我问你，暑假作业你做……嗯，你看过了么？」"
    y "「呃……」"
    y "「大概翻了翻，还没仔细看。」"
    scene cg04a3 #梁芷柔快餐店学习CG-1|就坐|无奈|CG04a3
    with dissolve
    voice "audio/voice/001119.ogg"
    l "「唉……」"
    "一种「果然如此」和「怒其不争」混合在一起的表情。"
    "呜…{cps=2}…我{/cps}好有负罪感啊。"
    voice "audio/voice/001120.ogg"
    l "「所以呢，你现在连基础的做题量都没有满足，跟你说这个太早了。」"
    voice "audio/voice/001121.ogg"
    l "「这两天你还是先把作业做完吧，然后再说别的。」"
    y "「好吧，全听你的。」"
    "我认命似的点了点头，开始和万恶的暑假作业进行斗争。"

    scene bg black #黑屏
    with fade
    "……{p}…………"

    stop sound fadeout 1.5
    play music "audio/music/bgm10.ogg" fadein 1.5 #梁芷柔～allegro vivace ver.

    $ persistent.cg_1_4_flag = True

    scene bg b07 #快餐店
    with fade
    "时间过去了20分钟。"
    y "「……」"
    y "「…………」"
    y "「………………呜。」"
    "精力…{cps=2}…开{/cps}始涣散了。"
    "说起来，一直以来，对于暑假作业这种东西，我虽然不至于出现那种拖到最后一天才决死冲锋的场面，但也全都是在死线临近的压迫下方才动工。"
    "在暑假刚开始就做作业这种事，有生以来还真是头一遭。"
    "感觉…{cps=2}…不{/cps}习惯啊。"
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
    y "「（这种水平…{cps=2}…我{/cps}真能赶得上吗？）」"

    scene bg black #黑屏
    with fade
    "……{p}…………"

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
    "算了，求助吧。反正本来就是来向她讨教的，不丢人…{cps=2}…应{/cps}该吧。"
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
    y "「呃，这个…{cps=2}…那{/cps}个…{cps=2}…{/cps}」"
    voice "audio/voice/001137.ogg"
    l "「……」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/001138.ogg"
    l "「唉，算啦算啦，也不可能一下子就给你扳过来。」"
    show chara lc01b #梁芷柔立绘|夏季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/001139.ogg"
    l "「正好我这边也告一段落了，先中场休息一会儿吧。」"
    y "「……是。」"

    stop music fadeout 1.5

    scene bg black #黑屏
    with fade
    "……{p}…………"

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
    y "「所以说啊…{cps=2}…啧{/cps}。」"
    voice "audio/voice/001142.ogg"
    l "「嗯……我倒是觉得还可以吧，至少目前来说。」"
    voice "audio/voice/001143.ogg"
    l "「一个人保持专注的时间是有限的，尤其是你的心思不在这上面的时候。所以你刚才这样也算是正常。」"
    voice "audio/voice/001144.ogg"
    l "「说到底还是你对学习没兴趣，注意力全都被别的东西吸引走了。」"
    l "「……」"
    voice "audio/voice/001145.ogg"
    l "「嗯……我能问问你吗？你刚才做题的时候，其实是在想什么？」"
    y "「想什么…{cps=2}…这{/cps}个……」"
    voice "audio/voice/001146.ogg"
    l "「你肯定是在走神，所以我想知道是什么干扰的你。」"
    voice "audio/voice/001147.ogg"
    l "「……嗯……是我打扰你了？」"
    "梁芷柔随口瞎猜了一句。"
    "反问的语气，显然连她自己也没当真。"
    "不过……"

    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    show memories #回忆滤镜
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
    y "「那当然不是。」"
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
    "对我们这些凡夫俗子来说，区别无非在于那一百之后的数字是二三十、四五十，还是六七十罢了。"
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

    play music "audio/music/bgm12.ogg" fadein 1.5 #快马加鞭

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
    "……{p}…………"
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
    "……{p}…………"
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

    scene cg04b1 #梁芷柔快餐店学习CG-2|讲题|CG04b1
    nvl show
    nvl_narrator "我学习的目的究竟是什么？"
    nvl_narrator "一本线、『小目标』？"
    nvl_narrator "是…{cps=2}…但{/cps}也不是。"
    nvl clear
    nvl_narrator "不论我敢不敢承认，但不得不说，我会鼓起学习的勇气，先决条件还得说是因为…{cps=2}…她{/cps}。"
    nvl_narrator "然而…{cps=2}……{/cps}…"
    nvl_narrator "通过这两天短暂但频繁的接触，我才发现，自己与她的差距，远比我想象中的要大。"
    nvl_narrator "不要说什么缩短距离的可能性了，我甚至连她已经走到了哪一步都无法理解。"
    nvl clear
    nvl_narrator "尽管我们现在坐在一起，挨得很近……"
    nvl_narrator "但彼此之间却盘桓着一条令人绝望的鸿沟。"
    nvl_narrator "咫尺，{w}天涯。"
    nvl clear

    scene bg black #黑屏
    with fade
    nvl hide
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
    y "「要是去年这时候的话，可能我还有点信心，但是现在…{cps=2}…就{/cps}剩一年了啊。」"
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
    "……{p}…………"

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
    y "「哦…{cps=2}…{/cps}{nw}"
    with vpunch
    y "「哦……{fast}啥！？」"
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
    "…{cps=2}…好{/cps}吧，我就知道。"
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
    nvl show
    nvl_narrator "我家的小区在黄河北岸边上，紧挨着旧城区西部的边缘，往西走一点就是新城区。"
    nvl_narrator "这两年，那边新盖了不少楼，据说还要划出一块工业园区，也不知道有没有人来。"
    nvl_narrator "这些新建筑有的已经完工了，但还有不少是半成品或者索性烂尾，总的来说，在多数人眼里，那边就是一片大工地，没事不愿意往过走。"
    nvl_narrator "当然，随着旧城区改造的同步实施，老城这边也被拆得不亦乐乎，变成了乌鸦笑猪黑的局面。"
    nvl clear
    scene bg b06 #商业街
    with fade
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    nvl hide
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
    "……{p}…………"
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
    y "「黄河吧？又不止我们家门口这一段…{cps=2}…哎{/cps}呀无所谓，总之是个面子工程。」"
    voice "audio/voice/001252.ogg"
    l "「嗯～」"
    "梁芷柔不置可否，把视线投向了左侧的黄河。"
    voice "audio/voice/001253.ogg"
    l "「说起来，这公园也修起来了啊？」"
    stop music fadeout 3.0
    y "「是啊……」"

    play music "audio/music/bgm11.ogg" fadein 1.5 #风轻云淡

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

    stop music fadeout 3.0
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
    "……{p}…………"

    play music "audio/music/bgm12.ogg" fadein 1.5 #快马加鞭
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
    "……{p}…………"
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
    y "「嗯…{cps=2}…嗯{/cps}？」"
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
    "只是…{cps=2}…说{/cps}实话，我也是真没有想到她居然会选择这些书。"
    "倒不是说这些书有什么奇怪的，或者说恰恰相反，是太大众化了，无论谁看都不稀奇。"
    "之前还以为她会看一些更加小众的作品呢……这种凭空瞎猜出来的高冷设定，显然与真实情况相去甚远。"
    show charad sg01 #书店店员立绘|普通|远
    with dissolve
    voice "audio/voice/021012.ogg"
    d "「哎！！」"
    play sound "audio/sound/effect12.ogg" noloop
    with vpunch
    "噗通！"
    play music "audio/music/bgm12.ogg" fadein 1.5 #快马加鞭
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
    y "「看来…{cps=2}…挺{/cps}沉的？」"
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
    l "「都说了不是男朋友！同学！是同学！！」"
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
    l "「搬得动……」"
    y "「得了啊，你别费那个劲了，还是我来吧。」"
    y "「走。」"
    with vpunch
    "我颠了颠怀里的包裹，换了个舒服一点的姿势，不由分说拔腿就走。"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    stop music fadeout 3.0
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
    "……{p}…………"

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
    y "「哦，那儿啊…{cps=2}…那{/cps}不也得有将近一公里呢吗？」"
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
    l "「这……嗯，好吧。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001310.ogg"
    l "「……谢谢啊！」"
    y "「呵，客气。」"

    scene bg black #黑屏
    with fade
    "……{p}…………"

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
    play music "audio/music/bgm09.ogg" fadein 1.5 #梁芷柔～theme ver.
    "西北这一带，由于经济条件所限，物价还是相对低廉的。"
    "无论是我们老家这样的县、镇，还是省城那种相对较大的城市，基本的日常开销都算不上很多，以至于我熟视无睹，忽略了这一点。"
    "然而，梁芷柔的未来…{cps=2}…却{/cps}不在这里。"
    "她将来的所在，一定是东部的某一个大城市。"
    "我对那种城市的生活完全没有概念，但想来花销不会很少，至少……相对于老家这边的家庭收入来说，会占用相当可观的一部分。"

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

    scene bg black #黑屏
    with fade
    "这种浑浑噩噩的状态，以前或许还没有什么实感，但在有了对比之后，差距一下子就清晰起来了。"
    "梁芷柔已经在规划那么遥远的事情了……但，我却对自己的未来一直很含糊，在此之前甚至都没有认真想过大学的事，更不要说做什么准备了。"
    "虽然不是不想做出改变，甚至已经冲动着迈出了第一步，但接下来该怎么走，还根本没有概念。"
    stop music fadeout 3.0
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

    play music "audio/music/bgm10.ogg" fadein 1.5 #梁芷柔～allegro vivace ver.
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/001324.ogg"
    l "「想什么呢？那么认真，跟你说话都不理我。」"
    y "「啊，没…什么……」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/001325.ogg"
    l "「没什么是什么啊！」"
    y "「哈哈…{cps=2}…我{/cps}在想啊，姐姐你真是懂事啊，不愧是我姐姐！」"
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
    "……{p}…………"

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
    "……{p}…………"
    "我目送梁芷柔乘坐的公交远去。"
    y "「嗯，回去吧。」"

    stop music fadeout 1.5
    scene bg black #黑屏
    with fade
    "……{p}…………"

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
    scene bg b05 #湿地公园|夏
    nvl show
    nvl_narrator "此前，我从未纠结过这种问题。"
    nvl_narrator "上学、高考，考上一个能给家里交代得过去的学校，找一个比较容易就业的专业，四年后找份足够糊口的工作，然后开始熬年头，随后在父母的催促中相亲、恋爱、结婚、生子……"
    nvl_narrator "我曾以为我的人生大抵如此。"
    nvl_narrator "或许平凡，但却轻松。"
    nvl clear

    show bg b00 #天空
    with dissolve
    play music "audio/music/bgm13.ogg" fadein 1.5 #With Memories
    nvl_narrator "勇攀高峰什么的听上去很不错，但所需的付出也不是一星半点。"
    nvl_narrator "「憧憬与梁芷柔同样的未来」？"
    nvl_narrator "在最初的冲动逐渐平复之后，我反而更加清楚地认识到了现实。"
    nvl clear
    nvl_narrator "姑且先不管她会不会对我这种单方面的想法有所回应，单只说想要勉强跟随她的步伐——去考一个和她同城的、档次还可以的大学——就已经需要我拿出前所未有的干劲去拼上一整年的命了。"
    nvl_narrator "这不是随随便便就能做到的事。"
    nvl_narrator "虽然我总说「以前曾经努力过」，但自己其实很清楚，即便是曾经的那种努力，也早已满足不了现在的需求了，何况此时连那时候的程度都还差得远。"
    nvl_narrator "而即便真的做到了，最后能否「称心如意」，也还未可知晓。"
    nvl clear
    scene bg black #黑屏
    with fade
    nvl hide
    "——那么，我该为这个虚无缥缈的想法押上所有筹码吗？"
    #回忆模式
    scene bg b03 #病房
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    show memories #回忆滤镜
    with fade
    voice "audio/voice/001042.ogg"
    l "「你说你，挺聪明的一个人，怎么就老是……哎。」"
    scene bg b07 #快餐店
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    show memories #回忆滤镜
    with fade
    voice "audio/voice/001175.ogg"
    l "「嘻嘻……可别这么说啊！你不相信自己，还不相信我啊？我都说你有天赋了，相信我，没错的。」"
    scene bg b07 #快餐店
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    show memories #回忆滤镜
    with fade
    voice "audio/voice/001207.ogg"
    l "「一本线嘛，小意思，包在姐姐身上。而且，除了这个小目标，如果你还能继续保持努力的话，最后考到百薇也不是不可能的。」"
    scene bg b06 #商业街
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    show memories #回忆滤镜
    with fade
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

    play music "audio/music/bgm11.ogg" fadein 3.0 #风轻云淡

    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with dissolve
    nvl show
    nvl_narrator "我们继续着每天的学习会。"
    nvl_narrator "之前的暑假作业只能算是开胃小菜，在如今的「正餐」面前不值一提。"
    nvl_narrator "那些梁芷柔十分轻松就能解决干净的习题，现在正如同大山一般压到了我的身上。"
    nvl_narrator "梁芷柔之前已经把这里面的困难题目都做过一遍了。她会从中筛选出难度适合的题目给我，再根据我做的情况进行讲解。"
    nvl_narrator "对她而言，解决我的问题可谓游刃有余，而且，随着她对我的知识结构的进一步了解，题目的针对性也在日渐增强。"
    nvl_narrator "虽然时日尚短，我却已经能明显地感受到自己在进步，若是能持之以恒，必然能够脱胎换骨。"
    nvl clear
    scene bg black #黑屏
    with dissolve
    nvl hide
    "只是…{cps=2}……{/cps}…{w}我依然没能从踌躇之中挣扎出来。"
    scene cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with fade
    nvl show
    nvl_narrator "现在的我，既缺乏一往无前的勇气，又不愿浅尝辄止即放弃。"
    nvl_narrator "「至少试着朝『小目标』努力一下吧！这样也不算辜负她了。」…{cps=2}…我{/cps}给自己找了这样一个借口。"
    nvl_narrator "连自己都知道是借口，这样的说辞当然毫无说服力，然而对于现在的我来说，实在也做不出什么决断。"
    nvl_narrator "这样的心态当然也影响到了现实中的状态，我的注意力变得更容易涣散了。"
    nvl_narrator "偏偏学习的压力还在加大……结果就是各种莫名其妙的失误频频出现，反过来更加影响心态，几乎要陷入恶性循环之中了。"
    nvl_narrator "不过……"
    nvl clear

    scene cg04b1 #梁芷柔快餐店学习CG-2|讲题|CG04b1
    with dissolve
    nvl hide
    voice "audio/voice/001350.ogg"
    l "「基本的东西一定要记住！」"
    voice "audio/voice/001351.ogg"
    l "「所谓『粗心』，永远只是『不会』的借口。理解还不到位就自以为会了，到用的时候自然要出错。」"
    voice "audio/voice/001352.ogg"
    l "「有不会的就要补上，不能拖。越拖就越多，时间长了补都没办法补。」"
    voice "audio/voice/001353.ogg"
    l "「听见了没有！？」"

    scene cg04b1 #梁芷柔快餐店学习CG-2|讲题|CG04b1
    nvl show
    nvl_narrator "梁芷柔却并没有因此而不耐烦。"
    nvl_narrator "倒不如说，她对此更加上心了，每次都不厌其烦地把我暴露出来的问题掰开揉碎地讲，还苦口婆心地给我传授她的各种学习心得。"
    nvl_narrator "可以感觉得到她是真心希望我的成绩能有所提高的……就不知她这样做是出于「姐姐」的关爱，还是真的认为我是个可造之材了。"
    nvl_narrator "无论如何，都可以称得上是仁至义尽，也让我愈发感到羞愧难当。"
    nvl clear

    scene bg black #黑屏
    with fade
    nvl hide
    stop music fadeout 3.0
    "不能……再这样颓废下去了，必须要有所改变。"
    "哪怕微不足道，哪怕最终于事无补。"
    "但至少，我不能让她白费苦心。"
    "……{p}…………"

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
    "……{p}…………"
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
    "……{p}…………"
    scene bg b04 #滨河路|夏
    with fade
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001363.ogg"
    l "「♪～～」"
    voice "audio/voice/001364.ogg"
    l "「♫～～」"
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
    l "「♬～～」"
    y "「……」"
    "正如她所说的那样，经过了一段时间的调整，这两天我总算是稍稍有所起色。"
    "我在强迫自己集中精神……效果还算是马马虎虎，尽管没办法达到自己真正主动的那种效率，但最起码不再是前面那种浑浑噩噩的状态了。"
    "保持这种状态并不是容易的事，不过说到底我也是没什么更好的办法了，只能先这样子把这个暑假硬扛过去——没准扛着扛着就习惯了呢？"
    "至少……在发现自己如此微小的进步，都能被她注意到之后，我感到自己的干劲又提起来了一点。"
    scene bg black #黑屏
    with fade
    "……{p}…………"
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
    y "「嗯……怎么说呢，感觉像是到了一个别的城市？」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001380.ogg"
    l "「啊，这倒也是。」"
    y "「对吧，别说是咱们这儿了，就算是在省城，也就是西区那种新开发的地段，这种风格的楼才比较多吧？」"
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
    "梁芷柔说得言之凿凿的，似乎对这方面颇有了解。"
    "不过，想想也是，铁定要去外地上学的人，自然会对这些事情多关注一些。"
    y "「见多识广啊姐姐……哎对了，这么一说我记得去年暑假你好像参加了一个外地的比赛来着？」"
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
    y "「哦，这个呀…{cps=2}…上{/cps}小学以前吧，{w}有一年冬天跟家里去首都旅过一次游。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/001388.ogg"
    l "「喔……」"
    y "「不过说实在的，没什么印象了，就记得被我爸妈带着去广场看升旗，因为起得太早，走到一半我就趴在我爸怀里睡着了。」"
    y "「等到睁开眼，国旗早就已经升到顶了。那我当场就不干了呀，哇哇地哭，我妈为了哄我，给我买了根冰糖葫芦，我吃到外面的糖衣，立刻开心了，也不哭了，就在那儿专心致志地舔。」"
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
    show memories #回忆滤镜
    with fade
    pause
    scene cg03a #梁芷柔探病CG-1|看书|CG03a
    show memories #回忆滤镜
    with fade
    pause
    play sound "audio/sound/effect04.ogg" noloop
    scene cg03b #梁芷柔探病CG-2|起风|CG03b
    show memories #回忆滤镜
    with dissolve
    pause
    scene bg black #黑屏
    with fade
    y "「……」"
    y "「…………」"
    scene bg b08 #新城区|夏
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with fade
    y "「嗯……」"
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
    "心里没底。怕自己做不到，更怕做不到的话，会让自己，以及…{cps=2}…让{/cps}她失望。"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/001407.ogg"
    l "「♬～」"
    hide chara
    with dissolve
    "不知道是没注意到还是故意无视我话里的情绪，梁芷柔似乎还蛮高兴的，轻快地走到了前面。"
    y "「（可恶……）」"
    "每到这种时候，就会厌恶起自己这种犹豫不决的心态。"
    "如果一直这样下去，只会一事无成。"
    "「追赶梁芷柔」什么的就更是痴人说梦了，连宣之于口的资格都不会有。"
    stop sound fadeout 3.0
    scene bg black #黑屏
    with fade
    "到了下决定的时候了。"
    "我…{cps=2}…必{/cps}须，要改变。"

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
    "……{p}…………"
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
    "……{p}…………"

    scene cg04d #梁芷柔快餐店学习CG-4|看书|CG04d
    with fade
    play music "audio/music/bgm11.ogg" fadein 1.5 #风轻云淡
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
    "……{p}…………"
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

    "……{p}…………"

    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    scene cg04c1 #梁芷柔快餐店学习CG-3|做题|饮料|CG04c1
    with fade
    "休息过后，照例的学习时间。"
    "不过，我的心思完全放不到学习上面。"
    l "「……」"
    y "「……」"
    "果然…{cps=2}…冷{/cps}静不下来。"
    "尤其是……在梁芷柔距离我只有一桌之隔的这种情况下，我哪可能做得到心无旁骛？"
    l "「……」"
    "梁芷柔倒是在很专心地写着习题，似乎完全没有受到节日气氛的影响。"
    "说实话，最近这些日子，我没少这样偷偷地看着她…{cps=2}…看{/cps}着这样的她。"
    "她聚精会神的模样，我怎么看也看不够。"
    "然而，今天的我，却无法放平心态去欣赏眼前的光景，反倒是……"
    "总有一种想要破坏掉她这份专注的冲动。"
    y "「……」"
    "为什么会这样呢？"
    "像现在这样，只会让我更加深刻地意识到…{cps=2}…盘{/cps}桓在我们之间的，那道巨大的鸿沟。"
    "在这样的日子、这样的气氛里，做一些符合节日氛围的事才对，不是吗？"
    "尽管明知这种想法完全不对，但我还是抱着这样略带卑劣的念头，情不自禁地开口了——"
    y "「喂。」"
    voice "audio/voice/001438.ogg"
    l "「……嗯？」"
    "梁芷柔手中的笔并没有停顿，但是回答的反应…{cps=2}…感{/cps}觉慢了半拍？"
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
    "虽然她能够如此集中精神，让我感到非常佩服，但在今天这种心态下，被无视还是会有些不爽。"
    "……也让我涌出一种「一不做二不休」的念头。"
    y "「……」"
    l "「……」"
    "要不要伸手在她眼前挥一挥？"
    "不，那太粗暴了……对了！"
    "机会难得，调戏她一下又会如何呢？"
    y "「待会儿做完题，咱俩一起去玩吧？」"
    voice "audio/voice/001442.ogg"
    l "「…………嗯。」"
    "还真答应了啊……这种操作也可以？"
    "虽然实际上并没有什么用吧，不过那一瞬间的感觉还…{cps=2}…不{/cps}错？"
    "应该把刚才这一段录下来，闪瞎班上那群家伙的狗眼。"
    "我赌我会被群殴一顿。"
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
    "短暂…{cps=2}…但{/cps}却无比恐怖的沉默，让我刹那间清醒了过来。"
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
    "受到了惊吓的她，慌张…{cps=2}…甚{/cps}至是有些夸张地躲避了一下。"
    with vpunch
    play sound "audio/sound/effect14.ogg" noloop
    "——哗啦。"
    scene cg04c3 #梁芷柔快餐店学习CG-3|做题|饮料倒|CG04c3
    "然后，将放在一边的饮料杯……打翻了。"
    "……{p}…………"

    play music "audio/music/bgm12.ogg" fadein 1.5 #快马加鞭
    scene cg04a #梁芷柔快餐店学习CG-1|就坐|CG04a
    with fade
    "一阵兵荒马乱之后，总算是把桌面收拾干净了。"
    "铺在桌子上的习题集首当其冲，几乎整张卷面都被沾湿了不说，水还渗到了后面几页。"
    "虽然我们本来也不是在上面直接写答案，倒也不至于完全不能用，不过梁芷柔还是想等它完全干燥，于是晾在了一边。"
    "而这还不是最大的问题。"
    "最要命的是她今天带来的那本休息时看的闲书，也被可乐狠狠地淹了一大片。"
    "书页被可乐浸泡以后留下的痕迹…{cps=2}…看{/cps}着应该会很糟心吧。"
    y "「呼……」"
    y "「……唉。」"
    "我真是自己作死啊。"
    scene cg04a1 #梁芷柔快餐店学习CG-1|就坐|微笑|CG04a1
    with dissolve
    voice "audio/voice/001445.ogg"
    l "「呵呵……你刚才到底是怎么了，闹这么大动静。」"
    "貌似，梁芷柔直到被我吓到之前，都在专心致志地做题，对我之前说了什么是一点印象也没有，那个可怕的停顿也只是因为遇到了一个需要思考的难点而已。"
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
    "她处于暂时无题可做的状态，我则是根本不在状态，索性就再次进入了休息时间。"
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
    y "「就算你要求也没用，再多了我是真做不到啊……现在这样已经是极限了。」"
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
    l "「所以说呀～」"
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
    "无论如何，学生逛街总是和这一层无缘的。"
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
    l "「书不一样嘛。书还是得要纸质的读着舒服、有感觉。再说了，有些书也没法用手机看啊，像那些题，排版全都乱套了。」"
    y "「……好吧，不愧是你。」"
    voice "audio/voice/001484.ogg"
    l "「嘻嘻。」"
    "梁芷柔说得的确有些道理，不过归根结底……应该还是不舍得花钱吧。"
    "……{p}…………"
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
    y "「要是…{cps=2}…不{/cps}那么急的话，要不跟我一起上去？要是有货的话就直接给你拿回去了，也省得我拿着来来回回的。」"
    "我稍微犹豫了一下，还是发出了邀请。"
    "仅仅是逛个书店而已，而且目标非常明确，是为了弥补自己过错做出的赔偿，与约会之类的字眼毫不沾边。"
    "应该…{cps=2}…没{/cps}什么不可以的吧？"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/001495.ogg"
    l "「嗯……」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/001496.ogg"
    l "「……嗯，好呀。」"
    with vpunch
    y "「呼……！」"
    hide chara
    with dissolve
    "梁芷柔考虑的时间其实并不长，但是对我来说，却颇有一种度秒如年的感觉。"
    "我也不知道自己在想什么。"
    "即便可以借此在她的身边多呆上那么一小会儿的时间，也并没有什么卵用。"
    "明明对此心知肚明，却还是忍不住这样做了。"
    "或许，这是每一只待在天鹅身边的癞蛤蟆…{cps=2}…的{/cps}通病？"
    stop sound fadeout 3.0

    "……{p}…………"

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～

    $ persistent.cg_3_4_flag = True

    scene bg b10 #百货商场
    with fade
    y "「……」"
    y "「…………呼。」"
    "当我们并肩迈入书店的那一刻，我居然有种阿姆斯特朗登月时的感受。"
    "从商场门口走到书店，在距离上并没多远，对我来说却是迈出了不得了的一步。"
    "真是紧张得我连冷汗都冒出来了。"
    scene bg black #黑屏
    with fade
    "……{p}…………"
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
    "仔细想想，这几天下来，类似的事我也见了不止一次了。"
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
    "……{p}…………"
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
    "不过，也已经有点岌岌可危了。"
    with fade
    "下到一楼的时候，楼梯口正对着一个卖金银饰品的柜台。"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    l "「……」"
    y "「……这啥咧？」"
    "柜台的前面，立着一面大幅的海报，上面以扎眼的字体和特效填满了「开业酬宾」、「跳楼甩卖」、「吐血打折」、「抽奖必中」之类夸张的文字。"
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
    "不过她并没有越过柜台，而是…{cps=2}…趴{/cps}在上面看了起来。"

    $ persistent.cg_2_3_flag = True

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
    "不过，能够在商家们多维度的洗脑下坚持这么久，已经算是了不起了。"
    y "「……」"
    scene cg05a1 #梁芷柔看首饰CG-1|观看|星星眼|CG05a1
    with dissolve
    "话说回来，这样的梁芷柔倒是第一次见到，也算是大饱眼福了。"
    voice "audio/voice/001518.ogg"
    l "「嗯嗯……」"
    y "「哇……」"
    "感觉口水都快流下来了。"
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
    l "「哎不不不，不用不用不用！」"
    y "「……对对，就是这个。」"
    voice "audio/voice/001525.ogg"
    l "「你等等啊，我都说了不用啦……」"
    y "「啊？你说啥呢，人太多了我听不清楚，待会儿说。」"
    voice "audio/voice/001526.ogg"
    l "「喂！」"
    "……{p}…………"

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
    "……{p}…………"
    scene cg05c #梁芷柔看首饰CG-3|试戴|CG05c
    with fade
    "虽然一脸被我气得哭笑不得的样子，不过梁芷柔还是接过了挂坠，随即戴上，开始对着台面上的镜子看来看去。"
    "站在她的侧面，还能够看到她的嘴角有意无意地挂着一丝笑意。"
    y "「……」"
    "有句话说得好——"
    "嘴上嚷嚷着不要，但身体还是很诚实的嘛。"
    y "「啧啧，挺不错的嘛。」"
    "挂坠虽然简单，倒也大方，搭配起来的效果居然还不错。"
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
    "……{p}…………"

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
    l "「只此一次，下不为例。再这么干我可要翻脸了啊？」"
    y "「噢。」"
    scene bg black #黑屏
    with fade
    "……{p}…………"
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
    l "「♫～」"
    "她应该是真的挺喜欢这个挂坠的吧……而且，毕竟只是个小玩意，无伤大雅。"
    y "「接下来…{cps=2}…走{/cps}走走，去抽奖，看看手气怎么样。」"
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
    "而且这个抽奖的门槛本来就很低……我不禁开始担心起这个活动的可靠性来了。"
    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/001555.ogg"
    l "「啊哈哈……我觉得不至于吧，好歹也是正规的商场啊……」"
    y "「嗯…{cps=2}…也{/cps}是。」"
    y "「继续看继续看，一等奖是…{cps=2}…3{/cps}2寸液晶电视？」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/001556.ogg"
    l "「这个也不错啊。」"
    y "「嗯嗯，这倒是常见的奖品。」"
    "这个就比较正常了。"
    "不过，感觉和特等奖的价值差距有点大啊。"
    "……这样看起来，那台笔记本或许是用来当做噱头的吧，实际上是不是真能抽到都要另说吧？"
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
    "……{p}…………"
    with fade
    "这个抽奖的中奖几率是百分之百的必中，而奖品则被分成了好几十个等级，看起来更像是找个借口把长期滞销的商品清理出去的样子。"
    "虽然等候的队伍不算短，不过因为只是抽奖，兑奖还要再到旁边，队伍前进的速度倒是还算快。我俩商量了一下，还是决定试试手气。"
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
    l "「哼，真是没有男子气概！」"
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
    "……{p}…………"


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
    with hpunch
    "原来她纠结的重点其实是这里吗？"
    y "「不不不，没关系，我虽然谈不上多喜欢，但也不讨厌的。没问题！」"
    "电影题材什么的根本不是重点啊！"
    "有生以来第一次和女生一起看电影，而且对象还是她的话……哪怕是「三\[哔——\]T\[哔——\]D」我也能给你看下去啊好不好？"
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
    "……她到底有多想看这个电影啊？"
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
    "另一方面，也是觉得她…{cps=2}…是{/cps}不是压抑自己太久了呢？"
    "明明自己其实很想去逛街，明明有着非常想要看的电影，却一直如同苦行僧一样约束着自己，把精力投入到学习之中去。"
    "到底是因为什么，才会让她有了这么巨大的动力，去贯彻这种行为呢？"
    "我不知道——虽然我很想要知道。"
    "不过，现在，在这个机缘巧合的现在…{cps=2}…我{/cps}更希望，她可以开开心心地放松片刻。"
    "这一次，我可不再是像之前那样抱着拖她后腿的卑鄙念头了，而是真真正正地这么想。"
    "希望…{cps=2}…这{/cps}样的休息，可以对她有好处。"

    scene bg black #黑屏
    with fade
    "……{p}…………"
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
    "……{p}…………"
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

    $ persistent.cg_3_3_flag = True

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
    "……{p}…………"
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
    "……{p}…………"
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
    "总之…{cps=2}…尽{/cps}可能让自己把注意力集中到电影上面吧。"
    with fade
    "……{p}…………"
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
    "不过，感觉上…{cps=2}…她{/cps}应该还是在全神贯注地沉浸在电影的世界中吧。"
    "刚才的那一瞬，应该只是她下意识的举动。或许她自己都没有注意到吧……"
    "这样也好。大概，真要是注意到了反而更麻烦。"
    stop sound fadeout 3.0

    "……{p}…………"
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
    "梁芷柔突然很郑重其事地对我道谢，这让我一下子有些愣神。"
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
    "我们…{cps=2}…终{/cps}究不一样。"
    "现在的我，根本没有资格去这样问她。"
    "所以，除了这样的话以外，我还能说什么呢？"
    "……{p}…………"

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
    nvl show
    nvl_narrator "尽管这一次的暑假是有生以来最短的，却也是最充实的。"
    nvl_narrator "许许多多个有生以来的第一次，都在这个短短的假期中发生了，可以说是极大地丰富了我的人生经验。"
    show cg04b #梁芷柔快餐店学习CG-2|做题|CG04b
    with dissolve
    nvl_narrator "回过头想想，我都有点佩服自己了……亏我能坚持得下来。"
    nvl_narrator "想当年中考的时候，我也就是在最后的备战关头，才开始主动给自己加了加码。而现在明明距离高考还有将近一个学年的时间，我却已经有了当初的那种紧张感。"
    nvl clear
    show cg04b1 #梁芷柔快餐店学习CG-2|讲题|CG04b1
    with dissolve
    nvl_narrator "为我带来这种改变的，毫无疑问就是眼前这个陪了我一整个暑假的女生。"
    nvl_narrator "我们俩之间有着巨大的差距，大到足以对未来绝望。通过这半个月的交往，我越来越清晰地认清了这个现实。"
    nvl clear
    scene bg black #黑屏
    with fade
    nvl hide
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
    y "「你说，你小学的时候成绩不好。」"
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
    "一般来说，小学考试的成绩，怎么都能维持在80多分吧……好一点的学生，平均分90以上问题不大。"
    "像我，六年级各科考试成绩就从来没下过90分……"
    "平均分70出头……偏科的话，还有可能有不及格？这真的是梁芷柔能考出来的成绩吗？"
    voice "audio/voice/001644.ogg"
    l "「对……所以毕业的时候，给我分配的学校是就近的十三中。」"
    y "「哦……啥！？」"
    with vpunch
    y "「十三中！？」"
    "要说前面的爆料还能撑得住，现在这个重磅炸弹可就真的把我给惊到了。"
    "十三中……我知道那个学校，新建没几年，是县里扶贫计划的一部分。"
    "早年间，县城里原本只有两所高中、四所初中，师资力量也很有限，经常是连九年义务教育都落实不下去。"
    "前几年为了强推义务教育，政府动用扶贫基金，斥资修建了一大批规模较小，但具备基本条件的初中。"
    "十三中也是其中的一所，就在县城里，招收的主要是家住附近的条件较差……或者成绩不怎么好的学生。"
    "那一类学校……感觉上，就好像是在说「虽然你们考不上高中，不过好歹把九年义务教育给我念完了」似的，是纯粹为了完成任务而建立的学校。"
    "梁芷柔居然是在这样的学校里上的初中？"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001645.ogg"
    l "「怎么啦，很惊讶吗？」"
    y "「我还以为你是本校直升上来的呢！」"
    "我们学校里包括了完整的初中部，而县一中也是县里排名最好的学校。"
    stop sound fadeout 3.0

    show chara lc05b #梁芷柔立绘|夏季私服|苦笑2|近
    with dissolve
    voice "audio/voice/001646.ogg"
    l "「呵呵，怎么可能啦，我当时的成绩完全够不上一中的标准的。」"

    play music "audio/music/bgm13.ogg" fadein 5.0 #With Memories
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
    "……{p}…………"
    scene bg b07 #快餐店
    with fade
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve

    voice "audio/voice/001657.ogg"
    l "「当时我妈的脸色，白得跟纸一样，那样子别提有多吓人了。我爸当时也不在家，我又小，也不知道是个什么情况，还以为我妈死了，一下子就傻了，什么都没做，就知道在那儿哇哇地哭。」"
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
    stop music fadeout 3.0

    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/001668.ogg"
    l "「怎么样，是不是一个挺无聊的故事？」"
    y "「才不是。」"
    hide chara
    with dissolve
    "原来如此。"
    "我多少明白…{cps=2}…为{/cps}什么她会觉得我和她有点「像」了。"
    "因为我的成绩一直还算凑合，我爸我妈倒是没有怎么逼过我，只是……现在想想，父母其实没少投来过期待的目光，却都被我熟视无睹了而已。"
    "哪怕…{cps=2}…其{/cps}实只要自己愿意，明明可以更进一步的。"
    "如果我一直这样蹉跎下去的话，即便没有像小时候的梁芷柔那样吃个大亏，也只能是泯然众人。"
    "正所谓少壮不努力，老大徒伤悲。"
    "长歌行的这句诗，明明早已司空见惯，却在这一刻，突然让我有了无比现实的感觉。"
    "如果不是经历了这一整个暑假超越以往极限的自习，我是肯定不会真正地认识到这一点的。"
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
    "……{p}…………"

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
    "……{p}…………"
    scene bg b00a #天空|候鸟
    with fade
    bird "「啾——」"
    "抬头望天，有大雁正从半空飞过。"
    y "「燕雀……安知鸿鹄之志……吗？」"
    "这批大雁正在进行最后的准备。"
    "半个月后，它们就将启程向南迁徙，飞越艰险的青藏高原。"
    "留给它们的安逸时间，已经不多了。"
    scene bg b05 #湿地公园|夏
    with fade
    "我遥遥望向河边的湿地公园。"
    "看着那些尚在嬉戏的水鸟。"
    "看了许久。"
    stop music fadeout 1.5
    "……{p}…………"

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

    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
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
    b "「是啊，这才几天啊，感觉没开始就过去了。」"
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

    y "「……」"
    scene bg b02 #城区
    with fade
    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音
    "望向窗外，可以看到商业街那边的建筑。"
    y "「这帮家伙啊，知足吧……」"
    "他们好歹还踏踏实实地歇了半个月。"
    with vpunch
    "我可是一天都没闲着啊——！！！"
    "甚至于，这个暑假我在学习上投入的精力，比之前在校的时候还要多出一大截呢！"
    "班主任要是知道了，大概会被感动得痛哭流涕吧？"
    "我可是彻彻底底地把他放假前说的「这两个星期的假期不是给你们玩的」落实到了实处啊！"
    "估计全班……不，全年级都算上，几百口人里真正能做到这个份上的，一个巴掌就能数得过来。"
    "虽然……"
    "在动机方面，应该和老师期望的有点不一样？"
    stop sound fadeout 1.5
    "……{p}…………"

    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
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
    "女生之间似乎永远有说不完的话题，只要想聊，总可以聊得热火朝天。不过是不是真的那么亲热，就谁也说不好了。"
    "比方说，现在和她聊得正开心的一个女生，就在背地里抱怨过梁芷柔「装模作样」。"
    "梁芷柔对此应该并非一无所知，但……她似乎并不在乎。"
    "她太清楚自己的目标了，一路奋进只为到达终点，才不会因为这些破事在半途驻足。"
    y "「……唉。」"
    "……这人和人的差距啊！"
    "这样想想，她愿意顺手捎我一程，也是着实难得了。"
    "虽然如此，我这边却还有一个跟不跟得上的问题……"
    "至于我那点小心思，就更甭提了。"
    stop sound fadeout 1.5

    scene bg black #黑屏
    with fade
    "……{p}…………"

    scene bg b01 #教室
    with fade
    show charaz h03 #老师立绘|夏季|皱眉
    with dissolve
    voice "audio/voice/012001.ogg"
    z "「……去年咱们学校成绩还不错，考上一本的人数再创新高！啊，但是呢！这是大学扩招所带来的必然结果，是历史的进程！你们赶上了好时候是不假，但并不是说就不需要个人的奋斗了……」"
    show charaz h04 #老师立绘|夏季|咆哮
    with dissolve
    voice "audio/voice/012002.ogg"
    z "「……老师带过很多届高三学生了，啊，什么样的学生我没见过？须知不听老人言吃亏在眼前，你们还年轻！这个时候呢最重要的目标就是提高自己的知识水平，考出好成绩来……」"
    "新学期第一节课，照例是思想动员。"
    "时隔半月，再次见到老师，发现他似乎也休息得不怎么样，声音一如既往的嘶哑，脸上也依旧是一大片的胡茬。"
    hide charaz
    with dissolve
    "再看看身边的同学，大概还都沉浸在假期之中没回过神来，同样是一个个东倒西歪，左耳朵进右耳朵出，懒散得不成样子。"
    "除了……"

    play sound "audio/sound/ambientnoise10.ogg" fadein 1.5 loop #安静学习环境噪音
    scene cg01a #梁芷柔听讲CG-1|标准|CG01a
    with fade
    l "「……」"
    y "「（果然。）」"
    "梁芷柔还是那样，无论什么时候都保持着标准的坐姿。"
    "到底是怎么磨炼出来的啊……这么坚韧的意志。"
    y "「（说起来……）」"
    "眼前的这一幕，实在是有点似曾相识。"
    "好像半个月前的时候，也是这个样子的……"
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
    "不知是因为看到了我的窘相还是别的什么，梁芷柔露出了狡黠的笑容。"
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

    "……{p}…………"
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
    "……{p}…………"
    voice "audio/voice/002003.ogg"
    l "「……喂。」"
    y "「啊？」"
    scene bg b01 #教室
    with fade
    with fade
    "睁开眼睛，看到梁芷柔笑吟吟地站在我的座位旁边。"
    show chara a09 #梁芷柔立绘|夏季校服|坏笑
    with dissolve
    play music "audio/music/bgm09.ogg" fadein 1.5 #梁芷柔～theme ver.
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
    "但梁芷柔…{cps=2}…居{/cps}然可以一心二用到这个程度吗？这未免非人了吧！？"
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
    "如果换成一个不熟悉她的人来看——就好比半个月以前的我——那肯定是完全看不出来的。"
    "但是现在，虽然还吃不太准，不过已经能够多少有所察觉了。"
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
    "……虽然，很可能老师刚才讲的就是这些内容。"
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
    "梁芷柔似乎对我敷衍的态度颇为不满，撅起了小嘴。"
    y "「本来就是嘛，我虽然比不上您老人家，但是比起其他人，恐怕还是要好上不少的吧。」"
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
    stop music fadeout 2.5
    "我们俩安静下来以后，周围的声音就一下子显得大了起来。"
    hide chara
    with dissolve

    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音

    e "「叽叽喳喳叽叽喳喳……」"
    "不知什么时候，以我的课桌为中心，周围一圈的人都被彻底清空，连我的同桌都不知道跑哪儿去了。"
    "但是人们并没有走远，而是在稍微远一点的位置上散布成一个同心圆的形状。"
    "所有的人全都目不转睛地盯着我……和梁芷柔。"
    e "「叽叽喳喳叽叽喳喳……」"
    "交头接耳的声音此起彼伏。"
    y "「……啥情况？」"
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
    voice "audio/voice/002027.ogg"
    l "「这个……」"
    "……我俩有什么奇怪的吗？"
    "我有些疑惑地望向梁芷柔，后者也是一脸的茫然。"
    hide chara
    with dissolve
    stop sound fadeout 3.0

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    voice "audio/voice/082001.ogg"
    f "「那个……」"
    y "「嗯？」"
    "一个女生……据我所知是个超级八卦的家伙，似乎终于掩盖不了自己的好奇，壮着胆子凑到了我们的旁边。"
    voice "audio/voice/082002.ogg"
    f "「你们俩……现在是个什么关系啊？」"
    y "「……啊？」"
    "我呆了一下，有点没搞明白……她在问什么？"
    voice "audio/voice/082003.ogg"
    f "「你看，放暑假之前，咱们班不是打架了吗？」"
    voice "audio/voice/082004.ogg"
    f "「是不是因为你奋不顾身舍命相救，所以梁芷柔就……嗯？」"
    "女生挑着眉毛，一幅欲言又止的模样，不过这个暗示倒是很明白了。"
    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
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
    with hpunch
    voice "audio/voice/002030.ogg"
    yl "「——才不对！！！」"
    stop music fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    scene bg b01 #教室
    with fade
    "一阵兵荒马乱之后，班级里总算是恢复了秩序。"
    show chara a04 #梁芷柔立绘|夏季校服|无奈
    with dissolve
    voice "audio/voice/002031.ogg"
    l "「唉……」"
    y "「这帮家伙……真是……」"
    "这帮人其实也就是在瞎起哄罢了，真要说起来，怕是他们自己也不相信我和梁芷柔之间有什么。"
    "归根结底，从前的我，确实极少和梁芷柔有什么交流……前面半个月的变化对我而言是连贯的，但在隔了一个暑假未见的同学们的眼里，那就是突如其来的改变。"
    show chara a09 #梁芷柔立绘|夏季校服|坏笑
    with dissolve
    voice "audio/voice/002032.ogg"
    l "「嘻嘻，这可都怪你啊，知道吗？」"
    y "「行。人在座位坐，锅从天上来。不对，椅子从旁边飞过来。」"
    show chara a03 #梁芷柔立绘|夏季校服|生气
    with dissolve
    voice "audio/voice/002033.ogg"
    l "「呸，又胡说！是不是还想再挨一次啊？不许再乱说了啊！」"
    play audio "audio/sound/effect06.ogg" noloop
    stop sound fadeout 3.0

    show chara a06 #梁芷柔立绘|夏季校服|吃惊
    with dissolve
    voice "audio/voice/002034.ogg"
    l "「啊……」"
    "上课铃响了。"
    show chara a04 #梁芷柔立绘|夏季校服|无奈
    with dissolve
    voice "audio/voice/002035.ogg"
    l "「上课的时候不许再乱看了，知道吗！」"
    hide chara
    with dissolve
    "悄悄撂下这样一句话，梁芷柔匆匆返回了自己的座位。"
    y "「……」"
    y "「好好好。」"
    "我向着她的背影，轻声答道。"

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音
    scene bg b02 #城区
    with fade
    "就这样，开学的第一天过去了。"
    "说实话，我虽然和梁芷柔一样，极力否认了我俩之间有什么非同寻常的关系，但……其实在内心之中，还是蛮享受这种感觉的。"
    "毕竟，我和她，相比她和别的同学，的确是有了那么一点「不同」的。"
    scene bg b08 #新城区|夏
    show chara c10 #梁芷柔立绘|夏季私服|开心
    show memories #回忆滤镜
    with fade
    voice "audio/voice/002036.ogg"
    l "「♪～」"
    "甚至，仿佛有一种时间还停留在「我和她的那个暑假」之中的感觉。"
    stop sound fadeout 3.0
    scene bg black #黑屏
    with fade
    "……"
    "然而……"
    "没过多久，我就深刻地意识到了——"
    "高三，已经切切实实地，到来了。"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t01 #转场 教室
    with fade
    pause

#开学后一周左右。

    scene bg b02 #城区
    with fade
    pause
    scene bg b01 #教室
    with fade
    "一周的时间倏然而过。"
    show charaz h03 #老师立绘|夏季|皱眉
    with dissolve
    voice "audio/voice/012003.ogg"
    z "「……我看到啊，有些同学的心还没有收回来！我知道，你们暑假没放够，但是这是高三！不是其他的时候！对你们来说时间是不够用的……」"
    hide charaz
    with dissolve
    "天气依然燥热。"
    "老师依然聒噪。"
    "大多数学生依然漫不经心。"
    "然而，终究还是有一些东西，正在悄然之间发生着变化。"
    show charaz h04 #老师立绘|夏季|咆哮
    with dissolve
    voice "audio/voice/012004.ogg"
    z "「……不要瞧不起早晚自习！学校、老师、家长都在为你们创造条件，为的就是让你们能放下其他的负担，专心搞好学习……」"
    hide charaz
    with dissolve
    "首先是上课的时间和内容。"
    "上个学期我们已经学完了所有的课程，接下来不会再有新的知识点需要掌握，于是要做的就只剩下复习、复习、再复习。"
    "早自习的时间被提前到7点半，下午则是新加了两节自习。据说这还只是第一阶段，随着时间的推移，还会进一步地提早拉晚。"
    "体育课被压缩到每周一节，勉强维持了一个形式，其他与学习无关的活动更是名存实亡。"
    show charaz h04 #老师立绘|夏季|咆哮
    with dissolve
    voice "audio/voice/012005.ogg"
    z "「……现在呀你们不要去想别的，什么都别想！就是专心学习，只有这样呢才对得起你们自己，对得起你们的父母，对得起咱们一中……」"
    hide charaz
    with dissolve
    "现在的我们，每天都是同一个流程——听老师串讲，发卷子、测试，然后背一筐作业回家。"
    "……{p}…………"
    with fade
    play sound "audio/sound/effect06.ogg" noloop
    "上午的课程结束了。"
    play music "audio/music/bgm03.ogg" fadein 1.5 #秋～绯月～
    y "「……呼。」"
    with hpunch
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
    "这种时候…{cps=2}…还{/cps}是别给她添麻烦了吧。"
    show chara a13b #梁芷柔立绘|夏季校服|疑惑2
    with dissolve
    voice "audio/voice/002038.ogg"
    l "「……嗯？」"
    y "「啊……」"
    "梁芷柔伸完懒腰，将头转向窗户…{cps=2}…也{/cps}就是我这一侧，恰好看到了我一脸欲言又止的模样。"
    show chara a13a #梁芷柔立绘|夏季校服|疑惑1
    with dissolve
    voice "audio/voice/002039.ogg"
    l "「怎么啦？」"
    y "「呃，没什么，没事。」"
    show chara a09 #梁芷柔立绘|夏季校服|坏笑
    with dissolve
    voice "audio/voice/002040.ogg"
    l "「嗯？呵……说吧，又哪不明白了？」"
    "虽然我不想打扰她了，不过梁芷柔早已看穿了我的想法，反倒自己主动问了过来。"
    y "「没事，我自己看吧。」"
    show chara la03 #梁芷柔立绘|夏季校服|生气|近
    with dissolve
    voice "audio/voice/002041.ogg"
    l "「少废话，赶紧的！」"
    y "「呃。」"
    "话说到这份上，再犹豫就矫情了。"
    y "「这道题。」"
    show chara la01b #梁芷柔立绘|夏季校服|普通|侧面|近
    with dissolve
    voice "audio/voice/002042.ogg"
    l "「我看看……」"
    voice "audio/voice/002043.ogg"
    l "「已知抛物线C，y方等于4x的焦点为F，过点K负1，0的直线I与C相交于AB两点，点A关于x轴的对称点为D……第一证明点F在直线BD上，第二设向量AB等于9分之8，求……」"
    voice "audio/voice/002044.ogg"
    l "「嗯……具体是哪不明白？」"
    y "「哦，是这样的……」"
    "……{p}…………"
    with fade
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/002045.ogg"
    l "「这样就明白了？」"
    y "「明白了。」"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/002046.ogg"
    l "「还有别的问题吗？」"
    y "「暂时没有了，多谢班长大人仗义出手，拨冗为在下指点迷津。」"
    "我后退一步，半屈着膝，装模作样地向梁芷柔抱了个拳。"
    show chara la06 #梁芷柔立绘|夏季校服|吃惊|近
    with dissolve
    pause 0.1
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/002047.ogg"
    l "「……」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/002048.ogg"
    l "「嘻嘻！」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/002049.ogg"
    l "「知道就好，本班长的时间是很宝贵滴～」"
    y "「是是是，打扰您饭后休息真是罪该万死。」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/002050.ogg"
    l "「哈哈。」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/002051.ogg"
    l "「哎，我说，那你明知该死还来找我是为什么啊？问老师去也可以吧。」"
    y "「这您就明知故问了不是？要能找得到老师我哪会来麻烦您呢。」"
    voice "audio/voice/002052.ogg"
    l "「喔，为什么呀，老师都去哪儿啦？」"
    y "「老师都被您霸占了啊。」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/002053.ogg"
    l "「嘻嘻……」"
    y "「所以您得对我负责……喂，第二次笑场了啊，还笑个没完，能不能愉快地玩耍了？」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/002054.ogg"
    l "「哈……谁让你这么贫啊！以前我怎么没发现你还有这种天赋啊，不说相声可惜了。」"
    y "「这才哪儿到哪儿啊，我一直都是这样的好不好，是你笑点太低了吧？」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/002055.ogg"
    l "「成成成，都是我不好行了吧。」"
    y "「呵呵呵……」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/002056.ogg"
    l "「你看，你自己也笑场了好不好？还说我……嘻嘻……」"
    "两个人都笑场了，这一幕当然也就玩不下去了。"
    "我俩偶尔会这样开开玩笑，虽然最初的时候颇是引人注目，不过久而久之，同学们也就司空见惯了。"
    "毕竟暑假前的那件事大家都一清二楚，我和梁芷柔关系会变好并不是什么难理解的事。"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/002057.ogg"
    l "「……呼。」"
    show chara la01b #梁芷柔立绘|夏季校服|普通|侧面|近
    with dissolve
    voice "audio/voice/002058.ogg"
    l "「嗯，不闹了，说正经的。」"
    y "「嗯？」"
    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
    voice "audio/voice/002059.ogg"
    l "「真没有别的问题啦？你可别死要面子活受罪啊。」"
    y "「真没了。真的，这我蒙你干什么啊！」"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/002060.ogg"
    l "「嗯～」"
    voice "audio/voice/002061.ogg"
    l "「看来还可以嘛……」"
    y "「嗯？」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/002062.ogg"
    l "「……嗯，没事。」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/002063.ogg"
    l "「不错，挺好的，继续努力！」"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    scene bg b04 #滨河路|夏
    with fade
    "放学后，急匆匆地踏上回家的道路。"
    "虽然放学的时间已经愈发拖晚，但本地的实际时区其实已经接近东六区，这个时候的天还是亮的。"
    "饭已经在学校吃过了，如果能尽快赶回家里，那么做完作业以后还可以再多看一会儿书，也不至于睡得太晚。"

    y "「……嗯？」"
    voice "audio/sound/effect03.ogg"
    "手机突然响了。"
    "打开一看，是班上的一个哥们，平时经常一起玩的。"
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
    g "「谁知道你跑那么快啊！前天就没找着你，有什么事啊你最近，每天都这么急？」"
    y "「这不一大堆作业呢吗？」"
    voice "audio/voice/092005.ogg"
    g "「作业急个屁啊！」"
    y "「还得看会儿书呢！」"
    voice "audio/voice/092006.ogg"
    g "「看！你！妹！」"
    voice "audio/voice/092007.ogg"
    g "「你是不是最近和梁芷柔在一起的时间太长了？学傻了吧？你再怎么学能学成她那样吗？」"
    y "「……」"
    "扎心了，偏偏我还不知道该怎么才能反驳回去。"
    "就在我绞尽脑汁措辞的时候，那家伙又发消息过来了。"
    voice "audio/voice/092008.ogg"
    g "「哎我\[哔——\]，对了你他妈不是想要追她吧？哈哈哈哈哈哈……」"
    voice "audio/voice/092009.ogg"
    g "「我告诉你你他妈没～戏！快点改邪归正陪我们来开黑啊！」"
    "这……"
    "被说中了。虽然这家伙应该是瞎猜的。"
    "估计也就是随口胡说了一句，自己都不会相信有这种可能性的那种。"
    "不过……"
    y "「……」"
    "前两天的风言风语才刚平静了一点……"
    "这要是再被炒起来，那就真麻烦了……吧。"
    "不管是对老师、同学，还是梁芷柔，都不好交代。"
    y "「……」"
    voice "audio/voice/092010.ogg"
    g "「别废话啊，明天，定死了啊！」"
    y "「……」"
    stop sound fadeout 3.0
    scene bg black #黑屏
    with fade
    y "「……哦。」"
    "……{p}…………"

    play sound "audio/sound/ambientnoise03.ogg" fadein 1.5 loop #傍晚环境噪音
    scene bg b04 #滨河路|夏
    with fade
    y "「……」"
    "心情突然变得十分恶劣。"
    "我自认为……我和梁芷柔的关系，比起其他同学和她的关系，是稍有一些不同的。"
    "这让我有了那么一点点的优越感，然而……"
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/092008.ogg"
    g "「哎我\[哔——\]，对了你他妈不是想要追她吧？哈哈哈哈哈哈……」"
    hide memories
    with dissolve
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
    "之前洪水的影响已经渐渐消除了，湿地公园正在逐步恢复，一些栖息于此的鸟类也愈发活跃，开始为之后的长途旅行做起了准备。"
    scene bg black #黑屏
    with fade
    "即将远行的候鸟，与驻守栖息的留鸟。"
    "它们各自会有怎样的未来呢？"
    scene bg b00 #天空
    with fade
    stop sound fadeout 3.0
    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t07 #转场 滨河路
    with fade
    pause

#几天后。
#9月初。

    scene bg b02 #城区
    with fade
    "过了几天。"


    play music "audio/music/bgm03.ogg" fadein 1.5 #秋～绯月～
    scene bg b01 #教室
    with fade
    "学校依旧枯燥无比。老师们只知道一个劲地给学生加码，搞得我们苦不堪言。尤其是其他两个年级也到了开学的日子，两相对比之下，更是让人难以平衡。"
    "这期间，为了不让自己显得孤立、落人口实，我一定程度地回归到了自己原来的朋友圈子，放学后一起玩了几次。"
    "然而这并不能让我放松心情，反而因为心里面装着事，每次都很不踏实。"
    "这他妈的……以前是学，学不下去；现在是玩，玩不舒服。简直要人命了。"
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
    stop music fadeout 2.5
    y "「啊？」"
    show chara b06 #梁芷柔立绘|冬季校服|吃惊
    with dissolve
    "刚走了没两步，就听到梁芷柔在后面叫住我。"
    voice "audio/voice/002070.ogg"
    l "「……」"
    show chara b08a #梁芷柔立绘|冬季校服|担心1
    with dissolve
    voice "audio/voice/002071.ogg"
    l "「算了。」"
    y "「……？」"
    "什么情况？"
    show chara b07b #梁芷柔立绘|冬季校服|消沉2
    with dissolve
    "梁芷柔欲言又止，犹豫反复了一小会儿。"
    l "「……」"
    show chara b08b #梁芷柔立绘|冬季校服|担心2
    with dissolve
    voice "audio/voice/002072.ogg"
    l "「嗯……我想说啊……」"
    voice "audio/voice/002073.ogg"
    l "「我觉得你最好还是……再多上点心比较好。」"
    y "「呃……」"
    show chara b08a #梁芷柔立绘|冬季校服|担心1
    with dissolve
    voice "audio/voice/002074.ogg"
    l "「我知道，你最近学得比较累。我也累，我明白。但是呢，越是这时候，越是得咬着牙抗过去。」"
    "梁芷柔有些担忧地看着我。"
    show chara b07a #梁芷柔立绘|冬季校服|消沉1
    with dissolve
    voice "audio/voice/002075.ogg"
    l "「所以啊，网吧还是……尽量少去点吧？」"
    with vpunch
    y "「……！」"
    show chara b06 #梁芷柔立绘|冬季校服|吃惊
    with dissolve
    voice "audio/voice/002076.ogg"
    l "「我不是要管你啊，但是……」"
    show chara b05a #梁芷柔立绘|冬季校服|苦笑1
    with dissolve
    voice "audio/voice/002077.ogg"
    l "「我觉得你还是应该……就是，你要是遇到瓶颈了我可以帮你嘛，你看你这两天都没来找过我。」"
    show chara b08b #梁芷柔立绘|冬季校服|担心2
    with dissolve
    voice "audio/voice/002078.ogg"
    l "「这刚刚有了点进步，你要是一放弃那就全完了。」"
    show chara b08a #梁芷柔立绘|冬季校服|担心1
    with dissolve
    voice "audio/voice/002079.ogg"
    l "「啊，好不好？」"
    y "「我……」"
    voice "audio/voice/082007.ogg"
    f "「哎，芷柔，走啊，去吃饭？」"
    "这时候，突然有其他的女生过来招呼梁芷柔。"
    show chara b06 #梁芷柔立绘|冬季校服|吃惊
    with dissolve
    voice "audio/voice/002080.ogg"
    l "「啊……」"
    voice "audio/voice/002081.ogg"
    l "「好，这就去。」"
    hide chara
    with dissolve
    y "「……」"
    voice "audio/voice/082008.ogg"
    f "「啊……难道说，我当了电灯泡啦？」"
    voice "audio/voice/082009.ogg"
    f "「哎哟，那可真是对不起啊……」"
    show chara sb12a #梁芷柔立绘|冬季校服|羞涩1|远
    with dissolve
    voice "audio/voice/002082.ogg"
    l "「才没有！」"
    show chara sb04 #梁芷柔立绘|冬季校服|无奈|远
    with dissolve
    voice "audio/voice/002083.ogg"
    l "「走走走，吃饭去！八卦不死你……」"
    hide chara
    with dissolve
    "梁芷柔似乎有些羞涩，一把抓住那个女生，连拉带拽地把对方拖走了。"
    "路过我旁边的时候，她稍稍停顿了一下。"
    show chara lb08a #梁芷柔立绘|冬季校服|担心1|近
    with dissolve
    voice "audio/voice/002084.ogg"
    l "「……你再想想吧。」"
    hide chara
    with dissolve
    "然后，两个女生头也不回地离开了教室。"
    scene bg black #黑屏
    with fade
    pause 1.0
    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    scene bg b01 #教室
    with fade
    y "「……」"
    "呆在原地目送她们离开教室，我的内心五味杂陈。"
    "梁芷柔一直在关心着我的情况。"
    "她会为我有进步而感到高兴，也会在我松懈的时候过来劝告。"
    "她是真的对我有所期待……期待我可以考出一个比现在更好的成绩。"
    "然而，当你所期望的，我所能达到的，我真正想要做到的…{cps=2}…这{/cps}一切全都错位的时候。"
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
    g "「正常！别伤心嘛！她嘛，情理之中，呵呵。」"
    y "「……」"
    y "「呵呵你妹。」"
    stop sound fadeout 3.0
    with hpunch
    "有气无力地回了他一句，我用双手抓住这货搭在我身上的胳膊，用力地将他拧得鬼哭狼嚎。"
    scene bg black #黑屏
    with fade

    play sound "audio/sound/transition.ogg" noloop
    scene trans t01 #转场 教室
    with fade
    pause

#开学后一个月左右。
#9月中下旬。

    scene bg b02 #城区
    with fade
    "高三生活的头一个月，在各种忙碌之中匆匆而过。"
    play music "audio/music/bgm03.ogg" fadein 1.5 #秋～绯月～
    scene bg b01 #教室
    with fade
    "学校开始下狠手了。它就像是一头喜爱玩弄猎物的怪兽，不断地折磨着我们的身体与心灵。"
    scene bg b01a #教室|夜
    with dissolve
    "毫无节制可言的拖堂，越来越长的留校自习，永无止境的考试和作业。"
    "每当觉得自己快要适应当前的节奏时，老师们总会将压力再提高一个档次，始终让人疲于奔命。"
    scene bg b04b #滨河路|夜
    with fade
    "时区已经不再能够阻止天色的改变了。当我们得以离开学校的时候，太阳早就已经落山。"
    "慢慢踱着步子，沿着河边向家走去。"
    "所谓「拖着疲惫的步伐」就是指的这种情况了吧……"
    "不过，其实身体上也没有累到那么严重的程度，更主要的还是精神压力。"
    scene bg b01a #教室|夜
    with fade
    show charaz h03 #老师立绘|夏季|皱眉
    with dissolve
    voice "audio/voice/012006.ogg"
    z "「……听说你最近老是缠着梁芷柔？」"
    voice "audio/voice/012007.ogg"
    z "「你哪有那么多问题可问的啊？嗯？还找不到我，我现在是忙，以前呢？前面这两年，你说你主动找过我几次啊？」"
    show charaz h01 #老师立绘|夏季|普通
    with dissolve
    voice "audio/voice/012008.ogg"
    z "「我可都听说了啊！你小子，对梁芷柔有意思？」"
    show charaz h04 #老师立绘|夏季|咆哮
    with dissolve
    voice "audio/voice/012009.ogg"
    z "「哼，我还不知道是没谱的事吗？但这事闹出影响来，你让梁芷柔怎么想啊？我告诉你啊，你给我躲她远点，听见没有！？」"
    show charaz h01 #老师立绘|夏季|普通
    with dissolve
    voice "audio/voice/012010.ogg"
    z "「其实呢，我也不是批评你，毕竟你最近考得确实是不错，看得出来你确实在努力，但是啊……」"
    show charaz h03 #老师立绘|夏季|皱眉
    with dissolve
    voice "audio/voice/012011.ogg"
    z "「你得明白，咱们这儿谁掉了链子都不怕，梁芷柔不行。这种事不怕一万，就怕万一……」"
    hide charaz
    with dissolve
    scene bg b04b #滨河路|夜
    with fade
    "老师们的消息渠道似乎有点滞后，直到现在这事都快没人提了，才后知后觉地过来「预防」。"
    "不过，相比起同学之间的传言，这种来自老师的压力无疑更有实质。"
    "虽然，其实我这段时间已经没怎么再麻烦过梁芷柔了……"
    y "「……」"
    "夏末秋初，残暑还没有完全消散，余温萦绕之下，给人一种时间还停留在一个月之前的错觉。"
    "是的，就仿佛……一切都没有改变。我只是画了个圆，最终还是回到了起点。"
    "之前，我自认卑微，只敢远远地仰望着梁芷柔的背影，不敢逾越分毫。"
    "如今，我自知渺小，只能远远地仰望着梁芷柔的背影，无法逾越分毫。"
    y "「……」"
    "没办法吧……"
    "一个月的时间，已经足以让人抚平冲动了。"
    "那么……"
    scene bg black #黑屏
    with fade
    "我该认命吗？"
    "不如就这么……"
    "……放弃了吧？"
    stop music fadeout 2.5

    "……{p}…………"
    voice "audio/voice/002085.ogg"
    l "「……咦？」"
    scene bg b04b #滨河路|夜
    with fade
    "意外地，耳边传来了一个熟悉的声音。"
    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    show chara b06 #梁芷柔立绘|冬季校服|吃惊
    with dissolve
    voice "audio/voice/002086.ogg"
    l "「叶雨潇？」"
    y "「啊？」"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/002087.ogg"
    l "「真的是你啊？」"
    y "「啊……嗯。」"
    "还真是……说曹操，曹操到。"
    "昏黄的灯光下，梁芷柔独自一人从我迎面的方向走了过来。"
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    voice "audio/voice/002088.ogg"
    l "「你怎么这么慢啊，我都往回走了你才过来。」"
    show chara b02 #梁芷柔立绘|冬季校服|皱眉
    with dissolve
    voice "audio/voice/002089.ogg"
    l "「这是又跑哪儿玩去了？」"
    with hpunch
    y "「没有没有！」"
    "……下意识地先否认了。"
    "由于反应太快，这一嗓子吼得有点大，几乎是嚷出来的。"
    "随后自己才意识到……我确实没有出去玩啊！"
    "这种意识脱节的情况是怎么回事……"
    y "「……我被郑老师摁住了，训了我半天才放出来。」"
    show chara b06 #梁芷柔立绘|冬季校服|吃惊
    with dissolve
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
    scene bg b04b #滨河路|夜
    with fade
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    voice "audio/voice/002091.ogg"
    l "「嗯……好吧。真不是去玩了？」"
    y "「你看我这样子，玩得动才怪……我现在就想睡觉。」"
    y "「倒是你啊，怎么跑这边来了，是去书店了？」"
    show chara b10 #梁芷柔立绘|冬季校服|开心
    with dissolve
    voice "audio/voice/002092.ogg"
    l "「对呀，新的书到了。」"
    "梁芷柔抬了抬手。"
    "这时我才注意到，她手中还拎着一个包裹。"
    y "「这次买的是什么啊？嗯，黄冈题库？」"
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    voice "audio/voice/002093.ogg"
    l "「哈哈……才不是呢！你再猜猜？」"
    "她扬了扬手里的包裹，并不大，看起来也并不如何沉重。"
    "的确，按照她的做题量，这要是练习题的话大概不够塞牙缝的吧……"
    y "「感觉像是课外读物，不过具体的就没法猜了吧。」"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/002094.ogg"
    l "「嗯，也算对吧。」"
    show chara b01b #梁芷柔立绘|冬季校服|普通|侧面
    with dissolve
    voice "audio/voice/002095.ogg"
    l "「呵，这次呢，买的是《了不起的盖茨比》、《东方快车谋杀案》，还有《枪炮、病菌与钢铁》。」"
    y "「……的英文版吧？」"
    "我已经从这八竿子打不到一起去的分类中察觉到了真相。"
    show chara b10 #梁芷柔立绘|冬季校服|开心
    with dissolve
    voice "audio/voice/002096.ogg"
    l "「嘻嘻。」"
    y "「我的妈呀，学霸的世界真可怕。」"
    "一边说，我一边朝她伸出手。"
    show chara b13a #梁芷柔立绘|冬季校服|疑惑1
    with dissolve
    voice "audio/voice/002097.ogg"
    l "「哎？」"
    y "「给我，我帮你拿吧。」"
    show chara b13b #梁芷柔立绘|冬季校服|疑惑2
    with dissolve
    voice "audio/voice/002098.ogg"
    l "「干什么啊？」"
    y "「我送你一段。」"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/002099.ogg"
    l "「不用啦，又不沉。」"
    y "「顺便嘛。」"
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    voice "audio/voice/002100.ogg"
    l "「真不用，别管我了，赶快回家休息吧，你看你都累成这样了……」"
    y "「还是送送你吧，反正也不差这一点了。」"
    voice "audio/voice/002101.ogg"
    l "「嗯……」"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/002102.ogg"
    l "「呵，好吧！」"
    "梁芷柔略微想了一下，点了点头，将包裹递给我，并肩朝桥的方向走去。"
    stop sound fadeout 2.0
    scene bg black #黑屏
    with fade
    "……{p}…………"
    play music "audio/music/bgm03.ogg" fadein 1.5 #秋～绯月～
    scene bg b04b #滨河路|夜
    with fade
    show chara lb01b #梁芷柔立绘|冬季校服|普通|侧面|近
    with dissolve
    voice "audio/voice/002103.ogg"
    l "「……还真巧。」"
    y "「嗯？」"
    voice "audio/voice/002104.ogg"
    l "「嗯，没什么。就是觉得，好久没和你一起走这里了。」"
    y "「啊……」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/002105.ogg"
    l "「对吧？每天放学那么晚，我还得最后一个走，连去个书店的时间都没有！」"
    show chara lb02 #梁芷柔立绘|冬季校服|皱眉|近
    with dissolve
    voice "audio/voice/002106.ogg"
    l "「你看你也给累成这样了……这阵子学校简直是疯了啊！一天到晚的加码，还让不让人活了！」"
    y "「……哈，哈哈。」"
    "听着梁芷柔的抱怨，我忍不住笑了起来。"
    "果然，她还是她。"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/002107.ogg"
    l "「你笑什么啊？」"
    y "「没想到你也会这样喊累啊？」"
    show chara lb03 #梁芷柔立绘|冬季校服|生气|近
    with dissolve
    voice "audio/voice/002108.ogg"
    l "「我也是人，当然会累啊！」"
    show chara lb02 #梁芷柔立绘|冬季校服|皱眉|近
    with dissolve
    voice "audio/voice/002109.ogg"
    l "「而且我不是一直在跟你说嘛，学习需要讲效率，可你看咱们现在，呵呵。」"
    y "「这也是没办法吧，又不是所有人都能有那个脑子。」"
    show chara lb03 #梁芷柔立绘|冬季校服|生气|近
    with dissolve
    voice "audio/voice/002110.ogg"
    l "「那也不能全指望题海战术往里填鸭啊……」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/002111.ogg"
    l "「杜甫说得好，『苟能制侵陵，岂在多杀伤』。」"
    show chara lb07b #梁芷柔立绘|冬季校服|消沉2|近
    with dissolve
    voice "audio/voice/002112.ogg"
    l "「哎……」"
    y "「好啦好啦，班长大人您真是辛苦了。」"
    y "「哎，其实我突然想起来，你没必要非得这么晚跑过来一趟啊？跟我说一声我明天早上给你带过去不就行了吗？」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/002113.ogg"
    l "「我这不是没找到你吗？」"
    "啊……的确，刚下课就被老师抓走了，当时梁芷柔大概在忙别的事，没注意。"
    y "「这个，这是意外吧……你可以给我打电话或者发个消息啊？」"
    show chara lb07a #梁芷柔立绘|冬季校服|消沉1|近
    with dissolve
    voice "audio/voice/002114.ogg"
    l "「嗯……还是算了吧。」"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/002115.ogg"
    l "「毕竟今天过来取，待会儿就可以看了。而且……」"
    show chara lb08a #梁芷柔立绘|冬季校服|担心1|近
    with dissolve
    voice "audio/voice/002116.ogg"
    l "「都这么累。」"
    y "「啊……」"
    y "「不，其实没事的，举手之劳。像这种事，以后随时找我就行。」"
    show chara lb08b #梁芷柔立绘|冬季校服|担心2|近
    with dissolve
    voice "audio/voice/002117.ogg"
    l "「可是……」"
    y "「而且啊，天这么黑还一个人走，你也不怕出点什么事，心可真够大的。」"
    show chara lb13a #梁芷柔立绘|冬季校服|疑惑1|近
    with dissolve
    voice "audio/voice/002118.ogg"
    l "「这能出什么事啊？」"
    y "「怎么不会啊，你看看周围，黑漆漆的。」"
    "老城区的基础设施相对陈旧，尽管路是重修了，但相当一部分路灯似乎还沿用着之前的设备，有些已经坏掉了。"
    "别说梁芷柔了，就算是住在这里十几年的我，走的时候也要多加小心才行。"
    "虽不见得会遇到什么坏人，但万一没看清路，磕了碰了也是很麻烦的。"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/002119.ogg"
    l "「哎……好啦，我知道啦！」"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/002120.ogg"
    l "「嘻嘻。」"
    y "「还笑。你啊，还是趁现在开始多长点心眼吧。」"
    y "「这也就是在咱们县，等以后换个大城市，还指不定怎么样呢！」"
    show chara lb06 #梁芷柔立绘|冬季校服|吃惊|近
    with dissolve
    voice "audio/voice/002121.ogg"
    l "「啊……」"
    show chara lb07a #梁芷柔立绘|冬季校服|消沉1|近
    with dissolve
    voice "audio/voice/002122.ogg"
    l "「……也是。」"
    l "「……」"
    show chara lb07b #梁芷柔立绘|冬季校服|消沉2|近
    with dissolve
    voice "audio/voice/002123.ogg"
    l "「是啊……」"
    "梁芷柔轻轻摇了摇头，苦笑了起来。"
    y "「呃……」"
    with hpunch
    "不对不对，我才反应过来。"
    "今天脑子简直是一团浆糊，感觉自己现在就是一个傻逼，来回来去说错话。"
    "但是……"
    l "「……」"
    "面对着神色有些黯淡的梁芷柔，我却不知该怎么办，才能将那种疏离感挥散。"
    stop music fadeout 2.5
    "……{p}…………"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    play sound "audio/sound/ambientnoise11.ogg" fadein 1.5 loop #道路车辆环境噪音
    scene bg b04b #滨河路|夜
    with fade
    show chara lb01a #梁芷柔立绘|冬季校服|普通|正面|近
    with dissolve
    voice "audio/voice/002124.ogg"
    l "「啊，到了。」"
    y "「嗯。」"
    "熬过了沉默的后半段，我将梁芷柔送到北岸的公交站旁。"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/002125.ogg"
    l "「那……今天谢谢你了。」"
    y "「客气什么。」"
    voice "audio/voice/002126.ogg"
    l "「呵呵……你也早点回去吧。」"
    y "「反正都过来了，把你送上车呗。」"
    show chara lb10 #梁芷柔立绘|冬季校服|开心|近
    with dissolve
    voice "audio/voice/002127.ogg"
    l "「不用啦，真不用。你看这边这么热闹，出不了事的。」"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/002128.ogg"
    l "「你也赶快回去好好休息吧。」"
    "这边紧挨着商业区，虽然进入夜晚，但总算还有不少人流，也有一些人在车站等车。"
    y "「嗯？真的没问题啦？」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/002129.ogg"
    l "「真的啦！」"
    y "「嗯，那你路上小心点。」"
    show chara lb10 #梁芷柔立绘|冬季校服|开心|近
    with dissolve
    voice "audio/voice/002130.ogg"
    l "「好～」"
    y "「到家给我发个短信。」"
    show chara lb06 #梁芷柔立绘|冬季校服|吃惊|近
    with dissolve
    voice "audio/voice/002131.ogg"
    l "「啊……？」"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/002132.ogg"
    l "「嗯……好。」"
    y "「那，我走啦。」"
    voice "audio/voice/002133.ogg"
    l "「嗯～」"
    "梁芷柔微笑着轻轻朝我挥了挥手。"
    "我也扬了一下手，当做告别的招呼，随即快步离开了。"
    stop sound fadeout 2.0
    scene bg black #黑屏
    with fade
    play sound "audio/sound/effect19.ogg" fadein 1.5 loop
    "……{p}…………"
    scene bg b04b #滨河路|夜
    with fade
    y "「……呼！呼！」"
    "我一路奔跑，直到回到了家的附近才慢下来。"
    y "「……呼！……」"
    "仿佛……在逃跑。"
    stop sound fadeout 2.0
    "……{p}…………"

    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    scene bg black #黑屏
    with fade
    "我知道。"
    "我知道我自己的弱小。"
    "我知道前路漫漫，遍布荆棘。"
    "我知道我所谓的「目标」几乎是痴人说梦。"
    "只是……"
    "只是，我也知道，我其实……还是不甘心。"
    scene bg b04b #滨河路|夜
    with fade
    play sound "audio/sound/effect03.ogg" noloop
    "……"
    stop sound
    "掏出手机，看到了梁芷柔发来的短信。"
    voice "audio/voice/002134.ogg"
    l "「『安全到达！^_^』」"
    y "「……」"
    "看完短信，抬头向天。"
    "虽然因为身处城市，有光源污染而使得许多星星无法看清……"
    "但即使如此，最为明亮的星星，也依然坚强地绽放出了自己的光芒。"
    scene bg b00c1 #天空|夜|上弦月
    with fade
    "是的，其实我知道该做什么，该怎么做。"
    "我曾以那颗星为指引，向前迈出了第一步，只是……如今却再一次踌躇不前。"
    bird "「啾——」"
    "夜色之中，不远处传来了鸟的鸣叫。"
    "候鸟的迁徙已经开始了一段时间，如斑头雁这样迁徙时间较早的鸟，甚至已经走得七七八八了。"
    "只有少数，因为各种各样的问题耽搁下来。"
    "如果它们不能及时跟上的话，或许就再也走不了了……"
    "到了那时，即使强行起飞，也只会迷失方向，成为迷鸟，根本无法到达自己想要前往的目的地。"
    stop music fadeout 2.5
    scene bg black #黑屏
    with fade
    "而我……"
    "……又该怎么做呢？"
    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t07 #转场 滨河路
    with fade
    pause

#03.深秋

    $ chapter = "03"

#一个多月后。
#10月下旬。

    scene bg b02 #城区
    with fade
    "10月，下旬。"

    scene bg b01a #教室|夜
    with fade
    play sound "audio/sound/effect10.ogg" fadein 0.5 loop #写字声
    y "「……」"
    y "「…………」"
    y "「（……呼。）」"
    y "「（好，做完了。）」"
    stop sound fadeout 3.0
    "我放下手中的笔，轻轻地喘出一口气来。"
    "抬头看了看班里的情况，奋笔疾书者有之，愁眉苦脸者有之，左顾右盼、游手好闲者亦有之。"
    y "「……」"
    "果然如此……"
    "俗话说得好，人心散了，队伍不好带啊。"

    play music "audio/music/bgm03.ogg" fadein 1.5 #秋～绯月～
    scene bg b02b #城区|夜
    with fade
    "扭过脸，望向窗外。"
    "天空早已是一片漆黑。"
    "而商业区和住宅区则闪耀着点点灯火。"
    y "「（唉……）」"
    scene bg b02b #城区|夜
    nvl show
    nvl_narrator "现在是晚上8点钟。"
    nvl_narrator "如今，即便是有时差，到了这个钟点，太阳也已经彻底下山了。"
    nvl_narrator "然而，我们却需要继续留在学校上晚自习。"
    nvl_narrator "学校之前还在说什么「至少到寒假前不会再延长自习时间了」，到了现在则成了「你们就知足吧，别的地方有的要自习到10点钟呢」之类，毫无信用可言。"
    nvl_narrator "不过，身为学生，当然无力改变什么，也只能无可奈何地接受。"
    nvl_narrator "话虽如此，尽管在校学习的时间确实是增加了，但对于大多数人来说，那个效果嘛……"
    nvl_narrator "呵呵。"
    nvl clear
    show bg b00c2 #天空|夜|下弦月
    with dissolve
    nvl_narrator "其实真要说的话，也不是不能理解学校这次朝令夕改的做法。"
    nvl_narrator "毕竟他们也是被突然袭击的受害者。"
    nvl_narrator "就在不久之前，学校得知省里搞出了一个大新闻——"
    nvl_narrator "「省教育厅下发通知，要求全省第一次模拟诊断考试提前到12月初进行。」"
    nvl_narrator "往年的第一次模拟考试一般都是在3月份前后，学校也是按照这个思路安排的教学，结果现在被上级这样横插了一刀下来，心情可想而知。"
    nvl clear
    nvl_narrator "不知道省厅到底是出于什么考量才做出的这种决定……不过，对于学校来说，这不重要。"
    nvl_narrator "重要的是，一中作为县里最好的高中，必须在任何时刻都能够保持自己的领先地位。"
    nvl_narrator "可以不再创新高，但绝不能被人超越。"
    nvl_narrator "还按照原来的教学计划的话，复习进度肯定赶不上，尽管竞争对手们也是一样的准备不足，但是显然不能把希望寄托在别人犯错上面。"
    nvl_narrator "于是，自然而然就演变成了眼下的这种状况。"
    nvl clear

    stop music fadeout 2.5

    play sound "audio/sound/ambientnoise10.ogg" fadein 1.5 loop #安静学习环境噪音
    scene bg b01a #教室|夜
    with fadehold
    nvl hide
    y "「……」"
    y "「…………」"
    y "「（……好了。）」"
    "对照着标准答案，估算着模拟试卷的分数。"
    y "「（这个分数……）」"
    "看着估算出来的分数，我微微皱了皱眉。"
    "成绩……其实不能算糟糕，相比自己以前，还有一定程度的进步。"
    "但是……"
    y "「（这样下去……还是不行吧。）」"
    "轻叹一声，我忍不住抬起头来，向另一侧看去。"
#追加CG差分
    #scene cg01e #梁芷柔听讲CG-5|做题|CG01e
    #with fade
    "梁芷柔还在做题。"
    "就如同在学习会时那样，她的桌子上还是堆放着数量惊人的习题集，她从中挑选出有意义的题目，并将之逐一解决。"
    y "「（……还是那么专注啊。）」"
    #scene bg b01a #教室|夜
    #with fade
    "一如既往，梁芷柔在学习的时候总是能够聚精会神。"
    "而我在这方面就十分欠缺了……"
    y "「（如果我也能那样的话……）」"
    with hpunch
    y "「（不对不对，妈的这就已经是在走神了啊！）」"
    y "「（看题看题！别想没用的！）」"
    "……{p}…………"
    scene bg black #黑屏
    with fade
    play sound "audio/sound/effect06.ogg" noloop #铃声
    pause 1.0
    scene bg b01a #教室|夜
    with fade
    "晚自习终于结束了。"
    "学生们陆陆续续地离开教室，我也简单收拾了一下，拎起书包准备回家。"
    y "「……嗯？」"
    voice "audio/voice/003001.ogg"
    l "「嗯～啊～～嗯～～～」"
    "梁芷柔并没有起身，而是坐在椅子上，闭眼仰头，发出意义不明的呻吟声。"
    "看起来相当疲惫……"
    y "「喂。」"
    voice "audio/voice/003002.ogg"
    l "「嗯？」"
    y "「你没事吧？」"
    voice "audio/voice/003003.ogg"
    l "「啊……哈哈，还好啦，就是有点累。」"
    "梁芷柔听出是我的声音，没有睁眼，只是随意地抬了一下胳膊表示打招呼。"
    voice "audio/voice/003004.ogg"
    l "「稍微歇一会儿就好了，放心吧。」"
    y "「真的吗？」"
    voice "audio/voice/003005.ogg"
    l "「真的啦！你快回去吧，好好休息啊。」"
    y "「……你别管我了，先担心担心自己吧，你这样子真的没事吗？」"
    voice "audio/voice/003006.ogg"
    l "「哎呀你就别操心了，没事，真的。」"
    voice "audio/voice/003007.ogg"
    l "「赶紧的，回家！我待会儿还得负责锁门呢，你们都撤了我也能早点撤。」"
    "她说得好有道理……我竟无言以对。"
    y "「那……我走啦。你回家的时候路上小心点。」"
    voice "audio/voice/003008.ogg"
    l "「嗯，好的～」"
    y "「……」"
    "看她这个样子，我也帮不上什么忙，反而影响她休息，还是别给她添乱了。"
    voice "audio/voice/003009.ogg"
    l "「……谢谢。」"
    y "「……哎？」"
    "刚要走，却听到梁芷柔轻轻的声音。"
    "回头看去，她还是保持着之前的姿势闭目养神，只是不再像之前那样一脸的倦意，而是嘴角挂着一丝微笑。"
    y "「……呵呵。」"
    y "「明天见。」"
    "我也压低了声音，轻轻地回应道。"
    scene bg black #黑屏
    with fade
    "……{p}…………"

    play music "audio/music/bgm03.ogg" fadein 1.5 #秋～绯月～
    scene bg b02b #城区|夜
    with fade
    "距离偶遇梁芷柔的那天晚上，已经过去一个月了。"
    "从那之后，我和梁芷柔的关系有了稍许的回暖，似乎又回到了暑假刚刚结束时的那种状态。"
    "碰到的时候会打招呼，偶尔聊天，或者我找她问一些题。"
    "不过，也就仅此而已。"
    "我还没有想明白自己的路在何方，自然也不敢越雷池一步。"
    scene bg b04b #滨河路|夜
    with fade
    "当然，这一个月，我也不是在原地踏步。"
    "无论如何，先把学习成绩提高上来一些，总是没有坏处的。最起码，也要先去实现她跟我说的那个“小目标”。"
    "是以，最近这一个月，我开始尝试着自己给自己加码。"
    "虽然做不到像梁芷柔那样的程度……但在原来的基础上更进一步，这点心劲我还是有的。"
    "回忆着平时、以及暑假学习会时梁芷柔学习的模样，我尝试着让自己更加认真、更加努力，更加……像她那样去学习。"
    "虽然还是做不到那么专心致志，但是至少大多数的时候，都能强迫自己把精力放在学习上了。"
    "成绩…{cps=2}…是{/cps}有的。"
    "最近的几次测验，成绩和名次都有所提高，而且还在不断地提高。"
    "班里原本是梁芷柔一骑绝尘甩开其他人一大块，剩下第二和第三彼此较劲，再往后的几名非常不稳定，完全看各人的状态。"
    "而现在，我已经固定在四五名左右的位置上了。"
    "老师对我的评价不错，但在我自己看来，依然……不够。"
    "就像梁芷柔之前说的那样，我们这里，前几名之间的成绩断档非常大。"
    "我现在这个成绩，发展下去大概可以考一个不错的二本，或者在本省里挑一个说得过去的一本。只要保持下去，“小目标”应该不是问题。"
    "然而，想要报考外省的一本，尤其是那些发达城市的一本院校，就相当困难了，更遑论那些知名学府，根本想都不要想。"
    "当然，在我们这个小县城，别说一本，哪怕只是谁家孩子考了个二本，那也是足以让他们全家欢天喜地了。"
    "所以，做到这一步，其实已经满足了父母和老师此前对我的期望，想来他们都不会有什么不满意。"
    "只是{cps=2}……{/cps}"
    scene bg b08 #新城区|夏
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/001394.ogg"
    l "「那你有没有想过走出去呢？」"
    scene bg b04b #滨河路|夜
    with fade
    "我，还不满足。"
    y "「……」"
    "但我又该怎么办呢？"
    "现在的我，正在渐渐进入瓶颈。"
    "最开始的立竿见影，是因为以前的基础问题太多太大。而在弥补了这些之后，再要继续解决掉那些更细碎、更困难的缺漏，可不是一件容易的事。"
    "那需要更大的决心和毅力，一往无前、心无旁骛。"
    "那不是现在这样一边追赶，一边还在思考追赶意义的我，所能做到的。"
    "所以…{cps=2}…我{/cps}，该怎么办？"
    stop music fadeout 2.5

    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t06 #转场 天空
    with fade
    pause

#梁芷柔生日前的最后一个周末。
#11月上旬。

    scene bg black #黑屏
    with fade
    play sound "audio/sound/effect03.ogg" noloop
    "……"
    stop sound
    y "「……哦，好的，好的。」"
    y "「我知道了，马上就过去，谢谢。」"

    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    scene bg b04a #滨河路|秋
    with fade
    "挂掉电话，迅速收拾出门。"

    play audio "audio/sound/effect04.ogg" noloop
    y "「……嘿，还挺凉。」"
    "进入11月以后，气温开始有了明显的下降。"
    "像前几天那样最高气温偶尔还能到20度左右的日子是一去不复返了，再过上一两周，更是会降到10度以下。"
    y "「也是，都是这个时候了……」"
    "我望向路边的树木。"
    "霜降过后不久，大多数的草木都逐渐变得枯黄，槐树之类的乔木更是落叶纷纷，清楚地昭示着季节的变迁——"
    "深秋，到了。"
    stop sound fadeout 3.0

    scene bg b08a #新城区|秋
    with fade
    pause
    scene bg b09 #书店
    with fade
    play sound "audio/sound/ambientnoise07.ogg" fadein 1.5 loop #书店环境噪音
    play audio "audio/sound/effect11.ogg" noloop
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/023001.ogg"
    d "「您好！」"
    y "「你好，我来取书。」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/023002.ogg"
    d "「啊，是，是我刚才给您打的电话。」"
    voice "audio/voice/023003.ogg"
    d "「叶雨潇……是吧？您来得还真快啊。」"
    y "「这不是挨得近嘛，我家就住旁边的。」"
    show charad g02 #书店店员立绘|惊讶
    with dissolve
    voice "audio/voice/023004.ogg"
    d "「噢。那还真是。」"
    hide charad
    with dissolve
    "店员小姐一边和我闲聊，一边把我订购的书从包裹堆里翻了出来。"
    stop sound fadeout 2.0

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    voice "audio/voice/023005.ogg"
    d "「唉，我看看啊，靠莱克忒……艾、艾、艾斯……乔……什、什么雷思，of letters……of 乔治……噢…威尔的……的原文精装本，对吧？」"
    y "「对，就是这个。」"
    "我从被书名折磨得有些抓狂的店员手中接过了《Collected Essays，Journalism and Letters of George Orwell》。"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/023006.ogg"
    d "「哈哈……我英语不行，你可别笑话我啊。」"
    y "「不会啦，其实这个我也是买来送人的。」"
    "虽然我的水平，倒是不至于连标题都念成这个样子，不过也不会去主动碰这种文集类的外文原版书。"
    "显而易见，这是我打算送给某个人的生日礼物。"
    "某个将要在11月10日迎来自己18岁生日的、可以拿英文原版当作休闲读物的人。"
    show charad g04 #书店店员立绘|坏笑
    with dissolve
    voice "audio/voice/023007.ogg"
    d "「哦，这样啊……」"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/023008.ogg"
    d "「是打算送给…{cps=2}…梁·芷·{/cps}柔吗？」"
    with hpunch
    y "「……」"
    show charad g04 #书店店员立绘|坏笑
    with dissolve
    "扭过头，看到店员小姐正憋着一脸坏笑。"
    "说来，我第一次和梁芷柔来这里的时候，就是这位店员小姐接待的我们，之后也碰见过不少次，一来二往之下，也算是混了个脸熟，见面能打个招呼。"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/023009.ogg"
    d "「啊。看来还真是。」"
    voice "audio/voice/023010.ogg"
    d "「嘻嘻，怎么样怎么样，你们俩进展得如何了？」"
    y "「您啊……」"
    "必须说，她业务能力很强，做事井井有条，待人接物也游刃有余……不过副作用就是太过于健谈，而且还八卦。"
    y "「什么进展不进展的……您可别瞎说啊，尤其是千万别当着她的面提这事啊！我们俩什么关系都没有的！」"
    show charad g04 #书店店员立绘|坏笑
    with dissolve
    voice "audio/voice/023011.ogg"
    d "「好好好好~我知道我知道，单相思不容易，我不会去给你们添乱啦。」"
    y "「……」"
    "看着店员小姐那狡黠的笑容，总感觉这话毫无可信度啊！"
    "要是因为这位店员小姐熊熊燃烧的八卦之心把我推向万劫不复的深渊的话，我一定会死不瞑目吧。"
    "有些挠头。"
    stop music fadeout 2.5

    play sound "audio/sound/ambientnoise07.ogg" fadein 1.5 loop #书店环境噪音
    show charad g02 #书店店员立绘|惊讶
    with dissolve
    voice "audio/voice/023012.ogg"
    d "「……哎，说起来啊，你们俩不是一起来的吗？」"
    y "「啊？」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/023013.ogg"
    d "「她刚还在这儿来着，也就刚走没一会儿，你过来的时候没看见她吗？」"
    voice "audio/voice/023014.ogg"
    d "「你们俩也就前后脚吧？」"
    y "「没看见啊，什么情况？」"
    voice "audio/voice/023015.ogg"
    show charad g02 #书店店员立绘|惊讶
    with dissolve
    d "「也许你们俩都光顾着闷头走路，谁都没看见谁吧……」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/023016.ogg"
    d "「她也是来取书的，上一次到货的时候跟她联系过，不过当时她没有空，今天才来取走的。」"
    y "「啊……可能是吧。」"
    show charad g02 #书店店员立绘|惊讶
    with dissolve
    voice "audio/voice/023017.ogg"
    d "「还有啊，我看她脸色可不太好，你知道出了什么事吗？」"
    y "「咦？不知道啊……」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/023018.ogg"
    d "「嗯，那也许就是累着了吧，毕竟你们高三嘛。」"
    y "「嗯……」"
    "的确……哪怕是梁芷柔，现在也做不到无事一身轻。"
    "光是我看到她露出疲态的样子就有好几次了……"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/023019.ogg"
    d "「回头啊，多关心关心人家吧，这种时候不就是该轮到你出场了嘛！」"
    y "「呃……？」"
    voice "audio/voice/023020.ogg"
    d "「嘿嘿，不好意思啦？」"
    show charad g04 #书店店员立绘|坏笑
    with dissolve
    voice "audio/voice/023021.ogg"
    d "「我跟你说啊，真没必要想那么多，就是这个时候才要上啊！多好的机会啊！女孩子最脆弱的时候！这时候不上什么时候上啊！」"
    "店员小姐一脸看热闹的不嫌事大的模样，突然进入了亢奋的说教模式。"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/023022.ogg"
    d "「女孩子啊，你不主动去追的话，是永远都追不上的。」"
    voice "audio/voice/023023.ogg"
    d "「该厚脸皮的时候就得厚起脸皮来！只要人家没表现出厌烦你的意思来，那就是有戏啊，对不对？」"
    voice "audio/voice/023024.ogg"
    d "「所以啊，这个时候别犹豫啦！我支持你，啊！」"
    y "「……」"
    "话是这么说没错……"
    y "「…………」"
    "但我张了张嘴，却不知道该怎么接这个茬。"
    "最后，也只能苦笑一下。"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/effect11.ogg" noloop
    scene bg b08a #新城区|秋
    with fade
    "我离开书店，一边向家的方向走，一边低头想着心事。"
    y "「……」"
    y "「……唉。」"

    play music "audio/music/bgm03.ogg" fadein 1.5 #秋～绯月～
    "说到底，店员小姐的建议虽然有些不太负责，但是大道理是没有错的。"
    "此前是班里同学之间的胡乱起哄，现在一个几乎是陌生人的店员也来八卦一二，虽然都是捕风捉影的事，但作为当事人的梁芷柔，也不会迟钝到一点感觉都没有。"
    "不过，她始终都是坦坦荡荡的，反倒是我一直摇摆不定、甚至还曾产生疏离。"
    "她又不是那种恨不得能包容一切的的傻白甜圣母……既然没有敬而远之，那最起码就是不排斥。"
    "但……我还是什么也做不了。"
    scene bg b04a #滨河路|秋
    with fade
    "现在的我，根本追赶不上梁芷柔的脚步。"
    "这已经是我自发努力下能做到的极限了，沿着眼前的形势发展下去，7个月以后，我们就将迎来天各一方的结局。"
    "而我却还是迟迟没有下定决心。"
    "甚至，虽然我还在努力，还在给自己鼓劲，但在内心之中…{cps=2}…说{/cps}不定也有些满足了。"
    "过去十多年一直都随波逐流、得过且过。"
    "老师和家长？{w}不是自夸，现在的我早就已经超过他们最初的期望了。"
    "他们最多也就是希望我能考上一个不错的二本来着……「去考大城市的好学校」这种选项，从一开始就根本不存在于他们的意识里。"
    "别说他们了，哪怕是梁芷柔，其实也只是在聊天的时候提过那么一次。"
    "而要说到梁芷柔…{cps=2}…就{/cps}算我千辛万苦，真的成功考上了和她相同城市的大学……又怎样？"
    "这只是一个先决条件而已，未来的事情，谁也说不准。"
    "我应该为了这个不可捉摸的未来赌上一切，抛弃安稳的现状，背上好高骛远、不切实际的嘲讽，去拼命，去争取那一份可能性吗？"
    "随着时间的推移，我已经变得越来越难以确定这个问题的答案了。"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    scene bg b05a #湿地公园|秋
    with fade
    y "「咦……？」"
    y "「……走过头了吗。」"
    "心事重重之下没注意看路，等注意到的时候，已经走到了湿地公园的旁边。"
    y "「……呼。」"
    "也罢。"
    "既然都走到这里了，不如索性进去溜达一圈，权当散散心吧。"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b05a #湿地公园|秋
    with fade
    "整个夏秋两季，湿地公园都在维护，没有接待游客，而过了11月中旬，又到了闭园的季节，今年都彻底报销了。"
    "不过这种程度的封闭，自然挡不住土生土长的本地居民……不如说，我进这公园就从来没走过正门。"
    y "「哇…{cps=2}…好{/cps}惨。」"
    "夏天时江水泛滥带来的破坏还有一些残留的痕迹，再加上到了深秋，万物萧索，此时的湿地公园显得有些凄凉。"
    "靠近滨河路一侧的墙体被冲垮，眼下还没有完全修好，栈道也吱吱呀呀的，出现了一些破损。"
    "人工设施之外，自然环境也未能幸免。"
    "滩涂上原本有不少芦苇，受灾以后在修整的时候都被铲除了，看上去光秃秃的不怎么协调。而几个季节性的景观湖，除了能看到几只鸭子在游荡以外，也见不到什么好景色。"
    "不过，反正我也不是来看景的，无所谓了。"
    with fadehold
    "漫步其中，呼吸着带着潮湿泥土气息的空气，感觉似乎稍稍好了一些。"
    y "「……」"
    y "「咦？」"
    "无意之间，目光扫过岸边的时候，我看到了一个熟悉的身影。"
    y "「那是……」"
    show chara sd07b #梁芷柔立绘|秋季私服|消沉2|远
    with dissolve
    "——是梁芷柔？"
    "有些意外。"
    "不会是认错人了吧……"
    scene bg black #黑屏
    with fade
    "揉了揉眼睛。"
    scene bg b05a #湿地公园|秋
    show chara sd07b #梁芷柔立绘|秋季私服|消沉2|远
    with dissolve
    l "「……」"
    "……还真是她啊。"
    "她从书店出来以后，没有直接回家，而是来了这里吗？"
    y "「……」"
    "这是什么情况？"
    stop sound fadeout 3.0

    scene cg08a #梁芷柔河边CG-1|单独远目|CG08a
    with fade
    "梁芷柔的神情……看上去似乎有些落寞，又有些迷茫，是我从没见过的表情。"
    "现在是闭园状态，整个湿地公园空空荡荡的，我一个大活人戳在那里，其实蛮显眼的。然而，梁芷柔此刻却愣愣地不知道在看哪里，并没有注意到我。"
    "怎么看都不对劲……"
    scene bg b09 #书店
    show charad g02 #书店店员立绘|惊讶
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/023017.ogg"
    d "「还有啊，我看她脸色可不太好，你知道出了什么事吗？」"
    scene cg08a #梁芷柔河边CG-1|单独远目|CG08a
    with fade
    "脑海中突然回想起店员小姐之前说过的话。"
    "要不要过去打个招呼呢……"
    scene bg b09 #书店
    show charad g03 #书店店员立绘|笑容
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/023019.ogg"
    d "「回头多关心关心人家吧，这种时候不就是该轮到你出场了嘛！」"
    scene bg b05a #湿地公园|秋
    with fade
    y "「……」"
    "好吧，不想那么多了。"
    "无论如何，先上再说。"
    with fade

    play sound "audio/sound/ambientnoise01.ogg" fadein 4.5 loop #河边环境噪音
    show chara d07b #梁芷柔立绘|秋季私服|消沉2
    with dissolve
    y "「……哟！」"
    show chara d06 #梁芷柔立绘|秋季私服|吃惊
    with dissolve
    voice "audio/voice/003010.ogg"
    l "「哎？」"
    y "「怎么啦？一个人跟这儿想什么哪？」"
    show chara d08a #梁芷柔立绘|秋季私服|担心1
    with dissolve
    voice "audio/voice/003011.ogg"
    l "「啊……哎？你怎么在这儿啊？」"
    y "「这话该我问才对吧？这可是我家门口。」"
    show chara d06 #梁芷柔立绘|秋季私服|吃惊
    with dissolve
    voice "audio/voice/003012.ogg"
    l "「啊……」"
    show chara d07b #梁芷柔立绘|秋季私服|消沉2
    with dissolve
    voice "audio/voice/003013.ogg"
    l "「……也对啊。」"
    "梁芷柔蠢呆呆地点了点头。"
    "虽然她这模样看着很好玩……不过现在可不是说这种事的时候。"
    y "「怎么搞的，你这是离家出走了？」"
    show chara d05a #梁芷柔立绘|秋季私服|苦笑1
    with dissolve
    voice "audio/voice/003014.ogg"
    l "「呵……」"
    scene cg08c #梁芷柔河边CG-3|转头|秋装|苦笑|CG08c
    with fade
    "梁芷柔只是苦笑了一下，轻轻摇了摇头。"
    "看来我果然没什么搞活气氛的天赋。{p}既然如此，那就单刀直入吧。"
    y "「怎么啦，能跟我说说不？」"
    scene cg08c1 #梁芷柔河边CG-3|转头|秋装|落寞|CG08c1
    with dissolve
    voice "audio/voice/003015.ogg"
    l "「你不懂的。」"
    y "「你都没说呢，怎么就知道我不懂啦？」"
    scene cg08c #梁芷柔河边CG-3|转头|秋装|苦笑|CG08c
    with dissolve
    voice "audio/voice/003016.ogg"
    l "「……」"
    scene cg08c2 #梁芷柔河边CG-3|转头|秋装|苦笑|闭眼|CG08c2
    with dissolve
    voice "audio/voice/003017.ogg"
    l "「……你不懂。」"
    "梁芷柔的声音如呢喃一般，将话又重复了一遍。"
    scene cg08a #梁芷柔河边CG-1|远目|秋装|落寞|CG08a
    with dissolve
    y "「……」"
    l "「……」"
    "对话瞬间陷入僵局。"
    "尴尬的氛围让我一度有些犹豫，想要放弃继续刨根问底，但梁芷柔这过于异常的表现又让我难以无视。"
    y "「……」"
    l "「……」"
    y "「……」"
    "……不行，还是得问个清楚。"
    "短短的几秒，已经让我有种百爪挠心的感觉了。要是不问明白，我今天大概是过不好了。"
    y "「……」"
    "我将手中的包裹放到脚边，然后与她相隔半米，也不再说话，就默默地看着她的侧脸。"
    voice "audio/voice/003018.ogg"
    l "「……」"
    scene cg08a1 #梁芷柔河边CG-1|远目|秋装|落寞|闭眼|CG08a1
    with dissolve
    voice "audio/voice/003019.ogg"
    l "「……唉。」"
    "似乎终于在我无声的注视下感受到了压力，梁芷柔没有再继续沉默下去。"
    scene cg08c4 #梁芷柔河边CG-3|转头|秋装|面无表情|CG08c4
    with dissolve
    voice "audio/voice/003020.ogg"
    l "「叶雨潇。」"
    y "「嗯？」"
    scene cg08c5 #梁芷柔河边CG-3|转头|秋装|犹豫|CG08c5
    with dissolve
    voice "audio/voice/003021.ogg"
    l "「我问你啊……」"
    voice "audio/voice/003022.ogg"
    l "「……你知道候鸟吗？」"
    y "「嗯？」"
    "我没能在第一时间理解她的话语。"
    "虽然总算是打破了沉默，但这话题也未免跳脱得太厉害了吧？"
    "不过，梁芷柔似乎也没指望我会回答，只是仰头望天，自顾自地说了下去。"
    scene bg b00 #天空
    with fade
    voice "audio/voice/003023.ogg"
    show text open02 at truecenter
    with dissolve
    pause
    scene bg b00a #天空|候鸟
    with dissolve
    voice "audio/voice/003024.ogg"
    show text open03 at truecenter
    with dissolve
    pause
    voice "audio/voice/003025.ogg"
    show text open04 at truecenter
    with dissolve
    pause
    voice "audio/voice/003026.ogg"
    show text open05 at truecenter
    with dissolve
    pause
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    voice "audio/voice/003027.ogg"
    show text open06 at truecenter
    with dissolve
    pause

    scene cg08c4 #梁芷柔河边CG-3|转头|秋装|面无表情|CG08c4
    with fade
    play sound "audio/sound/effect23.ogg" loop
    with vpunch
    y "「——！」"
    "她的声音轻柔空灵，但却如同一记重锤，狠狠地砸在我的心头。"
    y "「呃……我……」"
    "——什么？"
    "什么情况？"
    "这话是什么意思？"
    "是在对我说吗？是在说我吗？"
    "这是在拒绝我？"
    "是我想多了？还是说……"
    "……果然？她……"
    "她其实……？"
    stop sound fadeout 3.0
    "…………"
    "心里一下子乱成一锅粥。"
    "张着嘴，想要说点什么，却根本组织不起语言来。"

    play music "audio/music/bgm07.ogg" fadein 1.5 #哀毁骨立
    scene cg08c6 #梁芷柔河边CG-3|转头|秋装|失焦|CG08c6
    with dissolve
    "然而，梁芷柔……似乎并没有注意到我的混乱。"
    "她的视线虽然朝向我，但目光的焦点却不知飞到了哪里。"
    l "「……」"
    scene cg08c3 #梁芷柔河边CG-3|转头|秋装|落寞|闭眼|CG08c3
    with dissolve
    voice "audio/voice/003028.ogg"
    l "「雨潇。」"
    y "「啊，哎？」"
    scene cg08c7 #梁芷柔河边CG-3|转头|秋装|忧伤|CG08c7
    with dissolve
    voice "audio/voice/003029.ogg"
    l "「雨潇，你毕业以后想做什么？」"
    with hpunch
    "……啥？"
    "「雨潇」？"
    "这是在叫我吗？"
    with hpunch
    "等等，什么鬼？{w}我的姓呢？{w}你不是一直都叫我的全名吗？{p}怎么回事？{w}到底是什么情况？{w}才刚刚说出那样的话，怎么突然又……"
    "冲击一拨接着一拨，我的大脑一片空白，只能下意识地应答——"
    y "「毕业以后……上大学啊。」"
    voice "audio/voice/003030.ogg"
    l "「我的意思是说，上完大学以后呢？离开学校以后。」"
    y "「呃……」"
    scene cg08c3 #梁芷柔河边CG-3|转头|秋装|落寞|闭眼|CG08c3
    with dissolve
    voice "audio/voice/003031.ogg"
    l "「唉。」"
    scene cg08a #梁芷柔河边CG-1|远目|秋装|落寞|CG08a
    with dissolve
    "梁芷柔轻轻垂首，叹出一口气，又一次抬头向天，仰望着无垠的青空。"

    scene bg b00a #天空|候鸟
    with fade
    voice "audio/voice/003032.ogg"
    l "「雨潇，你有想过你的未来吗？你有想过……」"
    voice "audio/voice/003033.ogg"
    l "「……自己的梦想吗？」"
    y "「未来……和梦想……」"
    voice "audio/voice/003034.ogg"
    l "「我想过。」"
    scene cg08c8 #梁芷柔河边CG-3|转头|秋装|忧伤|犹豫|CG08c8
    with fade
    voice "audio/voice/003035.ogg"
    l "「还记得我当初跟你说过，我现在，是为了我自己的梦想在努力吧？」"
    y "「嗯。」"
    voice "audio/voice/003036.ogg"
    l "「当时我没有告诉你我的梦想是什么，因为，其实那是一个特别简单、也特别没意思的理由——」"
    scene cg08c9 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|CG08c9
    with dissolve
    voice "audio/voice/003037.ogg"
    l "「我想要去樱华市。」"
    voice "audio/voice/003038.ogg"
    l "「我想去樱华市上大学，毕业以后留在樱华工作，最终……真正的，留在那里。」"
    y "「樱华吗……」"
    scene bg b12 #樱华市
    with fade
    "樱华市……东部沿海省份的大都市，以风景秀丽著称，同时也是江南的金融、文化中心之一。"
    "那是真真正正的大城市，一个市的经济规模就能超过我们这边全省还有富余。"
    scene cg08c9 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|CG08c9
    with fade
    voice "audio/voice/003039.ogg"
    l "「嗯，樱华。」"
    scene cg08c8 #梁芷柔河边CG-3|转头|秋装|忧伤|犹豫|CG08c8
    with dissolve
    voice "audio/voice/003040.ogg"
    l "「是不是觉得我这个人特俗，特现实？我当时没好意思跟你说明，也是因为怕你这么想我。」"
    y "「……」"
    scene cg08a #梁芷柔河边CG-1|远目|秋装|落寞|CG08a
    with dissolve
    voice "audio/voice/003041.ogg"
    l "「可是，实际上就是这样，就是靠着这样的一个梦想，我才能一路支撑着走到现在。」"
    scene cg08c7 #梁芷柔河边CG-3|转头|秋装|忧伤|CG08c7
    with dissolve
    voice "audio/voice/003042.ogg"
    l "「我一直都坚信自己没问题，肯定可以做到，一直都这么跟自己说，给自己鼓劲……」"
    scene cg08c3 #梁芷柔河边CG-3|转头|秋装|落寞|闭眼|CG08c3
    with dissolve
    voice "audio/voice/003043.ogg"
    l "「但是，最近，我真的是……有点太累了……」"
    scene cg08c13 #梁芷柔河边CG-3|转头|秋装|忧伤|含泪|CG08c13
    with dissolve
    voice "audio/voice/003044.ogg"
    l "「雨潇，你说我这么拼命，到底是对……还是错呢？」"
    "她的声音越来越压抑，到了最后几近哽咽。"
    y "「哎？哎哎哎！？呃……你你你你别哭啊，这、这到底是……」"
    "看着梁芷柔泫然欲泣的脆弱模样，我的心脏就好像是被人狠狠地扎了一刀似的，刺痛得不行。"
    "然而，我甚至连发生了什么事都不知道。"

    scene bg b05a #湿地公园|秋
    show chara ld07b #梁芷柔立绘|秋季私服|消沉2|近
    with fade
    "一切都来得太过突然、太过混乱，我的大脑已经彻底死机了，连带着说话都变得结巴起来。"
    "……不行。"
    "这样下去不行。必须要做点什么。"
    "必须，要在现在，立刻，做点什么。"
    "不，哪怕到了最后我什么问题都解决不了，至少也要做一个合格的倾听者，让她把内心的憋屈倾诉出来吧！"
    "我深深地吸进一口气，强迫自己冷静下来，用尽量温和、稳重的语气，向她询问。"
    y "「……到底是怎么了？发生什么事了？」"
    show chara ld08a #梁芷柔立绘|秋季私服|担心1|近
    with dissolve
    l "「……」"
    y "「方便跟我说说吗？」"
    show chara ld08b #梁芷柔立绘|秋季私服|担心2|近
    with dissolve
    l "「……」"
    show chara ld07a #梁芷柔立绘|秋季私服|消沉1|近
    with dissolve
    voice "audio/voice/003045.ogg"
    l "「……呼。」"
    show chara ld05b #梁芷柔立绘|秋季私服|苦笑2|近
    with dissolve
    voice "audio/voice/003046.ogg"
    l "「嗯。」"
    "梁芷柔朝我露出一个带着歉意的苦笑。"
    show chara ld05a #梁芷柔立绘|秋季私服|苦笑1|近
    with dissolve
    voice "audio/voice/003047.ogg"
    l "「脑子有点乱，从哪儿说起才好呢……」"
    y "「没事，慢慢来，想到哪儿说哪儿呗。」"
    voice "audio/voice/003048.ogg"
    l "「嗯，还是从头开始说吧，从我想去樱华这事开始。」"
    "或许是刚才已经稍稍发泄出来了一点吧，她的情绪逐渐平稳了下来。"
    scene cg08c12 #梁芷柔河边CG-3|转头|秋装|淡然|CG08c12
    with fade
    voice "audio/voice/003049.ogg"
    l "「我之前跟你说过，我小学时候的成绩非常糟糕，是到了初中以后才有了很大提高的吧。」"
    y "「嗯。」"
    voice "audio/voice/003050.ogg"
    l "「我初中这三年，其实也没少努力的，中考的时候考了个全县第一。当时呀，还被二中拿来宣扬了好久，毕竟他们一直被一中这边压着一头嘛，这一回总算是翻了身了。」"
    scene cg08c11 #梁芷柔河边CG-3|转头|秋装|微笑|CG08c11
    with dissolve
    voice "audio/voice/003051.ogg"
    l "「我呢，也高兴了好一阵。说真的，那时候，是挺拿这个当回事的，毕竟之前有过小升初考试的前车之鉴嘛，这一次终于自己争气，打翻身仗了，不用父母操心了，多好。」"
    voice "audio/voice/003052.ogg"
    l "「而且啊，我父母也是真的很高兴、很高兴，当天晚上我妈给做了满满一桌子菜，一边吃一边说这个，说到最后我和我妈抱头痛哭，一点也不夸张，真是给高兴坏了。」"
    voice "audio/voice/003053.ogg"
    l "「然后呢，我爸就劝我们俩，说多高兴的一件事，你俩哭个啥，来来来，说说怎么庆祝！」"
    scene cg08c12 #梁芷柔河边CG-3|转头|秋装|淡然|CG08c12
    with dissolve
    voice "audio/voice/003054.ogg"
    l "「接下来话题就转到这边来了，最后一家子商量了半天，决定趁着暑假，他们俩一起把年假给休了，带着我，出去旅行。」"
    y "「噢……」"
    scene cg08c11 #梁芷柔河边CG-3|转头|秋装|微笑|CG08c11
    with dissolve
    voice "audio/voice/003055.ogg"
    l "「呵，你也猜到了吧，我中考的奖励，就是去樱华，旅游。」"

    scene bg black #黑屏
    with fade
    voice "audio/voice/003056.ogg"
    l "「那是我去过的最远的地方。」"
    scene bg b02a #城区|秋
    with fade
    voice "audio/voice/003057.ogg"
    l "「小时候嘛，我从来没有出过远门，最远的也就是到省城，不过几百里的路。」"
    voice "audio/voice/003058.ogg"
    l "「那时候我还一直以为省城就是最漂亮、最棒的地方了，其他的城市，再怎么好也就不过如此了吧？」"
    voice "audio/voice/003059.ogg"
    l "「后来岁数大一点，网络也逐渐普及起来了，我知道这个世界上还有很多很繁华的城市。」"
    voice "audio/voice/003060.ogg"
    l "「但是，这也只是个『概念』上的理解，实际上如何，我并没有真正见识过。毕竟，隔着显示器，再怎么漂亮的图片，也没有什么真实感。」"
    scene bg b12 #樱华市
    with fade
    voice "audio/voice/003061.ogg"
    l "「所以，樱华，就是我对大城市的第一个直观的印象。」"
    voice "audio/voice/003062.ogg"
    l "「我们没钱自由行，那一次是跟团走的，几乎是被导游当成一群羊在赶，白天晚上连轴转，一个接一个地跑景点。」"
    voice "audio/voice/003063.ogg"
    l "「整个过程走马观花似的，就是不停地走、不停地看，很累，说实话也没玩出个什么名堂来，但是我就是很开心，因为我长见识了。」"
    scene bg b12a #樱华市|夜晚
    with dissolve
    voice "audio/voice/003064.ogg"
    l "「我第一次真切地感受到，一个城市可以这么大、这么高，可以有无数的高楼大厦，无论走到哪里都有灯光，哪怕是深夜也几乎看不到星星。」"
    scene bg b02a #城区|秋
    with fade
    voice "audio/voice/003065.ogg"
    l "「我终于明白一个真正的大城市，应该是一个什么样子。省城和樱华比起来，就好像拿咱们这儿和省城比一样，根本就没有可比性。」"
    scene cg08c15 #梁芷柔河边CG-3|转头|秋装|讽刺|CG08c15
    with fade
    "说到这里，梁芷柔停顿了一下，自嘲地笑了笑。"
    y "「所以，你就想要以后去樱华发展么？」"
    scene cg08c9 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|CG08c9
    with dissolve
    voice "audio/voice/003066.ogg"
    l "「怎么会呢……当然不是了。」"
    scene cg08c12 #梁芷柔河边CG-3|转头|秋装|淡然|CG08c12
    with dissolve
    voice "audio/voice/003067.ogg"
    l "「那时候的我，虽然觉得樱华很好，很喜欢那里，但也就是以后还想再去一次，根本没考虑过未来的规划。」"
    scene cg08c4 #梁芷柔河边CG-3|转头|秋装|面无表情|CG08c4
    with dissolve
    voice "audio/voice/003068.ogg"
    l "「真正让我下定决心想要去那里发展的，是在一年以后。」"

    scene bg b00a #天空|候鸟
    with fade
    voice "audio/voice/003069.ogg"
    l "「你还记得高一暑假的时候，全国中学生数学竞赛么？」"
    y "「哎？……啊，你参加的那一次吧，有印象有印象。」"
    y "「毕竟从咱们学校出来的，杀过复赛到省队去参加全国决赛的，你是第一个人嘛。」"
    "这事在当时算是搞了个大新闻，其他学生固然惊为天人，老师们也一个个与有荣焉的样子。梁芷柔的学霸之名，正是从那之后才在学校里变得人尽皆知。"
    scene bg b12 #樱华市
    with fade
    voice "audio/voice/003070.ogg"
    l "「嗯，那次全国决赛的地点，恰好，也是在樱华。所以仅仅时隔一年，我就又去了一回樱华。」"
    voice "audio/voice/003071.ogg"
    l "「但是这一次，就不是什么很好的回忆了。」"
    scene cg08c #梁芷柔河边CG-3|转头|秋装|苦笑|CG08c
    with fade
    voice "audio/voice/003072.ogg"
    l "「那次比赛，学校那边宣传得是很好听，但是你知道吗？其实真正的结果是，我……或者说咱们省整个队，都是一败涂地，排名几乎垫底，什么成绩也没拿到。」"
    y "「呃……？」"
    voice "audio/voice/003073.ogg"
    l "「这还不算完，那一次比赛实际上是以夏令营的形式举办的，除了考试的那两天以外，后面还有一段时间是在进行学校学生之间的交流互动。」"
    scene cg08a2 #梁芷柔河边CG-1|远目|秋装|苦笑|CG08a2
    with dissolve
    voice "audio/voice/003074.ogg"
    l "「真的……从那时候开始，我才算是真真正正地明白了，咱们这里，和那些大城市之间，差距到底有多大。」"
    voice "audio/voice/003075.ogg"
    l "「可能在你看来，我已经算是不错的了，但是跟那些大城市里名校出身的选手比，那根本不是一个级别的。」"
    voice "audio/voice/003076.ogg"
    l "「同样是高一，我的知识储备，无论在深度上还是广度上，都差得不是一星半点。」"
    scene bg b00a #天空|候鸟
    with fade
    voice "audio/voice/003077.ogg"
    l "「那已经不是说光靠努力就能弥补得上的了……因为人家一点也不比我懒，甚至要更拼命。」"
    voice "audio/voice/003078.ogg"
    l "「那些选手都很聪明，家庭条件也都不错，父母一辈就受过良好的教育，所以也就更重视这些，他们从小的教育环境就比咱们好得多。」"
    voice "audio/voice/003079.ogg"
    l "「拿学校来说，咱们学校总共三位高级教师，已经是学校的宝贝了，但是在那边的一所重点学校，特级教师都有十几位甚至更多，高级教师的资格只是门槛。」"
    voice "audio/voice/003080.ogg"
    l "「更不用说硬件设施了……那边早就已经普及电教了，咱们这边还是只能靠黑板。」"
    scene bg b12 #樱华市
    with fade
    voice "audio/voice/003081.ogg"
    l "「而且除了上学，那边学生的眼界也比咱们更加开阔。」"
    voice "audio/voice/003082.ogg"
    l "「他们可以随时随地获取他们想要的信息……在那些大城市，有许许多多的书店，还有图书馆，有浩如烟海的书籍供他们阅览，更不用说还有互联网了。」"
    voice "audio/voice/003083.ogg"
    l "「你想想，你第一次玩电脑是在什么时候？反正我是到了初中以后才接触电脑的。但是那些人，他们从小就人手一台电脑，十几年前家里就连通了网络，现在每人都在用智能手机……或者带着平板电脑，大街上到处都是无线WIFI。」"
    voice "audio/voice/003084.ogg"
    l "「……甚至于，就连玩，他们都比你会玩。」"
    scene bg b00a #天空|候鸟
    with fade
    voice "audio/voice/003085.ogg"
    l "「他们之中，几乎是没有那种书呆子型的，每个人都多多少少有一些个人的兴趣爱好，而且玩得还很深。」"
    voice "audio/voice/003086.ogg"
    l "「有爱看书、爱画画的、有爱唱歌的，也有爱爬山、爱打球、爱游泳的，哪怕是玩电脑，也有玩到精通，可以自己写程序、制作游戏的。」"
    voice "audio/voice/003087.ogg"
    l "「就拿读书来说，我想看的书其实挺多的，但买不起，恨不得节衣缩食才能买下一部分，甚至还有根本不知道该去哪儿买的。但那些人，他们就完全没有这些顾虑。」"
    scene cg08c15 #梁芷柔河边CG-3|转头|秋装|讽刺|CG08c15
    with fade
    voice "audio/voice/003088.ogg"
    l "「总而言之……你想想，当你看着一个个先天条件和后天条件都比你好，然后还比你更努力的人，在你眼前成群结队地晃悠的时候……你说我有多受打击。」"
    y "「呃……」"
    scene bg b12a #樱华市|夜晚
    with fade
    voice "audio/voice/003089.ogg"
    l "「到了最后，在我意志最消沉的时候，我无意中听到樱华那边负责带领我们的几个老师之间的聊天。」"
    voice "audio/voice/003090.ogg"
    l "「有一个在一路上都很照顾我的老师，和别的老师感叹。」"
    voice "audio/voice/003091.ogg"
    l "「她说，可惜我不是她班上的孩子，不然一定可以取得更好的成绩的。」"
    voice "audio/voice/003092.ogg"
    l "「她还说，我只能等高考了，考到樱华那样的城市里，考到那些名牌重点大学，否则的话，很有可能就此被埋没。」"
    scene cg08c7 #梁芷柔河边CG-3|转头|秋装|忧伤|CG08c7
    with fade
    y "「……」"
    y "「所以你就……」"
    voice "audio/voice/003093.ogg"
    l "「是啊。」"
    scene cg08c9 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|CG08c9
    with dissolve
    voice "audio/voice/003094.ogg"
    l "「我是可以做到的，不是吗？」"
    scene cg08c10 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|含泪|CG08c10
    with dissolve
    voice "audio/voice/003095.ogg"
    l "「我已经这么努力了。」"
    voice "audio/voice/003096.ogg"
    l "「再多努力一把，让它变得更有价值，何乐而不为呢？」"
    scene cg08c14 #梁芷柔河边CG-3|转头|秋装|坚定|CG08c14
    with dissolve
    voice "audio/voice/003097.ogg"
    l "「所以，如你所见，从高二开始，我比以前更加认真，更加努力。」"
    voice "audio/voice/003098.ogg"
    l "「我竭尽全力，想要保证自己能够在高考中成功。」"
    y "「……」"
    "的确……"
    "听过这些话以后，我总算可以理解一些了。"
    "她……梁芷柔她为什么要、以及为什么能够如此孜孜不倦地努力用功。"
    "这个长期以来一直令我困惑的问题，随着视角的转变，终于抓住了一丝头绪。"
    "然而眼下的我，却没有时间感悟这些。"
    scene cg08c13 #梁芷柔河边CG-3|转头|秋装|忧伤|含泪|CG08c13
    with dissolve
    voice "audio/voice/003099.ogg"
    l "「但是……」"
    voice "audio/voice/003100.ogg"
    l "「你说……我的选择，真的是对的吗？」"
    y "「啊……哎、哎？」"
    "不知为何，本已平静下来的梁芷柔居然说着说着又哽咽起来。"
    y "「怎么了？为什么这么说？」"
    voice "audio/voice/003101.ogg"
    l "「前几天……前几天……」"
    scene cg08c7 #梁芷柔河边CG-3|转头|秋装|忧伤|CG08c7
    with dissolve
    "梁芷柔用力地吸了吸气，然后又长长地吐出来，将哭腔压了回去。"
    scene cg08c5 #梁芷柔河边CG-3|转头|秋装|犹豫|CG08c5
    with dissolve
    voice "audio/voice/003102.ogg"
    l "「前几天，周一吧。」"
    voice "audio/voice/003103.ogg"
    l "「郑老师专门跟我谈了谈。」"
    y "「郑明老师？」"
    voice "audio/voice/003104.ogg"
    l "「嗯……他跟我说，这次模拟诊断考试一定要沉住气，考出好成绩，给班上同学做出榜样来。」"
    y "「哦……然后呢？」"
    scene cg08c2 #梁芷柔河边CG-3|转头|秋装|苦笑|闭眼|CG08c2
    with dissolve
    "梁芷柔轻轻摇摇头。"
    y "「哎？呃……他好歹是咱们班主任，这么说说也没什么错吧？」"
    scene cg08c15 #梁芷柔河边CG-3|转头|秋装|讽刺|CG08c15
    with dissolve
    voice "audio/voice/003105.ogg"
    l "「是啊，是没什么错……」"
    scene cg08a2 #梁芷柔河边CG-1|远目|秋装|苦笑|CG08a2
    with dissolve
    voice "audio/voice/003106.ogg"
    l "「然后在周二，我去老师办公室搬卷子的时候，年级主任付老师把我叫到她那边，很关切地问我学习上还有没有什么拿不准的方面，要是有，她可以帮我想办法开小灶。」"
    voice "audio/voice/003107.ogg"
    l "「她跟我说，要把这次模拟诊断考试当成真正的高考来对待，绝对不能掉以轻心，只有这样才能真正检验出自己的水平，才能更好地在后面的阶段里弥补漏洞。」"
    y "「……」"
    scene cg08c #梁芷柔河边CG-3|转头|秋装|苦笑|CG08c
    with dissolve
    voice "audio/voice/003108.ogg"
    l "「呵呵……接着，周三，你还记得吗？晚自习的时候，我被老师叫出去了一小会儿。」"
    scene cg08c8 #梁芷柔河边CG-3|转头|秋装|忧伤|犹豫|CG08c8
    with dissolve
    voice "audio/voice/003109.ogg"
    l "「其实是余校长和教导主任过来了，说是例行巡视到咱们班了，所以就顺便找我聊一聊。」"
    scene cg08c7 #梁芷柔河边CG-3|转头|秋装|忧伤|CG08c7
    with dissolve
    voice "audio/voice/003110.ogg"
    l "「余校长……那个扑克脸，特别和蔼、真的是特别和蔼地问我复习得怎么样啦、考试有没有信心啊、压力大不大什么的。」"
    scene cg08c15 #梁芷柔河边CG-3|转头|秋装|讽刺|CG08c15
    with dissolve
    voice "audio/voice/003111.ogg"
    l "「呵呵呵……你说我压力大不大？」"
    y "「呃……」"
    "从第三者的角度听起来，整个事情似乎多少有些滑稽搞笑，不过换到当事人的角度，恐怕就不那么好玩了。"
    scene cg08c3 #梁芷柔河边CG-3|转头|秋装|落寞|闭眼|CG08c3
    with dissolve
    voice "audio/voice/003112.ogg"
    l "「真的……我觉得好累。」"
    scene cg08c1 #梁芷柔河边CG-3|转头|秋装|落寞|CG08c1
    with dissolve
    voice "audio/voice/003113.ogg"
    l "「不是因为这次模拟考试……而是我有时候会想，我真的只要考到樱华去，就能更好吗？」"
    y "「怎么说……？」"
    l "「……」"
    scene cg08a #梁芷柔河边CG-1|远目|秋装|落寞|CG08a
    with dissolve
    voice "audio/voice/003114.ogg"
    l "「你知道吗？那次比赛，樱华那边本地的几个选手，他们那些高中的老师根本就不会去关心这种模拟考试的。」"
    voice "audio/voice/003115.ogg"
    l "「甚至于，对于他们来说，高考都不是什么大问题。」"
    scene cg08a1 #梁芷柔河边CG-1|远目|秋装|落寞|闭眼|CG08a1
    with dissolve
    voice "audio/voice/003116.ogg"
    l "「呵……因为那些学校，每年连需要参加高考的学生都没有多少。」"
    scene cg08a #梁芷柔河边CG-1|远目|秋装|落寞|CG08a
    with dissolve
    voice "audio/voice/003117.ogg"
    l "「有的学校一个年级几百人，需要高考的只有十几个，其他的，早就保送或者预定出国留学了。」"
    voice "audio/voice/003118.ogg"
    l "「哪怕是剩下的这些人，一本率也在95\%以上，除了极个别的特殊学生，全都能考上不错的……对咱们这边的学生来说，是梦寐以求的学校。」"
    scene cg08a3 #梁芷柔河边CG-1|远目|秋装|垂目|CG08a3
    with dissolve
    voice "audio/voice/003119.ogg"
    l "「你说，我到了那边，真的可以和这些人……去竞争么？」"
    "梁芷柔说完以后，呆呆地望着河面看了好一会儿。"
    "片刻之后……又把头转了回来。"
    scene cg08c5 #梁芷柔河边CG-3|转头|秋装|犹豫|CG08c5
    with dissolve
    l "「……」"
    y "「……」"
    "她这是……在期待我来说些什么吗？"
    "说实话，这个问题不是我能回答得了的。"
    "我从来没有见识过那样的世界，更无法体会到她此时的感受，这个问题根本就超脱了我所能理解的范畴。"
    "但是……"
    y "「我觉得，没问题吧。」"
    scene cg08c16 #梁芷柔河边CG-3|转头|秋装|吃惊|CG08c16
    with dissolve
    voice "audio/voice/003120.ogg"
    l "「嗯？」"
    "我至少可以告诉她，我所能看到的她，是怎样的。"
    y "「我不知道你是不是最近压力太大自己钻了牛角尖，看不清楚自己，开始妄自菲薄了。」"
    y "「但是，在我看来……」"
    y "「你就是最厉害的。」"
    voice "audio/voice/003121.ogg"
    l "「啊……」"
    y "「这段时间我没少跟在你身边。我看得到，你是怎么努力的。所以我特别清楚你有多厉害。真的是很厉害。」"
    y "「可能你的那些个未来的竞争对手也很厉害吧，但你可是在咱们省都能排的上号的学霸，再怎么说凡事也要讲个正态分布吧？你也是最顶尖的那一批啊！」"
    scene cg08c11 #梁芷柔河边CG-3|转头|秋装|微笑|CG08c11
    with dissolve
    voice "audio/voice/003122.ogg"
    l "「呵呵……谢谢你。」"
    "梁芷柔笑着摇摇头。"
    scene cg08c9 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|CG08c9
    with dissolve
    voice "audio/voice/003123.ogg"
    l "「但是，真的不是这么简单的。」"
    scene cg08c5 #梁芷柔河边CG-3|转头|秋装|犹豫|CG08c5
    with dissolve
    voice "audio/voice/003124.ogg"
    l "「要光说考试，比如高考，我可能确实能比他们不少人考得都好吧……」"
    y "「那不就……」"
    scene cg08c8 #梁芷柔河边CG-3|转头|秋装|忧伤|犹豫|CG08c8
    with dissolve
    voice "audio/voice/003125.ogg"
    l "「但是呢，高考只是个转折点罢了。或者说，是个起点。」"
    voice "audio/voice/003126.ogg"
    l "「真正影响到你未来发展的，打基础的，还是得看大学这个阶段。」"
    y "「……」"

    scene bg b00a #天空|候鸟
    with fade
    voice "audio/voice/003127.ogg"
    l "「高中以前，学的都是基础知识。说句实话，只要方法对头，肯下功夫，再怎么着也不会差到哪去的。」"
    voice "audio/voice/003128.ogg"
    l "「像咱们这样，哪怕没有那么好的教育条件，只要努力，像我，也一样可以考的不错。」"
    voice "audio/voice/003129.ogg"
    l "「但是，到了大学以后，再想光靠努力来解决一切问题，就不可能了。」"
    voice "audio/voice/003130.ogg"
    l "「那时候，努力所能决定的……只是一个人的下限。」"
    voice "audio/voice/003131.ogg"
    l "「它只能决定……你在自己的上下限之间，至少可以爬到一个什么位置。」"
    y "「……」"
    voice "audio/voice/003132.ogg"
    l "「而决定一个人上限的因素，有很多很多。」"
    voice "audio/voice/003133.ogg"
    l "「你的天赋、你的教育环境、你的心态，还有各种机遇……」"
    scene cg08c9 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|CG08c9
    with fade
    voice "audio/voice/003134.ogg"
    l "「呵……别说这些了，等到了大学，我可能连像现在这样去努力都做不到。」"
    scene cg08c8 #梁芷柔河边CG-3|转头|秋装|忧伤|犹豫|CG08c8
    with dissolve
    voice "audio/voice/003135.ogg"
    l "「我家的经济条件不算宽裕。我以前也跟你说过，为了我上大学，我们全家都在节衣缩食。」"
    y "「嗯。」"
    voice "audio/voice/003136.ogg"
    l "「但即便如此，负担学费和基本的生活费，就已经是我家的极限了，我在那边除了住宿和食堂以外，所有的花销，都是额外的。」"
    voice "audio/voice/003137.ogg"
    l "「在樱华那样的地方，想要一点钱不花，几乎不现实。我肯定得去打工养活自己。」"
    y "「奖学金呢？」"
    scene cg08c9 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|CG08c9
    with dissolve
    voice "audio/voice/003138.ogg"
    l "「学校的学业奖学金数额没多高的。至于其他类型的奖金，经常还是需要参加各种评选、比赛还有社会活动来加分，换算下来，其实和打工没什么区别，风险还更大，很有可能最后都拿不到的。」"
    scene cg08c5 #梁芷柔河边CG-3|转头|秋装|犹豫|CG08c5
    with dissolve
    voice "audio/voice/003139.ogg"
    l "「总之，到了那边，我不可能再像现在这样什么都不用想，只要好好学习就成了。」"
    scene cg08c #梁芷柔河边CG-3|转头|秋装|苦笑|CG08c
    with dissolve
    voice "audio/voice/003140.ogg"
    l "「可是……那些大城市出身的学生，他们就没有这么多的顾虑。」"
    voice "audio/voice/003141.ogg"
    l "「只要是真的想学，很少会有节外生枝的障碍阻拦他们。」"
    scene cg08c14 #梁芷柔河边CG-3|转头|秋装|坚定|CG08c14
    with dissolve
    voice "audio/voice/003142.ogg"
    l "「要想赶上他们，我就得付出超过现在很多、很多的精力才行……还未必一定能赶得上。」"
    scene cg08c9 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|CG08c9
    with dissolve
    voice "audio/voice/003143.ogg"
    l "「可是，我能不去追吗？我拼命想要往那边考，总不能真等考上了以后，就这么碌碌无为熬个四年，最后只是蹭一张名牌大学的文凭出来吧？」"
    y "「……」"
    scene cg08a3 #梁芷柔河边CG-1|远目|秋装|垂目|CG08a3
    with dissolve
    voice "audio/voice/003144.ogg"
    l "「不可能，我不甘心的……真的……」"
    scene cg08a1 #梁芷柔河边CG-1|远目|秋装|落寞|闭眼|CG08a1
    with dissolve
    voice "audio/voice/003145.ogg"
    l "「可是，我真的是……真的是……」"
    voice "audio/voice/003146.ogg"
    l "「我真的是不知道……不知道我能不能做到……」"
    "梁芷柔一边说，一边像是想要否定一切似的，不停地摇头叹气。"
    "我已经记不清这是她今天第几次这样了。"
    "一直以来，在我眼中的梁芷柔，总是乐观、积极，目标明确，行动果断的。"
    "然而，现在的她却是如此的脆弱，如此…{cps=2}…凄{/cps}凉。"
    "这既让我感到心痛，也让我感到自己的无力。"

    scene bg black #黑屏
    with fade
    "我帮不上她，甚至触摸不到她的世界。"
    "往日的踌躇、怠惰，在这一刻终于全都转化为现实的报应。"
    "如果，如果我能再多努力一点，再多向她的世界靠拢一点……"
    "是不是，在这个时候，就可以多支持她一点呢？"
    scene cg08a2 #梁芷柔河边CG-1|远目|秋装|苦笑|CG08a2
    with fade
    voice "audio/voice/003147.ogg"
    l "「唉……」"
    voice "audio/voice/003148.ogg"
    l "「你说，我是不是就好像那些夏候鸟一样。」"
    scene bg b00a #天空|候鸟
    with fade
    voice "audio/voice/003149.ogg"
    l "「到了春天，一路向北，费尽千辛万苦到达了目的地，自以为攀上了人生的高峰。」"
    scene bg b00 #天空
    with dissolve
    voice "audio/voice/003150.ogg"
    l "「殊不知，那座『高峰』，对于冬候鸟而言，却仅仅只是他们旅程的出发点而已。」"
    y "「……」"
    voice "audio/voice/003151.ogg"
    l "「那些冬候鸟所追求的目标，是夏候鸟难以想象的……甚至于，那是一个夏候鸟根本不可能生存的环境。」"
    voice "audio/voice/003152.ogg"
    l "「而哪怕是那些不愿意外出闯荡的留鸟，也可以很轻松自在地生活，在那些夏候鸟……我们，需要付出无数努力才能到达的地方。」"
    voice "audio/voice/003153.ogg"
    l "「是不是这样呢？」"
    scene cg08a #梁芷柔河边CG-1|远目|秋装|落寞|CG08a
    with fade
    y "「……」"
    y "「我觉得，不是。」"
    scene cg08c4 #梁芷柔河边CG-3|转头|秋装|面无表情|CG08c4
    with dissolve
    y "「我这么比喻不知道对不对。」"
    y "「但是，如果用候鸟来打比方的话，至少，我真的是觉得，你已经是冬候鸟了。」"
    scene cg08c16 #梁芷柔河边CG-3|转头|秋装|吃惊|CG08c16
    with dissolve
    voice "audio/voice/003154.ogg"
    l "「……嗯？」"
    y "「要说的话，我才是那只夏候鸟……不，我连夏候鸟可能都算不上，得是夏候鸟那边的留鸟。」"
    y "「你看，我之前一直都觉得自己学习成绩可以了，在班里算排名靠前的，能考个二本，比起其他那些家伙，算是挺不错的了。」"
    y "「我这人懒，要没人推着，我可能到现在还都懒得动呢。」"
    y "「但是，你看我现在，还是动了。」"
    y "「一本的大学啊……以前我也就是睡觉的时候想想，做个梦，可你看现在，反正我是觉得我继续这么下去应该能考上，没问题，对不对？」"
    scene cg08c5 #梁芷柔河边CG-3|转头|秋装|犹豫|CG08c5
    with dissolve
    voice "audio/voice/003155.ogg"
    l "「嗯……」"
    y "「这都是因为你，是不是？你一直鼓励我，说我能行，给我指出一条路来。」"
    y "「真的，要不是你，要不是我看着你这么努力，让我也想、也跟着你一起努了一把力，我哪可能有现在这种进步。」"
    y "「你…{cps=2}…你{/cps}是我的目标啊。我都开始往前走了，你又哪能止步不前呢？」"
    y "「拿出信心来吧，你可是我『姐姐』呢！对不对？」"
    scene cg08c16 #梁芷柔河边CG-3|转头|秋装|吃惊|CG08c16
    with dissolve
    voice "audio/voice/003156.ogg"
    l "「啊……」"
    l "「……」"
    scene cg08c11 #梁芷柔河边CG-3|转头|秋装|微笑|CG08c11
    with dissolve
    voice "audio/voice/003157.ogg"
    l "「呵呵……说的也是呢。」"
    scene cg08c12 #梁芷柔河边CG-3|转头|秋装|淡然|CG08c12
    with dissolve
    voice "audio/voice/003158.ogg"
    l "「谢谢你。真的，跟你这么聊了聊，感觉好多了。」"
    voice "audio/voice/003159.ogg"
    l "「呼……」"
    voice "audio/voice/003160.ogg"
    l "「……雨潇。」"
    y "「嗯。」"
    scene cg08c9 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|CG08c9
    with dissolve
    voice "audio/voice/003161.ogg"
    l "「谢谢你。」"
    y "「哎？」"
    "梁芷柔又一次道了谢。"
    "只是，刚刚将愁眉舒展开来的她，不知何故，突然又露出了悲伤的表情。"
    scene cg08c10 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|含泪|CG08c10
    with dissolve
    voice "audio/voice/003162.ogg"
    l "「谢谢你，在我难过的时候能陪着我……」"
    voice "audio/voice/003163.ogg"
    l "「谢谢你在天黑的时候能陪我走夜路，在我遇到危险的时候会上来保护我……」"
    voice "audio/voice/003164.ogg"
    l "「一直都支持我，还想方设法给我鼓劲……」"
    voice "audio/voice/003165.ogg"
    l "「谢谢你……」"
    y "「……」"
    voice "audio/voice/003166.ogg"
    l "「可是……等过了明年，高三、高考完以后呢？」"
    scene cg08a #梁芷柔河边CG-1|远目|秋装|落寞|CG08a
    with dissolve
    voice "audio/voice/003167.ogg"
    l "「我们就要各奔东西了。」"
    with hpunch
    y "「什——」"
    voice "audio/voice/003168.ogg"
    l "「你会去到省城的大学，再努努劲，没准还能考上百薇？」"
    voice "audio/voice/003169.ogg"
    l "「对吧。离家也近，周围的同学也多……」"
    l "「……」"
    scene cg08a1 #梁芷柔河边CG-1|远目|秋装|落寞|闭眼|CG08a1
    with dissolve
    voice "audio/voice/003170.ogg"
    l "「而樱华……在那边，只有我一个人。」"
    with hpunch
    y "「——！」"
    scene cg08a #梁芷柔河边CG-1|远目|秋装|落寞|CG08a
    with dissolve
    voice "audio/voice/003171.ogg"
    l "「我们隔着几千里地。」"
    scene cg08a3 #梁芷柔河边CG-1|远目|秋装|垂目|CG08a3
    with dissolve
    voice "audio/voice/003172.ogg"
    l "「陌生的城市，陌生的学校，陌生的同学。」"
    voice "audio/voice/003173.ogg"
    l "「无论发生什么事，所有的一切都需要我自己一个人去面对。」"
    scene cg08c10 #梁芷柔河边CG-3|转头|秋装|忧伤|浅笑|含泪|CG08c10
    with dissolve
    voice "audio/voice/003174.ogg"
    l "「到了那时候，在我的身边，又还有谁，能像你这样支持我呢？」"
    y "「这……」"
    scene cg08c8 #梁芷柔河边CG-3|转头|秋装|忧伤|犹豫|CG08c8
    with dissolve
    voice "audio/voice/003175.ogg"
    l "「我不知道……自己有没有那么坚强。」"
    scene cg08c17 #梁芷柔河边CG-3|转头|秋装|强颜欢笑|CG08c17
    with dissolve
    voice "audio/voice/003176.ogg"
    l "「我不是冬候鸟，我和你一样的。」"
    voice "audio/voice/003177.ogg"
    l "「虽然嚷嚷着想要去樱华、留在樱华，但是说到底，我的根始终还在这里啊。」"
    scene cg08c8 #梁芷柔河边CG-3|转头|秋装|忧伤|犹豫|CG08c8
    with dissolve
    voice "audio/voice/003178.ogg"
    l "「我呢，哪怕将来一切顺利，我真的留在了那边，每到逢年过节的，总也要回来的。」"
    scene bg b00a #天空|候鸟
    with fade
    voice "audio/voice/003179.ogg"
    l "「真的就像候鸟一样。」"
    scene bg b00 #天空
    with dissolve
    voice "audio/voice/003180.ogg"
    l "「只不过，这只候鸟，落了单，有点孤独。」"
    scene cg08c14 #梁芷柔河边CG-3|转头|秋装|坚定|CG08c14
    with fade
    l "「……」"
    voice "audio/voice/003181.ogg"
    l "「……呼。」"
    voice "audio/voice/003182.ogg"
    l "「但是，也没办法，我必须去面对这些。这是代价，而且是我自作自受的。」"
    "梁芷柔长长地吐出一口气。她接下来再也没有言语，似乎终于发泄完了所有积压在内心深处的郁气。"
    scene bg black #黑屏
    with fade
    "……{p}…………"

    scene bg b04a #滨河路|秋
    with fade
    "将梁芷柔送到公交车站以后，我独自一人踏上了回家的路。"
    y "「……」"
    y "「…………」"
    with vpunch
    "用力地，朝着空气狠狠挥了一下拳头。"
    y "「妈的！」"
    with vpunch
    "我为什么不再多努一把力！"
    with vpunch
    "我为什么会觉得自己已经够努力的了！？"
    with vpunch
    "我为什么不早点想明白这种事！"
    scene bg b05a #湿地公园|秋
    with fade
    with hpunch
    y "「我他妈怎么这么没用！」"
    with hpunch
    y "「啊啊————————————！」"
    y "「……」"
    play sound "audio/sound/effect20.ogg" noloop
    with vpunch
    "——啪！"
    "我扬起头，用力地拍了拍自己的脸，像是要把自己打醒一样。"
    scene bg black #黑屏
    with fade
    y "「……呼。」"
    scene bg b00 #天空
    with fade
    y "「……」"
    stop music fadeout 2.5
    y "「不……」"
    y "「还没到放弃的时候……」"
    scene bg black #黑屏
    with fade
    y "「还有…{cps=2}…7{/cps}个月呢。」"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t08 #转场 樱华市
    with fade
    pause

#04.寒冬

    $ chapter = "04"

#11月下旬。

    scene bg b02c #城区|冬
    with fade
    "11月的下旬，秋意渐远，而凛冬将至。"

    scene bg b01 #教室
    with fade
    show charaz h04a #老师立绘|冬季|咆哮
    with dissolve
    voice "audio/voice/014001.ogg"
    z "「……你们现在最大的问题就是文盲！文盲知道什么意思吗？还不识字呢怎么能做得对题呀！？所以说，你们必须把词汇表给我背下来！啊？」"
    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/014002.ogg"
    z "「别说什么不会背、不会背的！我告诉你们，这事没什么难的，只要下苦功夫，谁都能背得下来！啊，咱们班上又不是没有这样的例子！你们就不能学学人家？」"
    show charaz h04a #老师立绘|冬季|咆哮
    with dissolve
    voice "audio/voice/014003.ogg"
    z "「我告诉你们啊，下个星期我检查！啊！那几个一贯考不过去的，你们自己想想后果——别看了，说的就是你！瞎瞅什么呢！？你还笑是不是，回头我把你爸叫过来，看你还笑不笑得出来……」"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    play audio "audio/sound/effect06.ogg" noloop
    scene bg b01 #教室
    with fade
    "…………"
    "下午的第一节课终于结束了。"
    play sound "audio/sound/ambientnoise09.ogg" fadein 2.5 loop #人群嘈杂环境噪音
    "班主任的咆哮与响彻全校的下课铃声混在一起，成为这场暴风骤雨般的洗礼的完美收尾。"
    "老师前脚才离开讲台，班上已然炸了锅。同学们如同一群被捅了窝的蜜蜂一般，一瞬间就四散开来，教室里充满了喧嚣。"
    y "「……唉。」"
    scene bg black #黑屏
    with fade
    "我把头拍在课本里，就这么闭着眼睛，含含糊糊地叹了口气，仿佛这样就能够获得短暂的安宁。"
    "想要长时间保持专注，真的是不容易啊……即便心理上已经有所准备，身体上的疲惫依然是不可避免的。"
    y "「（吸——）」"
    y "「——呼！」"
    scene bg b01 #教室
    with vpunch
    "用力地抬起头，将气呼出来的同时，猛地把眼睁开。"
    y "「（不能松懈……）」"
    stop sound fadeout 3.0
    scene bg b00 #天空
    with fade
    "距离第一次模拟诊断考试还有不到半个月。"
    "时间…{cps=2}…对{/cps}我来说，曾经可以肆意挥霍的时间，如今已经变成了弥足珍贵的奢侈品。"
    scene bg b05a #湿地公园|秋
    show chara d07a #梁芷柔立绘|秋季私服|消沉1
    show memories #回忆滤镜
    with dissolve
    "与梁芷柔在河边的那次交谈，已经是将近两周以前的事了。"
    "那天的事，我俩都闭口不再谈起，就好像从未发生过一样。"
    scene bg black #黑屏
    with fade
    "但是，有些东西，已经悄然改变了。"
    "……{p}…………"
    scene bg b01a #教室|夜
    with fade
    play sound "audio/sound/ambientnoise10.ogg" fadein 1.5 loop #安静学习环境噪音
    "晚自习。"
    "随着日期的推移，学校的压力也越来越大。"
    "自习逐渐变成了各科老师的串讲，剩下的时间也被置于监督之下，而不是只凭各人自觉。"
    "不过，对于现在的我来说，这倒并不是什么坏事。"
    "大多数人都被堆积如山的作业所支配，不再像以前那样干什么的都有，教室里的秩序可谓是空前良好。"
    "对真正想要学习的人来说，这样的环境再合适不过了。"
    y "「……」"
    y "「……」"
    y "「…………」"
    y "「（好，接下来的是……）」"
    y "「……」"
    y "「…………」"
    #scene cg01e #梁芷柔听讲CG-5|做题|CG01e
    #with fade
    "偶尔，我会朝梁芷柔的方向看一看。"
    l "「……」"
    "只是，无论何时，看到的总是她聚精会神的模样。"
    "……她并非超人。她也会疲惫，无论身心。"
    "只不过，与其他人不一样的是……她早就已经明确了自己的目标，并且会坚定不移地为之前行。"
    #scene bg b01a #教室|夜
    #with fade
    y "「……」"
    "在我曾经以为自己已经开始了解、接近了梁芷柔的那段时间里，一直能够感觉到彼此之间有着一层无形但确实存在的屏障。"
    "那时的我还不明白……还以为那只是由于我和她差距过大而导致的隔阂。"
    scene bg black #黑屏
    with fade
    "但是……此时此刻，我已经非常清楚地认识到，那所谓的「隔阂」，并非仅仅是我们此前「已有」的差距，更是我们时至今日「仍在」不断拉开的距离。"
    scene bg b01a #教室|夜
    with fade
    "现在的我，喜欢梁芷柔。"
    "而以前的我，是憧憬梁芷柔。"
    "因为憧憬，所以仰望……但却不了解。"
    "所以，也只会说出南辕北辙的、苍白无力的话语。"
    "她追寻的梦想、{w}她付出的努力、{w}她遇到的困惑。"
    "如果这一切全都未曾体会过，我又怎么可能真正理解得了她呢？"
    stop sound fadeout 3.0
    "……{p}…………"
    play audio "audio/sound/effect06.ogg" noloop
    pause
    y "「啊……」"
    "下课铃响了。"
    y "「……」"
    y "「呼。」"
    play sound "audio/sound/ambientnoise09.ogg" fadein 2.5 loop #人群嘈杂环境噪音
    "我放下笔，合上了卷子。"
    y "「已经是这个点了啊。」"
    "时钟指向8点40分，第二节晚自习结束了。"
    "后面还有最后一节……幸亏我们学校历来都是走读制，没有宿舍，不然老师们恨不得要让我们住在学校。"
    y "「……」"
    "坚持……是肯定要坚持下去的。"
    "要是连这点程度都受不了，那我不如趁早放弃算了。"
    "不过，在下一节课到来之前，还是尽量休息一下，养精蓄锐吧……"
    scene bg black #黑屏
    with fade
    stop sound fadeout 3.0
    "……{p}…………"
    #梁芷柔
    voice "audio/voice/004001.ogg"
    who "「哟。」"
    "朦胧之中，听到了一个熟悉的声音。"
    scene bg indistinct #白色朦胧
    with dissolve
    y "「啊……啊？啥啊？……」"
    #梁芷柔
    voice "audio/voice/004002.ogg"
    who "「嗯～还活着呐？」"
    y "「哦……我死了。」"
    scene bg black #黑屏
    with fade
    #梁芷柔
    voice "audio/voice/004003.ogg"
    who "「噗……喂，醒醒！」"
    y "「嗯……」"
    #梁芷柔
    voice "audio/voice/004004.ogg"
    who "「别睡啦！怎么搞的，这么惨……」"
    y "「嗯……」"
    #梁芷柔
    voice "audio/voice/004005.ogg"
    who "「起来啦，上课铃都响了……」"
    y "「……嗯……没有吧……我怎么没听见……」"
    y "「……呼噜……」"
    #梁芷柔
    voice "audio/voice/004006.ogg"
    who "「……？」"
    y "「……呼噜……呼噜！」"
    #梁芷柔
    voice "audio/voice/004007.ogg"
    who "「哎……」"
    y "「……呼噜！呼噜！！」"
    "……{p}…………"
    #梁芷柔
    voice "audio/voice/004008.ogg"
    who "「喂，喂！」"
    #梁芷柔
    voice "audio/voice/004009.ogg"
    who "「醒醒！真上课了！」"
    y "「……嗯……我没睡……」"
    y "「……呼噜！」"
    "……{p}…………"
    voice "audio/voice/004010.ogg"
    l "「你给我起来！」"
    play sound "audio/sound/effect20.ogg" noloop
    scene bg b01a #教室|夜
    with vpunch
    y "「哇！」"
    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    "脑袋被狠狠拍了一巴掌，一下子驱散了所有的睡意。"
    show chara lb03 #梁芷柔立绘|冬季校服|生气|近
    with dissolve
    "睁开眼睛，看到梁芷柔正在怒目瞪视着我。"
    play sound "audio/sound/effect21.ogg" noloop
    "给她这幅表情伴奏的，是全班同学哄堂大笑的声音。"
    y "「呃……」"
    voice "audio/voice/004011.ogg"
    l "「醒啦？」"
    y "「醒了……」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/004012.ogg"
    l "「终于肯醒啦？」"
    y "「呃……呵呵……那个……」"
    show chara lb03 #梁芷柔立绘|冬季校服|生气|近
    with dissolve
    voice "audio/voice/004013.ogg"
    l "「呵什么呵啊，知道我为什么要打你吗？」"
    y "「啊？」"
    show chara lb02 #梁芷柔立绘|冬季校服|皱眉|近
    with dissolve
    voice "audio/voice/004014.ogg"
    l "「就算是自习课，你真困了想睡觉也就罢了，求您动静小点成么？」"
    y "「呃……什么情况？」"
    show chara lb03 #梁芷柔立绘|冬季校服|生气|近
    with dissolve
    voice "audio/voice/004015.ogg"
    l "「你自己睡觉，能不能不要打扰别人？」"
    y "「……？？？」"
    "在我茫然不解的时候，旁边有好事的同学跑过来，一脸班长大人的狗腿子的模样，拿出手机，播放了一段录像给我看。"
    "山寨手机那特有的超大音量响彻教室。"
    play sound "audio/sound/effect24.ogg" loop
    y "「……呼噜……呼噜……呼噜！！！！……呼噜……嗯嗯……呼……呼噜！！！！……」"
    stop sound fadeout 3.0

    y "「……」"
    l "「……」"
    y "「呃……我……」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/004016.ogg"
    l "「明白啦？」"
    y "「明白了……」"
    "在班长模式的梁芷柔那强大的气场面前，我情不自禁地缩起了脖子。"
    show chara lb03 #梁芷柔立绘|冬季校服|生气|近
    with dissolve
    voice "audio/voice/004017.ogg"
    l "「别再睡了啊！」"
    y "「是……」"
    show chara lb09 #梁芷柔立绘|冬季校服|坏笑|近
    with dissolve
    voice "audio/voice/004018.ogg"
    l "「要睡……去一边偷偷睡去！」"
    y "「呃……」"
    play sound "audio/sound/effect21.ogg" noloop
    e "「哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈。」"
    "伴随着梁芷柔的笑场，全班同学也像是打开了什么阀门一样，又一次发出了惊天动地的哄堂大笑。"
    show chara lb03 #梁芷柔立绘|冬季校服|生气|近
    with dissolve
    voice "audio/voice/004019.ogg"
    l "「安静！安静点，想把老师招来啊！？」"
    "以及，班长大人慌张的镇压声。"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b04b #滨河路|夜
    with fade
    y "「唉………………」"
    play music "audio/music/bgm13.ogg" fadein 1.5 #With Memories
    "顶着满天的星星，我一边长吁短叹，一边走在回家的路上。"
    y "「这么下去不行啊……」"
    "这种自己给自己加码的高强度学习状态已经维持了一段时间了，出乎我意料的是，身体居然比精神更早一步产生了抗拒。"
    "其中的一大特征就是变得嗜睡……原本还以为能够靠课间休息时的闭目假寐缓一缓来着，但看今天这情况，恐怕也就是杯水车薪罢了。"
    "这不是光靠意志力就能解决的问题……看来时间的安排还需要更合理一些才行。"
    y "「……」"
    y "「是啊……」"
    y "「真是……不容易啊……」"
    "越是到这种时候，这种感觉越是强烈。"
    "当我开始尝试着像她那样努力的时候……"
    "我才明白……她究竟付出了多少努力，又曾遇到过怎样的困难。"
    show bg b00c2 #天空|夜|下弦月
    with fade
    "……我终于开始去真正地了解她了。"
    "如果，我能继续沿着这条路走下去的话，或许会有那么一天，我可以和她拥有共同的语言。"
    "直到那时，我们，才可以真正地「开始」。"
    stop music fadeout 3.0

    scene bg black #黑屏
    with fade
    "就不知，还能不能来得及了……"
    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t01 #转场 教室
    with fade
    pause

#随后的周末。

    scene bg b02c #城区|冬
    with fade
    "第二天，一个难得的休息日。"

    play sound "audio/sound/effect03.ogg" noloop
    pause
    stop sound

    play sound "audio/sound/ambientnoise04.ogg" fadein 1.5 loop #白天环境噪音
    y "「……喂？」"
    voice "audio/voice/004020.ogg"
    l "「早上好啊，你现在方便吗？没打扰你休息吧？」"
    y "「啊？哦，没有啊，我在看书呢。怎么想起给我打电话来了？」"
    voice "audio/voice/004021.ogg"
    l "「嘻嘻，那就好。」"
    voice "audio/voice/004022.ogg"
    l "「我嘛，当然是来抓壮丁的咯。」"
    y "「啊？」"
    voice "audio/voice/004023.ogg"
    l "「我在你家楼底下呢，你要是没事的话，来帮个忙呗？」"
    y "「……哈？」"
    voice "audio/voice/004024.ogg"
    l "「可以吗？」"
    y "「哦……噢，你稍微等一下，我换衣服。」"
    scene bg black #黑屏
    with fade
    stop sound fadeout 3.0
    "……{p}…………"

    play music "audio/music/bgm04.ogg" fadein 1.5 #冬～苍雪～
    scene bg b04c #滨河路|冬
    with fade
    show chara e09 #梁芷柔立绘|冬季私服|坏笑
    with dissolve
    voice "audio/voice/004025.ogg"
    l "「哟，睡神。」"
    y "「喂！」"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/004026.ogg"
    l "「哈哈哈。」"
    y "「……欺负我好玩吗？」"
    show chara e09 #梁芷柔立绘|冬季私服|坏笑
    with dissolve
    voice "audio/voice/004027.ogg"
    l "「好玩啊！」"
    y "「……」"
    show chara e07b #梁芷柔立绘|冬季私服|消沉2
    with dissolve
    voice "audio/voice/004028.ogg"
    l "「咳咳！」"
    show chara e07a #梁芷柔立绘|冬季私服|消沉1
    with dissolve
    voice "audio/voice/004029.ogg"
    l "「真没打扰你休息吧？虽然是这个点了，但就怕万一嘛……」"
    y "「我就算是头猪，11点也该起床了」"
    show chara e13a #梁芷柔立绘|冬季私服|疑惑1
    with dissolve
    voice "audio/voice/004030.ogg"
    l "「噢，那就好。」"
    y "「所以呢，班长大人您有何指教啊？」"
    show chara e09 #梁芷柔立绘|冬季私服|坏笑
    with dissolve
    voice "audio/voice/004031.ogg"
    l "「都说了是抓壮丁啊，跟我来呗！」"
    y "「……啊？」"
    scene bg b08b #新城区|冬
    with fade
    "……{p}…………"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/004032.ogg"
    l "「♪～」"
    y "「……」"
    hide chara
    with dissolve
    "我亦步亦趋地跟在梁芷柔的身后。"
    "看这方向，是要去书店吧……所谓的「抓壮丁」应该就是让我帮忙搬书了。"
    "不过这还真是稀奇，毕竟平时梁芷柔都是尽量避免给别人添麻烦的。"
    "是因为这次的书太多了？还是有别的什么事……"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/004033.ogg"
    l "「♫～～」"
    y "「（从表情上看不出来啊……）」"
    "梁芷柔心情似乎还算不错，路上一直哼着小曲儿，笑眯眯的。"
    "一时半会儿想不出有什么可能……算了，还是直接问吧。"
    y "「我说。」"
    show chara e13b #梁芷柔立绘|冬季私服|疑惑2
    with dissolve
    voice "audio/voice/004034.ogg"
    l "「嗯？」"
    y "「咱们这是去书店吧？」"
    show chara e11 #梁芷柔立绘|冬季私服|微笑
    with dissolve
    voice "audio/voice/004035.ogg"
    l "「是呀。」"
    y "「你又订了什么啊？」"
    show chara e09 #梁芷柔立绘|冬季私服|坏笑
    with dissolve
    voice "audio/voice/004036.ogg"
    l "「嘻嘻，你猜？」"
    y "「五什么三什么的那一摞吗？」"
    show chara e03 #梁芷柔立绘|冬季私服|生气
    with dissolve
    voice "audio/voice/004037.ogg"
    l "「哎哎哎，我还不至于对做题饥渴到这个份上哎！」"
    y "「那还能是什么啊……」"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/004038.ogg"
    l "「都是闲书啦，待会儿你就看到啦！」"
    y "「……」"
    y "「很多吗？」"
    show chara e13b #梁芷柔立绘|冬季私服|疑惑2
    with dissolve
    voice "audio/voice/004039.ogg"
    l "「嗯……不少吧，要不然干嘛抓你来呢？」"
    y "「要这么说的话，其实你跟店里说一声，我去取了回头给你带过去不就完了。」"
    show chara e05a #梁芷柔立绘|冬季私服|苦笑1
    with dissolve
    voice "audio/voice/004040.ogg"
    l "「那不合适吧……」"
    y "「这有啥不合适的，你还跟我客气这个。」"
    show chara e13a #梁芷柔立绘|冬季私服|疑惑1
    with dissolve
    voice "audio/voice/004041.ogg"
    l "「没有啊，我是在想，带着那么一堆闲书去学校的话会不会太招摇了？」"
    y "「……呃。」"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/004042.ogg"
    l "「嘻嘻，开玩笑啦，其实主要还是我等不及了嘛，想要今天就能看到。」"
    y "「所以说你到底都订了些什么啊……」"
    show chara e11 #梁芷柔立绘|冬季私服|微笑
    with dissolve
    voice "audio/voice/004043.ogg"
    l "「嗯？就是些小说啊剧本啊什么的……哎呀，马上就要到了，到时候你就知道了，别着急，啊。」"
    y "「因为我真的很好奇啊。」"
    show chara e13b #梁芷柔立绘|冬季私服|疑惑2
    with dissolve
    voice "audio/voice/004044.ogg"
    l "「为什么呀？」"
    y "「您老人家平时不都是订一堆参考书啊习题集啊什么的，然后再捎带几本课外读物嘛。」"
    show chara e13a #梁芷柔立绘|冬季私服|疑惑1
    with dissolve
    voice "audio/voice/004045.ogg"
    l "「嗯？嗯……好像，是吧。」"
    y "「所以说，『都是』闲书，还这么急着看，不奇怪吗？」"
    show chara e05b #梁芷柔立绘|冬季私服|苦笑2
    with dissolve
    voice "audio/voice/004046.ogg"
    l "「嗯……其实要说着急，倒也没急到那个份上。」"
    y "「哈？」"
    show chara e11 #梁芷柔立绘|冬季私服|微笑
    with dissolve
    voice "audio/voice/004047.ogg"
    l "「反正一会儿就能看到啦，多一点耐心不好吗？要知道心急吃不了热豆腐的。」"
    y "「……好好好，你说了算。」"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/004048.ogg"
    l "「嘻嘻。」"
    "梁芷柔一脸神神秘秘的，让我有些摸不到头脑。"
    "不过，以我对她的印象来看，多半是有什么猫腻在里面。"
    hide chara
    with dissolve
    "……算了，反正也快到了。"
    "就让我看看你葫芦里卖的是什么药吧！"
    stop music fadeout 2.5
    "……{p}…………"

    scene bg b09 #书店
    with fade
    play sound "audio/sound/effect11.ogg" noloop
    pause 1.5

    play sound "audio/sound/ambientnoise07.ogg" fadein 1.5 loop #书店环境噪音
    show charad sg04 #书店店员立绘|坏笑|远
    with dissolve
    voice "audio/voice/024001.ogg"
    d "「欢迎……哎哟，你们俩啊！」"
    "一进门，店员小姐就热情地迎了上来。"
    show charad g01 at left #书店店员立绘|普通
    show chara e11 at right #梁芷柔立绘|冬季私服|微笑
    with dissolve
    voice "audio/voice/004049.ogg"
    l "「对啊，抓了壮丁就来了。」"
    show charad g04 #书店店员立绘|坏笑
    with dissolve
    voice "audio/voice/024002.ogg"
    d "「嚯嚯……」"
    y "「……」"
    "店员小姐投来了意味深长的目光。"
    "……这种时候还是当做没看见吧。"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/024003.ogg"
    d "「好吧，你的书在这儿，你自己看吧。」"
    voice "audio/voice/024004.ogg"
    d "「……我反正是一个都不会念。」"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/004050.ogg"
    l "「好～好。」"
    hide chara
    hide charad
    with dissolve
    y "「……」"
    "店员小姐的外语水平不怎么样我是知道的，也就是说……"
    "难道都是外文书？"
    voice "audio/voice/004051.ogg"
    l "「嗯……我看看……」"
    voice "audio/voice/004052.ogg"
    l "「嗯嗯……嗯……应该是没错。」"
    y "「你到底买了啥啊？」"
    "我忍不住探头过去……"
    show chara le13a #梁芷柔立绘|冬季私服|疑惑1|近
    with dissolve
    "呜哇……满眼外文。"
#寻迹、寄甡
    y "「《A story of a song》《Symbiotic Love》……」"
#忆夏之铃、夏空的蒲公英、回忆忘却之匣
    y "「《Summer memory of bell》《Dandelions in the sky》《Memory Oblivion Box》……」"
#梦末、Leaflet、彷徨之街、我与我行将离去的小友
    y "「《Dream Ending》《Leaflet love story》《The Street of Adrift》《The Last Companion》……」"
    y "「……」"
    y "「…………」"
    y "「……你这是买了多少啊！？」"
    show chara le05a #梁芷柔立绘|冬季私服|苦笑1|近
    with dissolve
    voice "audio/voice/004053.ogg"
    l "「嘻嘻，打折嘛！」"
    y "「打折……这是把卖书的打死了吧……」"
    show chara le05a at right #梁芷柔立绘|冬季私服|苦笑1|近
    show charad lg02 at left #书店店员立绘|惊讶|近
    with dissolve
    voice "audio/voice/024005.ogg"
    d "「哎哎哎，我可还活得好好的！」"
    with hpunch
    "店员小姐和我也算很熟了，一边装作气愤的模样猛拍我的肩膀，一边见缝插针地推销商品。"
    show chara le13b #梁芷柔立绘|冬季私服|疑惑2|近
    show charad lg03 #书店店员立绘|笑容|近
    with dissolve
    voice "audio/voice/024006.ogg"
    d "「不过这一批确实是赶上了，都挺便宜的，我按二手价进的！你要是有兴趣也可以看看哦，我这儿有目录。」"
    y "「呃，谢谢，不用了……」"
    hide charad
    show chara le13b at truecenter #梁芷柔立绘|冬季私服|疑惑2|近
    with dissolve
    y "「所以咧？这都是些啥书啊？」"
    show chara le10 #梁芷柔立绘|冬季私服|开心|近
    with dissolve
    voice "audio/voice/004054.ogg"
    l "「都说了是闲书啊，小说啦，剧本啊什么的。」"
    y "「这全都是英文的？」"
    show chara le05a #梁芷柔立绘|冬季私服|苦笑1|近
    with dissolve
    voice "audio/voice/004055.ogg"
    l "「嗯，英文的……小说，和剧本。」"
    y "「……」"
    "虽然梁芷柔一再强调是闲书……但一般人是不会把纯外文读物当做消遣的吧？"
    "就算早有心理准备，还是多少被震到了。"
    show chara le11 #梁芷柔立绘|冬季私服|微笑|近
    with dissolve
    voice "audio/voice/004056.ogg"
    l "「我觉得你也可以试试看喔？要不要我借你两本？」"
    y "「还是算了吧，我晕英文。」"
    show chara le10 #梁芷柔立绘|冬季私服|开心|近
    with dissolve
    voice "audio/voice/004057.ogg"
    l "「少来啦，你什么情况我还不知道嘛！」"
    show chara le11 #梁芷柔立绘|冬季私服|微笑|近
    with dissolve
    voice "audio/voice/004058.ogg"
    l "「放心，其实真没那么难。」"
    y "「真不必了……我对那玩意有心理阴影……」"
    show chara le09 #梁芷柔立绘|冬季私服|坏笑|近
    with dissolve
    voice "audio/voice/004059.ogg"
    l "「哎？什么情况啊？来来来，说来听听。」"
    y "「其实也没啥，就是被某人恶心过，总觉得这个嘛……有点在装逼的感觉吧……」"
    show chara le13a #梁芷柔立绘|冬季私服|疑惑1|近
    with dissolve
    voice "audio/voice/004060.ogg"
    l "「哎？不是吧？谁啊……等等，不会是我吧？」"
    y "「不是不是不是不是，当然不是你了。」"
    y "「是咱们班那个冼望月。」"
    show chara le13b #梁芷柔立绘|冬季私服|疑惑2|近
    with dissolve
    voice "audio/voice/004061.ogg"
    l "「啊，他啊……他怎么你了？」"
    y "「那家伙的英文不是还不错吗？也不知道是真就觉得自己特有本事，还是怎么想的，反正特能吹。」"
    y "「他时不时的就爱跟我们念叨，啊，说英文原版的怎么怎么样，这个好那个不好的。」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/004062.ogg"
    l "「啊……」"
    y "「当时印象特深的是有一次我们一堆人出去喝酒，他喝多了，醉呼呼的，然后在那儿抓着我一个劲地念叨外文原版的事。」"
    y "「这也就罢了，最关键的是，他喜欢的书，恨不得给捧到天上去，不喜欢的书就说得好像一文不值似的。嗯，当时他推荐的那本书叫什么来着……？」"
    y "「《Ballade》？好像是吧，反正他张嘴就是这个这个写得怎么怎么不好，《Ballade》里就不会出现这样的问题；那个那个写得怎么怎么不好，《Ballade》里就不会出现这样的问题……」"
    y "「我估计原作者根本没想过的，他都能给吹爆了。」"
    show chara le05a #梁芷柔立绘|冬季私服|苦笑1|近
    with dissolve
    voice "audio/voice/004063.ogg"
    l "「呃……哈哈。这就是所谓的一粉顶十黑吧……」"
    y "「对吧，从那以后我听见外文原版就够了。」"
    show chara le13b #梁芷柔立绘|冬季私服|疑惑2|近
    with dissolve
    voice "audio/voice/004064.ogg"
    l "「嗯？等等，冼望月喝多了？」"
    y "「呃？」"
    show chara le02 #梁芷柔立绘|冬季私服|皱眉|近
    with dissolve
    voice "audio/voice/004065.ogg"
    l "「你说你们一堆人？出去喝酒了？什么时候的事啊？啊？都有谁啊？没有喝多了闹事吧？」"
    y "「……」"
    l "「……」"
    "糟糕……不小心说漏嘴了。"
    y "「呃……嗯……哈哈哈，那个，今天天气真好啊。」"
    show chara le03 #梁芷柔立绘|冬季私服|生气|近
    with dissolve
    voice "audio/voice/004066.ogg"
    l "「少～说～废～话……给我老实交代！」"
    with hpunch
    y "「哇啊！」"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"

    scene bg b08b #新城区|冬
    with fade
    pause 1.0
    scene bg b04c #滨河路|冬
    with fade
    pause 0.5
    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    "从书店出来之后，我们沿原路返回。"
    show chara se10 #梁芷柔立绘|冬季私服|开心|远
    with dissolve
    voice "audio/voice/004067.ogg"
    l "「♬～」"
    "梁芷柔迈着轻快的步伐，一边在前面走一边继续哼着她的小曲，拿到书似乎让她心情变得更好了。但这对于我来说就有点……"
    y "「……」"
    y "「我说大小姐您慢点走，我这儿拎着一堆书呢。」"
    show chara se09 #梁芷柔立绘|冬季私服|坏笑|远
    with dissolve
    voice "audio/voice/004068.ogg"
    l "「没事啦，待会儿我请你喝酒好不好，酒神？」"
    y "「哎哟喂你饶了我吧，那次我可真没喝多少哎！」"
    show chara se10 #梁芷柔立绘|冬季私服|开心|远
    with dissolve
    voice "audio/voice/004069.ogg"
    l "「嘿嘿。」"
    "梁芷柔回过身，狡黠地冲我笑笑。"
    show chara le11 #梁芷柔立绘|冬季私服|微笑|近
    with dissolve
    voice "audio/voice/004070.ogg"
    l "「好啦好啦，不玩你了。来，给我拿一半吧。」"
    y "「那倒不用，就是稍微走慢点就行了。」"
    show chara le01b #梁芷柔立绘|冬季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/004071.ogg"
    l "「嗯……好吧。」"
    "梁芷柔点点头，回到了我的身边，和我并肩而行。"
    hide chara
    with dissolve
    "记得最开始的时候，想帮她搬个书还得我自己抢着上。不过，如今的梁芷柔倒是已经不会再跟我那么客气了。"
    "这也算是关系变熟的一点体现了吧。"
    scene bg b04c #滨河路|冬
    with fade
    "……{p}…………"
    y "「我说啊。」"
    show chara le13b #梁芷柔立绘|冬季私服|疑惑2|近
    with dissolve
    voice "audio/voice/004072.ogg"
    l "「嗯？」"
    y "「今天你到底是过来干嘛来了？」"
    show chara le13a #梁芷柔立绘|冬季私服|疑惑1|近
    with dissolve
    voice "audio/voice/004073.ogg"
    l "「嗯，我啊，就是来取书呀，然后就是……」"
    show chara le12a #梁芷柔立绘|冬季私服|羞涩1|近
    with dissolve
    voice "audio/voice/004074.ogg"
    l "「嗯，来看看你。」"
    y "「哎？来看我？我有什么好看的……」"
    "有些摸不着头脑。虽然想到了梁芷柔应该是找我有什么事，但这个回答却总觉得有点微妙。"
    show chara le08b #梁芷柔立绘|冬季私服|担心2|近
    with dissolve
    voice "audio/voice/004075.ogg"
    l "「嗯……我问你啊，你今天都干什么了？」"
    y "「干什么……没干什么啊，睡醒了吃早饭，然后看书，再往后就被你叫出来了……」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/004076.ogg"
    l "「就这些？」"
    y "「就这些啊，不然还能干什么……」"
    show chara le05a #梁芷柔立绘|冬季私服|苦笑1|近
    with dissolve
    voice "audio/voice/004077.ogg"
    l "「没想过出去玩玩嘛？或者看看小说，玩会儿电脑什么的。」"
    y "「哎，哪还有那功夫啊。」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/004078.ogg"
    l "「嗯～～」"
    show chara le05b #梁芷柔立绘|冬季私服|苦笑2|近
    with dissolve
    voice "audio/voice/004079.ogg"
    l "「这可不好啊，休息日还是得放松放松的。」"
    y "「哎哟？」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/004080.ogg"
    l "「怎么啦？」"
    y "「我的妈呀，这还真是……够稀奇的。」"
    show chara le02 #梁芷柔立绘|冬季私服|皱眉|近
    with dissolve
    voice "audio/voice/004081.ogg"
    l "「我说这话奇怪吗？」"
    y "「奇怪吧？你自己不就是个现成的反例……」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/004082.ogg"
    l "「谁说的啊，我可是该学习的时候专心学习，该休息的时候就好好休息的。」"
    voice "audio/voice/004083.ogg"
    l "「要不然，你以为你手里抱着的是什么？」"
    y "「英文教材？」"
    show chara le03 #梁芷柔立绘|冬季私服|生气|近
    with dissolve
    voice "audio/voice/004084.ogg"
    l "「呸！学英语那是顺便的事，按您这位酒神的话说，就是喝完白的，来两瓶啤的漱漱口。」"
    y "「呃……」"
    "……我好像还真说过类似的话，而且也是在差不多这样的场景下来着。"
    show chara le08a #梁芷柔立绘|冬季私服|担心1|近
    with dissolve
    voice "audio/voice/004085.ogg"
    l "「但我不会把自己整天都泡在酒缸里，对不对？那样只能把自己给淹死了。」"
    y "「……」"
    show chara le08b #梁芷柔立绘|冬季私服|担心2|近
    with dissolve
    voice "audio/voice/004086.ogg"
    l "「……唉。」"
    show chara le08a #梁芷柔立绘|冬季私服|担心1|近
    with dissolve
    voice "audio/voice/004087.ogg"
    l "「你呀，最近每天几点睡觉啊？」"
    y "「啊？」"
    show chara le03 #梁芷柔立绘|冬季私服|生气|近
    with dissolve
    voice "audio/voice/004088.ogg"
    l "「几点睡？回家以后复习到几点？」"
    y "「……」"
    show chara le07b #梁芷柔立绘|冬季私服|消沉2|近
    with dissolve
    voice "audio/voice/004089.ogg"
    l "「你自己没注意吗？你最近……总是特别疲惫。」"
    "说到这里，梁芷柔已经变得很认真了。"
    y "「啊……」"
    "原来如此。"
    "这也难怪，昨天那个样子，当然会被她注意到。"
    "不过……这里还是蒙混过去比较好。"
    y "「我……还好吧。」"
    show chara le07a #梁芷柔立绘|冬季私服|消沉1|近
    with dissolve
    voice "audio/voice/004090.ogg"
    l "「……还嘴硬。」"
    y "「这……不是，我……这不就是昨天在上课的时候睡了个觉嘛，打个呼噜而已，不用追到家里来训我吧。」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/004091.ogg"
    l "「……我没有在训你，我也不是在说昨天那一件事。」"
    show chara le02 #梁芷柔立绘|冬季私服|皱眉|近
    with dissolve
    voice "audio/voice/004092.ogg"
    l "「你最近……一直就有点不太对劲。」"
    y "「我……怎么了？」"
    show chara le08b #梁芷柔立绘|冬季私服|担心2|近
    with dissolve
    voice "audio/voice/004093.ogg"
    l "「你突然在特别努力地学习。」"
    y "「努力学习……不好啊？」"
    show chara le08a #梁芷柔立绘|冬季私服|担心1|近
    with dissolve
    voice "audio/voice/004094.ogg"
    l "「好是好，可是，你太努力了，努力过头了。」"
    show chara le02 #梁芷柔立绘|冬季私服|皱眉|近
    with dissolve
    voice "audio/voice/004095.ogg"
    l "「你是以为我看不出来吗？别忘了啊，你遇到的问题还都是我给你解答的呢，我可能什么都没有注意到吗？」"
    y "「我这不是为了实现那个小目标嘛……这还是你给我定的。」"
    show chara le07b #梁芷柔立绘|冬季私服|消沉2|近
    with dissolve
    voice "audio/voice/004096.ogg"
    l "「……要真是这样，那倒简单了。」"
    show chara le02 #梁芷柔立绘|冬季私服|皱眉|近
    with dissolve
    voice "audio/voice/004097.ogg"
    l "「可是，你具体什么想法我不敢说，但肯定不是因为那个小目标。」"
    "梁芷柔摇了摇头，轻声，但却直截了当地戳穿了我的伪装。"
    show chara le12a #梁芷柔立绘|冬季私服|羞涩1|近
    with dissolve
    voice "audio/voice/004098.ogg"
    l "「雨潇……」"
    voice "audio/voice/004099.ogg"
    l "「你到底是怎么想的？」"
    y "「……」"
    voice "audio/voice/004100.ogg"
    l "「如果……如果是因为上次……」"
    stop sound fadeout 3.0

    y "「……芷柔。」"
    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    show chara le12b #梁芷柔立绘|冬季私服|羞涩2|近
    with dissolve
    voice "audio/voice/004102.ogg"
    l "「啊！？」"
    "我突然打断了她的话。"
    show chara le12a #梁芷柔立绘|冬季私服|羞涩1|近
    with dissolve
    "骤然被我直呼其名，梁芷柔似乎吓了一跳，说到一半的话也给惊得吞了回去，狐疑地看着我。"
    "不过，我在这里打断她，并不是为了否认什么，而是因为……「这件事」，是我自己主动想要做的事情。"
    "我不再像从前那样，需要被人推着、拖着，才肯挪上一挪。"
    "所以，有些话，应该、也必须由我自己说出来。"
    y "「……」"
    y "「……对不起。」"
    show chara le12b #梁芷柔立绘|冬季私服|羞涩2|近
    with dissolve
    voice "audio/voice/004103.ogg"
    l "「哎？」"
    y "「我之前……太天真，好多事想得太简单了，幼稚。」"
    y "「说到底，我一点都没经历过，也就一直都不理解，现在想想，自己还老是大言不惭的，真的是……哎。」"
    y "「上次跟你说了半天，结果南辕北辙的，一点意义都没有……抱歉。」"
    y "「所以……那次，从那之后，有些事我想了想，想明白了。」"
    y "「我不想再跟以前似的那样了……」"
    y "「我……也想去试一试。」"
    show chara le12a #梁芷柔立绘|冬季私服|羞涩1|近
    with dissolve
    voice "audio/voice/004104.ogg"
    l "「嗯……」"
    y "「呵，过程肯定不会太顺利，也肯定少不了继续麻烦你，不过，我决定了。」"
    y "「这是我自己做出的决定。虽然不能说跟你没关系吧……但是，这确确实实是我自己的想法，也必须要我自己去找答案。」"
    y "「所以，这一次，我会拼尽我的全力。」"
    y "「这一次考试，是我要迈过的第一道坎。把它迈过去，我才能找到自己的方向，才能知道自己未来该往什么地方努力。」"
    y "「只有到了那个时候，我才能回答你，你刚才的这个问题。」"
    y "「……所以，你能等一下吗？」"
    y "「等到，那个时候……」"
    show chara le12b #梁芷柔立绘|冬季私服|羞涩2|近
    with dissolve
    l "「……」"
    y "「……」"
    "话说完了，我等待着梁芷柔的答复。"
    "心里……七上八下的，其实一点也不像表现的那么淡定。"
    "毕竟，这个时机实在是……不怎么样。"
    "处心积虑了半天，结果早早的就被当事人一眼戳穿，如果以阴谋家的标准来评判，简直是烂到家了。"
    "但我也确实没想到梁芷柔会如此敏锐，或者说，她会如此……关注我。"
    "也不知道是该高兴还是怎样。"
    l "「……」"
    show chara le12a #梁芷柔立绘|冬季私服|羞涩1|近
    with dissolve
    voice "audio/voice/004105.ogg"
    l "「…………嗯。」"
    "梁芷柔欲言又止，犹豫了几次，最后只是轻轻嗯了一声。"
    "看不出很明显的情绪，但……至少不算坏。"

    show chara le12b #梁芷柔立绘|冬季私服|羞涩2|近
    with dissolve
    voice "audio/voice/004106.ogg"
    l "「你呀……也真是的。」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/004107.ogg"
    l "「咳咳！既然你都说到这个份上了，那我现在也就不多说什么了。」"
    voice "audio/voice/004108.ogg"
    l "「……等到这次考完试之后，再一起和你算总账。」"
    y "「嘿嘿。」"
    stop music fadeout 3.0
    show chara le03 #梁芷柔立绘|冬季私服|生气|近
    with dissolve
    voice "audio/voice/004109.ogg"
    l "「但！是！有一点！」"
    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    y "「……嗯？」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/004110.ogg"
    l "「你这次的隐瞒不报让我很不爽啊，我要求你立即补偿我。」"
    y "「这……」"
    y "「你要怎么补偿啊？」"
    show chara le01b #梁芷柔立绘|冬季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/004111.ogg"
    l "「第一，继续帮我把书搬到车站去，这次我可不会跟你客气什么了。」"
    y "「成成成，这不是事儿。本来也是要去的。」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/004112.ogg"
    l "「第二，我要你答应我一件事，现在、立刻、无条件去做。」"
    y "「啊？」"
    show chara le03 #梁芷柔立绘|冬季私服|生气|近
    with dissolve
    voice "audio/voice/004113.ogg"
    l "「听见没有？」"
    y "「……好好好，您说了算，啥都听你的。」"
    y "「说吧，什么事？」"
    show chara le11 #梁芷柔立绘|冬季私服|微笑|近
    with dissolve
    voice "audio/voice/004114.ogg"
    l "「求我。」"
    y "「……」"
    y "「…………啊？」"
    show chara le09 #梁芷柔立绘|冬季私服|坏笑|近
    with dissolve
    voice "audio/voice/004115.ogg"
    l "「求我啊。求我告诉你怎么才能更好地安排时间，怎么一边保证休息时间一边挤出时间来学习呀？」"
    y "「喂！」"
    show chara le10 #梁芷柔立绘|冬季私服|开心|近
    with dissolve
    voice "audio/voice/004116.ogg"
    l "「嘻嘻。」"
    "这家伙……自己已经忍不住笑出声来了啊。"
    "一时无语。"
    "但……"
    y "「……呵……呵呵。」"
    "紧接着，我也忍不住和她一起笑了起来。"
    y "「唉，我费了多大的劲才把气氛煽起来啊，全毁了。」"
    show chara le11 #梁芷柔立绘|冬季私服|微笑|近
    with dissolve
    voice "audio/voice/004117.ogg"
    l "「那我不管，你说的啊，少不了要麻烦我的。」"
    y "「好吧好吧，那怎么着，需要我跪下嘛？」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/004118.ogg"
    l "「嗯……为了不让你把我的书弄脏，免了吧。」"
    y "「那还真得谢谢您了啊……」"
    show chara le10 #梁芷柔立绘|冬季私服|开心|近
    with dissolve
    voice "audio/voice/004119.ogg"
    l "「哪里哪里。赶快的！」"
    y "「成吧……」"
    y "「咳！嗯……求您了，善良的班长大人，告诉我安排作息的诀窍吧！求求你！」"
    show chara le09 #梁芷柔立绘|冬季私服|坏笑|近
    with dissolve
    voice "audio/voice/004120.ogg"
    l "「很好。那我就大发慈悲地告诉你吧！」"
    y "「……」"
    y "「呵……」"
    show chara le13b #梁芷柔立绘|冬季私服|疑惑2|近
    with dissolve
    voice "audio/voice/004121.ogg"
    l "「……？」"
    y "「……谢谢你，真的。谢谢你。」"
    l "「……」"
    hide chara
    with dissolve
#考虑追加CG
    "面对我由衷的感激，梁芷柔如同迈着舞步一般，轻巧地转身，留给我一个背影。"
    voice "audio/voice/004122.ogg"
    l "「呵……不客气。」"
    voice "audio/voice/004123.ogg"
    l "「不过……」"
    voice "audio/voice/004124.ogg"
    l "「……不许让我失望啊。」"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t07 #转场 滨河路
    with fade
    pause

#12月上旬。
#第一次模拟诊断考试。

    scene bg b02c #城区|冬
    with fade
    pause 1.0
    scene bg b11 #考场
    with fade
    pause 0.5
    play music "audio/music/bgm04.ogg" fadein 0.5 #冬～苍雪～
    y "「呼……」"
    "半个月的时间转瞬即过，第一次模拟诊断考试的日子终于到来了。"
    "按照规定，这种正式的模拟考试需要变更考场，所以……"
    y "「怎么样，重回初中母校的感觉？」"
    show chara lb13a #梁芷柔立绘|冬季校服|疑惑1|近
    with dissolve
    voice "audio/voice/004125.ogg"
    l "「嗯……老样子？或者说更破了吧……」"
    y "「哎哟，这让你以前的老师，还有那些被教育要向你学习、打败一中的后辈们听见了可怎么得了。」"
    show chara lb02 #梁芷柔立绘|冬季校服|皱眉|近
    with dissolve
    voice "audio/voice/004126.ogg"
    l "「本来就是嘛，再说了，咱们学校不也一样好不到哪去嘛……」"
    y "「那倒也是。」"
    hide chara
    with dissolve
    "我们这次的考场被安排在了县二中，也就是梁芷柔初中时的学校。"
    "历经了长年累月的竞争，两所学校之间的仇恨早已不可磨灭，在进门的时候，我没少收到二中老师们充满蔑视的白眼。"
    show chara lb13b #梁芷柔立绘|冬季校服|疑惑2|近
    with dissolve
    "不过，另一个人的待遇就不一样了。"
    "说起来，梁芷柔当年的同学倒是大半升到了二中，只是这个时候都被发配到其他学校考试去了，反而没几个熟人。"
    "但同学不在，老师却还是原来的那些，一见到她，全都大惊小怪地围了上来，问长问短，那样子几乎比亲闺女还亲。"
    "直到进入考场，都还有老师依依不舍地在门口伸头往里看。"
    y "「倒是没想到，三年过去了，你还是很受欢迎哈。」"
    show chara lb13a #梁芷柔立绘|冬季校服|疑惑1|近
    with dissolve
    voice "audio/voice/004127.ogg"
    l "「嗯……毕竟我让他们成为『中考状元的老师』嘛，还有职称。」"
    "哇……真现实。"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/004128.ogg"
    l "「先别说这个，你呢，你怎么样？昨天睡得好不好？」"
    y "「没问题，放心吧。」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/004129.ogg"
    l "「可别在考场上睡过去啊！」"
    y "「哎哟不会啦。小的谨遵您老人家的懿旨，休息得可好了。」"
    show chara lb03 #梁芷柔立绘|冬季校服|生气|近
    with dissolve
    voice "audio/voice/004130.ogg"
    l "「很好。」"
    "梁芷柔装模作样地点点头……"
    show chara lb10 #梁芷柔立绘|冬季校服|开心|近
    with dissolve
    voice "audio/voice/004131.ogg"
    l "「嘻嘻……」"
    "然后就扑哧一声笑了出来。"
    y "「你看看，又笑场了。你行不行啊？」"
    show chara lb09 #梁芷柔立绘|冬季校服|坏笑|近
    with dissolve
    voice "audio/voice/004132.ogg"
    l "「嗯，呵呵……」"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/004133.ogg"
    l "「加油。」"
    y "「……」"
    y "「嗯！」"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……{p}…………"

    scene bg b11 #考场
    with fade
    play sound "audio/sound/effect10.ogg" fadein 0.5 loop #写字声
    y "「（唔……）」"
    "第一科考的是语文。"
    "虽然是理科生，不过我的语文还算可以。"
    y "「（下列句子中，成语使用不恰当的一项是……）」"
    y "「（针对我国一些地方炫耀消费……蔚为大观……？什么鬼……就是你了……）」"
    "感觉题目倒是不算很难。"
    "不过……越是这种时候越需要集中注意力，避免在阴沟里翻船。"
    "……{p}…………"
    y "「（填写原文……）」"
    y "「（于嗟鸠兮？嗯，无食桑葚吧……）」"
    "……{p}…………"
    y "「（翱至零口北，有畜鸡二十二者……哎哟，《截冠雄鸡志》啊。）」"
    y "「（前两天刚好看过来着……运气不错啊……）」"
    "……{p}…………"
    scene bg black #黑屏
    with fade
    play sound "audio/sound/effect06.ogg" noloop
    pause 1.0
    scene bg b11 #考场
    with fade
    "第一场考试结束了。"
    voice "audio/voice/004134.ogg"
    l "「嗯～～」"
    y "「哟，怎么样……我说不是吧？你这是刚睡醒还是怎么的？」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/004135.ogg"
    l "「得了吧你，哪有那么夸张啊，伸了个懒腰而已嘛。」"
    y "「跟举手投降似的。」"
    show chara lb09 #梁芷柔立绘|冬季校服|坏笑|近
    with dissolve
    voice "audio/voice/004136.ogg"
    l "「哼！少废话！」"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/004137.ogg"
    l "「考得怎么样？」"
    y "「嗯，语文嘛，还好吧。而且这次运气不错，不少题以前都见过。」"
    show chara lb13b #梁芷柔立绘|冬季校服|疑惑2|近
    with dissolve
    voice "audio/voice/004138.ogg"
    l "「嗯？是么……」"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/004139.ogg"
    l "「呵呵，我想大概不是运气吧……」"
    "梁芷柔露出一个意味深长的笑容。"
    show chara lb10 #梁芷柔立绘|冬季校服|开心|近
    with dissolve
    voice "audio/voice/004140.ogg"
    l "「下午数学也要加油啊。」"
    y "「那是，这还用说。」"
    y "「倒是你啊，昨天睡得好不好？可别在考场上睡过去啊！」"
    show chara lb12a #梁芷柔立绘|冬季校服|羞涩1|近
    with dissolve
    voice "audio/voice/004141.ogg"
    l "「呸呸呸，去去去，你个小心眼。」"
    show chara lb03 #梁芷柔立绘|冬季校服|生气|近
    with dissolve
    voice "audio/voice/004142.ogg"
    l "「而且我没睡觉！」"
    y "「哈哈……好吧好吧……」"
    y "「咱俩都加油！」"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b11 #考场
    with fade
    play sound "audio/sound/effect10.ogg" fadein 0.5 loop #写字声
    "……数学。"
    "理科班重中之重的一门课程。"
    "尴尬的是，数学是我以往问题最大的一科。"
    "虽然经过了恶补，但究竟改善到了什么程度，还需要这一次的考试来检验。"
    y "「……」"
    y "「（抛物线x方等于4y上的点到其焦点的最短距离为……）」"
    y "「（焦点坐标P……抛物线点Q……Q到P等于Q到y等于负1……所以是1吗……）」"
    y "「（已知m，4，n是等差数列，那么根2的m次方乘根2的n次方等于……）」"
    y "「（16嘛……mn的最大值……还是16嘛……）」"
    "似乎……数学也比想象中的要容易一些嘛。"
    "大概是因为有很多题型已经在之前的练习中见识过了吧……至少思路上还是比较清楚的。"
    y "「（直角梯形ABCD，AD平行于BC，AD垂直于DC，BC等于2AD等于2DC……四边形ABEF是正方形……ABEF沿AB折起……）」"
    y "「（第一，求证BE1垂直于DC……）」"
    y "「（唔……）」"
    y "「（因为ABE1F1为正方形，所以BE垂直于AB……因为ABCD垂直于ABE1F1，ABCD交ABE1F1等于AB……BE属于ABE1F1……）」"
    "进入了解答大题的阶段。"
    "有些地方需要多想一想才能动笔，不过总体上答题还算顺畅。"
    y "「……」"
    "果然是题目比较简单吗……"
    y "「……」"
    "……不对。"
    stop sound fadeout 0.5
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/004139.ogg"
    l "「呵呵，我想大概不是运气吧……」"
    play sound "audio/sound/effect10.ogg" fadein 0.5 loop #写字声
    scene bg b11 #考场
    with fade
    y "「……」"
    "是了，原来如此。"
    "不是题出得简单了，而是我的水平，比我以为的提升得更快了一些。"
    y "「（是了……）」"
    "是因为……我前一段时间的努力。"
    "我前一段时间所付出的努力……是确确实实有效果的。"
    stop sound fadeout 0.5
    scene bg b04c #滨河路|冬
    show chara le12a #梁芷柔立绘|冬季私服|羞涩1|近
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/004098.ogg"
    l "「雨潇……」"
    voice "audio/voice/004099.ogg"
    l "「你到底是怎么想的？」"
    play sound "audio/sound/effect10.ogg" fadein 0.5 loop #写字声
    scene bg b11 #考场
    with fade
    "或许，现在的我，已经可以回答那时的问题了。"
    y "「（尽管我们之间的差距依然巨大……）」"
    y "「（但是……）」"
    y "「（我要缩短它……我会缩短它，不断地缩短它……）」"
    y "「（直到……）」"
    stop sound fadeout 1.5

    scene bg black #黑屏
    with fade
    pause 1.0

    play sound "audio/sound/transition.ogg" noloop
    scene trans t09 #转场 考场
    with fade
    pause

#12月中旬。
#公布第一次模拟诊断考试成绩。

    scene bg b04c #滨河路|冬
    with fade
    "几天后。"
    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音

    y "「呼……」"
    y "「哎呀，真冷……」"
    "我呵出一口哈气，搓了搓手。"
    "进入了12月以后，气温明显下降，每天的最高气温也仅仅止步于冰点附近而已，更不用说太阳初升的现在了。"
    "不，算上和东部地区的时差，现在其实应该还算是在夜里才对。"
    "路上看不到多少行人。这个时间段本来也不是上班的高峰，甚至大多数人都还没有起床呢吧。"
    "备考生就是苦啊……"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b05b #湿地公园|冬
    with fade
    y "「……」"
    "默默地朝着学校的方向前进。"
    "路过湿地公园的时候，我朝里面看了看。"
    "现在……这里还只是一片平静的河滩。"
    "天空中偶尔传来几声鸟鸣，显得有些清冷。"
    "不过……"
    y "「……」"
    y "「待会儿……」"
    y "「……应该会挺热闹的吧。」"
    stop sound fadeout 3.0
    "……{p}…………"

    scene bg b01 #教室
    with fade
    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    "早自习。"
    "往常基本上都很安静的教室，今天却充满了嘈杂的交谈声。"
    e "「叽叽喳喳叽叽喳喳叽叽喳喳……」"
    e "「喳喳叽叽喳喳叽叽喳喳叽叽……」"
    show chara b03 #梁芷柔立绘|冬季校服|生气
    with dissolve
    voice "audio/voice/004143.ogg"
    l "「……咳咳！」"
#【声音减弱】
    e "「……」"
    l "「……」"
    "在班长大人的瞪视下，一众人等似乎略有收敛，然而……"
#【声音增大】
    e "「叽叽喳喳叽叽喳喳叽叽喳喳……」"
    "很快就故态复发了。"
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    voice "audio/voice/004144.ogg"
    l "「唉……」"
    "果然，就算是梁芷柔，面对这种场面也是无能为力的。毕竟……"
    "有道是，山雨欲来风满楼。"

    scene bg b01 #教室
    with fade
    "……{p}…………"
    "早自习就在一片嘈杂声之中度过了。"
    "然而，随着正式上课的时间的临近，班里非但没有平静下来，反而变得更加吵闹。"
    e "「叽叽喳喳叽叽喳喳叽叽喳喳……」"
    play audio "audio/sound/effect22.ogg" noloop
    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/014004.ogg"
    z "「……嗯？」"
    stop sound fadeout 3.0
    e "「……」"
    "老师到来的一瞬间，就好像什么地方有个静音键被按下去了似的，所有的噪音都突然被终结了。"

    play music "audio/music/bgm06.ogg" fadein 1.5 #悬而未决
    "整个班里弥漫着一股诡异的气氛。"
    "所谓……人心惶惶。"
    show charaz h01a #老师立绘|冬季|普通
    with dissolve
    z "「……」"
    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/014005.ogg"
    z "「咳！」"
    "班主任……也毫不客气，起手式就是一个虎躯一震的大招。"
    "管不管用姑且不论，但看得出来他不怎么高兴。"
    "大概有些人要倒霉了吧。"
    stop music fadeout 2.5

    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/014006.ogg"
    z "「废话不多说了啊！这次模拟诊断考试都考成了什么样子，看来你们自己也多少有点底了吧，啊？反正我话说在前头，你们有些人呢，要是觉得这样下去也成，那就继续这么混，啊，一直混到高考也没关系……」"
    show charaz h04a #老师立绘|冬季|咆哮
    with dissolve
    voice "audio/voice/014007.ogg"
    z "「但是呢，你们要想好好学，那就自己好好想想，想想该怎么做！啊？」"
    voice "audio/voice/014008.ogg"
    z "「结果呢？你们倒好啊，你们看看你们都考得是什么呀，啊！再这么下去，一中的脸都给你们丢光了！」"
    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/014009.ogg"
    z "「……我告诉你们啊，这次考试，咱们班不是没有考得好的，进步很多的。但是大多数人，我都不能说满意！你们自己掂量着办，啊！接下来呢，我叫到名字的，上来拿成绩单。」"
    y "「（……呼。）」"
    "我轻轻呼出一口气。"
    "揭开答案的时刻到来了。"
    "我们第一次模拟诊断考试的成绩，即将公布。"
    show charaz h01a #老师立绘|冬季|普通
    with dissolve
    voice "audio/voice/014010.ogg"
    z "「梁芷柔。」"
    hide charaz
    show chara b01a #梁芷柔立绘|冬季校服|普通|正面
    with dissolve
    voice "audio/voice/004145.ogg"
    l "「到。」"
    hide chara
    show charaz h02a #老师立绘|冬季|微笑
    with dissolve
    voice "audio/voice/014011.ogg"
    z "「来。」"
    "第一个被叫到的人，不出所有人意料，当然是梁芷柔。"
    "不过班主任一反刚才咆哮的姿态，把音调降低了差不多两个八度，转换成了温柔得几乎不像话的语气。"
    show charaz h01a #老师立绘|冬季|普通
    with dissolve
    voice "audio/voice/014012.ogg"
    z "「语文118，数学141，英语142，理综260，总分661。」"
    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    "听到这个成绩，班里骤然爆出一阵短暂的议论声。"
    "尽管早就该见怪不怪了，不过在比较正式、重要的考试中拿到这个分数，还是会让人感慨不已。"
    stop sound fadeout 3.0
    show charaz h02a #老师立绘|冬季|微笑
    with dissolve
    voice "audio/voice/014013.ogg"
    z "「考得不错，还有上升的空间，啊。时间还有一些，以全省为目标，继续努力。」"
    hide charaz
    show chara b01a #梁芷柔立绘|冬季校服|普通|正面
    with dissolve
    voice "audio/voice/004146.ogg"
    l "「好的。」"
    hide chara
    show charaz h01a #老师立绘|冬季|普通
    with dissolve
    z "「……」"
    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/014014.ogg"
    z "「你们看看啊？咱们班上也不是没有榜样对不对？我也不是说，你们一定要学到人家那个水平，啊，那是难为你们了！但是啊，能追多少是多少啊？」"
    "这也同样算是见怪不怪了……我们的班主任几乎不会放过任何赞扬梁芷柔的机会。"
    "同学们纷纷点头称是，不过大多数人就都心不在焉了。"
    voice "audio/voice/014015.ogg"
    z "「唉，我跟你们说啊，你们还别听不进去，知道吗！咱们班这次就有一个现成的例子。」"
    "老师似乎也感受到了班上同学的敷衍，很不满意地打算举个例子来佐证自己的言论。"
    show charaz h04a #老师立绘|冬季|咆哮
    with dissolve
    voice "audio/voice/014016.ogg"
    z "「叶雨潇！」"
    with hpunch
    y "「——！」"
    play sound "audio/sound/effect23.ogg" loop
    hide charaz
    with dissolve
    "虽然多少已经有了心理准备，但真的被点到名字的时候，还是忍不住紧张了一下。"
    y "「（冷静，冷静！）」"
    y "「（吸——）」"
    stop sound fadeout 3.0
    y "「……到。」"
    "我深吸了一口气，站起身来应答。"
    "伴随着我的起立，班上同学们略显好奇的目光也都纷纷向我集中过来。"
    scene cg01b4 #梁芷柔听讲CG-2|眼睛向后瞟视|冬装|CG01b4
    with dissolve
    l "「……」"
    "就连梁芷柔也忍不住侧目。"
    scene bg b01 #教室
    with fade
    y "「（那么，接下来……）」"
    "决定性的时刻到来了。"
    show charaz h01a #老师立绘|冬季|普通
    with dissolve
    voice "audio/voice/014017.ogg"
    z "「语文114，数学108，英语103，理综215，总分540。」"
    with vpunch
    y "「（……呼！）」"
    "我悄悄地握了一下拳。"
    l "「……」"
    play sound "audio/sound/ambientnoise09.ogg" fadein 2.0 loop #人群嘈杂环境噪音
    e "「——！？」"
    e "「叽叽喳喳叽叽喳喳叽叽喳喳……」"
    "在短暂的沉默之后，班上小小地炸了一回锅。"
    "大多数的人都把目光集中到了我的身上，也有一些人去看其他几个成绩靠前的学生。"
    "看来这帮家伙是大吃了一惊。毕竟，即便是高考，这也是个稳过一本线的成绩了。"
    stop sound fadeout 3.0
    "虽然，对于我……和她来说，只能算是一个完成得不错的「小目标」而已……"
    show charaz h02a #老师立绘|冬季|微笑
    with dissolve
    voice "audio/voice/014018.ogg"
    z "「来。」"
    "班主任用仅次于对待梁芷柔的语气招呼我上到讲台边。"
    show charaz lh01a #老师立绘|冬季|普通|近
    with dissolve
    voice "audio/voice/014019.ogg"
    z "「叶雨潇以前什么情况你们都清楚。人聪明，底子不错，就是呢，不好好学习，啊，白白浪费了这么好的条件。但是呢，人家现在知道努力了，对不对？你们说，这个学期他的成绩提高了多少啊？」"
    show charaz lh03a #老师立绘|冬季|皱眉|近
    with dissolve
    voice "audio/voice/014020.ogg"
    z "「所以啊，有志者事竟成！只要肯学，就没有不进步的，知不知道啊！来，叶雨潇，你给大家讲讲，这个学期会这么努力，你是怎么想的啊？」"
    y "「咦？」"
    show charaz lh02a #老师立绘|冬季|微笑|近
    with dissolve
    voice "audio/voice/014021.ogg"
    z "「咳，别害羞，啊！好事嘛，有什么好害羞的。你呢，就给同学们讲讲，你为什么要努力！」"
    y "「这……」"
    "稍微迟疑了一下。"
    "多年养成的泯然于众的习惯，让我多少还是有些犹豫…{cps=2}…不{/cps}过，算了，管他呢？"
    "难得有这么好的一个机会，此时不说，更待何时？"

    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.

    hide charaz
    with dissolve
    "我点了点头，转过身。"
    "正面迎向班上的同学们。"
    show chara lb13b #梁芷柔立绘|冬季校服|疑惑2|近
    with dissolve
    "以及……她。"
    l "「……」"
    y "「……」"
    "梁芷柔也在看着我。"
    hide chara
    with dissolve
    "深深吸气。"
    "虽然班主任阴差阳错地说了句「有什么好害羞的」，不过那是他不知道我想要说什么。不知道再过几秒钟，他会不会暴跳如雷地想要把我活撕了？"
    "不管了。"
    y "「呼……」"
    "我将胸中的郁气尽数吐出。"
    y "「梁芷柔。」"
    show chara lb13a #梁芷柔立绘|冬季校服|疑惑1|近
    with dissolve
    voice "audio/voice/004147.ogg"
    l "「哎？」"
    hide chara
    show charaz lh03a #老师立绘|冬季|皱眉|近
    with dissolve
    voice "audio/voice/014022.ogg"
    z "「啊？」"
    hide charaz
    with dissolve
    e "「……！？」"
    show chara lb13a #梁芷柔立绘|冬季校服|疑惑1|近
    with dissolve
    y "「我要——」"
    with vpunch
    y "「追上你！！！」"
    show chara lb12a #梁芷柔立绘|冬季校服|羞涩1|近
    with dissolve
    pause 0.2
    show chara lb12b #梁芷柔立绘|冬季校服|羞涩2|近
    with dissolve
    l "「——！」"
    "……{p}…………"
    scene bg b00 #天空
    with dissolve
    with vpunch
    play sound "audio/sound/effect25.ogg" noloop
    e "「——轰！」"
    pause 2.0
    "就这样。"
    "在那一天，县一中有史以来最大的话题诞生了。"
    stop music fadeout 1.5
    scene bg black #黑屏
    with fade
    pause 0.5

    play sound "audio/sound/transition.ogg" noloop
    scene trans t01 #转场 教室
    with fade
    pause

#05.早春

    $ chapter = "05"

#1月中旬。

    scene bg b00 #天空
    with fade
    play sound "audio/sound/ambientnoise04.ogg" fadein 1.5 loop #白天环境噪音
    "时光飞逝。"
    "第一次模拟诊断考试过去一个多月了，如今已经是一月的中旬，期末考试马上就要到了。"
    "换句话说，再过几天，我就将迎来高中生涯里最后的假期。"
    scene bg b01 #教室
    with fade
    stop sound fadeout 3.0
    "……"
    play music "audio/music/bgm11.ogg" fadein 1.5 #风轻云淡
    "…………"
    y "「唉……」"
    y "「……啊……」"
    y "「嗯………………」"
    "用下巴戳着课本，把自己挂在课桌上，无力地发出意义不明的呻吟声。"
    "真是累啊……好想睡觉啊……"
    y "「……」"
    y "「唉。」"
    "相比起第一次诊断模拟考试时班上的紧张气氛，期末考试显得波澜不惊。毕竟是学校自己组织的考试，与全省的统考没法比。"
    "但我并没有松懈的资本。"
    "之前的「小目标」仅仅只是个开始。当我真正开始直面考验的时候，才理解到自己差了多少东西。"
    "所以，从一模考试结束以后到现在的这一个月，尽管不会再像之前那样拼命压榨自己，但我依然不敢有丝毫放松。"
    "我非常清楚，留给我的时间……不多了。"
    y "「……」"
    voice "audio/voice/005001.ogg"
    l "「哟！」"
    show chara lb10 #梁芷柔立绘|冬季校服|开心|近
    with dissolve
    "耳边传来了熟悉的声音。"
    y "「哎……？」"
    y "「啊……你啊。」"
    show chara lb09 #梁芷柔立绘|冬季校服|坏笑|近
    with dissolve
    voice "audio/voice/005002.ogg"
    l "「嗯。怎么啦，无病呻吟哪？」"
    y "「是啊，累死了。」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/005003.ogg"
    l "「……唉。」"
    "梁芷柔一脸无可奈的模样。"
    "大概是我这幅仰着头百无聊赖地瘫在椅子背上的模样，实在是太难看了吧。"
    show chara lb02 #梁芷柔立绘|冬季校服|皱眉|近
    with dissolve
    voice "audio/voice/005004.ogg"
    l "「行啦行啦，这也没几天了，到时候你就可以解脱啦。」"
    y "「算了吧，我早就不对寒假报什么期望了，我不信你没安排。」"
    show chara lb10 #梁芷柔立绘|冬季校服|开心|近
    with dissolve
    voice "audio/voice/005005.ogg"
    l "「哎哟，觉悟不错嘛？」"
    y "「哀大莫过于心死嘛，当然往好了说，这叫吃得苦中苦。」"
    show chara lb09 #梁芷柔立绘|冬季校服|坏笑|近
    with dissolve
    voice "audio/voice/005006.ogg"
    l "「所谓『天将降大任于是人也』嘛。别的先不说，至少心态摆正是很重要的。」"
    y "「谁知道呢。也没准待会儿就飞过来一个椅子，直接把我砸成植物人了。」"
    play sound "audio/sound/effect20.ogg" noloop
    with vpunch
    show chara lb03 #梁芷柔立绘|冬季校服|生气|近
    with dissolve
    y "「哎哟。」"
    "脑门被拍了一巴掌。"
    voice "audio/voice/005007.ogg"
    l "「就知道贫。」"
    show chara lb02 #梁芷柔立绘|冬季校服|皱眉|近
    with dissolve
    voice "audio/voice/005008.ogg"
    l "「要不怎么着，我给你来一下？」"
    "打完了你才说啊！"
    y "「……完了，我被你打傻了。」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/005009.ogg"
    l "「去去去，是不是没打够啊？」"
    y "「嗯，连把椅子都没有。」"
    show chara lb13b #梁芷柔立绘|冬季校服|疑惑2|近
    with dissolve
    voice "audio/voice/005010.ogg"
    l "「哼！」"
    "梁芷柔恐吓似的挥了挥手，不过终究没有再打下来。"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/005011.ogg"
    l "「你啊，坚持坚持吧。现在你可是咱们班上的希望之星，郑老师可是把你当成标杆来立的。要是你现在掉了链子，那可不是闹着玩的。」"
    y "「唉……我知道。」"
    y "「真是的，我努力又不是因为他，这人自己加这么多戏真是麻烦死了……」"
    show chara lb12a #梁芷柔立绘|冬季校服|羞涩1|近
    with dissolve
    voice "audio/voice/005012.ogg"
    l "「啊……」"
    show chara lb04 #梁芷柔立绘|冬季校服|无奈|近
    with dissolve
    voice "audio/voice/005013.ogg"
    l "「咳咳！反正啊，这个状态你得调整调整，啊。」"
    y "「知道啦知道啦……」"
    y "「……」"
    pause 1.0
    with vpunch
    "从仰望星空的死鱼眼模式切换回正常的坐姿。"
    y "「哎……」"
    show chara lb13a #梁芷柔立绘|冬季校服|疑惑1|近
    with dissolve
    voice "audio/voice/005014.ogg"
    l "「嗯？怎么了？」"
    y "「没什么，就是觉得时间过得真是快啊。」"
    y "「一晃就又要到期末了。」"
    y "「想想上学期，或者哪怕是一两个月以前呢……都想象不到现在会是这么个样子。」"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/005015.ogg"
    l "「嗯……是啊。」"
    voice "audio/voice/005016.ogg"
    l "「想想还真是。」"
    show chara lb05a #梁芷柔立绘|冬季校服|苦笑1|近
    with dissolve
    voice "audio/voice/005017.ogg"
    l "「时间过得好快啊。」"
    l "「……」"
    show chara lb11 #梁芷柔立绘|冬季校服|微笑|近
    with dissolve
    voice "audio/voice/005018.ogg"
    l "「呵……行啦，你加油吧，啊。」"
    hide chara
    with dissolve
    "梁芷柔轻轻朝我挥挥手，回到了自己的座位上。"
    stop music fadeout 3.0
    y "「呼……」"
    y "「……」"
    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    "左右看了看，不出意外还是有一些异样的目光。"
    e "「叽叽喳喳叽叽喳喳……」"
    "这帮家伙……又开始八卦了吧。"
    "不过，也难怪。"
    "我和梁芷柔最近这段时间确实是有一点「肆无忌惮」。"
    "以前我们交流时还要注意一下众人的目光，但现在已经变得毫不避讳了，偶尔还会有一点肢体上的接触。"
    "就算有人议论，也没有丝毫收敛，甚至变本加厉。"
    "……管他们呢？愿意说就说去吧！"
    "我们用这种带着些许仪式感的放肆，确认着自己，以及彼此的信念。"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……"
    scene bg b00a #天空|候鸟
    with fade
    "前路漫漫，一人前行，孤独且艰难。"
    "那么，便由两个人互相扶持着走下去好了。"

    scene bg b04c #滨河路|冬
    with fade
    "……"
    play sound "audio/sound/ambientnoise03.ogg" fadein 1.5 loop #傍晚环境噪音
    "…………"
    "因为临近周末，放学的时间难得早了那么一点点。"
    y "「亲贤臣，远小人，此先汉所以兴隆也；亲小人，远贤臣，此后汉所以倾颓也……」"
    y "「先帝在时，每与臣论此事，未尝不叹息痛恨于桓、灵也……」"
    y "「侍中、尚书、长史、参军，此悉贞良死节之臣……」"
    y "「愿陛下亲之信之，则汉室之隆，可计日而待也……」"
    y "「臣本布衣，躬耕于南阳……」"
    y "「苟全性命于乱世……」"
    bird "「啾——」"
    y "「啊……」"
    "一边走一边巩固背诵，不知不觉中，发现已经快要到家了。"
    scene bg b05b #湿地公园|冬
    with fade
    "湿地公园中，传来了候鸟的叫声。"
    y "「……」"
    "说起来，这里的修缮也到了尾声。"
    "去年洪水的痕迹几乎已经看不到了，估计过不了多久就可以重新开业了吧？"
    "不过，再过一段时间，等到开春以后，栖息在这里的冬候鸟也会飞往北方。"
    "届时虽然鸟儿会变得更多一些，但就不是现在园子里的这一批了。"
    "而我，在它们回来之前，就要毕业了。"
    "当我考上大学以后，必定会离开这里……离开这生活了18年的家乡。"
    "那时候，想要再次看到眼前的这片景色，就没现在这么简单了。"
    "虽然……我还不知道自己的未来能够去往何方。"
    y "「……」"
    show memories zorder 10 #回忆滤镜
    with fade
    "……"
    "一个月前。"
    "我在第一次模拟诊断考试之后搞出了那个「大新闻」，旋即被梁芷柔堵在了回家的路上。"
    show chara b03 #梁芷柔立绘|冬季校服|生气
    with dissolve
    voice "audio/voice/005019.ogg"
    l "「哎你你你你……你没事吧你？」"
    voice "audio/voice/005020.ogg"
    l "「你这是要我命啊！」"
    y "「所以说啊，我这不是在道歉呢么……当时一激动，脑子一抽就说出来了，没想那么多……」"
    voice "audio/voice/005021.ogg"
    l "「你是没想那么多！那万一郑老师想多了呢？他往我妈那儿一捅，那可热闹了啊！」"
    y "「这……他不也没想那么多么……」"
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    voice "audio/voice/005022.ogg"
    l "「得亏他是没想那么多！吓死我了！」"
    y "「是是是，对不起，真的。」"
    l "「……」"
    show chara b07b #梁芷柔立绘|冬季校服|消沉2
    with dissolve
    voice "audio/voice/005023.ogg"
    l "「唉。」"
    show chara b07a #梁芷柔立绘|冬季校服|消沉1
    with dissolve
    voice "audio/voice/005024.ogg"
    l "「幸亏你之后还知道往回找补一下，啊，『我是想要追赶梁芷柔的成绩』，唉……这他都能信……」"
    y "「那是，你看我后面演得多像啊，结结巴巴的话都说不利索了，不就是一个没有表达清楚嘛，多大点事。」"
    y "「而且了，你想想，在他们眼里，我跟你『表白』这事得多玄幻啊，一点都不真实。」"
    y "「『这里怎么可能会有人真的能和那个梁芷柔，啊，那个跟我们这些凡夫俗子完全不是一个世界的梁芷柔，扯上什么关系呢？』」"
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    l "「……」"
    y "「总之呢，过程惊心动魄，结果还算圆满。」"
    show chara b03 #梁芷柔立绘|冬季校服|生气
    with dissolve
    voice "audio/voice/005025.ogg"
    l "「呸！什么圆满啊！你还真好意思说啊……那下次是不是直接圆寂得了！」"
    y "「呃……」"
    show chara b02 #梁芷柔立绘|冬季校服|皱眉
    with dissolve
    voice "audio/voice/005026.ogg"
    l "「总之，下次不许再这么胡闹了，知道吗！？」"
    show chara b03 #梁芷柔立绘|冬季校服|生气
    with dissolve
    voice "audio/voice/005027.ogg"
    l "「……不对！什么下次，没有下次了！嗯……也不是！哎呀真是的……」"
    show chara b12b #梁芷柔立绘|冬季校服|羞涩2
    with dissolve
    voice "audio/voice/005028.ogg"
    l "「反正，我不答应！」"
    y "「啊？什么不答应……」"
    show chara b03 #梁芷柔立绘|冬季校服|生气
    with dissolve
    voice "audio/voice/005029.ogg"
    l "「你说是什么！」"
    show chara b12a #梁芷柔立绘|冬季校服|羞涩1
    with dissolve
    voice "audio/voice/005030.ogg"
    l "「你你你……追……那个……就是……你自己想去吧！」"
    y "「呃。」"
    "非常明白了。"
    "但是……现在该怎么办才好啊……"
    "所谓冲动是魔鬼，这是彻底给弄巧成拙了吧……我还有救吗……"
    l "「……」"
    y "「……？」"
    show chara b12b #梁芷柔立绘|冬季校服|羞涩2
    with dissolve
    voice "audio/voice/005031.ogg"
    l "「反正……现在……我不答应。」"
    y "「哎？」"
    l "「……」"
    show chara b12a #梁芷柔立绘|冬季校服|羞涩1
    with dissolve
    voice "audio/voice/005032.ogg"
    l "「如果……如果你真的能做到的话……」"
    voice "audio/voice/005033.ogg"
    l "「如果！如果你真的能追上来……呃，也不用和我一样，最起码，可以考到樱华的话……」"
    voice "audio/voice/005034.ogg"
    l "「到时候，至少，咱俩还可以有四年的时间在同一个城市里。」"
    show chara b12b #梁芷柔立绘|冬季校服|羞涩2
    with dissolve
    voice "audio/voice/005035.ogg"
    l "「那样的话……我也……不是不能考虑一下，给你个机会喔？」"
    show chara b03 #梁芷柔立绘|冬季校服|生气
    with dissolve
    voice "audio/voice/005036.ogg"
    l "「……但是可不一定啊！我只是说可能，明白吗？就算你也考过来了也不一定！」"
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    voice "audio/voice/005037.ogg"
    l "「明白了吗……你看着办吧，啊！」"
    hide chara
    with dissolve
    play audio "<from 0 to 3>audio/sound/effect19.ogg" noloop
    "丢下这句话以后，梁芷柔立刻转身，一溜烟逃了。"
    y "「呃……」"
    "……{p}…………"

    scene bg b00a #天空|候鸟
    with fade
    "……是的。"
    "她已经十分清楚地回应了我。"
    "按说这是件挺开心的事，但是……"
    "一切，都需要有一个前提——"
    "我得能够赶上她的步伐。{w}至少，也要能够望其项背。"
    "能做到吗？凭自己现在付出的这些努力…{cps=2}…还{/cps}来得及吗？"
    "为什么没有更早一些下定决心、更早一些付诸实施呢？那样的话，应该可以把握更大一些吧？"

    scene bg b05b #湿地公园|冬
    with fade
    "摇摇头，试图将心中的忐忑抚平，但却徒劳无功。"
    "虚度光阴的过去与无法把握的未来，如同两块大石，始终压在心头之上。"
    "必须……要更努力一些才行。"
    y "「还有不到半年……」"
    stop sound fadeout 3.0
    scene bg black #黑屏
    with fade
    y "「只剩下……不到半年了。」"
    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t06 #转场 天空
    with fade
    pause

#1月下旬。
#期末考试后。

    scene bg b02c #城区|冬
    with fade
    "几天之后，期末考试如期而至。"
    "过程乏善可陈，成绩也完全在预期范围之内，是一个能够体现出我这段日子努力的成果，却又没有什么意外之喜的分数。"
    "就这样，高三的第一学期即将结束了。"

    scene bg b01 #教室
    with fade
    show charaz h01a #老师立绘|冬季|普通
    with dissolve
    voice "audio/voice/015001.ogg"
    z "「……现在的你们，一定要做到分秒必争！接下来，就是最后的冲刺阶段了，在这最后的四个多月里，每一分每一秒，对你们来说都非常的珍贵！……」"
    voice "audio/voice/015002.ogg"
    z "「……你们啊，是这个县里面最好的中学、最好的班级里的学生，是你们父母的希望，也是全县的脸面，要争口气呀！……」"
    hide charaz
    with dissolve
    play sound "audio/sound/ambientnoise10.ogg" fadein 1.5 loop #安静学习环境噪音
    "若是评选每个学期最难熬的时刻，想来放假前的最后一天肯定能够金榜题名。"
    "老师照例在做着他的思想动员工作。毕竟是老生常谈了，尽管嘶吼得声嘶力竭，教室内却弥漫着一股昏昏沉沉的气息。"
    "如果不是凛冽的寒风拍打在窗户上呼呼作响——而且还顺着不怎么严实的窗户缝钻进来了——那大概就又会是一场全员入睡的惨剧吧。"
    "这场面仿佛是半年前那一天的再现，不禁令我想起被飞椅骑脸的惨痛记忆。"
    "下意识地朝梁芷柔那边看了看。"
    scene cg01a1 #梁芷柔听讲CG-1|标准|冬装|CG01a1
    with fade
    l "「……」"
    y "「（呜哇……正襟危坐啊。）」"
    "不愧是好学生的代表，即使是这么无聊的训话，照样看起来一丝不苟。"
    "嗯……「看起来」。"
    "以我对她的了解，现在她多半已经开始走神了……"
    scene cg01b4 #梁芷柔听讲CG-2|眼睛向后瞟视|冬装|CG01b4
    with dissolve
    l "「……？」"
    y "「（啊……）」"
    "非常迅速地被发现了。"
    y "「（……嗯？）」"
    scene cg01b5 #梁芷柔听讲CG-2|笑瞪|冬装|CG01b5
    with dissolve
    voice "audio/voice/005038.ogg"
    l "「……」"
    y "「（喂喂喂什么意思嘛。）」"
    y "「（随便看你一眼都能被发现，你这是有多闲啊，还好意思瞪我。）」"
    y "「（哼哼哼……）」"
    y "「（既然如此，那就别怪我了。）」"
    "反瞪回去。"
    "不仅如此，还挤眉弄眼做了个鬼脸，指了指讲台的方向。"
    scene cg01d #梁芷柔听讲CG-4|笑喷|CG01d
    with dissolve
    voice "audio/voice/005039.ogg"
    l "「……噗。」"
    "在我的卖力演出之下，梁芷柔一个没忍住，笑出声来。"
    "虽然声音不大，也飞快地绷住了脸，但之前那一脸严肃、认真听讲的形象，还是被我成功破坏掉了。"
    y "「（噢耶，胜利！）」"
    "我耀武扬威地在课桌底下朝她攥了攥拳。"
    stop sound fadeout 3.0

    voice "audio/voice/015003.ogg"
    z "「叶——雨——潇！！！」"
    y "「啊，到！」"
    scene bg b01 #教室
    with fade
    show charaz h04a #老师立绘|冬季|咆哮
    with dissolve
    voice "audio/voice/015004.ogg"
    z "「干什么呢你！啊？那么大动作，你以为老师是瞎子，看不见啊？啊！？」"
    y "「不是，我……那个……」"
    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/015005.ogg"
    z "「不是什么不是啊！啊？那你说说，你自己说说，你跟那儿干嘛呢？」"
    y "「呃……」"
    voice "audio/voice/015006.ogg"
    z "「还敢顶嘴了啊……你是不是觉得自己最近成绩不错，就可以翘尾巴了？啊？现在是你放松的时候吗！？」"
    show charaz h04a #老师立绘|冬季|咆哮
    with dissolve
    voice "audio/voice/015007.ogg"
    z "「要都照你这个样子，稍微有点进步就不知道自己姓什么了，那能行吗？行百里者半九十你知不知道？你现在这个时候放松了，那毁的可是你一辈子！」"
    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/015008.ogg"
    z "「你得知道，这人哪，什么时候开始努力都不算晚！你这才哪到哪啊？现在是停下来的时候吗？啊？」"
    y "「……」"
    hide charaz
    with dissolve
    "……呜啊啊啊。"
    "班主任喷起人来可谓永无止境，一旦被他当成目标，那就只剩下等死了。"
    y "「……」"
    "不对，怎么就只有我被抓住了呢！"
    scene cg01b6 #梁芷柔听讲CG-2|笑|冬装|CG01b6
    with fade
    "我面带不甘之色，瞥了我的共犯一眼。"
    l "「……」"
    "梁芷柔也在瞟着我这一边。"
    "看到我的眼神，她吐了吐舌头，微微咧嘴以示歉意。"
    voice "audio/voice/015009.ogg"
    z "「还乱瞅！啊？看什么哪？你说你看什么哪？啊？你说！」"
    scene bg b01 #教室
    show charaz h03a #老师立绘|冬季|皱眉
    y "「呃……」"
    y "「没看什么……」"
    voice "audio/voice/015010.ogg"
    z "「行了行了行了，你以为我看不见吗？」"
    voice "audio/voice/015011.ogg"
    z "「你是不是觉得，我为什么只管你、不管她啊？啊？她还用得着我管吗？她自己就可以管好自己！你行吗？啊？」"
    show charaz h04a #老师立绘|冬季|咆哮
    with dissolve
    voice "audio/voice/015012.ogg"
    z "「呵，梁芷柔，你能跟人家比么？你是能考上清北了还是能考上樱大了？可你再看看，你现在什么样，她又是什么样啊？」"
    voice "audio/voice/015013.ogg"
    z "「你自己说的，要以梁芷柔为目标，对吧？目标定得很好啊，那你得去实现哪？啊？光看她能管用吗？」"
    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/015014.ogg"
    z "「唉……我啊，老师也不求你在成绩上真能追得上她，但你好歹得跟她一样努力吧？啊？」"
    show charaz h01a #老师立绘|冬季|普通
    with dissolve
    voice "audio/voice/015015.ogg"
    z "「这结果呢？唉……你啊，你也别怨我说你，这有些人哪，我都不愿意说了！」"
    "班主任一边说一边把嘴炮的火力向周围延伸，开始覆盖到整个班级。"
    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/015016.ogg"
    z "「就你，啊，还有你！还有脸在这儿笑呢？啊？你以为我不知道你们在下面都传些什么话呢，啊！你说说，你们满脑子都想的是什么呀？翻来覆去就那点龌龊想法，除了这个以外就没点别的了？」"
    show charaz h04a #老师立绘|冬季|咆哮
    with dissolve
    voice "audio/voice/015017.ogg"
    z "「你们还有脸说他？啊？你、你、你，还有你，啊，你们那点破事，真以为没人知道啊？」"
    show charaz h03a #老师立绘|冬季|皱眉
    with dissolve
    voice "audio/voice/015018.ogg"
    z "「你们要是能考出他们俩的水平……都不用说他们『俩』，说梁芷柔是我为难你们了，就叶雨潇吧，啊！你们能到他那个分数，你们爱怎么折腾怎么折腾，我不管你们。」"
    show charaz h04a #老师立绘|冬季|咆哮
    with dissolve
    voice "audio/voice/015019.ogg"
    z "「但是要是到不了啊，以后在学校就别给我整这些有的没的，啊，不是时候！知道吗！」"
    "……{p}…………"
    hide charaz
    with fade
    play sound "audio/sound/effect06.ogg" noloop
    y "「呃…{cps=2}………{/cps}………………」"
    "好不容易熬到下课，感觉整个人都不好了。"
    stop sound fadeout 1.5
    play music "audio/music/bgm04.ogg" fadein 2.5 #冬～苍雪～
    show chara b10 #梁芷柔立绘|冬季校服|开心
    with dissolve
    voice "audio/voice/005040.ogg"
    l "「嘿嘿嘿。」"
    y "「……瞅把你给乐的。」"
    y "「这人不讲理啊，凭什么光点我。」"
    show chara b09 #梁芷柔立绘|冬季校服|坏笑
    with dissolve
    voice "audio/voice/005041.ogg"
    l "「因为像我这样的人，他连说都不愿意说了啊。」"
    y "「啊呸！」"
    y "「幸灾乐祸好玩吗？」"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/005042.ogg"
    l "「哈哈……不过还是得说，郑老师这是真的很看重你啊？」"
    y "「得了吧，他更看重你，可就是不说你。」"
    show chara b01b #梁芷柔立绘|冬季校服|普通|侧面
    with dissolve
    voice "audio/voice/005043.ogg"
    l "「所以说，我那是跳出三界之外，不在五行当中了。」"
    y "「喂喂喂这话你自己说啊？」"
    show chara b09 #梁芷柔立绘|冬季校服|坏笑
    with dissolve
    voice "audio/voice/005044.ogg"
    l "「嘿嘿嘿，事实嘛。」"
    y "「……哎，结果还不是个势利眼，成绩决定一切。」"
    show chara b01a #梁芷柔立绘|冬季校服|普通|正面
    with dissolve
    voice "audio/voice/005045.ogg"
    l "「好啦好啦，反正呢，你要是不想让他那么絮叨，就继续努力，把成绩再提高点呗？」"
    y "「唉。」"
    voice "audio/voice/005046.ogg"
    l "「所以呢……」"
    y "「所以？」"
    show chara b09 #梁芷柔立绘|冬季校服|坏笑
    with dissolve
    voice "audio/voice/005047.ogg"
    l "「来看看你这次期末考试的问题吧。」"
    "梁芷柔笑嘻嘻地抖了抖手中的几张卷子。"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/005048.ogg"
    l "「虽然这次是学校自主出题，难度有点不太平衡，不过还是可以拿来参考一下的。」"
    y "「所以……怎么样？」"
    show chara b01b #梁芷柔立绘|冬季校服|普通|侧面
    with dissolve
    voice "audio/voice/005049.ogg"
    l "「还行吧。」"
    show chara b01a #梁芷柔立绘|冬季校服|普通|正面
    with dissolve
    voice "audio/voice/005050.ogg"
    l "「半年前那种低级错误基本是不会出现了，基础方面弥补得还算不错，嗯……」"
    show chara b13a #梁芷柔立绘|冬季校服|疑惑1
    with dissolve
    voice "audio/voice/005051.ogg"
    l "「不过还是得说……看跟什么比吧。」"
    show chara b01a #梁芷柔立绘|冬季校服|普通|正面
    with dissolve
    voice "audio/voice/005052.ogg"
    l "「如果是『小目标』或者再高一点，比如百薇那样的大学——如果是以这个为目标，可以说是很不错了。」"
    voice "audio/voice/005053.ogg"
    l "「照这个样子下去，接下来只要不出大问题，基本上十拿九稳。」"
    y "「『不过』……？」"
    show chara b02 #梁芷柔立绘|冬季校服|皱眉
    with dissolve
    voice "audio/voice/005054.ogg"
    l "「嗯。如果……把目标再往上提一提的话，按照现在这个进度，就不好说了。」"
    show chara b13b #梁芷柔立绘|冬季校服|疑惑2
    with dissolve
    voice "audio/voice/005055.ogg"
    l "「……只能说，有希望。」"
    y "「嗯……」"
    show chara b02 #梁芷柔立绘|冬季校服|皱眉
    with dissolve
    l "「……」"
    show chara b08b #梁芷柔立绘|冬季校服|担心2
    with dissolve
    voice "audio/voice/005056.ogg"
    l "「那个……」"
    y "「看来，必须得更努力了呗！」"
    show chara b06 #梁芷柔立绘|冬季校服|吃惊
    with dissolve
    voice "audio/voice/005057.ogg"
    l "「啊……」"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/005058.ogg"
    l "「嘻嘻，对呀。」"
    show chara b10 #梁芷柔立绘|冬季校服|开心
    with dissolve
    voice "audio/voice/005059.ogg"
    l "「加油吧！」"
    stop music fadeout 2.5
    hide chara
    with fade
    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    "……{p}…………"
    show chara lb01b #梁芷柔立绘|冬季校服|普通|侧面|近
    with dissolve
    voice "audio/voice/005060.ogg"
    l "「……嗯，大致就是这样了。」"
    y "「好……」"
    hide chara
    with dissolve
    "在下课之后到大扫除之前的这一段时间里，梁芷柔给我简单讲了讲通过这次考试发现的问题。"
    "讲完以后，梁芷柔像是在检查是否还有什么欠缺之处似的，随手翻看着我的那几套卷子。"
    show chara lb13a #梁芷柔立绘|冬季校服|疑惑1|近
    with dissolve
    voice "audio/voice/005061.ogg"
    l "「……这里……是这样啊……原来如此……」"
    show chara lb13b #梁芷柔立绘|冬季校服|疑惑2|近
    with dissolve
    voice "audio/voice/005062.ogg"
    l "「……这样的话……那……」"
    show chara lb02 #梁芷柔立绘|冬季校服|皱眉|近
    with dissolve
    voice "audio/voice/005063.ogg"
    l "「嗯……」"
    show chara lb13a #梁芷柔立绘|冬季校服|疑惑1|近
    with dissolve
    voice "audio/voice/005064.ogg"
    l "「哎，雨潇。」"
    y "「啊？啊，怎么了？」"
    hide chara
    with dissolve
    "被直呼名字，一下子还有点反应不过来。"
    "看梁芷柔的模样，似乎是沉浸在思考之中，下意识地这样叫了我。"
    "……有点开心。"
    show chara b13b #梁芷柔立绘|冬季校服|疑惑2
    with dissolve
    voice "audio/voice/005065.ogg"
    l "「嗯，是这样的。我刚才想了一下，你现在这个情况呢，基本的东西其实已经准备得差不多了。所以呢，我觉得啊，应该调整一下复习的方向了。」"
    y "「调整……怎么调整？」"
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    voice "audio/voice/005066.ogg"
    l "「对你来说，现在的重点不在于差漏补缺，而是综合强化。」"
    show chara b01b #梁芷柔立绘|冬季校服|普通|侧面
    with dissolve
    voice "audio/voice/005067.ogg"
    l "「从现在起，你要开始整理自己的所有知识点，把它们融会贯通，形成连贯的网络，另外还要锻炼自己的解题速度和分配时间的能力，学会更好地应对考试。」"
    show chara b01a #梁芷柔立绘|冬季校服|普通|正面
    with dissolve
    voice "audio/voice/005068.ogg"
    l "「简单来说，就是需要你多做一些综合性的题目，保证你综合运用知识的水平。」"
    show chara b13a #梁芷柔立绘|冬季校服|疑惑1
    with dissolve
    voice "audio/voice/005069.ogg"
    l "「啊还有，就是一些有针对性的高水平卷子，把它们当成是真正的高考来做，严格在规定的时间里完成，训练你的临场发挥。」"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/005070.ogg"
    l "「这种事情吧，说起来容易，做起来还是挺难的。当然，要是真的能练好，对提高分数也很有效果。考试型选手可是很吃香的！」"
    y "「哎，应试教育啊！」"
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    voice "audio/voice/005071.ogg"
    l "「是呀……」"
    show chara b09 #梁芷柔立绘|冬季校服|坏笑
    with dissolve
    voice "audio/voice/005072.ogg"
    l "「不过啊，对咱们来说呢，也多亏了这个应试教育，现在还能有高考这个机会呀！咱们可是既得利益者啊。」"
    y "「也是。」"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/005073.ogg"
    l "「所以啦，没什么可抱怨的。」"
    show chara b01b #梁芷柔立绘|冬季校服|普通|侧面
    with dissolve
    voice "audio/voice/005074.ogg"
    l "「有这个功夫，还不如赶快抓紧时间，多学一点呢。」"
    y "「好好好……」"
    show chara b10 #梁芷柔立绘|冬季校服|开心
    with dissolve
    voice "audio/voice/005075.ogg"
    l "「嗯。没有哭闹，很有觉悟。」"
    y "「呃……这点思想准备还是有的啦。」"
    show chara b09 #梁芷柔立绘|冬季校服|坏笑
    with dissolve
    voice "audio/voice/005076.ogg"
    l "「很好，具体的我会给你拉出清单来的，到时候别叫苦喔，嘿嘿嘿。」"
    y "「……你这笑声听起来怎么有股阴谋的味道啊。」"
    show chara b10 #梁芷柔立绘|冬季校服|开心
    with dissolve
    voice "audio/voice/005077.ogg"
    l "「嘻嘻，不会啦，你想太多了。那就明天见喽？」"
    y "「嗯。」"
    "梁芷柔露出满意的笑容，朝我挥了挥手，回到自己的位子上去收拾东西了。"
    hide chara
    with dissolve
    stop sound fadeout 3.0
    "……{p}…………"
    scene bg b04c #滨河路|冬
    with fade
    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    y "「……」"
    y "「呼。」"
    "从现在起，高中生活的最后一个假期就算是开始了。"
    "话虽如此，我却与休息无缘。"
    "从明天开始，我要和梁芷柔在外面碰头，就像暑假时的那样，进行只属于我们俩的学习会。"
    y "「从明天开始到立春之后……距离年三十也就只剩两天啊。」"
    y "「……呼。」"
    "每一天都在争分夺秒，亡羊补牢。"
    "就不知……是否还未为晚矣了。"
    stop sound fadeout 3.0

    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t01 #转场 教室
    with fade
    pause

#次日。
#寒假第一天。

    play sound "audio/sound/ambientnoise04.ogg" fadein 1.5 loop #白天环境噪音

    scene bg b02c #城区|冬
    with fade
    "寒假的第一天。"
    "一如半年之前那样，我在吃过午饭之后，来到百货商场里的快餐店和梁芷柔碰头。"
    scene bg b06 #商业街
    with fade
    pause
    stop sound fadeout 3.0

    scene bg b07 #快餐店
    with fade
    pause
    scene cg04b5 #梁芷柔快餐店学习CG-2|做题|愁眉苦脸|冬装|CG04b5
    with fade
    play sound "audio/sound/effect10.ogg" fadein 0.5 loop #写字声
    "……{p}…………"
    l "「……」"
    y "「……」"
    y "「（嗯……）」"
    y "「（已知函数fx等于xcosx减sinx，x属于0到二分之派，求证函数fx小于等于0……若a小于x分之sinx小于b对x属于0，二分之派恒成立，求a的最大值与b的最小值……）」"
    y "「（求a和b的极值其实就是求函数sinx除以x的取值范围嘛，求导试试……）」"
    y "「（啊，分子这不就是第一问里那个式子吗？看起来思路没错……）」"
    y "「（求导之后是单调的啊……那a和b就是f0和f二分之派了呗……）」"
    y "「（……）」"
    y "「（f0没定义啊！！什么鬼！）」"
    y "「（嗯？嗯……对了，取极限试试看……）」"
    "……{p}…………"
    with fade
    y "「（好了，搞定！）」"
    y "「（嗯……看看答案……）」"
    y "「（哈？）」"
    y "「（这啥啊……一大长串……）」"
    y "「（我看看……他这是……因为x已经限制大于0了，所以乘上来……然后求导……再然后呢……分情况讨论了啊……）」"
    y "「（……感觉这个标准答案……好麻烦？）」"
    y "「（不过这样的话我到底是做对了没有啊……虽然感觉没有错……）」"
    y "「那个……」"
    scene cg04b3 #梁芷柔快餐店学习CG-2|做题|冬装|CG04b3
    with dissolve
    stop sound fadeout 3.0
    voice "audio/voice/005078.ogg"
    l "「嗯？」"
    y "「有个题稍微有点拿不准，帮我看看？」"
    voice "audio/voice/005079.ogg"
    l "「嗯？哪个？」"
    y "「这个……」"
    voice "audio/voice/005080.ogg"
    l "「我看看我看看……」"
    scene cg04b6 #梁芷柔快餐店学习CG-2|讲题|冬装|CG04b6
    with dissolve
    l "「……」"
    l "「…………」"
    voice "audio/voice/005081.ogg"
    l "「……嗯……」"
    y "「……」"
    voice "audio/voice/005082.ogg"
    l "「没问题，你做对了。」"
    y "「……呼！」"
    scene cg04b2 #梁芷柔快餐店学习CG-2|讲题|坏笑|冬装|CG04b2
    with dissolve
    voice "audio/voice/005083.ogg"
    l "「嘿嘿，不错嘛，知道用极限了，这个比原答案还要强哦！」"
    y "「嗯嗯嗯，我觉得也是。」"
    voice "audio/voice/005084.ogg"
    l "「嘿，说你胖还就喘上了……其实还有更简单的办法你要不要听一下，嗯？」"
    y "「啊？」"
    scene cg04b6 #梁芷柔快餐店学习CG-2|讲题|冬装|CG04b6
    with dissolve
    voice "audio/voice/005085.ogg"
    l "「sinx除以x的话，就是这个点跟原点连线的斜率啊。」"
    voice "audio/voice/005086.ogg"
    l "「那其实sinx除以x的范围就是正弦函数曲线上的点跟原点连线的斜率范围，当然是单调减小的嘛，a就是f二分之派了。」"
    voice "audio/voice/005087.ogg"
    l "「最大斜率就是原点处的切线，至于斜率……都不用算了，物理学单摆的时候就说x很小的时候sinx约等于x嘛，斜率就是1了！」"
    y "「……」"
    scene cg04b2 #梁芷柔快餐店学习CG-2|讲题|坏笑|冬装|CG04b2
    with dissolve
    "梁芷柔一脸得意地看着我。"
    y "「行吧，大写的服。」"
    voice "audio/voice/005088.ogg"
    l "「嘿嘿，很好。」"
    scene cg04b6 #梁芷柔快餐店学习CG-2|讲题|冬装|CG04b6
    with dissolve
    voice "audio/voice/005089.ogg"
    l "「正好了，借着这道题再跟你说一遍——」"
    voice "audio/voice/005090.ogg"
    l "「解题思路很重要！」"
    voice "audio/voice/005091.ogg"
    l "「你看原来的答案啊，也对，但是呢，方法笨得要死，真到了考试的时候啊，会消耗你大量的时间。」"
    voice "audio/voice/005092.ogg"
    l "「所以这个时候对知识点的综合运用……答案的切入点就很重要了。」"
    y "「嗯……」"
    voice "audio/voice/005093.ogg"
    l "「你看啊，比如刚才这道题吧……」"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b07 #快餐店
    with fade
    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    "精神高度集中的状态下，时间总是过得很快。"
    "一转眼，第一天的学习会就到了末尾。"
    y "「……呼。」"
    show chara le13b #梁芷柔立绘|冬季私服|疑惑2|近
    with dissolve
    voice "audio/voice/005094.ogg"
    l "「嗯？怎么啦，累了？」"
    y "「还行吧……」"
    y "「虽然确实是挺费脑子的。」"
    show chara le09 #梁芷柔立绘|冬季私服|坏笑|近
    with dissolve
    voice "audio/voice/005095.ogg"
    l "「费脑子呀？呵，这可才是第一天啊。」"
    show chara le10 #梁芷柔立绘|冬季私服|开心|近
    with dissolve
    voice "audio/voice/005096.ogg"
    l "「后面有的是真正费脑子的地方，做好心理准备吧。」"
    y "「成吧，我今天回去吃顿好的，十八年后又是一条好汉。」"
    show chara le09 #梁芷柔立绘|冬季私服|坏笑|近
    with dissolve
    voice "audio/voice/005097.ogg"
    l "「喔，说得跟真的似的。」"
    show chara le01b #梁芷柔立绘|冬季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/005098.ogg"
    l "「不过啊，说正经，你今天状态还挺不错的。」"
    show chara le11 #梁芷柔立绘|冬季私服|微笑|近
    with dissolve
    voice "audio/voice/005099.ogg"
    l "「很专注，很好！」"
    y "「啊，是啊。」"
    y "「说实话，我自己都没想到。」"
    "刚开始见面的时候，因为是时隔许久的又一次长时间独处，我还有点心猿意马。"
    "不过等到真正开始做题的时候，就很快调整角色进入到状态里了。"
    show chara le13a #梁芷柔立绘|冬季私服|疑惑1|近
    with dissolve
    voice "audio/voice/005100.ogg"
    l "「嗯……比我当初强多了，我刚开始想要好好学习的时候，花了一年的时间才能静下心来呢。」"
    y "「那是，我又不是12岁的小屁孩了。」"
    show chara le03 #梁芷柔立绘|冬季私服|生气|近
    with dissolve
    voice "audio/voice/005101.ogg"
    l "「谁是小屁孩啊！？」"
    y "「哈哈哈，反正不是我。」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/005102.ogg"
    l "「你还真是蹬鼻子上脸啊……看来还是精力过剩哈？要不要明天再加点？」"
    y "「来啊，断头饭我都准备吃了，来来来，尽管来！」"
    show chara le10 #梁芷柔立绘|冬季私服|开心|近
    with dissolve
    voice "audio/voice/005103.ogg"
    l "「嚯，死猪不怕开水烫了是吧？啊？」"
    hide chara
    with dissolve
    pause
    with vpunch
    y "「哎哟疼疼疼！别揪耳朵！我服，我服了行吗？别动手！」"
    "……{p}…………"
    with fade
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    y "「疼死我了，不带你这样的！」"
    voice "audio/voice/005104.ogg"
    l "「我不管，谁让你嘲笑我的。」"
    y "「开个玩笑而已，至于嘛。」"
    show chara le03 #梁芷柔立绘|冬季私服|生气|近
    with dissolve
    voice "audio/voice/005105.ogg"
    l "「哼！」"
    y "「……」"
    y "「呵呵……」"
    show chara le02 #梁芷柔立绘|冬季私服|皱眉|近
    with dissolve
    voice "audio/voice/005106.ogg"
    l "「你还笑！」"
    y "「啊，不是，我不是笑这个。」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/005107.ogg"
    l "「那是在笑什么啊？」"
    y "「我在想啊，这事就是这么奇妙。」"
    show chara le13b #梁芷柔立绘|冬季私服|疑惑2|近
    with dissolve
    voice "audio/voice/005108.ogg"
    l "「嗯？」"
    y "「现在我可以和你聊学习聊得这么认真，甚至还挺开心的。」"
    show chara le13a #梁芷柔立绘|冬季私服|疑惑1|近
    with dissolve
    voice "audio/voice/005109.ogg"
    l "「啊……」"
    y "「要是以前，我早就该叫苦连天了吧。」"
    y "「哪儿能想得到还能像现在这样，自己给自己加码的。」"
    y "「那感觉，就像是突然一下子开窍了吧，砰的一下，突然明白了。」"
    y "「然后呢，发现，哎呀，自己还有得救，还可以抢救一下，不要放弃治疗。」"
    y "「哎……真是……」"
    y "「要是再早一点就好了，那就……」"
    show chara le01b #梁芷柔立绘|冬季私服|普通|侧面|近
    with dissolve
    l "「……」"
    show chara le11 #梁芷柔立绘|冬季私服|微笑|近
    with dissolve
    voice "audio/voice/005110.ogg"
    l "「现在，也不晚。」"
    y "「嗯。」"
    show chara le01b #梁芷柔立绘|冬季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/005111.ogg"
    l "「我可不是在安慰你啊，灌鸡汤什么的……我很认真的。」"
    voice "audio/voice/005112.ogg"
    l "「毕竟你现在的目标是去樱华，又不是考樱大。剩下的这点差距啊，只要你能继续保持下去，就肯定没问题！」"
    show chara le11 #梁芷柔立绘|冬季私服|微笑|近
    with dissolve
    voice "audio/voice/005113.ogg"
    l "「听我的，对自己多一点自信，好不好？」"
    show chara le01a #梁芷柔立绘|冬季私服|普通|正面|近
    with dissolve
    voice "audio/voice/005114.ogg"
    l "「相信自己。你看，我这么好的眼光都相信你了，你自己还不相信自己吗？」"
    y "「……」"
    "「相信自己，相信你，相信你所相信的我。」"
    "梁芷柔的声音，如同有魔力一般，感染了我。"
    "我轻轻点了点头。"
    y "「……谢谢你。」"
    show chara le11 #梁芷柔立绘|冬季私服|微笑|近
    with dissolve
    voice "audio/voice/005115.ogg"
    l "「嗯！」"
    "梁芷柔微笑着，如同早春的阳光，温和沁润。"
    stop sound fadeout 3.0

    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t03 #转场 快餐店
    with fade
    pause

#之后某日。
#临近春节。

    scene bg b00 #天空
    with fade
    play music "audio/music/bgm01.ogg" fadein 1.5 #春～樱飞～
    "我们的学习会再次开始了。"
    "在同样的地方，和同样的她，做着同样的事。"
    "但，心境却已经有所不同。"
    "说实话，连我自己都没想到，在和梁芷柔独处的时候，居然还能如此地心无旁骛。"
    "想要拥有未来，首先需要现在的付出——道理简单，却也很难做到。所幸，我终于认识到了这一点。"
    "怀揣着希望，将全部精力专注于学习，将曾经的浑浑噩噩所荒废的时间一分一秒地抢回来。"
    "每天都有进步，每天都能弄懂一些以前不明白的东西……每天，都过得很充实。"
    "就这样，日子一天一天地过去了。"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene cg04b3 #梁芷柔快餐店学习CG-2|做题|冬装|CG04b3
    with fade
    play sound "audio/sound/effect10.ogg" fadein 0.5 loop #写字声
    "腊月廿七。"
    "今年没有年三十，后天就是除夕了。"
    "天大地大，过年最大，再怎么说，我们也不可能去压榨这两天的时间。"
    "而寒假，虽然说是从小年放到元宵，其实最多也就是到初七。再往后，高三的学生就要开始返校了……虽然名为补习，实际上就是开学。"
    "所以，今天就是我们学习会的最后一天了。"
    y "「嗯……」"
    "放下手里刚刚做完的卷子，挠了挠头。"
    "感觉……有点毛躁。"
    "今天之后，接下来的这几天大概就是我高考前的最后一次连休了吧……想想后面将要面临的鏖战，这仅存的一周假期就愈发显得珍贵。"
    "修行不足啊，还是容易被其他事情干扰。什么时候我也能像梁芷柔那样毫无杂念就好了。"
    "不过，说到梁芷柔……"
    voice "audio/voice/005116.ogg"
    l "「嗯……」"
    scene cg04b5 #梁芷柔快餐店学习CG-2|做题|愁眉苦脸|冬装|CG04b5
    with dissolve
    voice "audio/voice/005117.ogg"
    l "「嗯？」"
    voice "audio/voice/005118.ogg"
    l "「……嗯……嗯？？」"
    "有点出乎意料的是……梁芷柔今天也不大对劲。"
    "也不知道发生了什么事情，总之从刚才开始就是一脸苦大仇深的模样。"
    y "「怎么了？」"
    voice "audio/voice/005119.ogg"
    l "「嗯……这题……好奇怪……」"
    y "「啥？」"
    voice "audio/voice/005120.ogg"
    l "「没事，我再看看吧……」"
    y "「哦……」"
    with fade
    "……{p}…………"
    l "「……」"
    "20分钟过去了，期间梁芷柔断断续续地把习题集往后翻了几页，但看题的时候始终是一幅怪异的表情。"
    stop sound fadeout 3.0
    with fade
    "……{p}…………"
    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    "又过了几分钟。"
    l "「……」"
    scene cg04b4 #梁芷柔快餐店学习CG-2|做题|暴怒|冬装|CG04b4
    with dissolve
    voice "audio/voice/005121.ogg"
    l "「嗯～～～受不了了！」"
    voice "audio/voice/005122.ogg"
    l "「坑爹呢这是！」"
    y "「呃……」"
    voice "audio/voice/005123.ogg"
    l "「我就说嘛……什么玩意儿……」"
    voice "audio/voice/005124.ogg"
    l "「啊啊不行不行不行，这题根本没法做！」"
    y "「你这到底是怎么了？」"
    voice "audio/voice/005125.ogg"
    l "「你看看，这题出的……」"
    y "「嗯……？」"
    scene bg b07 #快餐店
    with fade
    "从梁芷柔手里接过习题集，一边看一边轻声地念起来。"
    y "「一个正整数，可以表示为a乘b乘c乘100a加10b加c的和，且a、b、c均为正整数，a大于b大于c，求该正整数取值范围……」"
    y "「嗯，最小一组解是a3b2c1，也就是6乘以321……1926吧，取值范围是1926到正无限？」"
    y "「……什么鬼。」"
    show chara le03 #梁芷柔立绘|冬季私服|生气|近
    with dissolve
    voice "audio/voice/005126.ogg"
    l "「是吧？也不知道这都是从哪儿找的题库，全都特别奇葩。要么是这样的，要么是超纲的，还有的根本就是题出错了。」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/005127.ogg"
    l "「我这半个小时都在干什么啊……简直是在浪费生命！」"
    y "「啊，其实不到半个小时。」"
    y "「你刚开始不对劲的时候我就注意到了……我看看啊，你大概，嗯，大概跟它较了24分钟的劲。」"
    show chara le02 #梁芷柔立绘|冬季私服|皱眉|近
    with dissolve
    voice "audio/voice/005128.ogg"
    l "「那也是24分钟啊！一天才24个小时，这就等于我今天的每1分钟，都有1秒钟不翼而飞了！」"
    y "「所以说啊……你干嘛非得跟它较这么大的劲？」"
    show chara le07b #梁芷柔立绘|冬季私服|消沉2|近
    with dissolve
    voice "audio/voice/005129.ogg"
    l "「因为没别的题可做了呀。」"
    y "「啊？」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/005130.ogg"
    l "「手头上就这么一本了。这不是临近春节了嘛，物流都歇了，书店那边也没进货。」"
    show chara le07a #梁芷柔立绘|冬季私服|消沉1|近
    with dissolve
    voice "audio/voice/005131.ogg"
    l "「原本以为好歹能撑过今天……那不就正好了嘛，结果谁想到是这么个玩意。」"
    y "「哈哈哈，你这就是玩了一辈子鹰，结果最后被家雀儿啄瞎了眼的那种了。」"
    show chara le04 #梁芷柔立绘|冬季私服|无奈|近
    with dissolve
    voice "audio/voice/005132.ogg"
    l "「呸呸呸，瞅把你给乐的。别得意的那么早啊，我是没事干了，可你不一样啊，嗯？」"
    y "「啊～是是是，我知道我知道。」"
    "举起手晃了晃，表示投降。"
    "论进度的话，我当然远比不上梁芷柔。在我俩共享卷子的情况下，此刻的我还有的是题可做。"
    y "「嗯……」"
    "先把手头的部分告一段落吧……"
    "看了看手里做到一半的卷子，稍微估算了一下时间。"
    y "「大概还需要20分钟……」"
    y "「劳您大驾，多等我一会儿吧。」"
    show chara le10 #梁芷柔立绘|冬季私服|开心|近
    with dissolve
    voice "audio/voice/005133.ogg"
    l "「嗯！」"
    "梁芷柔随意地点了点头，拿了本闲书出来读，我则继续和卷子的剩余部分奋斗起来。"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b07 #快餐店
    with fade
    y "「呼……」"
    play music "audio/music/bgm10.ogg" fadein 1.5 #梁芷柔～allegro vivace ver.

    "搞定了！"
    "基本在预想的时间内做完了剩余的部分，看来我的判断力也是有提高的。"
    show chara e09 #梁芷柔立绘|冬季私服|坏笑
    with dissolve
    voice "audio/voice/005134.ogg"
    l "「嗯？做完啦？」"
    y "「嗯……嗯？」"
    "一抬头，发现梁芷柔正笑眯眯地看着我。"
    y "「什么啊，笑得这么奇怪……」"
    show chara e11 #梁芷柔立绘|冬季私服|微笑
    with dissolve
    voice "audio/voice/005135.ogg"
    l "「嗯，没什么。」"
    voice "audio/voice/005136.ogg"
    l "「就是看看你。毕竟难得有这种我闲着、你忙活的时候嘛。」"
    y "「呃，行吧……我有什么可看的……」"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/005137.ogg"
    l "「当然有啦！」"
    y "「那你看出什么名堂来了？」"
    show chara e09 #梁芷柔立绘|冬季私服|坏笑
    with dissolve
    voice "audio/voice/005138.ogg"
    l "「嗯，呵呵，你觉得呢？」"
    y "「啊？」"
    show chara e11 #梁芷柔立绘|冬季私服|微笑
    with dissolve
    voice "audio/voice/005139.ogg"
    l "「你觉得你刚才做题的时候是什么样子？」"
    y "「我……我哪知道啊，我又看不见我自己。」"
    y "「你赶紧的，别卖关子了。说吧，我刚才什么样？」"
    show chara e09 #梁芷柔立绘|冬季私服|坏笑
    with dissolve
    voice "audio/voice/005140.ogg"
    l "「一个急不可耐，一脸猴急想要出去玩的家伙。」"
    y "「啊？」"
    "是这样吗？"
    "虽然之前确实是有那么一点心浮气躁，但我以为自己大致上还算是沉住气了啊……"
    "难道我其实已经表现得很明显了？"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/005141.ogg"
    l "「……嘻嘻。」"
    y "「嗯？」"
    show chara e09 #梁芷柔立绘|冬季私服|坏笑
    with dissolve
    voice "audio/voice/005142.ogg"
    l "「骗你的。」"
    y "「……啊？」"
    show chara e11 #梁芷柔立绘|冬季私服|微笑
    with dissolve
    voice "audio/voice/005143.ogg"
    l "「其实你很认真的，我看了你半天你都没注意。嘻嘻，难道我刚才诈你那一下，其实猜中啦？」"
    y "「啊……有点。」"
    show chara e09 #梁芷柔立绘|冬季私服|坏笑
    with dissolve
    voice "audio/voice/005144.ogg"
    l "「嗯～想去玩？」"
    y "「是。」"
    show chara e13b #梁芷柔立绘|冬季私服|疑惑2
    with dissolve
    voice "audio/voice/005145.ogg"
    l "「这样啊……」"
    show chara e13a #梁芷柔立绘|冬季私服|疑惑1
    with dissolve
    voice "audio/voice/005146.ogg"
    l "「那不如这样吧，你先陪我去个地方？」"
    y "「哎？」"
    show chara e13b #梁芷柔立绘|冬季私服|疑惑2
    with dissolve
    voice "audio/voice/005147.ogg"
    l "「有个地方，想去看看。陪我一下呗？」"
    y "「我没问题。」"
    "一时间猜不透梁芷柔这葫芦里面卖的什么药，但总之先答应下来就是了。"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/005148.ogg"
    l "「嘻嘻，那走吧。」"
    scene bg black #黑屏
    with fade
    stop music fadeout 2.5

    "……{p}…………"
    voice "audio/voice/005149.ogg"
    l "「……到啦！」"
    scene bg b05b #湿地公园|冬
    with fade
    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音

    y "「……」"
    y "「嗯？居然是这儿……」"
    show chara e13a #梁芷柔立绘|冬季私服|疑惑1
    with dissolve
    voice "audio/voice/005150.ogg"
    l "「嗯？怎么啦？」"
    y "「你怎么想起来这里了？」"
    "跟着梁芷柔一路走来，最终的目的地居然是……我家门口的那个湿地公园。"
    show chara e13b #梁芷柔立绘|冬季私服|疑惑2
    with dissolve
    voice "audio/voice/005151.ogg"
    l "「嗯，不知道为什么，就是想来。」"
    show chara e13a #梁芷柔立绘|冬季私服|疑惑1
    with dissolve
    voice "audio/voice/005152.ogg"
    l "「硬要说的话……哇，好多鸟！哎，鸭子！好多啊！好可爱！」"
    hide chara
    with moveoutleft
    "话刚说到一半，梁芷柔的注意力就被旁边的水鸟们吸引走了。"
    y "「……喂喂喂。」"
    "好歹你也是土生土长的本地人，在这个城市里住了18年，不要看上去好像第一次见到似的好不好？"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with moveinleft
    voice "audio/voice/005153.ogg"
    l "「啊，那边也有……」"
    hide chara
    with moveoutright
    y "「喂，别乱跑！」"
    "尤其是别一边叫唤一边乱跑……"
    "就算修缮得已经差不多了，但公园到底还是处于未开放的状态，我们现在算是「非法入侵」，太高调了会惹麻烦的。"
    show chara e10 #梁芷柔立绘|冬季私服|开心
    with dissolve
    voice "audio/voice/005154.ogg"
    l "「怕什么嘛，掉不下去的！」"
    y "「我怕的又不是你掉河里！」"
    y "「我水性不错的，你真掉下去我捞你上来就是了。」"
    show chara e04 #梁芷柔立绘|冬季私服|无奈
    with dissolve
    voice "audio/voice/005155.ogg"
    l "「……」"
    "我一边跟上梁芷柔，一边四下观察。好在已经临近过年，这里的工作人员大概也都放假了，并没有发现其他人的踪影。"
    show chara e01b #梁芷柔立绘|冬季私服|普通|侧面
    with dissolve
    voice "audio/voice/005156.ogg"
    l "「哎，好啦好啦，不乱跑了。」"
    show chara e11 #梁芷柔立绘|冬季私服|微笑
    with dissolve
    voice "audio/voice/005157.ogg"
    l "「陪我呆一会儿吧。」"
    y "「噢。」"
    scene cg08b #梁芷柔河边CG-2|远目|冬装|远目|CG08b
    with fade
    "我们俩找了个地方，并排靠在栏杆边，梁芷柔捋了捋头发，朝河面望去。"
    "顺着她的目光看过去，视线越过了冬日的芦苇花，落在东逝而去的黄河之上。"
    voice "audio/voice/005158.ogg"
    l "「好美啊……」"
    "处在枯水期的黄河，水很清，也很缓。阳光洒过，波光粼粼。"
    "浅浅的河面上，有无数的水鸟翩翩起舞。"
    l "「……」"
    voice "audio/voice/005159.ogg"
    l "「好美。」"
    y "「嗯，是啊。」"
    "哪怕早已是司空见惯，但眼前的这幅景色依然不禁让人赞叹。"
    l "「……」"
    y "「……」"
    scene cg08d #梁芷柔河边CG-4|转头|冬装|微笑|CG08d
    with dissolve
    voice "audio/voice/005160.ogg"
    l "「哎。」"
    y "「嗯？」"
    scene cg08d1 #梁芷柔河边CG-4|转头|冬装|羞涩|CG08d1
    with dissolve
    voice "audio/voice/005161.ogg"
    l "「刚才……」"
    voice "audio/voice/005162.ogg"
    l "「你刚才问我为什么要来这里，我说我也不知道。」"
    voice "audio/voice/005163.ogg"
    l "「但其实……我只是有点，不知道该怎么说才好。」"
    scene cg08b1 #梁芷柔河边CG-2|远目|冬装|远目|微笑|CG08b1
    with dissolve
    voice "audio/voice/005164.ogg"
    l "「我呢，想要多来这里看看，然后……尽可能多记住一点，这里的景色。」"
    scene bg b05b #湿地公园|冬
    with fade
    voice "audio/voice/005165.ogg"
    l "「我希望把这一切都烙在自己的记忆里，让我可以在未来回想起这里的时候，浮现出来的是一幅鲜活的画面，而不只是一个朦胧的印象。」"
    l "「……」"
    voice "audio/voice/005166.ogg"
    l "「在未来……我们一起回忆这段日子的时候。」"
    play sound "audio/sound/effect23.ogg" loop
    with vpunch
    y "「——！」"
    "在听到这话的一瞬间，我的心脏骤然狂跳起来。"
    stop sound fadeout 3.0
    "力度之大，都能让我自己直接听到那砰砰的响声。"
    scene cg08d2 #梁芷柔河边CG-4|转头|冬装|微笑|脸红|CG08d2
    with fade
    "我扭过头，想要看看她的模样，却发现她此时也正好转过脸来，恰好与我四目相对。"
    "她的眼眸映出一片流光，亮晶晶的，令人怦然心动。"
    "张了张嘴，却说不出话来。"
    "梁芷柔也没有再说什么，只是微笑着，看着我。"
    l "「……」"
    y "「……」"
    scene cg08d3 #梁芷柔河边CG-4|转头|冬装|微笑|脸红|特写|CG08d3
    with dissolve
    "不知不觉中，我们之间的距离，似乎正在逐渐…{cps=2}…缩{/cps}短。"
    "周围的声音，似乎突然消失了。"
    "……江水的声音，{w}风拂过芦苇的声音，{w}候鸟嬉戏的声音。"
    "外面街道上见不到行人。{w}河对岸此刻也没什么动静。"
    "那一瞬间，有一种仿佛整个世界就只剩下自己和自己眼前的这个女孩的错觉。"
    voice "audio/voice/005167.ogg"
    l "「……呼……」"
    "看着她红扑扑的脸蛋。"
    "感受她呼出的白色哈气。"
    "聆听她略微急促的呼吸声。"
    scene cg08d4 #梁芷柔河边CG-4|转头|冬装|脸红|CG08d4
    with dissolve
    l "「……」"
    y "「……」"
    play sound "audio/sound/effect23.ogg" loop
    "我情不自禁地向前探着身子，而她似乎也没有躲避的意思。"
    "一厘米、两厘米……"
    "我们之间的距离，越来越近。"
    l "「……」"
    scene cg08d5 #梁芷柔河边CG-4|转头|冬装|脸红|闭眼|CG08d5
    with dissolve
    "她轻轻闭上了眼睛。"
    "微微颤抖的睫毛，描述着她此刻的心情。"
    y "「……」"
    stop sound fadeout 3.0
    scene bg black #黑屏
    with fade
    "我深深吸了一口气，也闭上眼。"
    "然后——"
    play audio "audio/sound/effect26.ogg" noloop
    bird "「嘎——！」"
    scene bg b00a #天空|候鸟
    with fade
    bird "「嘎嘎嘎——！」"
    play audio "audio/sound/effect27.ogg" noloop
    bird "「扑棱扑棱扑棱扑棱扑棱扑棱扑棱扑棱扑棱——」"
    "就在我们即将接触的那一瞬间，有一大滩水鸟不知因为什么被惊得四散飞起，闹出了好大的动静。"
    scene cg08d6 #梁芷柔河边CG-4|转头|冬装|吃惊|CG08d6
    with fade
    voice "audio/voice/005168.ogg"
    l "「啊……！」"
    y "「呃……」"
    "我们都被吓了一跳，我不自觉地绷紧了身子，梁芷柔也倒吸了一口凉气，睁开了眼睛。"
    l "「……」"
    y "「……」"
    "气氛被破坏了，刚才热血上涌的冲动也飞快地冷静了下来，只剩下彼此近距离的面面相觑。"
    l "「……」"
    y "「……」"
    "有点……尴尬。"
    "我有些不知所措，倒是梁芷柔，在经过了最初的那一瞬间的惊慌之后，很快淡定了下来。"
    scene cg08d2 #梁芷柔河边CG-4|转头|冬装|微笑|脸红|CG08d2
    with dissolve
    l "「……」"
    "……不止如此。她还一副饶有兴致的模样，似乎想看看我接下来会怎么做。"
    y "「……」"
    "这是在挑衅吧？{w}这一定是在挑衅吧？{w}你知不知道你这样做会被……"
    "……算了，我知道，我什么也不敢做的。"
    voice "audio/voice/005169.ogg"
    l "「嘻……嘻嘻！」"
    "看着我的样子，梁芷柔很开心地笑了起来。"
    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    scene cg08e #梁芷柔河边CG-5|顶脑门|笑|CG08e
    with dissolve
    "然后，她微微前倾，把她的额头与我的额头贴在了一起。"
    voice "audio/voice/005170.ogg"
    l "「有句话说的好。」"
    voice "audio/voice/005171.ogg"
    l "「『在看风景的时候，在乎的并不是风景有多美，而是陪在你身边看风景的那个人是谁。』……」"
    y "「嗯。」"
    scene cg08e1 #梁芷柔河边CG-5|顶脑门|微笑|CG08e1
    with dissolve
    voice "audio/voice/005172.ogg"
    l "「明年……以后每次过年的时候，你都陪我来这里看风景，好不好？」"
    y "「……好。」"
    "我轻轻点了点头。"
    "我们俩的脑门是顶在一起的，我的动作也带着她的头一起晃动起来。"
    voice "audio/voice/005173.ogg"
    l "「嘻嘻。」"
    "似乎是觉得很好玩，梁芷柔开始用力，和我顶起牛来。"
    y "「哎哟。」"
    scene cg08e #梁芷柔河边CG-5|顶脑门|笑|CG08e
    with dissolve
    voice "audio/voice/005174.ogg"
    l "「哈哈哈。」"
    "我装作不敌的样子，和她拉锯了两个回合，逗得她又笑了起来。"
    "……{p}…………"

    scene bg b05b #湿地公园|冬
    with fade
    "玩闹了一会儿以后，我们没有继续再粘在一起，只是牵着的手却没有松开。"
    "时值午后，冬末春初的阳光晒得人暖暖的，丝毫感觉不到寒冷。"
    "我们就这样肩并肩靠在一起，沐浴着阳光，盯着眼前这片无比熟悉，却仿佛怎么也看不够的景色。"
    scene bg b00 #天空
    with fade
    "胡马依北风，越鸟巢南枝。"
    "道路阻且长，会面安可知。"
    "对于将来，现在的我还不敢夸下海口。"
    "但是，我会在接下来的日子里，继续不断向前追赶。"
    "直到…{cps=2}…真{/cps}正能够支撑起我们的未来的时候……"
    stop music fadeout 2.5

    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t03 #转场 快餐店
    with fade
    pause

#大年初五。

    scene bg black #黑屏
    with fade
    "……{p}…………"
    stop sound
    play music "audio/music/bgm06.ogg" fadein 1.5 #悬而未决

    "这一天，终于到来了。"
    "就好像那些或悲观、或阴谋的崩溃论者所说过的那样……"
    "工厂停工、商店关门、政府停顿……只有警察和武警，每一天都处在高度的紧张之中。"
    "原本车水马龙的繁华大城市，此时正变得萧条空荡。"
    "有钱的富人全家奔向海外，没钱的穷人则争相返回老家，所有的长途交通工具全部爆满，人们为了抢到一张车票而拼尽全力。"
    "而家乡的情况也并未好到哪去：所有人都急切地想要把手中的货币尽量多地换成食物或者其他什么实际的货物，这同样引发了抢购狂潮。"
    "其间，在某一天晚上，几乎全国的家庭都围绕在电视机前，怀着期盼的心情等待着中央电视台面向全国的播放。"
    "中央台的播放持续长达四个多小时，人们怀着复杂的心情坚持着将之全部看完，却又异口同声地对其内容进行了大肆抨击。"
    "当晚，全国大多数城市都陷入了弥漫的硝烟之中。人们成群结队地外出，在各个街道、广场点燃了大量的爆炸物，不时会有人因此受伤，尤其以眼伤者居多。"
    "还有许多家庭在门口的两侧和上方张贴标语，表达来年的诉求。"
    "而在激情过后，耗尽了精力的人们开始选择闷在家里休养，终日混吃等死、无所事事，或者带着孩子到亲属的家里，以孩子的名义讨要钱财。"
    stop music fadeout 2.5
    "是的，这一切都真实地发生了……"
    "春节，到了。"

    scene cg09a #梁芷柔逛社火CG-1|冰糖葫芦|CG09a
    with fade
    play music "audio/music/bgm05.ogg" fadein 1.5 #恭贺新禧
    voice "audio/voice/005175.ogg"
    l "「人好多啊～」"
    show cg09g1 #梁芷柔逛社火CG-7|表情差分|皱眉|CG09g1
    with dissolve
    voice "audio/voice/005176.ogg"
    l "「哎呀怎么搞的嘛……人怎么这么多啊！挤死了！嗯……」"
    y "「那你还非要来。」"
    voice "audio/voice/005177.ogg"
    l "「肯定要来啊！因为是社火嘛！」"
    y "「我觉得更像是小商品集散中心外加灵长类野生动物园……」"
    y "「话说你有那么传统嘛，居然喜欢看这个？」"
    show cg09g2 #梁芷柔逛社火CG-7|表情差分|无奈|CG09g2
    with dissolve
    voice "audio/voice/005178.ogg"
    l "「其实啊，我也就是来凑个热闹。」"
    y "「哎……」"
    voice "audio/voice/005179.ogg"
    l "「毕竟家里待不下去了嘛，这算是……嗯……跑出来避难吧。」"
    y "「啥情况，家里怎么啦？」"
    show cg09g1 #梁芷柔逛社火CG-7|表情差分|皱眉|CG09g1
    with dissolve
    voice "audio/voice/005180.ogg"
    l "「别提了，我这两天没完没了地串门、被串门，累死了！还烦！」"
    voice "audio/voice/005181.ogg"
    l "「也不知道我们家怎么有那么多亲戚，七大姑八大姨一个挨一个，没完没了的。」"
    y "「过年嘛，正常。」"
    voice "audio/voice/005182.ogg"
    l "「可问题是他们全都拿我当枪使啊！那什么，『你看看你表姐，今年可是要考到樱大去的啊，你再瞧瞧你，真没出息！』……唉！」"
    voice "audio/voice/005183.ogg"
    show cg09g5 #梁芷柔逛社火CG-7|表情差分|生气|CG09g5
    with dissolve
    l "「你是不知道，我这两天就是标准的『别人家的孩子』，把我那一帮堂的表的兄弟姐妹都得罪遍了！」"
    show cg09g2 #梁芷柔逛社火CG-7|表情差分|无奈|CG09g2
    with dissolve
    voice "audio/voice/005184.ogg"
    l "「我还没办法，只能赔笑脸，『啊，谢谢谢谢，不敢当不敢当』……唉，真受不了。」"
    y "「……原来如此。我说呢，昨天我还琢磨了半天，心说您老人家这是怎么了？」"
    show cg09g3 #梁芷柔逛社火CG-7|表情差分|疑惑|CG09g3
    with dissolve
    voice "audio/voice/005185.ogg"
    l "「嗯？怎么啦，我约你出来很奇怪吗？」"
    y "「倒不是奇怪……也不对，你知道吗，你当时那条短信，就跟有配音似的。」"
    scene bg b02c #城区|冬
    show memories #回忆滤镜
    with fade
    "……{p}…………"
    scene bg b02c #城区|冬
    show chara le03 #梁芷柔立绘|冬季私服|生气|近
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/005186.ogg"
    l "「『明天陪我玩！』」"
    hide chara
    with dissolve
    y "「…………」"

    scene cg09a #梁芷柔逛社火CG-1|冰糖葫芦|CG09a
    show cg09g3 #梁芷柔逛社火CG-7|表情差分|疑惑|CG09g3
    with fade
    voice "audio/voice/005187.ogg"
    l "「所以呢，你就给我回了一个『啊？』字过来？」"
    y "「条件反射、条件反射，脑子抽抽了，不知道怎么回事。」"
    "说实话，那还是我第一次见到梁芷柔用这么明确的命令口吻。"
    "结果当时我都不知道自己怎么想的，直接回复了一个「啊？」，然后紧接着就接到了第二条短信，内容是集合的时间和地点。"
    "看样子是根本就没考虑过我这边的想法，在发出上一条短信的时候就紧接着敲下一条了吧。"
    y "「毕竟你这气场太强大了，我只顾瑟瑟发抖，都忘了给你打个电话问问了。」"
    show cg09g2 #梁芷柔逛社火CG-7|表情差分|无奈|CG09g2
    with dissolve
    voice "audio/voice/005188.ogg"
    l "「呵，幸亏你是没打电话啊，当时我正在饭桌上被我几个姑姑轮番轰炸呢。」"
    voice "audio/voice/005189.ogg"
    l "「你要是打过来了我肯定也不知道该说什么。然后呢，你想象一下吧，当着那一群人的面，接了一个男生的电话……啊，我死定了。」"
    y "「……」"
    voice "audio/voice/005190.ogg"
    l "「哎呀好啦好啦，不说那些啦！今天我要彻底放松，别的什么都不想……啊，有铁板鱿鱼！」"
    show cg09g4 #梁芷柔逛社火CG-7|表情差分|兴奋|CG09g4
    with dissolve
    pause 0.5
    scene cg09b #梁芷柔逛社火CG-2|消失|CG09b
    with dissolve
    "梁芷柔一边吃着冰糖葫芦，一边突然朝旁边的摊位冲去。"
    y "「喂喂喂，小心点，别扎着！行不行啊，要不要我帮你先拿着？」"
    voice "audio/voice/005191.ogg"
    l "「（嚼嚼）……不用！」"
    y "「啊……」"
    "梁芷柔娇小的身躯瞬间没入围在摊铺周边的人群之中。"
    "只能看到她高高举起的、抓着糖葫芦的右手……似乎是想要保护糖葫芦，但又实在没有足够的空间，只能摆出这样的造型来了。"
    y "「……唉。」"
    "我挠了挠头，跟在她的身后，杀入汹涌的人潮当中。"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene cg09a1 #梁芷柔逛社火CG-1|鱿鱼+冰糖葫芦（半）|CG09a1
    with fade
    "护着梁芷柔从人群里杀了出来。"
    voice "audio/voice/005192.ogg"
    l "「来，你的那份。」"
    y "「谢谢啊。」"
    y "「冰糖葫芦呢？没事吧？」"
    voice "audio/voice/005193.ogg"
    l "「活得好好的呢。」"
    "梁芷柔将吃到一半的糖葫芦给我看。"
    y "「嗯？怎么少了？让人给挤掉了？」"
    show cg09g3 #梁芷柔逛社火CG-7|表情差分|疑惑|CG09g3
    with dissolve
    voice "audio/voice/005194.ogg"
    l "「没有啊，吃了。」"
    y "「哦……啊？」"
    y "「这种时候你还能吃进东西啊！？」"
    "刚才看你都快被人给挤得脚离了地了……"
    voice "audio/voice/005195.ogg"
    l "「是啊，就这样……」"
    "梁芷柔给我摆了个杂技里面吞剑的造型。"
    y "「这也行……」"
    y "「你就不能等会儿吃吗？多危险啊？」"
    scene cg09a1 #梁芷柔逛社火CG-1|鱿鱼+冰糖葫芦（半）|CG09a1
    with fade
    voice "audio/voice/005196.ogg"
    l "「嗯……可是想吃了嘛。」"
    y "「呃……」"
    y "「那也太危险了啊！万一戳着自己怎么办……」"
    voice "audio/voice/005197.ogg"
    l "「啊，好啦好啦知道啦！嘻嘻，赶快吃鱿鱼吧，凉了就不好吃啦！啊呜。」"
    voice "audio/voice/005198.ogg"
    l "「嗯嗯……真好吃，好久没吃鱿鱼了……啊，羊肉串！」"
    show cg09g4 #梁芷柔逛社火CG-7|表情差分|兴奋|CG09g4
    with dissolve
    pause 0.5
    scene cg09b #梁芷柔逛社火CG-2|消失|CG09b
    with dissolve
    y "「……」"
    stop music fadeout 2.5
    "总感觉……今天……"
    "应该不会那么容易度过了……"
    scene bg black #黑屏
    with fade
    "……{p}…………"

    scene cg09a2 #梁芷柔逛社火CG-1|人潮|棉花糖+羊肉串（半）|CG09a2
    with fade
    play sound "audio/sound/ambientnoise08.ogg" fadein 1.5 loop #商场环境噪音

    y "「呼、呼……」"
    "所谓「女生都是吃货」的说法，在今天之前，我一直以为只是在说她们的食欲很旺盛。"
    "然而现在，我终于发现这里面其实还有一个隐藏的buff，一个绝对不下于「女生逛街」的buff。"
    "那就是……「在为了满足食欲而采取的觅食行动中，体力不减」。"
    "经过几轮厮杀之后，像我这样的凡夫俗子此刻已经显露出疲态了，可梁芷柔依旧是一副两眼放光、四处寻找猎物的姿态。"
    show cg09g1 #梁芷柔逛社火CG-7|表情差分|皱眉|CG09g1
    with dissolve
    voice "audio/voice/005199.ogg"
    l "「哎，臭豆腐！嗯，感觉味道有点冲啊，但是又有点想吃……」"
    show cg09g4 #梁芷柔逛社火CG-7|表情差分|兴奋|CG09g4
    with dissolve
    voice "audio/voice/005200.ogg"
    l "「啊，是灰豆子！好久都没吃过了，嗯……」"
    show cg09g3 #梁芷柔逛社火CG-7|表情差分|疑惑|CG09g3
    with dissolve
    voice "audio/voice/005201.ogg"
    l "「酿皮……哎呀怎么办啊，这个也好想吃啊……」"
    y "「……」"
    "感觉她什么都想吃。"
    "而且，这一路已经吃了那么多东西了，居然也不见她吃饱。"
    scene cg09a2 #梁芷柔逛社火CG-1|人潮|棉花糖+羊肉串（半）|CG09a2
    with dissolve
    voice "audio/voice/005202.ogg"
    l "「嘿嘿……嗯？怎么啦？」"
    "似乎注意到我一直在看着她，梁芷柔扭过头来，发出了疑问。"
    y "「啊，我只是在想……」"
    y "「你怎么跟饿了三天没吃饭似的。」"
    voice "audio/voice/005203.ogg"
    l "「啊，哈哈……」"
    voice "audio/voice/005204.ogg"
    l "「怎么啦，不行吗？」"
    y "「行行行，您使劲吃好了。」"
    voice "audio/voice/005205.ogg"
    l "「哼！」"
    "梁芷柔先是尴尬地笑了笑，随即又像是恼羞成怒似的板起了脸，狠狠地瞪了我一眼，把头扭向另一侧。"
    "我笑呵呵地看着她的侧脸，红扑扑的。"
    y "「我就说嘛，每逢佳节胖三斤啊，全是这么来的。」"
    show cg09g5 #梁芷柔逛社火CG-7|表情差分|生气|CG09g5
    with dissolve
    voice "audio/voice/005206.ogg"
    l "「你！」"
    "果然，「胖」这个字大概是全世界年轻女性共同的软肋。"
    "刚才还一副不要再理我的样子的梁芷柔瞬间就气急败坏地把头转回来了。"
    voice "audio/voice/005207.ogg"
    l "「不许说我胖！不许说不许说不许说！你才是胖子呢！」"
    y "「哈哈哈哈，好吧好吧，不胖不胖……哎哟哎哟哎哟！」"
    "梁芷柔上来想要捶我一顿，但她双手全都抓着食物的钎子，十分不方便，只能用手背象征性地砸了那么两拳，但又觉得不解气，只好再提起膝盖，顶了我大腿外侧一下子。"
    "这样的攻击当然连挠痒痒都算不上，不过该有的受伤模样还是需要装出来的。"
    y "「哎哟哎哟班长大人饶命，小的再也不敢了啊，哈哈哈……您不胖，您真的不胖！」"
    voice "audio/voice/005208.ogg"
    l "「我本来也不胖！」"
    y "「对啊，瘦，特苗条！哎哟，哈哈哈，别踹我了，真的啊。」"
    "我一边笑着躲闪，一边看向梁芷柔。"
    "的确，梁芷柔的身材还是蛮不错的。"
    "即使被冬服包裹，但仍然可以隐约看到她身体的曲线。"
    voice "audio/voice/005209.ogg"
    l "「哼！看什么看啊？」"
    y "「我在想啊，吃了那么多东西，还能这么瘦，你吃的东西都吃到哪里去了……」"
    "对女生来说，这种怎么吃都吃不胖的体质应该算是梦寐以求的吧。"
    "我上下打量了一遍梁芷柔，想不出她摄入那些卡路里都去了哪里。"
    y "「（卡路里啊……会转化成脂肪，堆积在什么地方吧……）」"
    y "「（脂肪……）」"
    y "「（脂肪啊……）」"
    y "「（嗯？脂肪……）」"
    "在念叨这个词的时候，我的眼神不由自主地把目光的焦点从梁芷柔的脸上往下挪了挪。"
    "的确，说到脂肪，那倒是还有个地方可以……"
    show cg09g3 #梁芷柔逛社火CG-7|表情差分|疑惑|CG09g3
    with dissolve
    voice "audio/voice/005210.ogg"
    l "「嗯？……啊，看哪呢你！！！」"
    with vpunch
    y "「哎哟！」"
    scene cg09a3 #梁芷柔逛社火CG-1|棉花糖+羊肉串（半）|捂脸|CG09a3
    with dissolve
    "梁芷柔以女生特有的敏感，在一瞬间就察觉了我的视线，然后毫不犹豫地发起了自我防卫。"
    "看得出她只是想要捂住我的眼睛，不过由于是慌乱之中仓促动手，她实际上是在用攥着羊肉串的那只手……"
    "直接给了我一拳。"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"

    scene cg09a4 #梁芷柔逛社火CG-1|棉花糖|噘嘴|CG09a4
    with fade
    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷

    voice "audio/voice/005211.ogg"
    l "「……哼。」"
    y "「好啦，都说了是我不好啦。」"
    voice "audio/voice/005212.ogg"
    l "「……哼！」"
    y "「呃……」"
    l "「……」"
    y "「……」"
    voice "audio/voice/005213.ogg"
    l "「……你眼睛。」"
    y "「哎？」"
    voice "audio/voice/005214.ogg"
    l "「你眼睛有没有事啊？要不要去洗洗？」"
    y "「呃……啊，还好，没事。」"
    voice "audio/voice/005215.ogg"
    l "「真没事？」"
    y "「真没事……」"
    "刚才那一拳，力气倒是不大，不过羊肉串糊了我一脸，辣椒直接拍进眼里去了。"
    "我现在泪流不止，看上去仿佛是在哭着求梁芷柔原谅一样。"
    voice "audio/voice/005216.ogg"
    l "「……哼，谁让你瞎瞅的。」"
    voice "audio/voice/005217.ogg"
    l "「都是你不好！自找的！」"
    y "「是啊，都是我不好，刚才我就说了嘛！」"
    voice "audio/voice/005218.ogg"
    l "「知道就好！」"
    voice "audio/voice/005219.ogg"
    l "「我告诉你啊，下次你要再这样我还得这么打你，知道吗？」"
    y "「行行行，没问题！见一次打一次，好不好？」"
    voice "audio/voice/005220.ogg"
    l "「哼！」"
    y "「那，接下来吃什么？要不我再去给你重新买一根羊肉串？」"
    voice "audio/voice/005221.ogg"
    l "「不吃了！怕胖！」"
    y "「呃……」"
    l "「……」"
    voice "audio/voice/005222.ogg"
    l "「唉。」"
    voice "audio/voice/005223.ogg"
    l "「好啦好啦。我有那么凶嘛？瞧把你给吓的。」"
    y "「有啊，你看你那模样，跟要活撕了我似的。」"
    stop music fadeout 2.5
    voice "audio/voice/005224.ogg"
    l "「本来就是，自作孽。」"
    l "「……」"
    play sound "audio/sound/ambientnoise08.ogg" fadein 5.0 loop #商场环境噪音
    voice "audio/voice/005225.ogg"
    l "「……过来。」"
    y "「嗯？」"
    scene cg09c #梁芷柔逛社火CG-3|贴近|CG09c
    with dissolve
    "梁芷柔突然踮起脚尖，凑到我眼前，仔细地看我的眼睛。"
    voice "audio/voice/005226.ogg"
    l "「还红着呢……」"
    voice "audio/voice/005227.ogg"
    l "「……疼吗？」"
    "她轻轻扒着我的眼皮，像模像样地观察起来。"
    y "「哎哟……？」"
    voice "audio/voice/005228.ogg"
    l "「哎别乱动。」"
    voice "audio/voice/005229.ogg"
    l "「……嗯……」"
    "还挺认真的……"
    "也不知道她这么看能看出什么名堂来……不过她纤细的手指在我脸上滑过的时候，感觉蛮舒服的，就任由她摆布了。"
    "说来……"
    "贴得真近啊……"
    "感觉自己努努嘴就能亲上去了。"
    y "「……」"
    "还是算了。"
    "要是现在刺激到梁芷柔，我的眼珠就该保不住了。"
    l "「……」"
    "看了一会儿，大概是觉得没什么毛病，梁芷柔终于放心了。"
    voice "audio/voice/005230.ogg"
    l "「呼！」"
    "最后，她朝我的眼睛轻轻吹了口气，仿佛这样就可以把疼痛吹飞。"
    voice "audio/voice/005231.ogg"
    l "「好了！应该是没事了！」"
    voice "audio/voice/005232.ogg"
    l "「走啦，去那边看看！」"
    y "「呵……好。」"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene cg09a5 #梁芷柔逛社火CG-1|棉花糖|CG09a5
    with fade
    play music "audio/music/bgm05.ogg" fadein 1.5 #恭贺新禧

    voice "audio/voice/005233.ogg"
    l "「哎，你看你看！好可爱啊」"
    y "「哦，是面人啊……」"
    voice "audio/voice/005234.ogg"
    l "「我要过去看看！」"
    y "「啊……」"
    scene cg09b #梁芷柔逛社火CG-2|消失|CG09b
    with dissolve
    "不等我反应过来，梁芷柔已经风风火火地朝商铺跑过去了。"
    y "「……」"
    "我们现在已经走出了餐饮区，附近基本都是卖小玩意儿的。"
    "不过梁芷柔似乎依然乐此不疲地跑来跑去，兴致丝毫不见减弱。"
    scene cg09a6 #梁芷柔逛社火CG-1|棉花糖+面人|CG09a6
    with dissolve
    voice "audio/voice/005235.ogg"
    l "「我回来啦！」"
    "不过片刻，梁芷柔又跑回来了，手里还多了个面人。"
    y "「嗯。我看看，这啥啊，孙悟空？」"
    voice "audio/voice/005236.ogg"
    l "「是呀。」"
    y "「嚯……你还喜欢这玩意儿啊？」"
    voice "audio/voice/005237.ogg"
    l "「怎么啦，不行啊？」"
    y "「谁也没说不行啊，我这不就是随口问一句嘛……」"
    voice "audio/voice/005238.ogg"
    l "「这不是过年嘛，就是得有这东西才像是过年呀！」"
    y "「也是。」"
    voice "audio/voice/005239.ogg"
    l "「啊！」"
    scene cg09b #梁芷柔逛社火CG-2|消失|CG09b
    with dissolve
    "梁芷柔似乎发现了什么，忽然一下子又跑开了。"
    y "「……」"
    y "「又怎么了……」"
    "……"
    scene cg09a7 #梁芷柔逛社火CG-1|棉花糖+面人+糖人|CG09a7
    with dissolve
    voice "audio/voice/005240.ogg"
    l "「哎呀，快来，快帮我一下，拿不了了！」"
    "很快，梁芷柔从人群中钻了出来。"
    y "「嗯？这是……」"
    "这次梁芷柔手上又多了个糖人。"
    "不过她之前两只手上就都有东西了，这次大概是接过来的时候攥得不太稳，糖人在她手上晃来晃去，摇摇欲坠。"
    voice "audio/voice/005241.ogg"
    l "「快！来！帮！我！拿！一！下！」"
    y "「哦哦，来了来了。」"
    "我赶紧上去把她手里占地儿最大的棉花糖接了过来。"
    scene cg09a8 #梁芷柔逛社火CG-1|面人+糖人|CG09a8
    with dissolve
    voice "audio/voice/005242.ogg"
    l "「嘻嘻……」"
    y "「还笑……拿不了就别一股脑买这么多东西啊，还都是怕碰的！」"
    voice "audio/voice/005243.ogg"
    l "「可是……哎呀不管啦，我就是想买嘛！」"
    y "「……」"
    y "「好吧你随便吧……」"
    voice "audio/voice/005244.ogg"
    l "「耶！」"
    y "「先别耶，棉花糖怎么办啊？」"
    voice "audio/voice/005245.ogg"
    l "「吃啊。」"
    "明明刚才还在说因为怕胖不要吃东西了……"
    y "「行吧，那我给你拿糖人吧。」"
    voice "audio/voice/005246.ogg"
    l "「不，我要拿着玩。」"
    y "「你这……那把面人给我？」"
    voice "audio/voice/005247.ogg"
    l "「这个我也要拿着！」"
    y "「……那你怎么吃棉花糖啊？」"
    scene cg09a9 #梁芷柔逛社火CG-1|面人+糖人|张嘴|CG09a9
    with dissolve
    voice "audio/voice/005248.ogg"
    l "「啊——」"
    y "「……」"
    l "「……」"
    y "「什、什么意思……」"
    voice "audio/voice/005249.ogg"
    l "「啊、啊——」"
    "梁芷柔用手里的面人指了指我这边的棉花糖，然后又朝着自己张开的嘴里晃了晃。"
    y "「……喂你啊？」"
    voice "audio/voice/005250.ogg"
    l "「啊～～～」"
    "你是三岁小孩吗！？"
    y "「……」"
    "虽然有一大堆想要吐槽的地方，但是话到嘴边，又咽了回去。"
    "大概……她这几天确实被亲戚们折腾得不轻吧？结果一旦不再需要扮演成熟端庄的好学生，就立刻触底反弹，开始放飞自我了。"
    y "「……哎，真是，懒死你算了。」"
    y "「来，小心点啊，别扎着。」"
    scene cg09a10 #梁芷柔逛社火CG-1|面人+糖人|吃棉花糖|CG09a10
    with dissolve
    voice "audio/voice/005251.ogg"
    l "「唔嗯……嗯嗯……」"
    voice "audio/voice/005252.ogg"
    l "「啊……嗯……」"
    y "「行了行了，先吃两口得了，小心太甜了齁着。」"
    scene cg09a8 #梁芷柔逛社火CG-1|面人+糖人|CG09a8
    with dissolve
    voice "audio/voice/005253.ogg"
    l "「好～」"
    y "「好什么好，我说你真的是个吃货啊，嘴里就没停过，就算买这些小玩意儿，都买的是糖人面人，还是吃的！」"
    voice "audio/voice/005254.ogg"
    l "「糖人又不能吃！」"
    y "「但原材料还是吃的东西啊。」"
    voice "audio/voice/005255.ogg"
    l "「哼！好吧，真对不起，我是个吃货。」"
    y "「别啊，吃货好啊，吃货多可爱。」"
    scene cg09a11 #梁芷柔逛社火CG-1|面人+糖人|羞涩|CG09a11
    with dissolve
    voice "audio/voice/005256.ogg"
    l "「啊……嘻嘻……」"
    voice "audio/voice/005257.ogg"
    l "「……哼！」"
    y "「呵呵，走吧。」"

    scene bg black #黑屏
    with fade
    "……{p}…………"

    scene cg09a12 #梁芷柔逛社火CG-1|风车+饮料|CG09a12
    with fade
    "跟随着梁芷柔在社火里南征北战了一圈之后，我们终于来到了表演传统节目的区域。"
    "顺便一提，糖人、面人什么的易碎怕碰的玩意儿此时都在我手上小心伺候着，梁芷柔正攥着一个三个轮的大号风车，忽悠忽悠地玩得不亦乐乎。"
    voice "audio/voice/005258.ogg"
    l "「啊！快看，是鼓队！」"
    show sd01 at truecenter #SD|太平鼓|SD01
    with dissolve
    "一支鼓队正在在前面表演。"
    y "「太平鼓啊……」"
    "这也是社火的必备节目了。"
    "至少在我们这儿的地界上，说到社火，就必定会有鼓队。"
    "虽然我们这里是个穷乡僻壤，不过最基本的传统还是不会丢掉的。"
    "就像眼前这支鼓队，人数不算多，也都是些业余爱好者，但该有的气势却丝毫不差。"
    "24个人摆开阵势，单手撑鼓，配合身体的舞动，将鼓甩得上下翻飞，同时徐疾有致地击打鼓面。"
    "鼓点犹如同滔滔黄河一般，气势汹涌、连绵不绝。"
    y "「敲得正经不错啊。」"
    voice "audio/voice/005259.ogg"
    l "「嗯，是呀。」"
    "梁芷柔一边点头，一边掏出手机给鼓队拍了张照片。"
    hide sd01
    with dissolve
    voice "audio/voice/005260.ogg"
    l "「不许个愿吗？」"
    y "「这也能许愿啊？」"
    voice "audio/voice/005261.ogg"
    l "「太平鼓嘛，原本就是为了祈祷和平呀、祝愿风调雨顺什么的。」"
    voice "audio/voice/005262.ogg"
    l "「所以借着机会，来个个人愿望也没什么问题吧？」"
    y "「嗯，祈祷和平啊……」"
    y "「希望今年也不会再有椅子飞过来了！」"
    voice "audio/voice/005263.ogg"
    l "「哈哈，又来了！不带你这样的啊，严肃点！」"
    y "「呵呵，好吧好吧。」"
    y "「（希望……我能追得上你的步伐吧……）」"
    voice "audio/voice/005264.ogg"
    l "「嗯？你说什么？」"
    y "「啥都没说，真正的愿望都是埋在心里的，说出来就不灵了。」"
    voice "audio/voice/005265.ogg"
    l "「哼～好吧。」"
    "……{p}…………"
    scene cg09a12 #梁芷柔逛社火CG-1|风车+饮料|CG09a12
    with fade
    y "「啊，这边是舞狮子啊。」"
    "从太平鼓阵那边离开之后，没走多远就来到了舞狮子的场地。"
    scene cg09a14 #梁芷柔逛社火CG-1|风车+饮料|舞狮子|CG09a14
    with dissolve
    "场地中，几只「狮子」正在「驯狮人」的引导下争抢绣球。"
    y "「每次看到这种舞狮的，就觉得好像在看『黄\[哔——\]鸿』。」"
    voice "audio/voice/005266.ogg"
    l "「哈哈，啊，但是黄\[哔——\]鸿是南方的吧？那边的舞狮好像和咱们这里的不太一样。」"
    y "「差不多啦，狮王争霸里不是也都凑到一块去了嘛？」"
    voice "audio/voice/005267.ogg"
    l "「嗯……」"
    y "「『傲气傲笑万重浪』～」"
    "一边唱，我一边模仿场地里的「狮子」，朝梁芷柔张牙舞爪地晃了晃脑袋。"
    voice "audio/voice/005268.ogg"
    l "「嘻嘻，傻死了！」"
    "……{p}…………"
    scene cg09a12 #梁芷柔逛社火CG-1|风车+饮料|CG09a12
    with fade
    "又走了没多久，迎面走来一队人马。"
    voice "audio/voice/005269.ogg"
    l "「咦，这是……」"
    show sd02 at truecenter #SD|铁芯子|SD02
    with dissolve
    y "「这个是叫铁芯子吧？」"
    voice "audio/voice/005270.ogg"
    l "「嗯……」"
    "「铁芯子」也是传统项目，类似于杂技，最下面是辆小车，几个人像叠罗汉那样，用铁棍支撑着挑到半空，但却总能保持着平衡。"
    voice "audio/voice/005271.ogg"
    l "「噫……不行不行，我看不了这个。」"
    hide sd02
    with dissolve
    y "「嗯？怎么啦？」"
    voice "audio/voice/005272.ogg"
    l "「瘆的慌。我老觉得他们会掉下来……」"
    y "「唉？不会吧，人都是绑在上面的，掉不下来吧？」"
    voice "audio/voice/005273.ogg"
    l "「反正我看着害怕！」"
    "也是。这就类似于「吊顶的大风扇会不会突然掉下来」呀、「游乐场的机器会不会把人甩出去」啊之类的，明明都是极特殊情况下才会发生的事，但平时就是会非常担心。"
    y "「哈哈哈，好吧好吧，胆真小啊你。」"
    voice "audio/voice/005274.ogg"
    l "「怎么啦，我就是胆小怎么啦！」"
    y "「好好好，走，咱们走还不成吗？没事，啊！咱们看其他的去。」"
    scene bg black #黑屏
    with fade
    stop music fadeout 2.5

    "……{p}…………"
    scene cg09d2 #梁芷柔逛社火CG-4|血社火|CG09d2
    with fade
    voice "audio/voice/005275.ogg"
    l "「——啊啊啊啊啊！！！！！」"
    with vpunch
    play music "audio/music/bgm06.ogg" fadein 1.5 #悬而未决
    y "「……」"
    voice "audio/voice/005276.ogg"
    l "「哇啊……呜呜……」"
    y "「……」"
    l "「……」"
    y "「行啦，没事的……」"
    voice "audio/voice/005277.ogg"
    l "「不行！」"
    voice "audio/voice/005278.ogg"
    l "「这这这这这这这这这这……」"
    show sd03 at truecenter #SD|血社火|SD03
    with dissolve
    voice "audio/voice/005279.ogg"
    l "「这什么呀这是！」"
    y "「血社火……吧？」"
    "离开铁芯子的场地没多远，就看到了另一拨人的表演。"
    "这群演员的卖相一个比一个可怕，什么锄头啊剪子啊，甚至还有板凳，通过化妆技术「插」在脑门上，溅出一脑袋的「血」。"
    hide sd03
    with dissolve
    stop music fadeout 2.5
    "在发现对方的一瞬间，梁芷柔直接把手里的风车和饮料瓶都扔到不知哪里去了，整个人也如脱兔一般窜到我的背后，一边哆嗦一边死死抱住我的胳膊不肯撒手。"
    "吓哭了啊这是……"
    y "「好啦好啦，没事，这都是化妆化出来的，不是真的啦。别怕啦，没事没事，啊？」"
    "说老实话，刚刚看到这一堆血瓢的时候，我也是吓了一跳。"
    "虽然我也是第一次见到真人版，不过以前见到过照片，好歹还不至于被吓得太厉害。"
    voice "audio/voice/005280.ogg"
    l "「呜……真、真的吗……」"
    y "「真的啦，你看这儿旁边这么多人呢。」"
    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    l "「……」"
    "血社火的队伍大概是对这种情况司空见惯了，毫无停顿地继续前进，很快走过去了。"
    scene cg09d #梁芷柔逛社火CG-4|抱紧|CG09d
    with dissolve
    y "「好啦，没事了，他们都走远了。」"
    voice "audio/voice/005281.ogg"
    l "「嗯……看不见了？」"
    y "「看不见了。」"
    voice "audio/voice/005282.ogg"
    l "「真的看不见啦？」"
    y "「真的啦！」"
    voice "audio/voice/005283.ogg"
    l "「真的真的吗？」"
    y "「哎哟你搁这儿套娃哪，我什么时候骗过你啊。」"
    l "「……」"
    y "「……」"
    scene cg09d3 #梁芷柔逛社火CG-4|抱紧|抬头|CG09d3
    with dissolve
    "梁芷柔像个小动物一样，小心翼翼地抬起头来，在环顾四周确认了没有危险之后，终于长长地喘出一口气来。"
    voice "audio/voice/005284.ogg"
    l "「——吓死我了！」"
    "虽然人是放松了一点，不过声音还带着哭腔。"
    y "「哎哟，没事啊，乖，不至于的啊。」"
    voice "audio/voice/005285.ogg"
    l "「可是，就是好可怕啊！」"
    y "「呃，是挺吓人的啦。你不知道血社火吗？」"
    voice "audio/voice/005286.ogg"
    l "「听说过，可没见过啊！」"
    y "「行了，这不就算是见过了吗？没事，啊。」"
    voice "audio/voice/005287.ogg"
    l "「才不是没事！我不想看这个！谁去看这么吓人的东西啊！」"
    y "「好好好，不看不看，咱不看这个，以后都不看，好不好？」"
    voice "audio/voice/005288.ogg"
    l "「嗯！」"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    scene cg09e #梁芷柔逛社火CG-5|抓衣角|CG09e
    with fade
    "我们再次转战别处。"
    "梁芷柔余悸未消，一路上死死地抓着我的衣摆，一副泫然欲泣的模样。"
    y "「哎，前面这是啥……」"
    voice "audio/voice/005289.ogg"
    l "「——！！」"
    stop sound fadeout 3.0

    scene cg09d #梁芷柔逛社火CG-4|抱紧|CG09d
    with dissolve
    y "「……」"
    l "「……」"
    y "「…………」"
    l "「…………」"
    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    y "「你这是又咋了？」"
    voice "audio/voice/005290.ogg"
    l "「这次是什么啊？可怕不可怕啊？」"
    y "「……放心吧，是跑旱船。」"
    y "「应该……算是吧。」"
    voice "audio/voice/005291.ogg"
    l "「应该……？」"
    scene cg09d3 #梁芷柔逛社火CG-4|抱紧|抬头|CG09d3
    with dissolve
    voice "audio/voice/005292.ogg"
    l "「……」"
    show sd04 at truecenter #SD|跑旱船|SD04
    with dissolve
    voice "audio/voice/005293.ogg"
    l "「这是……啥？」"
    "映入眼帘的，并非是那些传统跑旱船那种画着脸谱妆、穿着花花绿绿的戏服的演员们，而是一帮看上去和我们同龄、穿着各种奇怪服饰的女孩子。"
    "在我们挤进场边的时候，正有几个身披白色头蓬、带着高毛帽的女孩说说笑笑地往场下走，为首的一个女生喊叫着「Kirov reporting」之类的词组，不时引得同伴们笑成一片。"
    l "「……」"
    y "「……」"
    voice "audio/voice/005294.ogg"
    l "「这能算是跑旱船吗……」"
    y "「在地上跑的船……叫跑旱船也没错吧？」"
    "我四下看了看，发现旁边立着一块提示牌，上面确实写着「跑旱船」。"
    y "「嗯？」"
    "以及，在牌子旁边，似乎还有一行小字。"
    y "「百薇大学…{cps=2}…动{/cps}漫社？」"
    hide sd04
    with dissolve
    voice "audio/voice/005295.ogg"
    l "「呃……」"
    y "「这……」"
    voice "audio/voice/005296.ogg"
    l "「这『节目』能进社火里演吗？」"
    y "「不知…{cps=2}…道{/cps}？」"
    y "「……城里人真会玩。」"
    stop music fadeout 2.5
    scene cg09f #梁芷柔逛社火CG-6|牵手|CG09f
    with dissolve
    l "「……」"
    voice "audio/voice/005297.ogg"
    l "「呵呵……」"

    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    "不再担惊受怕的梁芷柔，没有继续死抱着我的胳膊，但也没有完全松开，而是……自然而然地牵起了我的手。"
    "虽然也渐渐地习以为常了，不过偶尔还是会觉得有点不可思议。"
    "毕竟……想想看，就在半年前，在电影院里不小心被她抓住手的时候，我还会紧张得像是要死了一样。"
    voice "audio/voice/005298.ogg"
    l "「雨潇。」"
    y "「嗯？」"
    voice "audio/voice/005299.ogg"
    l "「谢谢你。」"
    y "「谢我干什么？」"
    voice "audio/voice/005300.ogg"
    l "「我今天玩得特别开心！」"
    voice "audio/voice/005301.ogg"
    l "「这是我从小到大，逛社火逛得最开心的一次！」"
    y "「呵……有那么好吗？」"
    voice "audio/voice/005302.ogg"
    l "「有啊。因为……」"
    voice "audio/voice/005303.ogg"
    l "「嘻嘻，好啦，反正你知道我特别开心就行了。」"
    y "「唉？什么跟什么啊，话就说一半。」"
    voice "audio/voice/005304.ogg"
    l "「哎呀你就别问了嘛，对女生刨根问底可不好！」"
    y "「……得。你开心就好。」"
    voice "audio/voice/005305.ogg"
    l "「呵，那我们再多玩一会儿好不好？听说晚上会放花，我们看完再回去行吗？」"
    y "「我没问题，你家里……？」"
    voice "audio/voice/005306.ogg"
    l "「我打过招呼了，也不会特别晚的。反正这儿离我们家也挺近的，人又多，出不了事。」"
    y "「行吧。」"
    voice "audio/voice/005307.ogg"
    l "「嗯！我们走吧！」"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene cg09f #梁芷柔逛社火CG-6|牵手|CG09f
    with fade
    "在那之后，我们又在社火里逛了好半天。"
    play sound "audio/sound/ambientnoise08.ogg" fadein 1.5 loop #商场环境噪音
    y "「呼……」"
    voice "audio/voice/005308.ogg"
    l "「哈、哈……」"
    y "「累了吧？那边有椅子，歇会儿吧。」"
    voice "audio/voice/005309.ogg"
    l "「嗯。」"
    scene cg10a #梁芷柔看烟花CG-1|黄昏|CG10a
    with fade
    voice "audio/voice/005310.ogg"
    l "「哎哟！可算是坐下啦！」"
    y "「是啊，这一下午可真没少走路，感觉得有一年没这么走过了。」"
    voice "audio/voice/005311.ogg"
    l "「我看看……快3万步了哎，咱们都逛了什么啊走这么远？」"
    y "「谁知道，我一直都是跟着你走的。」"
    voice "audio/voice/005312.ogg"
    l "「哈哈，是吗？」"
    y "「走走也好，反正整天坐在那儿做卷子，都快长椅子上了。」"
    scene cg10b #梁芷柔看烟花CG-2|伸懒腰|CG10b
    with dissolve
    voice "audio/voice/005313.ogg"
    l "「对……呵……啊。」"
    voice "audio/voice/005314.ogg"
    l "「呵……嗯～～～～～！」"
    "梁芷柔一边打呵欠，一边抻了个大大的懒腰。"
    y "「哎哟我的天，眼泪都挤出来了。」"
    y "「形象啊，美女，注意点形象。」"
    scene cg10a1 #梁芷柔看烟花CG-1|黄昏|噘嘴|CG10a1
    with fade
    voice "audio/voice/005315.ogg"
    l "「去去去，少贫嘴了。呵～欠……」"
    "看来她真是给累惨了啊，呵欠一个接一个的。"
    "不过话说回来，论起体力消耗，我其实也好不到哪去……"
    y "「呵～欠～」"
    "被梁芷柔的呵欠所传染，我也忍不住来了一个。"
    scene cg10a #梁芷柔看烟花CG-1|黄昏|CG10a
    with fade
    voice "audio/voice/005316.ogg"
    l "「你还说我呢……半斤八两。」"
    y "「没办法啊，走路的时候还行，这一停下来感觉就明显了。」"
    y "「好好歇会儿吧，还得看烟花呢。」"
    voice "audio/voice/005317.ogg"
    l "「嗯……还有多久啊？」"
    y "「怎么也得天全黑了才行吧？我看看啊，估计还得要半个小时吧。」"
    voice "audio/voice/005318.ogg"
    l "「哎～好久啊。」"
    y "「咱俩先坐这儿好好歇会儿吧。你要不要喝点什么？我去买。」"
    voice "audio/voice/005319.ogg"
    l "「呵欠～你看着买吧，随便什么都行……」"
    y "「OK。」"
    stop sound fadeout 3.0
    scene cg10b #梁芷柔看烟花CG-2|伸懒腰|CG10b
    with dissolve
    voice "audio/voice/005320.ogg"
    l "「嗯，快点啊。」"
    y "「好啦知道啦。」"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    y "「抱歉抱歉，人太多了排了半天才……唉？」"
    y "「啥情况这是……」"

    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    scene cg10c #梁芷柔看烟花CG-3|独自睡着|CG10c
    with fade
    "几分钟之后，当我拿着饮料回来的时候，发现梁芷柔已经靠在长椅上睡着了。"
    "她微微地歪着头，乌黑的秀发散在肩上，如同墨色的瀑布一般，煞是好看。"
    "虽然很想再多看上两眼……但这么下去可不行啊！"
    scene cg10c1 #梁芷柔看烟花CG-3|梁芷柔睡着|叶雨潇坐下|CG10c1
    with dissolve
    y "「喂喂喂，醒醒，别睡了，会着凉的啊！」"
    voice "audio/voice/005321.ogg"
    l "「嗯？……雨潇？」"
    scene cg10c2 #梁芷柔看烟花CG-3|梁芷柔睡着|睁眼|CG10c2
    with dissolve
    "梁芷柔迷迷糊糊地睁开眼，抬头看了看我的脸，似乎是在确认我是谁。"
    y "「嗯，是我。」"
    voice "audio/voice/005322.ogg"
    l "「啊，我睡着了？」"
    y "「是啊，睡得呼呼的，猪一样。」"
    voice "audio/voice/005323.ogg"
    l "「哼……你才是猪……呵～欠～」"
    l "「……」"
    voice "audio/voice/005324.ogg"
    l "「ZZZ……」"
    y "「喂？别又睡过去啊！？」"
    voice "audio/voice/005325.ogg"
    l "「没事……我还以为是坏人呢……是你就没事了……」"
    y "「什么叫是我就没事了啊！？这大冷天的，你这样会感冒的知道不知道啊……」"
    voice "audio/voice/005326.ogg"
    l "「嗯～那就抱抱……抱抱就不冷了。」"
    y "「什么抱……哎！？」"
    scene cg10c3 #梁芷柔看烟花CG-3|梁芷柔睡着|抱叶雨潇|CG10c3
    with dissolve
    "没等我反应，梁芷柔就一头扎了过来，两只胳膊抱住我的脖子，把自己挂在了我的身上。"
    with hpunch
    voice "audio/voice/005327.ogg"
    l "「嗯……好暖和呀……」"
    y "「喂！？」"
    voice "audio/voice/005328.ogg"
    l "「嗯……别动……呼……」"
    y "「……」"
    voice "audio/voice/005329.ogg"
    l "「……呼……呼……」"
    y "「这……」"
    voice "audio/voice/005330.ogg"
    l "「……呼……呼……呼……」"
    "梁芷柔咽了下口水，微微晃了晃脑袋，丝毫没有想要醒过来的意思。"
    "而我则根本是一动也不敢动，就这么风中凌乱地僵在原地。"
    scene cg10c4 #梁芷柔看烟花CG-3|梁芷柔睡着|抱叶雨潇|脸特写|CG10c4
    with dissolve
    voice "audio/voice/005331.ogg"
    l "「……呼……呼……」"
    y "「……唉。」"
    "真是个不靠谱的家伙。"
    y "「你呀你。」"
    y "「你知不知道这样会让我占便宜的啊？」"
    "我用几乎是默念的音量，数落着身边的少女。"
    y "「你这么抱着，我可是挺享受的啊。再这样下去我可就真的不管你感不感冒了啊？」"
    y "「呵……也不知道最开始的那个生人勿近的女学霸跑哪去了啊？怎么就变成现在这个迷迷糊糊的吃货了呢？」"
    y "「怎么就变得……让我越来越喜欢你了呢？」"
    voice "audio/voice/005332.ogg"
    l "「……嗯……」"
    y "「嗯？」"
    "似乎是我扭头看她的动作让她有所感觉，梁芷柔稍微扭动了一下身子，想要再次找到一个舒服的位置。"
    y "「……」"
    y "「（不管了！）」"
    "借着她这次的动静，我的手臂从她后背绕过去，轻轻搂住了她。"
    scene cg10c5 #梁芷柔看烟花CG-3|梁芷柔睡着|相拥|CG10c5
    with dissolve
    y "「（尽量抱暖和一点就好了……吧？）」"
    y "「……」"
    voice "audio/voice/005333.ogg"
    l "「……呼……」"
    "被我抱进怀里的梁芷柔，一点也不客气地顺势又换了个姿势，像个小猫似的蜷缩成一小团。"
    y "「……」"
    "好可爱，怎么看都觉得好可爱，总之就是非常可爱。"
    y "「……」"
    "有点……想亲她一下。"
    voice "audio/voice/005334.ogg"
    l "「……呼……」"
    y "「……」"
    "看这样子，完全就是睡过去了，亲一下应该不会被发现吧。"
    "不，就算被发现了也没什么事吧？毕竟之前也有过类似的情况……"
    "……应该是……没事……的吧？"
    voice "audio/voice/005335.ogg"
    l "「……呼……」"
    y "「……」"
    "不对不对，趁人不备做这种事还是太过分了。再说又不是没有光明正大的机会……"
    "可是……"
    "果然还是好想亲一下啊！！"
    y "「（等等！等等！等等！冷静！要冷静！不能这么干！）」"
    y "「（对了，赶快转移注意力！只要别想这些乱七八糟的就行了！）」"
    "强行压抑住躁动的念头，我把视线投向来来往往的路人，希望能分散一下我的关注点。"
    y "「（哎，今天到处都是成双成对的啊。）」"
    y "「（也是，谁没事自己一个人来逛社火啊……）」"
    y "「（啊，哈哈，看到一个单身的！）」"
    y "「（居然瞪我？瞪我干什么，没见过搂着妹子的吗！哈哈哈哈哈哈！）」"
    y "「（噢，这一队怎么都是姑娘……哦哦，这是刚才那些『新派旱船』的女生吧，都是百薇大学的……）」"
    y "「（百薇啊，去年我还完全不敢去想呢……）」"
    y "「（嗯……）」"
    y "「……呵……欠……」"
    scene cg10c6 #梁芷柔看烟花CG-3|两人睡着|相拥|CG10c6
    with dissolve
    y "「……」"
    y "「……呼……」"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene cg10c7 #梁芷柔看烟花CG-3|两人睡着|相拥|夜幕|CG10c7
    with fade
    y "「……呼……」"
    voice "audio/voice/005335.ogg"
    l "「……呼……」"
    "……"
    play audio "audio/sound/effect28.ogg" noloop
    "「——砰啪！」"
    scene cg10c8 #梁芷柔看烟花CG-3|两人睁眼|相拥|夜幕|光影绽放|CG10c8
    with dissolve
    voice "audio/voice/005336.ogg"
    l "「——嗯！？」"
    y "「啊！」"
    "不知什么时候，一声巨响将我们从睡梦中惊醒。"
    scene bg b00d #天空|烟花
    with fade
    "睁开眼，正好看到一朵烟花灿烂地盛开于夜空之中。"
    voice "audio/voice/005337.ogg"
    l "「哎？哎？怎么回事？」"
    y "「烟花……？」"

    play sound "audio/sound/ambientnoise12.ogg" fadein 1.5 loop #烟花环境噪音
    "「嗖——」"
    "「——砰啪！」"
    "我们还没有反应过来，第二朵烟花也已升空，旋即绽放。"
    "紧接着，更多的烟花被点燃，爆竹之声不绝于耳。"
    voice "audio/voice/005338.ogg"
    l "「哇……」"
    "一开始，梁芷柔还有点半梦半醒的样子，不过很快，她就被那些五颜六色的花火吸引住了。"
    scene cg10d #梁芷柔看烟花CG-4|看烟花|光影绽放|CG10d
    with fade
    voice "audio/voice/005339.ogg"
    l "「好漂亮啊！」"
    y "「嗯，的确……」"
    "天空中，烟花接二连三不断地绽开，将整片天幕映照得五彩斑斓。"
    "天色已经黑下来了，烟花的魅力得以完全展现出来。"
    y "「（话说回来，我也睡过去了？这是睡了多久啊……）」"
    y "「（我看看……哎哟这得有半个多小时了吧，完蛋了这肯定要病啊……）」"
    scene cg10d1 #梁芷柔看烟花CG-4|看烟花|光影绽放|举手指天|CG10d1
    with dissolve
    voice "audio/voice/005340.ogg"
    l "「哎哎哎你看你看！」"
    y "「嗯？」"
    "我还在担心身体，身边的女生却没想那么多，只顾着欣赏眼前的美景。"
    voice "audio/voice/005341.ogg"
    l "「哇！好美啊！」"
    l "「……」"
    voice "audio/voice/005342.ogg"
    l "「嘻嘻……太好了。」"
    y "「嗯？什么？」"
    voice "audio/voice/005343.ogg"
    l "「我说太！好！啦！」"
    y "「什么太好啦？」"
    voice "audio/voice/005344.ogg"
    l "「今天！能和你一起来！我觉得特——别——好！」"
    "烟花砰砰啪啪的，声音很大，但梁芷柔用更大的声音，在我的耳边清楚地说出了这句话。"
    y "「我也是！」"
    voice "audio/voice/005345.ogg"
    l "「嗯！以后……啊……」"
    voice "audio/voice/005346.ogg"
    l "「……阿嚏！」"
    y "「哎哟，还是给冻着了！」"
    voice "audio/voice/005347.ogg"
    l "「嘻嘻，没事！」"
    "梁芷柔揉了揉自己的鼻子，毫不在意。"
    "虽然已经睡醒了，不过她似乎没有从我怀里离开的意思，反而靠的更近了。"
    scene cg10d2 #梁芷柔看烟花CG-4|看烟花|贴脸|光影绽放|CG10d2
    with dissolve
    "两个人的脸蛋都是冰冰的，但是，贴在一起却感觉不到寒冷。"
    voice "audio/voice/005348.ogg"
    l "「这样就不冷了！」"
    y "「哈哈，好吧！」"
    "我也将她抱得更紧了一些。"
    "「——砰啪！」"
    voice "audio/voice/005349.ogg"
    l "「看啊，烟花好漂亮！」"
    y "「知道啦知道啦，翻来覆去说了这么多遍了，耳朵都起茧子了！」"
    voice "audio/voice/005350.ogg"
    l "「哼，我就要说！烟花好漂亮好漂亮好漂……阿嚏！」"
    y "「哎哟哟哟哟哟哟……鼻涕都要出来了！我给你找找纸巾啊……啊……」"
    y "「阿嚏！」"
    voice "audio/voice/005351.ogg"
    l "「哈哈哈哈！你还说我呢？……阿嚏！」"
    y "「得……咱俩这下全完蛋。」"
    voice "audio/voice/005352.ogg"
    l "「嘻嘻！」"
    voice "audio/voice/005353.ogg"
    l "「偶尔放纵一次，有什么不好嘛！」"
    y "「说的也是啊。」"
    y "「……那就让烟花……和感冒来得更猛烈一些吧！」"
    voice "audio/voice/005354.ogg"
    l "「嘻嘻，傻死了！」"
    scene bg b00d #天空|烟花
    with fade
    "我俩抱在一起，看着漫天绚烂，花开花落。"
    "「——砰啪！」"
    "「——砰啪！」"
    "「嗖——」"
    "也许，有人喜欢说什么烟花易冷。"
    "但是，那又怎么样？"
    "此时、此刻。"
    "我所怀抱的——"
    "已是我的整个世界。"
    stop sound fadeout 3.0
    "……{p}…………"

#2月14日，情人节。
#开学第一天。

    scene bg black #黑屏
    with fade
    "无论是谁，青春的时候都会偶尔放纵。"
    "这当然没什么不好，只要……肯付出相应代价的话。"
    play sound "audio/sound/ambientnoise10.ogg" fadein 1.5 loop #安静学习环境噪音
    scene cg01a1 #梁芷柔听讲CG-1|标准|冬装|CG01a1
    with fade
    l "「……」"
    y "「……」"
    voice "audio/voice/005355.ogg"
    l "「咳咳咳。」"
    y "「……」"
    l "「……」"
    y "「咳……咳咳！」"
    l "「……」"
    y "「……」"
    stop sound fadeout 3.0
    "……{p}…………"

    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    scene bg b01 #教室
    with fade
    show chara b07a #梁芷柔立绘|冬季校服|消沉1
    with dissolve
    y "「……」"
    l "「……」"
    y "「那啥……」"
    show chara b02 #梁芷柔立绘|冬季校服|皱眉
    with dissolve
    voice "audio/voice/005356.ogg"
    l "「……少说话，嗓子难受。」"
    y "「……」"
    l "「……」"
    y "「噗。」"
    show chara b09 #梁芷柔立绘|冬季校服|坏笑
    with dissolve
    voice "audio/voice/005357.ogg"
    l "「嘻嘻……咳！」"
    show chara b07b #梁芷柔立绘|冬季校服|消沉2
    with dissolve
    y "「好了不废话了……咳，给你这个。」"
    "我压低声音，装作随意地将一样东西丢在她桌子上。"
    show chara b06 #梁芷柔立绘|冬季校服|吃惊
    with dissolve
    voice "audio/voice/005358.ogg"
    l "「……啊，这是……」"
    y "「刚才上课的时候偷偷做的。」"
    "丢给她的，是一朵红色的折纸玫瑰花。"
    "今年的春节来的比较早，结果就是初七开学的第一天，恰好赶上情人节。"
    "在学校当然不能带真花过来，所以就提前学了折纸的方法，带了张红纸，现场折了一朵出来。"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/005359.ogg"
    l "「嘻嘻……谢谢。」"
    show chara b10 #梁芷柔立绘|冬季校服|开心
    with dissolve
    voice "audio/voice/005360.ogg"
    l "「那么这个就请你收下咯。」"
    y "「嗯？」"
    "梁芷柔也悄悄递给我一个锡纸包着的……指甲盖大小的玩意。"
    y "「这啥啊……噢噢。」"
    "拆开包装，里面是一颗巧克力豆。"
    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    voice "audio/voice/005361.ogg"
    l "「嗓子不好，不许多吃，意思意思吧。」"
    y "「呵呵，好。」"
    "我将巧克力豆扔进嘴里，感受着丝丝的甜意。"
    hide chara
    with dissolve
    stop sound fadeout 3.0

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    voice "audio/voice/055001.ogg"
    a "「哎哟，学霸们又在交流经验哪？」"
    y "「啊？」"
    voice "audio/voice/065001.ogg"
    b "「行了你啊，人家是模范夫妻，感冒都一起，你过来添什么乱哪！」"
    voice "audio/voice/065002.ogg"
    b "「哦～那个老叶，不打扰你……嗯，那个，『学习』了啊？加油啊！」"
    y "「什么鬼！……咳咳！欺负我现在说不出话来，你等着……咳咳！」"
    voice "audio/voice/055002.ogg"
    a "「行啦行啦，别勉强。年轻人，要适度！」"
    y "「你给我滚！」"
    play audio "audio/voice/055003.ogg" noloop
    play audio "audio/voice/065003.ogg" noloop
    ab "「哈哈哈哈哈——」"
    stop music fadeout 2.5

    show chara b04 #梁芷柔立绘|冬季校服|无奈
    with dissolve
    "轰走了两个来捣乱的逗比，我和梁芷柔相顾无言。"
    y "「……别理他们，抽疯呢。」"
    show chara b11 #梁芷柔立绘|冬季校服|微笑
    with dissolve
    voice "audio/voice/005362.ogg"
    l "「嘻嘻，没事啦。再说……」"
    y "「嗯？」"

    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    show chara lb09 #梁芷柔立绘|冬季校服|坏笑|近
    with dissolve
    voice "audio/voice/005363.ogg"
    l "「他们也不算说错嘛？」"
    y "「啊……」"
    show chara b10 #梁芷柔立绘|冬季校服|开心
    with dissolve
    voice "audio/voice/005364.ogg"
    l "「……嘻嘻！好啦，回去吧，该上课了。」"
    scene bg b00a #天空|候鸟
    with fade
    "新的，也是最后的学期开始了。"
    "我，与她，都斗志满满。"
    "为了那个目标，我们共同的目标。"
    "发起了最后的冲刺——"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    pause

    play sound "audio/sound/transition.ogg" noloop
    scene trans t06 #转场 天空
    with fade
    pause

#06.初夏

#4月中旬。
#二诊考试成绩公布后。

    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    scene bg b02d #城区|春
    with fade
    "四月，草长莺飞。"
    "黄河告别了自己的枯水期，逐渐高涨的河水为县城洗去了凛冬时的灰白色，进而变为生机盎然的叠翠。"
    "湿地公园经过一个秋冬的修护保养，修复了当初被水淹没的痕迹，植被也已全部复苏，终于重新对游人开放。"
    "不过，现在里面还没有多少鸟就是了。"
    "本地的候鸟早已启程前往遥远的西伯利亚，而南方飞来此处的候鸟还大多尚未抵达。"
    "此时此刻，翱翔在这片天空之上的，多是从南方途经此地，之后还要继续向北前行的过境鸟。"
    stop sound fadeout 3.0
    "……{p}…………"
    scene bg b01 #教室
    with fade
    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    y "「……」"
    y "「唉。」"
    "高中的最后一个学期是极端枯燥乏味的。"
    "每天像是机器人一样精密地保持着两点一线的作息，在学校除了复习就是考试，终日重复不停，乏善可陈。"
    "好在，比起其他人来，我还算是不那么无聊的。毕竟……"
    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
    voice "audio/voice/006001.ogg"
    l "「嗯？怎么啦？」"
    "我可以和她在一起。"
    y "「这个嘛，我在想啊……」"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/006002.ogg"
    l "「嗯。」"
    stop sound fadeout 3.0

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    y "「前两天的体检，这结果不是已经出来了吗？」"
    voice "audio/voice/006003.ogg"
    l "「是呀。」"
    y "「我想看看你的那份报告啊。」"
    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
    voice "audio/voice/006004.ogg"
    l "「哈？你看它干什么？」"
    y "「我挺好奇的。比如，体重啊，有没有量三围啊……」"
    with hpunch
    play sound "audio/sound/effect29.ogg" noloop
    show chara la03 #梁芷柔立绘|夏季校服|生气|近
    with dissolve
    y "「哎哟哟哟哟。」"
    y "「住手！疼死我了！快住手啊，别人都看着呢！」"
    voice "audio/voice/006005.ogg"
    l "「哼！」"
    y "「噫。哎哟我的耳朵啊……」"
    voice "audio/voice/006006.ogg"
    l "「活该，一点正经的都没有！」"
    y "「哎呀，开个玩笑嘛，干嘛那么认真。」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    l "「……」"
    y "「好吧好吧我错了，我错了还不行吗？」"
    l "「……」"
    y "「……我真错了，饶了我吧。」"
    show chara la03 #梁芷柔立绘|夏季校服|生气|近
    with dissolve
    voice "audio/voice/006007.ogg"
    l "「哼，你啊，你这张嘴！」"
    "梁芷柔用食指戳着我的脑门，用力地推了一下。"
    with vpunch
    play sound "audio/sound/effect30.ogg" noloop
    y "「哎哟哟。」"
    stop music fadeout 2.5

    play music "audio/music/bgm01.ogg" fadein 1.5 #春～樱飞～
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/006008.ogg"
    l "「所以呢，你到底在想什么，啊？」"
    y "「……」"
    y "「嗯……怎么说呢。」"
    y "「我在想……待会儿不就是报考咨询了吗？」"
    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
    voice "audio/voice/006009.ogg"
    l "「嗯。」"
    y "「我该怎么跟郑老师说，他才不会活撕了我呢？」"
    show chara la05a #梁芷柔立绘|夏季校服|苦笑1|近
    with dissolve
    voice "audio/voice/006010.ogg"
    l "「这……」"
    show chara la05b #梁芷柔立绘|夏季校服|苦笑2|近
    with dissolve
    voice "audio/voice/006011.ogg"
    l "「这个嘛……」"
    y "「唉……」"
    y "「要是开门见山地说『我要去樱华上大学』，你觉得他是会先啐我一脸呢，还是直接大耳刮子就上来了。」"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/006012.ogg"
    l "「不至于吧？郑老师哪有那么狠。」"
    y "「那是对你不狠。对别人……呵呵。」"
    y "「再说了，你也知道，咱们这地方，别说郑老师了，从校长往下，哪一个不是想重点想疯了的……他们能饶得了我才怪。」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/006013.ogg"
    l "「这倒也是……郑老师他们肯定还是希望你考个重点，起码是211吧。」"
    y "「也不用什么起码211了，肯定就是百薇。211啊985啊，还有其他的一大堆什么计划，应有尽有，还优待本省的考生，完美。」"
    voice "audio/voice/006014.ogg"
    l "「嗯……」"
    y "「结果呢，我放着百薇不去考，偏要往樱华跑，这个司马昭之心啊，估计是瞒不住了。」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/006015.ogg"
    l "「呵呵……反正也瞒不住了，那你还担心个什么啊？」"
    y "「是啊，伸头是一刀，缩头也是一刀，走一步算一步吧。反正最后填志愿的是我，他又不能不让我去考。」"
    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
    voice "audio/voice/006016.ogg"
    l "「哪有那么严重啊……不过，你家里那边怎么办？」"
    y "「这个倒是问题不大。我你又不是不知道，搁一年前我能考上个二本他们就要狂喜乱舞了，好说。」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/006017.ogg"
    l "「那就行。」"
    y "「不过我怕老郑一着急，把这事往你家里捅啊？」"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/006018.ogg"
    l "「我嘛……也还好吧。」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/006019.ogg"
    l "「虽然之前确实是比较怕，不过就像你刚才说的，反正都到这个时候了。」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/006020.ogg"
    l "「咱们是谁啊，高三考生！谁敢在这个时候主动让咱们不痛快啊？想不想让我好好考了？发挥失常了谁负责啊？县状元还想不想要了？」"
    y "「哇，养寇自重啊你这个。」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/006021.ogg"
    l "「嘻嘻，物尽其用嘛。」"
    "梁芷柔露出狡黠的笑容，我也笑了起来，朝她伸出大拇指，点赞。"
    "不过，事到这里还不算完。"
    stop music fadeout 2.5

    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    y "「然后呢，就是另一个问题了……」"
    y "「说到底，这个志愿，我该怎么报呢？」"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/006022.ogg"
    l "「啊……」"
    "话题转换到这边，我变得有些愁眉苦脸。"
    "樱华市的高校资源分布很奇葩，由于各种各样的原因，樱华市的优秀大学数量在一线城市里算是比较少的。"
    "樱华大学的确是在全国都名列前茅的超一流大学，不过除了它以外，樱华市再也没有其他的重点大学了。"
    "非重点的大学当然还是有的，不过……"
    y "「理工科的话，也就是樱华理工大学和樱华工业大学了吧。」"
    show chara la08a #梁芷柔立绘|夏季校服|担心1|近
    with dissolve
    voice "audio/voice/006023.ogg"
    l "「嗯……要说的话当然最好是去理工大学，但它那个分数线……你……」"
    y "「是啊……」"
    y "「不算是重点，但愣是比百薇还难考，这上哪儿讲理去。」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/006024.ogg"
    l "「人家再怎么说也是经常参加国家重点项目的大学，不是重点又不代表水平不行。而且毕竟地理位置摆在那里，要这个分数也正常。」"
    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
    voice "audio/voice/006025.ogg"
    l "「你这次二诊……考了572分吧？」"
    y "「是啊。」"
    "月初，县里进行了第二次模拟诊断考试，我拿到了一个比较微妙的成绩。"
    "与一诊相比算是进步不小，也让我荣登全校第二名的宝座，抛开梁芷柔这样的妖孽不谈，已经可以说是登顶了。"
    "然而这只是矬子里面拔将军罢了，放到全省排名，我还在1500名开外。"
    "去年百薇大学在省内招了1200人，我这个排名目前算是勉强够到了边，再努一努力的话应该可以做到比较稳妥。"
    "但外省的大学就不像百薇这么好说话了，能不能更进一步，我是一点把握也没有。"
    "但偏偏……也不是完全没有希望。"
    "这就很难受了。"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/006026.ogg"
    l "「其实我觉得，这次二诊的题还是比较难的。像你这样，基础打得还行，但是高端题拿不准的，被一刀切下来了好多。」"
    show chara la01a #梁芷柔立绘|夏季校服|普通|正面|近
    with dissolve
    voice "audio/voice/006027.ogg"
    l "「如果高考不这么极端的话，你的分数应该还能再上去一截。」"
    y "「但别人的分数也一样上去了吧？没意义啊？」"
    voice "audio/voice/006028.ogg"
    l "「就算都提高也是有多有少的呀，而且你又不考本省的大学，肯定是有利的。但是……」"
    show chara la08b #梁芷柔立绘|夏季校服|担心2|近
    with dissolve
    voice "audio/voice/006029.ogg"
    l "「就算是这样，也还是不太稳啊。」"
    y "「嗯……」"
    l "「……」"
    show chara la07b #梁芷柔立绘|夏季校服|消沉2|近
    with dissolve
    voice "audio/voice/006030.ogg"
    l "「稳妥起见的话，要不……考虑一下工业大学？」"
    y "「工业大学吗……」"
    y "「……」"
    y "「稳倒是稳了，可是……」"
    "的确，樱华工业大学往年基本上只是在省控线往上50分左右，比我现在的成绩都还要低上一点，报考不成问题。"
    "不过，看这个分数也就知道了，这就是一所很普通的一本大学而已。"
    "虽然它是省内理工类排名仅次于樱华大学和樱华理工大学的高校，但却不是因为它有多么好，而是因为那里就只有这么几所还说得过去的大学。"
    "要真是报考理工完全无望，工大倒也可以算是一根救命稻草，然而现在……就只是鸡肋了。"
    l "「……」"
    show chara la07a #梁芷柔立绘|夏季校服|消沉1|近
    with dissolve
    voice "audio/voice/006031.ogg"
    l "「最起码……你可以先考过去不是？」"
    y "「……嗯？」"
    "愣了一下，下意识地朝梁芷柔看去。"
    show chara la07b #梁芷柔立绘|夏季校服|消沉2|近
    with dissolve
    l "「……」"
    "梁芷柔抿着嘴，似乎说出这句话让她花费了很大的力气。"
    y "「……」"
    "原来如此。"
    "本来还有点奇怪。连我都不太想考虑的一所学校，怎么还能入得了梁芷柔的眼。"
    "但现在，看到她这个样子，我就明白了。"
    show chara la08a #梁芷柔立绘|夏季校服|担心1|近
    with dissolve
    voice "audio/voice/006032.ogg"
    l "「如果只看排名的话啊，在全国确实有点靠后了，不过基本的水平应该还是有的。」"
    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
    voice "audio/voice/006033.ogg"
    l "「而且考那边的话，专业肯定比较好选啊，其实也不见得就比理工大差了。」"
    show chara la01a #梁芷柔立绘|夏季校服|普通|正面|近
    with dissolve
    voice "audio/voice/006034.ogg"
    l "「我查过了，他们的工科其实也很不错，有几个学科ESI也能排进\1\%呢……」"
    "说出第一句之后，梁芷柔像是打开了一个闸门，开始不停地继续补充起来。"
    "大概她思考这事也很久了吧，准备工作……确实是做得很足，也很有道理。"
    y "「……」"
    "说实话，完全出乎了我的意料。"
    "然而，事情当然不是那么简单的。"
    "师资力量、设施条件、同学圈子，不同学校之间的差异有多么巨大……"
    "她明明应该比我更清楚才对。"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/006035.ogg"
    l "「之后还可以考研的嘛，本地区本专业，只是跨个学校的话，没那么难的……」"
    "她接受了我，哪怕我只能从一个不那么高的起点开始。"
    "我不觉得她是不再看重这些东西了。"
    "她这样做……是因为她准备押上自己一生中最美好的一段年华，去等待、去赌我在更远一点的未来可以破茧成蝶。"
    y "「……」"
    "虽然如此，我却不能就这么心安理得地接受她的好意。"
    "倒不如说，经她这样一说，反而让我想明白了自己该做的选择。"
    y "「芷柔，等一下。」"
    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
    voice "audio/voice/006036.ogg"
    l "「啊……嗯？」"
    y "「这个问题我之前也想过很多遍，刚才听你说的时候我又认真想了想，终于想明白了。」"
    y "「我……不打算报工大。」"
    show chara la06 #梁芷柔立绘|夏季校服|吃惊|近
    with dissolve
    voice "audio/voice/006037.ogg"
    l "「……哎？」"
    show chara la08a #梁芷柔立绘|夏季校服|担心1|近
    with dissolve
    voice "audio/voice/006038.ogg"
    l "「为什么呀，一点都不考虑吗？」"
    y "「嗯。」"
    show chara la08b #梁芷柔立绘|夏季校服|担心2|近
    with dissolve
    voice "audio/voice/006039.ogg"
    l "「可你现在不一定能考得上理工大啊？」"
    y "「是啊，但也不一定就考不上嘛，总得去试试。」"
    y "「这不是还有两个月呢么？继续努力就是了，有多少力努多少力，拼到底为止。」"
    show chara la07b #梁芷柔立绘|夏季校服|消沉2|近
    with dissolve
    voice "audio/voice/006040.ogg"
    l "「但万一……」"
    y "「我在想……」"
    y "「只是考过去…{cps=2}…就{/cps}够了吗？」"
    show chara la06 #梁芷柔立绘|夏季校服|吃惊|近
    with dissolve
    l "「……」"
    y "「先考到樱华去，哪怕只是一所很普通的大学，然后再用多出来的四年时间完成逆袭？」"
    show chara la08b #梁芷柔立绘|夏季校服|担心2|近
    with dissolve
    y "「不是完全没有可能。」"
    y "「但是，你不觉得，那是比我考理工大更不稳定的一件事吗？」"
    y "「要真是这么容易就能做到，你干嘛还要拼命往樱大这样的学校考？就是因为它真的不一样啊。」"
    show chara la07a #梁芷柔立绘|夏季校服|消沉1|近
    with dissolve
    y "「……」"
    y "「虽然我现在是能比较容易地考上工大，但是……我才想起来，这其实不是我的目的。」"
    y "「我不是简单地为了『去樱华』而去考那边的大学……」"
    y "「而是为了『追上你』，『和你一起』去樱华。」"
    show chara la07b #梁芷柔立绘|夏季校服|消沉2|近
    with dissolve
    voice "audio/voice/006041.ogg"
    l "「啊……」"
    y "「所以，其实对我来说，不用等到高考，我的考试从现在……从半年前，就已经开始了。」"
    y "「在你突飞猛进的那几年里，我一直无所事事，什么也没做地荒废着。」"
    y "「如果现在，我不能保持在进步速度上超过你，那我恐怕永远、永远都没办法实现这个目标。」"
    y "「这半年，我觉得我还是有点机会的。但之后怎么样，其实我还是很没谱。」"
    y "「因为你要去的是樱大啊……那是全国最顶尖的几所大学了。」"
    y "「就算我能考到理工大，想要赶上你都非常困难，我又不是什么天赋异禀的天才。」"
    y "「但这已经是没办法的办法了，毕竟前面我浪费了那么多时间，现在只能尽量抢救抢救。」"
    y "「可如果我只能去工大那样的学校的话……我知道我自己，根本就不行，做不到的。」"
    y "「你想想，那种情况下，你能等我多久？就算你能等吧！可要让你那么等，我还不如直接去考百薇算了，好歹也是一流的名校呢。」"
    y "「所以……我想明白了。理工大就是我的底线。」"
    y "「如果我现在没有勇气朝它冲刺，退而求其次了，那我这一辈子，就什么都冲不过去了。」"
    y "「谢谢你……但……」"
    y "「我还是得去挑战一次。」"
    show chara la07a #梁芷柔立绘|夏季校服|消沉1|近
    with dissolve
    l "「……」"
    show chara la05a #梁芷柔立绘|夏季校服|苦笑1|近
    with dissolve
    voice "audio/voice/006042.ogg"
    l "「……嗯。」"
    "梁芷柔欲言又止，最终只是点了点头。"
    "那神色……该说是担忧呢，还是欣慰呢？也许二者兼有吧？"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/006043.ogg"
    l "「那你……」"
    voice "audio/voice/096001.ogg"
    g "「班长！」"
    show chara la13b #梁芷柔立绘|夏季校服|疑惑2|近
    with dissolve
    voice "audio/voice/096002.ogg"
    g "「郑老师说现在开始咨询，让你组织一下，按学号过去。还有就是说，让班里面别太乱了，教导主任也在呢。」"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/006044.ogg"
    l "「……哦，好。」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/006045.ogg"
    l "「那……就先这样。」"
    y "「嗯，你先忙去吧。」"
    show chara la01b #梁芷柔立绘|夏季校服|普通|侧面|近
    with dissolve
    voice "audio/voice/006046.ogg"
    l "「嗯。」"
    l "「……」"
    show chara la07b #梁芷柔立绘|夏季校服|消沉2|近
    with dissolve
    voice "audio/voice/006047.ogg"
    l "「其实……你说的对。」"
    show chara la08a #梁芷柔立绘|夏季校服|担心1|近
    with dissolve
    voice "audio/voice/006048.ogg"
    l "「我只是有点害怕……不过，也是。如果这样的坎都迈不过去的话，我怎么能给你那个机会呢？」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/006049.ogg"
    l "「呵呵……好了！」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/006050.ogg"
    l "「不说丧气话了！加油吧，先把郑老师搞定再说！」"
    y "「喂喂喂，你这还不丧啊……」"
    show chara la09 #梁芷柔立绘|夏季校服|坏笑|近
    with dissolve
    voice "audio/voice/006051.ogg"
    l "「嘻嘻，早晚的事。我看好你哦！」"
    y "「……行吧。」"
    y "「我会活着回来的。」"
    hide chara
    with dissolve
    y "「……」"
    y "「谢谢你。」"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/ambientnoise07.ogg" fadein 1.5 loop #书店环境噪音
    scene bg b01 #教室
    with fade
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    z "「……」"
    z "「…………」"
    voice "audio/voice/016001.ogg"
    z "「……嗯……」"
    voice "audio/voice/016002.ogg"
    z "「你觉得……」"
    voice "audio/voice/016003.ogg"
    z "「我是应该先啐你一脸呢，还是直接给你个大耳刮子啊？」"
    y "「……这样不好吧，郑老师。」"
    show charaz lh04 #老师立绘|夏季|咆哮|近
    with dissolve
    voice "audio/voice/016004.ogg"
    z "「要不，我还是活撕了你算了。」"
    y "「呃……」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/016005.ogg"
    z "「你小子啊，这是毫不掩饰了呀，啊？哼……」"
    show charaz lh04 #老师立绘|夏季|咆哮|近
    with dissolve
    voice "audio/voice/016006.ogg"
    z "「放着好好的百薇不去报，偏要去樱华理工，啊？什么都不如，还比百薇难考，你怎么那么想得开啊？嗯？」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/016007.ogg"
    z "「你这倒是说到做到，呵！说追梁芷柔，还真要去追呀？」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/016008.ogg"
    z "「不是我说你，啊，你这岁数的孩子，有点这样的想法是正常的，啊。但是这个人哪，总得量力而行吧？啊？有点自知之明，知道吗？」"
    voice "audio/voice/016009.ogg"
    z "「这丑小鸭变白天鹅，是那么好变的啊？当然了，你比鸭子强，但我说啊，也就是个大鹅的水平，比这天鹅还差得远呢。」"
    voice "audio/voice/016010.ogg"
    z "「你就不想想，你这样就真的能追得上人家吗？我知道，你们俩现在关系挺好的，我又不瞎，我不理你们，是因为你们俩之前都管得住自己，但是你现在这个吧，我不管就不行了！」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/016011.ogg"
    z "「这毕竟……高考啊，是关系你一辈子的事情。」"
    y "「……」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/016012.ogg"
    z "「唉……你将来呢，可能会谈很多次的恋爱，甚至结婚了，都可以结了离、离了结。但是高考、大学，这些你的前学历，选完了就是板上钉钉的，改不了啦。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/016013.ogg"
    z "「我不是说樱华理工不好，那也是2011计划的大学，而且还在樱华，有它的优势。但除了地理位置，其他的说到底，和百薇还是有差距的。」"
    voice "audio/voice/016014.ogg"
    z "「我想啊，你将来还是想去大城市发展的对吧？」"
    voice "audio/voice/016015.ogg"
    z "「这四年以后啊，你拿着百薇的文凭出去，啊，和你拿着樱华理工的文凭出去，你觉得能一样吗？」"
    show charaz lh04 #老师立绘|夏季|咆哮|近
    with dissolve
    voice "audio/voice/016016.ogg"
    z "「你要说你不在乎、不指着这个也就罢了，但是可能么？啊？你家是有矿还是怎么的？你不用找工作啦？」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/016017.ogg"
    z "「你给人递简历的时候，人家第一眼看的就是这个。一个全国排三十，一个六七十名往外，换成你，你怎么选哪？」"
    y "「……」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/016018.ogg"
    z "「唉……这说到家里啊，还有一个事，你想清楚了没有啊？」"
    voice "audio/voice/016019.ogg"
    z "「百薇和樱华，虽然都是省会城市，不过这消费水平可不一样啊。那边物价有多贵，你知道吗？」"
    voice "audio/voice/016020.ogg"
    z "「是，那边挣得也多，你以后呢可以留在那边把钱挣回来。但是你毕业以后再去不好吗？就非得在这时候啊？」"
    voice "audio/voice/016021.ogg"
    z "「你家什么情况我也知道，供你去是没问题，可也不是随随便便什么压力都没有的吧！」"
    voice "audio/voice/016022.ogg"
    z "「你是不是觉得你家里养你18年很容易啊？你知不知道你到那边上学要花多少钱哪？」"
    show charaz lh04 #老师立绘|夏季|咆哮|近
    with dissolve
    voice "audio/voice/016023.ogg"
    z "「你这不光是自己任性，啊，你花的是你父母的钱，你知道吗？你觉得这么干，合适吗？」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/016024.ogg"
    z "「就因为一个……啊？」"
    z "「……」"
    voice "audio/voice/016025.ogg"
    z "「唉！」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/016026.ogg"
    z "「说说吧，你是怎么想的……啊，除了梁芷柔啊，不算她。」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/016027.ogg"
    z "「我倒是要看看，你还能说出点什么来。要是能说得过去，也行，啊，要是说不过去……哼……」"
    voice "audio/voice/016028.ogg"
    z "「……你就等着吧。」"
    y "「呼。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    "还好。"
    "班主任毕竟凶名在外，我还真怕他一上来就不问青红皂白地把我给否决掉。"
    "不过，尽管说了好一通长篇大论，好歹还算是给了我一个机会。"
    "不得不说，虽然包括我在内的很多人都总觉得郑老师太过严厉，但同时，我们也得承认，他是个相当认真负责的人。"
    "他说的这些都颇有道理，确实是真的在替我着想。可惜，我也只能辜负他的好意了。"
    "毕竟，我也有自己的坚持。"
    stop sound fadeout 3.0
    y "「……」"

    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    "深吸了一口气，在心中组织了一下语言。"
    y "「郑老师。」"
    y "「您说的没错，我想去樱华，起因确实是梁芷柔。」"
    y "「不过，也不只是因为她。」"
    y "「……」"
    y "「梁芷柔……是我努力学习的动力，没有她的话，我可能，嗯，我肯定没现在这么努力。」"
    z "「……」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    "老师瞪了我一眼，不过还是没打断我，用眼神示意我继续说。"
    y "「不过……其实最开始的时候，我连自己能不能达到一本线都没谱，根本没想那么远的事。」"
    y "「我就是想稍微接近她一点，能有点共同话题，万一顺便还考了个一本，那当然最好了。」"
    y "「梁芷柔也是这么给我定的目标，至少到一本线，而最终的目标……其实也就是百薇。」"
    y "「……」"
    y "「百薇大学……确实是好，咱们这里也都认这块牌子。」"
    y "「我要是没记错，在您上大学那会儿，百薇在全国的高校榜里甚至还能排进前十呢吧？」"
    voice "audio/voice/016029.ogg"
    z "「嗯。」"
    y "「可现在，它排在三十名，对吧？」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/016030.ogg"
    z "「……嗯。」"
    "老师脸颊微微抽了抽，犹豫了一下，不过还是点头承认了。"
    y "「二十几年，百薇在全国……掉了二十几名。它的录取分数线甚至比排名掉得还快，都快跌出前一百了。」"
    y "「我不是瞧不起它，我不会、也没这个资格，但是……」"
    y "「我有的时候会想，为什么会变成这样？」"
    y "「网上有人戏称百薇是全国最苦的重点大学，说它流失出去的师资力量都足够再建一所百薇大学了。」"
    y "「而且，咱们这里的好学生，像梁芷柔这样的，只要有条件、分数够的，也全都优先考虑外省的那些大学。」"
    y "「就算您劝我去考百薇，那也是为了等到毕业以后……再离开这里，去大城市找工作。」"
    y "「为什么大家都要往外跑？」"
    y "「我一开始也想不明白，但是看着梁芷柔，我又觉得我多少明白了一点。」"
    y "「那些地方，那些像樱华这样的大城市，有……梦想。」"
    y "「那里有他们的梦想，或者可以实现他们的梦想，甚至那里本身就是他们的梦想。」"
    z "「……」"
    y "「……」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    "老师张了张嘴，似乎是想要说些什么，不过最终也没有说出来。"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    y "「老师，我呢，从小到大也没出过几次远门，没什么见识，也谈不上什么像样的梦想。」"
    y "「一直以来都是循规蹈矩的，老老实实上学、念书，成绩比上不足比下有余，没有不满意，也没多少追求。」"
    y "「我曾经以为我以后也会是这个样子。考一个还可以的大学，等毕了业，按部就班地找一份差不多的工作，普普通通地过日子。」"
    y "「将来的路，大概会往什么方向走、走成什么样子，全都能猜个差不多。」"
    y "「……」"
    y "「当然，这也没什么不好的。」"
    y "「但是现在，跟梁芷柔待久了，她让我看到了另外一种可能。」"
    y "「我发现，我能做到的事，其实要比自己以为的更多。」"
    y "「我不一定要按照现在的路，一成不变地走下去。」"
    y "「老师，就像您说的，高考是关系我们一辈子的事。」"
    y "「所以我才要抓住这个机会，走出去。」"
    y "「虽然我不知道那会走到什么地方去，能走多远……」"
    y "「但正是因为这样，我才想去试试看，看看自己……能够做到什么，究竟想做什么，让自己变得更加完整。」"
    y "「所以，我需要一个更大的舞台。」"
    y "「百薇……是不够的。」"
    y "「……」"
    y "「当然，也许我会碰个头破血流，再灰头土脸地折回来……也许最后发现还不如现在这样。」"
    y "「但那也得是我去尝试过以后，才能让我死心。」"
    y "「要是留下来了……我只会变回从前那样。」"
    y "「就算有些地方发生了一点改变，比如可以考上当初根本不敢想的百薇大学，将来没准也还是会去那些大城市发展……」"
    y "「但那只是让前途更宽了一点，基本的方向没有变。」"
    y "「找工作，过日子。可能能找到一份更好的工作，让日子过得更好一点，但也就仅此而已。」"
    y "「而到了那时候……恐怕我也一辈子都不会再有现在这样的想法了。」"
    y "「所以……」"
    y "「……」"
    y "「这就是我为什么想要跟梁芷柔一起往樱华考的理由。」"
    y "「老师。」"
    z "「……」"
    z "「…………」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/016031.ogg"
    z "「嗯………………」"
    "老师的眉头拧成一片扭曲的沟壑，长吁短叹了一阵。"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/016032.ogg"
    z "「……『梦想』啊。」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/016033.ogg"
    z "「倒是个好东西。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/016034.ogg"
    z "「嗯……不过你想没想过啊，梦想这个东西，说到底还是需要现实来支撑的。」"
    voice "audio/voice/016035.ogg"
    z "「我就当你能考过去。但你到了那边，能不能找到你这个梦想呢……」"
    voice "audio/voice/016036.ogg"
    z "「你是……真的想明白了吗？」"
    voice "audio/voice/016037.ogg"
    z "「你年轻，有点闯劲是好事。不过老师作为过来人哪，还是得劝你一句：你这条路，可不好走啊。」"
    y "「是……我知道。」"
    y "「老师，谢谢您。」"
    y "「不过，老师，我还是想去试试。」"
    stop music fadeout 2.5

    play sound "audio/sound/ambientnoise07.ogg" fadein 1.5 loop #书店环境噪音
    z "「……」"
    voice "audio/voice/016038.ogg"
    z "「唉！」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/016039.ogg"
    z "「好吧，算你小子过关了。」"
    y "「哎？啊，谢谢您！」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/016040.ogg"
    z "「哎！别急啊，着什么急呢，我还没说完呢！」"
    voice "audio/voice/016041.ogg"
    z "「这死罪可免，活罪难逃。啊，有两个条件你答应也得答应，不答应也得答应。」"
    y "「啊？」"
    voice "audio/voice/016042.ogg"
    z "「第一，你的第一志愿可以报樱华理工，但是第二志愿你必须给我报百薇。」"
    voice "audio/voice/016043.ogg"
    z "「这百薇对本地考生有特殊政策，就算有分数级差，可能也挑不到什么好专业了，但万一第一志愿落榜了，起码你还能有个救啊。」"
    y "「……」"
    voice "audio/voice/016044.ogg"
    z "「第二呢，从现在开始，到临考之前，你每天都得单独补课。」"
    y "「……啊？」"
    show charaz lh04 #老师立绘|夏季|咆哮|近
    with dissolve
    voice "audio/voice/016045.ogg"
    z "「啊什么啊？就你现在这样，敢说自己能考上吗？你总不能都指着梁芷柔吧？她自己不复习啦？你当我们这些老师都是死人啊？」"
    y "「啊……呃……不是……我……」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/016046.ogg"
    z "「没有什么不是。听到没有啊？我告诉你啊，我会跟各科老师都打好招呼，回头单独给你一份课表，你给我来加课！」"
    voice "audio/voice/016047.ogg"
    z "「这虽然说吧，我不太看好你考樱华那边的大学，但你最后要连百薇也上不了……哼，别以为你毕业了，我就拿你没办法！」"
    y "「呃……好。」"
    y "「……」"
    y "「老师……您为什么要……」"
    show charaz lh04 #老师立绘|夏季|咆哮|近
    with dissolve
    voice "audio/voice/016048.ogg"
    z "「为什么，你说为什么？你他娘的是咱们学校年级第二名好不好？咱们这儿啊，除了梁芷柔就是你了，你跟我说为什么？」"
    voice "audio/voice/016049.ogg"
    z "「你要是考砸了，咱们一中的招牌还要不要了？我们的脸还要不要了？啊？」"
    voice "audio/voice/016050.ogg"
    z "「还有你自己！啊？不想多考点分啊？不想找你的梦想啦？让你来你就来，听明白没有？」"
    y "「明白了明白了！」"
    y "「……」"
    y "「老师……谢谢您。」"
    "我站起身，朝郑老师恭恭敬敬地鞠了一躬。"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    "老师「哼」了一声，摆出一副不耐烦的样子朝我挥了挥手。"
    voice "audio/voice/016051.ogg"
    z "「哎走走走走走，赶紧的，叫下一个进来。」"
    y "「是！」"
    scene bg black #黑屏
    with fade
    stop sound fadeout 3.0

    "……{p}…………"
    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    scene bg b01 #教室
    with fade
    show chara la06 #梁芷柔立绘|夏季校服|吃惊|近
    with dissolve
    voice "audio/voice/006052.ogg"
    l "「……咦？」"
    y "「怎么啦，这么吃惊？」"
    show chara la13a #梁芷柔立绘|夏季校服|疑惑1|近
    with dissolve
    voice "audio/voice/006053.ogg"
    l "「你居然活着回来了！」"
    y "「喂！」"
    show chara la10 #梁芷柔立绘|夏季校服|开心|近
    with dissolve
    voice "audio/voice/006054.ogg"
    l "「哈哈……你到底跟郑老师说了什么啊，这么管用？」"
    y "「嗯……」"
    y "「我跟他说啊——」"
    show chara la11 #梁芷柔立绘|夏季校服|微笑|近
    with dissolve
    voice "audio/voice/006055.ogg"
    l "「嗯。」"
    y "「『做人如果没有梦想，那跟咸鱼有什么区别』？」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    l "「……」"
    show chara la06 #梁芷柔立绘|夏季校服|吃惊|近
    with dissolve
    voice "audio/voice/006056.ogg"
    l "「哈？」"
    y "「然后郑老师就感动地放我了一条生路。」"
    show chara la02 #梁芷柔立绘|夏季校服|皱眉|近
    with dissolve
    voice "audio/voice/006057.ogg"
    l "「哎哎，说正经的哪！」"
    y "「这还不够正经啊？啊，当然了我也还说了点别的——」"
    y "「『你是要当一辈子懦夫，还是要当英雄！哪怕只有几分钟』？」"
    show chara la08b #梁芷柔立绘|夏季校服|担心2|近
    with dissolve
    l "「……」"
    y "「……」"
    y "「怎么样，帅吧？」"
    show chara la04 #梁芷柔立绘|夏季校服|无奈|近
    with dissolve
    voice "audio/voice/006058.ogg"
    l "「……我不想理你了。」"
    y "「喂喂喂别啊！」"
    show chara la02 #梁芷柔立绘|夏季校服|皱眉|近
    with dissolve
    voice "audio/voice/006059.ogg"
    l "「你这嘴啊，满嘴跑火车。」"
    y "「呵呵。」"
    show chara la01a #梁芷柔立绘|夏季校服|普通|正面|近
    with dissolve
    y "「其实你还真冤枉我了，不过这只是中心思想和主要内容嘛，具体的当然不是这样了。你听我说啊……」"
    stop sound fadeout 3.0

    scene bg b00a #天空|候鸟
    with fade
    "我即将迎来在这片天空下的最后一场挑战。"
    "这场挑战，是为了给我的人生开启一片新天地。"
    "尽管直到此时，我仍然不能完全把握住自己的未来。"
    "但我已经非常清楚，自己该怎样去做，才不会在未来后悔。"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t01 #转场 教室
    with fade
    pause

#6月2日。
#高考前的假期。

    play music "audio/music/bgm01.ogg" fadein 1.5 #春～樱飞～
    scene bg b02 #城区|夏
    with fade
    "时间匆匆而过，一转眼已是六月。"
    "初夏为山峦裹上了苍翠欲滴的盛装。"
    "而我们，也终于迎来了自己高中生涯的最后一天。"
    scene bg b11 #考场
    with fade
    y "「呼……这就算是可以了吧？」"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/006060.ogg"
    l "「嗯。辛苦啦。」"
    y "「还好吧……」"
    y "「……」"
    show chara a13b #梁芷柔立绘|夏季校服|疑惑2
    with dissolve
    voice "audio/voice/006061.ogg"
    l "「嗯？怎么了？」"
    y "「啊，没什么。」"
    y "「就是觉得教室突然变得这么干净了，有点不习惯。」"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/006062.ogg"
    l "「哈哈，毕竟是考场嘛。」"
    y "「嗯……」"
    y "「高中……这就算是结束了吧……」"
    show chara a01b #梁芷柔立绘|夏季校服|普通|侧面
    with dissolve
    l "「……」"
    show chara a11 #梁芷柔立绘|夏季校服|微笑
    with dissolve
    voice "audio/voice/006063.ogg"
    l "「嗯，是啊……」"
    y "「你说，你觉得自己高中这三年，算是过得怎么样？」"
    show chara a13a #梁芷柔立绘|夏季校服|疑惑1
    with dissolve
    voice "audio/voice/006064.ogg"
    l "「嗯……挺不好的吧？」"
    y "「嗯？」"
    show chara a07b #梁芷柔立绘|夏季校服|消沉2
    with dissolve
    voice "audio/voice/006065.ogg"
    l "「中考从二中考到一中，还以为自己这就算是翻身了，谁知道踌躇满志了不到一年，就又在樱华被人虐得不成人形。」"
    show chara a07a #梁芷柔立绘|夏季校服|消沉1
    with dissolve
    voice "audio/voice/006066.ogg"
    l "「然后呢，哭着鼻子逃回来头悬梁锥刺股，其他女生都在吃喝玩乐、打扮自己、谈恋爱，只有我每天泡在书海里面挣扎，最后因为压力太大还差点把自己给搞崩溃了……妈呀，我自己都觉得我好惨。」"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/006067.ogg"
    l "「哎，说起来，我居然都没有得近视，还真是奇迹了。」"
    y "「呃，这个嘛……」"
    show chara a11 #梁芷柔立绘|夏季校服|微笑
    with dissolve
    voice "audio/voice/006068.ogg"
    l "「嘻嘻，不过嘛，最后这一年不一样。」"
    show chara a09 #梁芷柔立绘|夏季校服|坏笑
    with dissolve
    voice "audio/voice/006069.ogg"
    l "「因为啊，有人陪在我身边，愿意和我一起承受这一切。」"
    show chara a05a #梁芷柔立绘|夏季校服|苦笑1
    with dissolve
    voice "audio/voice/006070.ogg"
    l "「所以……我想说，谢谢你。」"
    y "「……」"
    y "「咳。应该是我谢谢你吧。要不是你，我都不知道自己现在会是个什么样子。」"
    y "「我这最后一年才真是……不一样了。」"
    y "「虽然，心里还是有点没谱吧……」"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/006071.ogg"
    l "「哎呀你就别瞎紧张、自己吓唬自己了，想想你这最后的一个多月，那么多魔鬼训练难道都是闹着玩的啊？」"
    y "「啊……别提这个，求你了。」"
    show chara a11 #梁芷柔立绘|夏季校服|微笑
    with dissolve
    voice "audio/voice/006072.ogg"
    l "「嘻嘻。好啦，知道啦！你也别瞎想了。」"
    show chara a10 #梁芷柔立绘|夏季校服|开心
    with dissolve
    voice "audio/voice/006073.ogg"
    l "「走吧，回家吧！」"
    y "「嗯……嗯。」"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    scene bg b04 #滨河路|夏
    with fade
    "我们离开了学校。"
    "高考的时候，我们都不会在本校的考场进行考试。也就是说，自这一刻起，我不会再以「本校学生」的身份踏足一中了。"
    "在两个月前，我年满18周岁，在法律意义上成为了一名成年人。"
    "而在今天，我的高中生涯也画上了句号。"
    stop sound fadeout 3.0
    "虽然我还年轻，但已经不再只是个孩子了。"
    "接下来，我会按照自己的选择，朝着外面的世界，迈出步伐。"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t09 #转场 考场
    with fade
    pause

#6月7日。
#高考第一天。

    play sound "audio/sound/ambientnoise04.ogg" fadein 1.5 loop #白天环境噪音
    scene bg b02 #城区|夏
    with fade
    "六月的清晨，阳光早早地洒满了大地。"
    "吃过早饭，将所有的证件和文具反复检查了几遍之后，我走出了家门。"
    "时间比计划中的要提前了一点，虽然考场的距离稍远，但依然足以让我优哉游哉地溜达过去。"
    scene bg b04 #滨河路|夏
    with fade
    y "「……呼。」"
    "呼吸着新鲜的空气，在河边漫步。"
    "最近一年都紧紧张张的。真到了最后的决战时刻，反倒有种悠闲的感觉，也是十分奇妙了。"

    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    scene bg b05 #湿地公园|夏
    with fade
    "路过湿地公园的时候，站在路边远远地朝里面眺望了一会儿。"
    bird "「啾啾——」"
    bird "「嘎——」"
    "可以听到水鸟嬉戏的声音。"
    "这个时候，大多数的候鸟都已经结束了迁徙，开始繁衍生息，湿地公园也因此变得十分热闹。"
    "当然……"
    scene bg b00a #天空|候鸟
    with fade
    "应该，也还有一些候鸟，依然在天空中奋力翱翔吧……"
    y "「……」"
    voice "audio/voice/026001.ogg"
    d "「咦？小叶？」"
    y "「啊……」"
    scene bg b05 #湿地公园|夏
    with fade
    show charad g02 #书店店员立绘|惊讶
    with dissolve
    "回头一看，发现是我和梁芷柔常去的那家小书店的店员小姐。"
    "这一年来没少见，彼此也算是熟悉了。"
    y "「吴姐，上班去啊？」"
    voice "audio/voice/026002.ogg"
    d "「嗯，你这是？」"
    y "「去考试。」"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/026003.ogg"
    d "「哦……啊？考试？噢！对了，今天高考啊！」"
    y "「是啊。」"
    voice "audio/voice/026004.ogg"
    d "「哎哟，那可得加油啊！怎么样啊，打算考哪儿呀？」"
    y "「嗯……樱华那边。」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/026005.ogg"
    d "「哎……？哦……」"
    show charad g04 #书店店员立绘|坏笑
    with dissolve
    voice "audio/voice/026006.ogg"
    d "「……嚯嚯，樱华啊。」"
    voice "audio/voice/026007.ogg"
    d "「原来如此，原来是樱华啊……」"
    y "「吴姐……你笑得太诡异了。」"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/026008.ogg"
    d "「嘻嘻，我怎么诡异啦？不耽误你了，赶快去学校吧。加油喔！」"
    y "「哦，好！谢谢！」"
    voice "audio/voice/026009.ogg"
    d "「不客气！」"
    show charad g02 #书店店员立绘|惊讶
    with dissolve
    voice "audio/voice/026010.ogg"
    d "「啊，对了。」"
    y "「嗯？」"
    show charad g04 #书店店员立绘|坏笑
    with dissolve
    voice "audio/voice/026011.ogg"
    d "「既然这样，那你帮我给小梁也带个好呗！」"
    y "「呃？」"
    voice "audio/voice/026012.ogg"
    d "「嘿嘿，你懂啦！加油噢！我看好你！」"
    y "「……懂个鬼啊！」"
    hide charad
    with dissolve
    voice "audio/voice/026013.ogg"
    d "「哎呀，青春真好啊～想当初我上学的时候咋就没这么好的事呢……」"
    "店员小姐一边恶作剧似的朝我挥手，一边走掉了。"
    stop sound fadeout 2.0
    y "「……」"

    scene bg b11 #考场
    with fade
    "话虽如此，其实我这两天根本就见不到梁芷柔。"
    play sound "audio/sound/ambientnoise10.ogg" fadein 1.5 loop #安静学习环境噪音
    "我们被分到不同的考场，甚至连学校都不是同一个。"
    y "「呼……」"
    "将一切都准备妥当，我坐在座位上，观察着其他的考生"
    "整个考场都没有认识的人，只有少数几个似乎是和我同级、看着稍微有点脸熟的家伙。"
    "神色……不一而同。"
    "淡定者有之、紧张者有之、嬉闹者亦有之，甚至还有几个家伙看上去已经生无可恋了。"
    "而我在他们的眼里又是什么样呢？"
    play audio "audio/sound/effect06.ogg" noloop
    y "「啊……」"
    stop sound fadeout 3.0

    "预备铃响，考试快要开始了。"
    "学生们纷纷在自己的位置上坐定，监考老师进来宣读完考场规则，然后一众人等开始静静等待正式考试的铃声。"
    scene bg b11 #考场
    with fade
    "决战，开始了。"
    "上午的科目是语文。"
    "将姓名和准考证号等一堆基础信息填写完毕以后，我没有急着看卷子，而是先深深地吸了一口气。"
    y "「（吸——）」"
    y "「……呼！」"
    "然后——"
    play sound "audio/sound/effect10.ogg" fadein 0.5 loop #写字声
    "审题、动笔。"
    "积攒了整整一年的力量，在这一刻终于毫无保留地释放出来。"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b11 #考场
    with fade
    "伴随着着时间的流逝，我的答题卡也逐渐填写得完整起来。"
    y "「……」"
    "截至目前，一切都算顺利。"
    "题目中规中矩，自己的发挥也比较正常。"
    "前面的题都已经做完，检查过一遍以后也没发现什么问题。"
    stop sound fadeout 3.0
    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    y "「（……那，接下来就是作文了。）」"
    "我看了看作文的题目。"
    y "「……」"
    "怎么说呢，感觉……倒是很巧。"
    "「18.阅读下面的材料，根据要求写一篇不少于800字的文章。」"
    "『候鸟迁移过程艰辛万分，既要克服长途飞行的辛劳，亦要克服大自然严峻的挑战。在大风沙中寻找出正确方向、在冰天雪地中保护自己、在汪洋浩瀚海洋中猎食……』"
    "『有的候鸟，默默承受着一切，挺着胸与大自然作战到底；而有的候鸟，则停留在沿途的城市里，享受到其中丰富的食物，甚至不再离开，转为留鸟。』"
    "「请综合材料内容及含义作文，体现你的思考、权衡与选择。」"
    "「要求选好角度，确定立意，明确文体，自拟标题。不要套作，不得抄袭。」"
    y "「……」"
    y "「（候鸟……与留鸟吗？）」"
    y "「（呵……）」"
    "我挠了挠脑袋，微微一笑，将答题纸展平。"
    "轻轻吸了口气，开始写下我的标题——"
    scene bg b00a #天空|候鸟
    with fade
    "『在梦想的天空下』"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    pause 1.0

    play sound "audio/sound/transition.ogg" noloop
    scene trans t06 #转场 天空
    with fade
    pause

#07.终章

#6月22日。
#高考成绩公布。

    scene bg black #黑屏
    with fade
    y "「……咳咳……那我出门啦！」"
    y "「还有啊，老爸你少抽两根，这家里都快变毒气室了！」"
    y "「至于对你儿子那么不放心嘛……」"
    play sound "audio/sound/effect22.ogg" noloop
    pause 4
    stop sound

    play music "audio/music/bgm02.ogg" fadein 1.5 #夏～澄空～
    scene bg b04 #滨河路|夏
    with fade
    y "「……哇！」"
    y "「好晒。」"
    "进入六月下旬，天气明显变得炎热起来。"
    "这还没到最难熬的时候……不过也够人一呛了。"
    scene bg b06 #商业街
    with fade
    "……{p}…………"
    "一边躲避阳光的直晒，一边用尽可能快的速度赶往目的地。"

    scene bg b07 #快餐店
    with fade
    play sound "audio/sound/effect04.ogg" noloop
    with hpunch
    y "「……呼！」"

    "推开快餐店大门的那一刻，扑面而来的冷气令我打了个激灵。"
    y "「啊……活过来了……」"
    y "「我看看……」"
    y "「啊，那儿呢。」"
    y "「……哟！」"
    play music "audio/music/bgm09.ogg" fadein 1.5 #梁芷柔～theme ver.
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007001.ogg"
    l "「啊，过来啦？」"
    y "「嗯。你到了多久了？」"
    show chara c13b #梁芷柔立绘|夏季私服|疑惑2
    with dissolve
    voice "audio/voice/007002.ogg"
    l "「两三分钟？毕竟我家离这边近一点嘛。」"
    show chara c02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/007003.ogg"
    l "「哎哟，看你出的这一脑门的汗，干嘛跑这么急啊。」"
    y "「哪用得着跑啊，光晒就能晒死我了。」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/007004.ogg"
    l "「也是。来，给你。」"
    y "「噢，谢了。」"
    "我接过梁芷柔递来的餐巾纸，随便在脸上抹了一把。"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/007005.ogg"
    l "「还有这个。」"
    "这次递过来的是一杯可乐。"
    y "「哎哟，真周到。」"
    y "「（吸——）」"
    with vpunch
    y "「……嗝！」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/007006.ogg"
    l "「哎哟，喝慢点，别再呛着。」"
    y "「呼……」"
    y "「啊……这次是真活过来了。」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/007007.ogg"
    l "「嘻嘻。」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/007008.ogg"
    l "「所以呢？可以公布答案了？」"
    y "「嗯……」"
    "是的。"
    "今天是6月22日，高考成绩公布的日子。"
    "经过了一上午的忐忑与紧张之后，终于等到分数出来的我，和梁芷柔约好了在这里碰头。"
    y "「咳咳……那我就……」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/007009.ogg"
    l "「哎等等，你就不先关心一下我吗？不问问我考得怎么样？」"
    y "「啊，你……还用问吗？」"
    show chara lc13b #梁芷柔立绘|夏季私服|疑惑2|近
    with dissolve
    voice "audio/voice/007010.ogg"
    l "「那可不一定吧，万一我考砸了呢？」"
    y "「想都没想过。」"
    y "「……再说咱们不是做过一次估分了吗，就算估得再不准，能差出多少去啊？」"
    show chara lc03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/007011.ogg"
    l "「万一啦！什么事没个万一啊？」"
    y "「这……」"
    y "「瞅你现在这表情，真要考砸了还这样，那不如去报国家戏曲学院或者首都电影学院吧？反正你这么漂亮。」"
    show chara lc12a #梁芷柔立绘|夏季私服|羞涩1|近
    with dissolve
    voice "audio/voice/007012.ogg"
    l "「哎～真是的，讨厌！」"
    y "「本来就是嘛。那……你到底考得怎么样啊？」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/007013.ogg"
    l "「嗯……六百……」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/007014.ogg"
    l "「……七十七。」"
    y "「嗯～厉害！」"
    "我模仿东北亚地区某个八零后国家领导人的姿势，故作夸张地鼓了鼓掌。"
    show chara lc03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/007015.ogg"
    l "「哎哎哎哎哎你还能再假点么？」"
    y "「真的哎，我是真心觉得你很厉害啊，比我不知道高到哪里去了！」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/007016.ogg"
    l "「嘁。」"
    y "「本来就是嘛，跟你自己估的就差了2分……你还好意思说我假，你都这样了，还非得要求我担心一下？」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/007017.ogg"
    l "「怎么啦不行嘛？哼。」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/007018.ogg"
    l "「……你呢？你多少分？」"
    y "「我啊……」"
    "在报出分数之前，我忍不住先深吸了一口气……尽量让自己显得平静一些。"
    y "「……594分。」"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/007019.ogg"
    l "「真的啊？」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/007020.ogg"
    l "「这……你够可以的啊！比之前估的还要高一点呢！」"
    y "「是啊，可能是一些主观题……像是作文什么的，比预想的多拿了点分吧。」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/007021.ogg"
    l "「嗯！嗯！」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/007022.ogg"
    l "「考得不错，恭喜你。」"
    y "「……谢谢你！」"
    "我郑重地向梁芷柔致以谢意。"
    "虽说大恩不言谢，但这个时候，除了谢谢也不知道还能说什么了。"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/007023.ogg"
    l "「哎呀，干嘛这么客气嘛。」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/007024.ogg"
    l "「说到底还是你自己努力啊，呵。」"
    show chara lc09 #梁芷柔立绘|夏季私服|坏笑|近
    with dissolve
    voice "audio/voice/007025.ogg"
    l "「哎，说起来，你这上午都是什么心情啊？紧张不紧张？」"
    y "「别提了！」"
    y "「我其实还算好，毕竟试是我自己考的，还算有点底。我爸妈那就不行了，比我急得多，从早上起来就在家里转来转去的，来回来去地看那个表，中午饭都没好好吃。」"
    y "「不是下午两点钟出成绩吗，一点半的时候他们俩就都聚在电脑前面了，但是那又刷不出来，结果我们一家子就那么大眼瞪小眼地干坐着……我爸跟那儿一根接一根地抽烟，把屋子里熏得跟毒气室似的。」"
    y "「就那半个小时，我感觉跟过了半个月似的……然后到两点，这不是可以查了嘛，但是教育考试院的网站又出问题了，可能是在那一瞬间被挤爆了吧，反正死活上不去……」"
    y "「唉，你就想吧。当时那场面啊……太可怕了，我算是知道什么叫皇上不急太监急了。」"
    show chara lc01b #梁芷柔立绘|夏季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/007026.ogg"
    l "「可怜天下父母心啊……其实都一样，我爸妈也没好到哪去。吃完饭，我爸收拾了一半，也不知道怎么就转到我这边来了，结果厨房那边冰箱门都没关，就一直那么敞着。」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/007027.ogg"
    l "「要是在平时我妈早跟他急了，那会儿就跟没看见一样。直到成绩出来以后，放下了心，才想起来跟我爸算账。」"
    y "「哎，叔叔阿姨对你还不放心啊？」"
    show chara lc13b #梁芷柔立绘|夏季私服|疑惑2|近
    with dissolve
    voice "audio/voice/007028.ogg"
    l "「太关心了嘛，就容易忍不住瞎想。毕竟是高考嘛，万一状态有个起伏什么的，谁也说不准啊。」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/007029.ogg"
    l "「你别看我自己好像挺有谱的，成绩出来之前，我也一样会胡思乱想，像是『哎呀，这道题是不是应该换一个答法更好啊』什么的。」"
    y "「那知道成绩以后的心情呢？」"
    show chara lc13b #梁芷柔立绘|夏季私服|疑惑2|近
    with dissolve
    voice "audio/voice/007030.ogg"
    l "「现在，当然是踏实了。不过啊……」"
    show chara lc08b #梁芷柔立绘|夏季私服|担心2|近
    with dissolve
    voice "audio/voice/007031.ogg"
    l "「直到刚才都还有一点不踏实的。」"
    y "「嗯？」"
    show chara lc01a #梁芷柔立绘|夏季私服|普通|正面|近
    with dissolve
    voice "audio/voice/007032.ogg"
    l "「嗯……因为还不知道你的成绩呀！」"
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve
    voice "audio/voice/007033.ogg"
    l "「虽然感觉你考得应该还不错，但是，万一呢……是吧？」"
    y "「啊……嗯。」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/007034.ogg"
    l "「哼，我才不像某些人似的，那么没心没肺的。」"
    y "「我这是充分信任你啊！」"
    show chara lc03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/007035.ogg"
    l "「哼！」"
    y "「呃……」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/007036.ogg"
    l "「……好啦，说正经的。」"
    y "「嗯。」"
    show chara lc01b #梁芷柔立绘|夏季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/007037.ogg"
    l "「现在成绩是出来了，但是一本线估计还得过几个小时才能出……也可能要到明天，所以现在是什么情况其实还不好说。」"
    voice "audio/voice/007038.ogg"
    l "「我个人感觉今年的题还是比较简单的，分数虽然高，但是录取线估计也很高。」"
    y "「嗯……也就是说去年的分数线没什么参考价值了吧？」"
    voice "audio/voice/007039.ogg"
    l "「恐怕是。不过嘛，估一个大概的数值还是可以的。」"
    y "「嗯……」"
    show chara lc13b #梁芷柔立绘|夏季私服|疑惑2|近
    with dissolve
    voice "audio/voice/007040.ogg"
    l "「料敌从宽，姑且先按照比去年高了15分来计算好了。」"
    y "「这样啊。」"
    "我翻了翻去年的大学录取分数线。"
    y "「嗯……我看看……」"
    show chara lc13a #梁芷柔立绘|夏季私服|疑惑1|近
    with dissolve
    voice "audio/voice/007041.ogg"
    l "「怎么样？」"
    y "「应该是……」"
    y "「……能上线。」"
    show chara lc10 #梁芷柔立绘|夏季私服|开心|近
    with dissolve
    voice "audio/voice/007042.ogg"
    l "「那就好！」"
    y "「……呼。」"
    "梁芷柔喜形于色，兴奋地拍了拍手，我也是长出了一口气。"
    "之前自己的估分大概是585分左右，不过现在多了将近10分，自然也会更有底气。"
    "虽然这么推算出来的结论没有那么准确，但大致上还是可以参考的。"
    y "「总算是……哎，真是，提心吊胆的，这几天。」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/007043.ogg"
    l "「嘻嘻，那现在呢？」"
    y "「好多了。」"
    show chara lc04 #梁芷柔立绘|夏季私服|无奈|近
    with dissolve
    voice "audio/voice/007044.ogg"
    l "「哎～那不还是没好利索嘛！」"
    y "「毕竟是估出来的分数线啊，具体的还得看明天……而且之后还有专业啊什么的，现在都还说不准。」"
    y "「不过不管怎么说，算是开了个好头吧。」"
    show chara lc11 #梁芷柔立绘|夏季私服|微笑|近
    with dissolve
    voice "audio/voice/007045.ogg"
    l "「嗯！」"
    l "「……」"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    voice "audio/voice/007046.ogg"
    l "「嗯……那个，你……」"
    y "「怎么了？」"
    show chara lc06 #梁芷柔立绘|夏季私服|吃惊|近
    with dissolve
    voice "audio/voice/007047.ogg"
    l "「啊，不，没事……」"
    show chara lc01b #梁芷柔立绘|夏季私服|普通|侧面|近
    with dissolve
    voice "audio/voice/007048.ogg"
    l "「……没事了。」"
    y "「嗯……？」"
    show chara lc05a #梁芷柔立绘|夏季私服|苦笑1|近
    with dissolve
    voice "audio/voice/007049.ogg"
    l "「希望，明天来的是个好消息吧！」"
    y "「……」"
    y "「嗯……」"
    y "「是啊……希望是个好消息……」"
    "虽然梁芷柔并没有说出口，但我知道她想说的是什么。"
    "我的分数差不多刚好卡在樱华理工的录取线上，可能会被录取，也可能差那么一点被刷掉。"
    "目标已经确定，能做的也都尽力做到了最好，剩下的就只有听天由命了。"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "只是……"
    "如果那个结果不尽人意的话？"
    scene bg b00 #天空
    with fade
    "如果那样，我……该怎么办呢？"
    "我……和她。我们，又该怎么办呢？"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t03 #转场 快餐店
    with fade
    pause

#7月20日。
#本科一批录取工作开始。

    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音
    scene bg b02 #城区|夏
    with fade
    "七月，烈日炎炎。"
    "虽然天气热得让人不怎么想动弹，不过，最近这段时间我还是没少出门。"
    "当然，不只我自己一个人。"
    stop sound fadeout 3.0

    play music "audio/music/bgm12.ogg" fadein 1.5 #快马加鞭
    scene bg b06 #商业街
    with fade
    "我和梁芷柔走遍了这座小城的每一个角落，在这些早就熟悉无比的景色中，烙上属于我们两个人共同的记忆。"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    l "「……」"
    voice "audio/voice/007050.ogg"
    l "「一晃，这一年就过去了啊……」"
    y "「嗯？」"
    show chara c13b #梁芷柔立绘|夏季私服|疑惑2
    with dissolve
    voice "audio/voice/007051.ogg"
    l "「去年，差不多就是这两天吧？你救了我一命。」"
    y "「啊，啊！你说那事啊？」"
    y "「我记得还得再过两天吧…{cps=2}…不{/cps}过也差不多了。」"
    y "「这么想想还真是，一年了啊。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007052.ogg"
    l "「嗯，呵呵。」"
    y "「怎么了？」"
    show chara c01b #梁芷柔立绘|夏季私服|普通|侧面
    with dissolve
    voice "audio/voice/007053.ogg"
    l "「没什么，就是觉得缘分这个东西，真是很奇妙。」"
    show chara c02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/007054.ogg"
    l "「要是没有那一次……也不知道咱们俩现在会是怎么样。」"
    y "「嗯……」"
    "反正……肯定不会是现在这个样。"
    "这么说起来，我还得感谢那个椅子。"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/007055.ogg"
    l "「……说起来，你那边怎么样了？」"
    y "「还是院校在阅，没下文。」"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/007056.ogg"
    l "「唉……别想那么多啦，这不才第三天嘛，耐心等吧。」"
    y "「啧，最烦的就是这鞋啊，只扔下来一只。」"
    y "「是死是活，好歹给个痛快话啊。唉……」"
    scene bg b00 #天空
    with fade
    "梁芷柔的判断还是相当准确的，一本线和预料的相差无几，我也随即按照计划在志愿上填报了樱华理工大学。"
    "一个月匆匆而过，就在两天前，本科一批的录取工作正式开始了。"
    "我的档案当天即被省招办投到了樱华理工大学。换句话说，顺利通过了理工大的投档线。这姑且算是个好消息……"
    "但接下来就比较让人费解了。"
    "当日下午，我的考生状态从「已经投档」变成了「院校在阅」，本来满心期待第二天就能出来结果，谁知道转眼三天过去了，状态却还是「院校在阅」，一字未改。"
    "也不知道是哪里出了什么问题……"
    scene bg b04 #滨河路|夏
    with fade
    show chara c01b #梁芷柔立绘|夏季私服|普通|侧面
    with dissolve
    y "「你呢？你那边怎么样啊？」"
    show chara c05b #梁芷柔立绘|夏季私服|苦笑2
    with dissolve
    voice "audio/voice/007057.ogg"
    l "「我啊……」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007058.ogg"
    l "「……预录取。」"
    "果然……她这边倒还是一如既往的稳。"
    "不过，虽说早在意料之中，但在听到她亲口说出确定的结果时，还是会情不自禁地为她感到开心。"
    y "「恭喜了。」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/007059.ogg"
    l "「谢谢。」"
    y "「说是预录取……其实没什么特别特殊的情况的话，也就是录取了吧？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007060.ogg"
    l "「算是吧。」"
    show chara c13b #梁芷柔立绘|夏季私服|疑惑2
    with dissolve
    voice "audio/voice/007061.ogg"
    l "「其实樱大的人已经来过电话了……和我直接确认过。」"
    y "「哦？」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/007062.ogg"
    l "「我毕竟也是排进全省前十名里的人嘛，再加上是咱们这个小地方出来的……可能比较有噱头？反正我觉得樱大那边对我还算是挺感兴趣的。」"
    y "「那他们都跟你说什么了？就光和你确认了一下？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007063.ogg"
    l "「还说了点助学金什么的事，条件还不错。」"
    y "「这么好啊？」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/007064.ogg"
    l "「也算正常吧，毕竟我没往首都考而是主动去的樱华……好像他们几家每年抢生源也抢得挺狠的？」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/007065.ogg"
    l "「当然相应的，我也需要配合他们做一些宣传方面的活动，上个新闻什么的。」"
    y "「嗯？类似于……『十二年寒窗苦读，美女学霸终于圆了樱华梦』这样的？」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/007066.ogg"
    l "「哈哈哈……差不多吧。」"
    show chara c01b #梁芷柔立绘|夏季私服|普通|侧面
    with dissolve
    voice "audio/voice/007067.ogg"
    l "「再有就是，我好像还是咱们县第一个考上樱大的人，那边想要用我的形象，推广他们的西部扶贫助学项目。」"
    y "「哎，形象代言人啊？」"
    show chara c05b #梁芷柔立绘|夏季私服|苦笑2
    with dissolve
    voice "audio/voice/007068.ogg"
    l "「没那么夸张，有好多人呢。我也就是提供一张照片，然后在他们的宣传片和海报里面蹭个镜头罢了。」"
    y "「那也已经很厉害了啊，真的。」"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/007069.ogg"
    l "「毕竟只是个虚名，还不知道俩月以后，咱们得累成什么样呢。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/007070.ogg"
    l "「一方面是能不能跟得上学习进度，另一方面还有个能不能融入环境的问题。」"
    y "「这个嘛……感觉我倒是需要担心一下，但你不至于吧？」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/007071.ogg"
    l "「当然至于了，最起码也不能无视吧……」"
    y "「呃？」"
    y "「你学习就不用说了，这年头人际关系这么看脸，这不应该是你的优势吗？」"
    show chara c12b #梁芷柔立绘|夏季私服|羞涩2
    with dissolve
    voice "audio/voice/007072.ogg"
    l "「去你的……不是，就算按你这么说，这也是把双刃剑啊！」"
    show chara c02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/007073.ogg"
    l "「你是不知道女生之间有多少麻烦事……我已经做好了四人寝室建五个群的心理准备了。」"
    y "「这么可怕的吗？」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/007074.ogg"
    l "「你以为呢？而且不只是宿舍，其他的圈子也是一样啊……尤其又是在樱华这样的大城市，很多地方都需要开销的。」"
    show chara c07a #梁芷柔立绘|夏季私服|消沉1
    with dissolve
    voice "audio/voice/007075.ogg"
    l "「没办法，穷啊！」"
    show chara c07b #梁芷柔立绘|夏季私服|消沉2
    with dissolve
    voice "audio/voice/007076.ogg"
    l "「学费啊住宿费啊什么的倒还好说，有助学金奖学金，实在不行还有国家助学贷款什么的，但这些都是用来做基本保障的，其他的问题还是得自己解决。」"
    y "「呃……」"
    scene bg b08 #新城区|夏
    with fade
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/007077.ogg"
    l "「说到这个，你想过到了那边以后打什么工了吗？」"
    y "「打工？啊，还没想好。」"
    y "「我觉得我还是优先考虑一下能不能跟得上学习进度的问题吧……」"
    y "「你呢？你打算干什么去？」"
    show chara c13b #梁芷柔立绘|夏季私服|疑惑2
    with dissolve
    voice "audio/voice/007078.ogg"
    l "「嗯，家教吧？」"
    y "「家教……？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007079.ogg"
    l "「对啊，先做一年，专门挑那边的应届高考生，给他们补课。」"
    y "「应届高考生吗？」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/007080.ogg"
    l "「对啊，怎么啦？」"
    y "「没，我还以为是去教初中生呢……」"
    show chara c13b #梁芷柔立绘|夏季私服|疑惑2
    with dissolve
    voice "audio/voice/007081.ogg"
    l "「初中生啊，那也不是不行。不过就有点浪费了。」"
    y "「浪费？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007082.ogg"
    l "「对啊。你是不是觉得初中的知识点更容易一点？但你别忘了，咱们现在最大的优势是什么啊？」"
    y "「哦……我明白了。」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/007083.ogg"
    l "「对吧？刚高考完！高考阶段的所有知识点、所有注意事项，咱们全都是最清楚不过的了！」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007084.ogg"
    l "「而且能从教育条件这么落后的地方考过去，就已经证明了咱们的学习方法一定是最有效的。」"
    y "「这倒是。」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/007085.ogg"
    l "「更何况啊……」"
    y "「嗯？」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/007086.ogg"
    l "「我本来就有当家教的经验啊！别忘了，我这一年可是天天拿你练手的。」"
    y "「这……还真是。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007087.ogg"
    l "「对吧？所以我就决定是它了！」"
    y "「嗯嗯。」"
    y "「……嗯？」"
    show chara c13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/007088.ogg"
    l "「怎么了？」"
    y "「你教应届高考生的话，那不也就比咱们小一岁吗？」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    voice "audio/voice/007089.ogg"
    l "「嗯，那当然啊。」"
    y "「这个没问题吗？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007090.ogg"
    l "「嗯。其实同龄人之间可能有的时候会更容易交流吧？本来补课就是用的课余时间，这样可能还不会让他们有那么强烈的抵触感……」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/007091.ogg"
    l "「啊……呵呵，我明白了。」"
    y "「嗯？」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/007092.ogg"
    l "「放～心～啦！我会专门挑女生来教的，不用那么紧张！」"
    y "「喂喂喂喂喂，我可没这么说啊！我不是这意思！」"
    show chara c09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/007093.ogg"
    l "「嘻嘻，那怎么着？我随便来咯？」"
    y "「……」"
    y "「还是女生吧。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007094.ogg"
    l "「嘻嘻，不过其实本来也没什么事啦！就像你之前那样，但凡是个想要认真学习的，才不会有那么多乱七八糟的心思在那儿呢。」"
    y "「嗯。」"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    play sound "audio/sound/effect11.ogg" noloop
    "……{p}…………"

    scene bg b04 #滨河路|夏
    with fade
    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    y "「……呼。」"
    show chara c08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/007095.ogg"
    l "「沉不沉？」"
    y "「没事。」"
    y "「一想到自己现在抱的不再是习题集，就觉得浑身都是劲，完全不在话下。」"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/007096.ogg"
    l "「哼，就知道臭贫。」"
    y "「说起来，你这么多书，以后怎么办啊？带到樱华去吗？」"
    show chara c08b #梁芷柔立绘|夏季私服|担心2
    with dissolve
    voice "audio/voice/007097.ogg"
    l "「那肯定是不行的吧，宿舍里哪有地方搁啊……大概是只能放在老家了。」"
    y "「也是。」"
    y "「不过那干嘛还要买实体的书呢？下载电子版的不好吗？」"
    show chara c08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/007098.ogg"
    l "「嗯……我还是喜欢摸着纸的感觉，可能是这么多年习惯了吧，反正用手机看东西，总有点看不下去。」"
    show chara c07b #梁芷柔立绘|夏季私服|消沉2
    with dissolve
    voice "audio/voice/007099.ogg"
    l "「不过，之后恐怕只能勉强自己改一改了，毕竟条件有限嘛。」"
    y "「……学霸的烦恼啊。」"
    show chara c02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/007100.ogg"
    l "「咳！别笑我了，说的好像事不关己似的。这种麻烦事以后也少不了的，你又能比我好多少啊？」"
    y "「这倒是。」"
    "的确，我也是要离开家的人，在这个方面上，我们俩的处境是相同的。"
    show chara c04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/007101.ogg"
    l "「还有啊……这就又说回刚才那个话题了，虽然学习确实是很重要的，不过大学毕竟不是高三了，也不是光靠努力学习就能解决一切问题的。」"
    show chara c01b #梁芷柔立绘|夏季私服|普通|侧面
    with dissolve
    voice "audio/voice/007102.ogg"
    l "「闷头学到自闭可能会比跟不上进度的问题还要大，没准孤独到抑郁，反过来再影响成绩，恶性循环，谁都救不了。」"
    show chara c13b #梁芷柔立绘|夏季私服|疑惑2
    with dissolve
    voice "audio/voice/007103.ogg"
    l "「我觉得还是得去打打工，有一些社交活动什么的。最好能提前做一些打算。」"
    y "「……」"
    y "「我明白你的意思。我也不是不想，但是……」"
    y "「现在这个样子，总觉得自己好像悬在半空一样，踏不下心来。」"
    y "「让我再缓两天吧……」"
    y "「……最起码，等录取的事情定下来再说。」"
    show chara c01a #梁芷柔立绘|夏季私服|普通|正面
    with dissolve
    l "「……」"
    show chara c07a #梁芷柔立绘|夏季私服|消沉1
    with dissolve
    voice "audio/voice/007104.ogg"
    l "「嗯，也是。」"
    show chara c07b #梁芷柔立绘|夏季私服|消沉2
    with dissolve
    voice "audio/voice/007105.ogg"
    l "「……也是。」"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/007106.ogg"
    l "「都到这时候了，就别胡思乱想了。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007107.ogg"
    l "「相信自己，好吗？」"
    y "「……」"
    y "「嗯。没事，咱们走吧。」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/007108.ogg"
    l "「……嗯。」"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t04 #转场 书店
    with fade
    pause

#7月22日。
#第一志愿落榜。

    scene bg black #黑屏
    with fade
    "说是要「相信自己」，但实际上，真能做到的人，往往也不需要被别人这样劝解了。"
    "我就这样又继续煎熬了两天，直到——"
    play music "audio/music/bgm06.ogg" fadein 1.5 #悬而未决
    "那个悬而未决的「第二只鞋子」，终于落了地。"
    y "「……」"
    with vpunch
    y "「我……\[哔——\]！」"
    stop music fadeout 2.5

    y "「……我出去透透气。」"
    play sound "audio/sound/effect22.ogg" noloop

    scene bg b02 #城区|夏
    with fade
    pause
    scene bg b04 #滨河路|夏
    with fade
    pause
    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    scene bg b05 #湿地公园|夏
    with fade
    "……{p}…………"
    "不知是不是之前提心吊胆得太久了？"
    "真到了这一刻，我其实……反而表露不出太多的情绪来了。"
    y "「唉……」"
    "漫无目的地溜达了一会儿之后，我进到了湿地公园里面。"
    "木然地坐在岸边，望着波光粼粼的水面发呆。"
    y "「……」"
    y "「……」"
    stop sound fadeout 3.0
    play music "audio/music/bgm07.ogg" fadein 1.5 #哀毁骨立
    y "「你妈的，为什么啊……」"
    y "「就差那么2分……什么地方凑不出这2分啊！」"
    y "「关键这分还是被专业级差给砍下去的……这不玩我呢么？」"
    scene bg b05 #湿地公园|夏
    nvl show
    nvl_narrator "我的第一志愿……落榜了。"
    nvl_narrator "直到好久以后，我才弄明白了这次落榜的原因。"
    nvl_narrator "樱华理工大学的最低录取分数线是586分，按理说分数是足够了，但……我在专业的选择上出了问题。"
    nvl clear
    nvl_narrator "因为试卷难度变化和大小年等一系列原因，我报的前两个专业的录取线虚高，根本就考不上。"
    nvl_narrator "而后面的两个专业……虽然录取线较低，但却因为要扣减专业级差的分数，也全都没有兜住。"
    nvl_narrator "作为樱华仅有的几所好学校之一，理工大的生源非常充足，结果就是我连专业调剂的机会都没有，直接出局。"
    nvl clear
    nvl_narrator "最害怕的事情，还是发生了。"
    nvl_narrator "明明早就想到过可能会有这种情况。"
    nvl_narrator "明明早就做过不知多少次的心理准备。"
    nvl_narrator "但真到面对的时候，还是完全没办法去坦然接受。"
    nvl clear
    nvl_narrator "现在的心情，其实也不是那种「天都塌下来了」的感觉，没有那么夸张。"
    nvl_narrator "就是迷茫，搞不清状况。"
    nvl_narrator "我知道今年的高考题比较容易，我知道分数线可能会被拉高，我知道自己的分数不是绝对稳妥……但我也觉得自己真的算是考得不错了，这么久的努力不是白费功夫，应该还是有不小的希望的……"
    nvl clear
    nvl_narrator "在这种患得患失之间徘徊的我，在面对结果的这一刻，一下子就乱套了。"
    nvl_narrator "甚至不由自主地开始胡思乱想起来——"
    nvl clear
    nvl_narrator "其实是分数算错了？"
    nvl_narrator "也可能教育考试院的网站被人黑了？"
    nvl_narrator "如果我能黑掉高校的录取系统的话？"
    nvl_narrator "说不定我可以时光倒流，穿越到一年以前去？"
    nvl clear
    nvl_narrator "……"
    nvl_narrator "…………"
    nvl_narrator "……………………"
    nvl clear
    nvl_narrator "可能人到了非常失望的时候，思维都会变得混乱。"
    nvl_narrator "想到最后，我都已经不知道自己在想什么了，也就索性什么都不去想。"
    nvl_narrator "只是坐在原地，发呆。"
    nvl clear
    scene bg black #黑屏
    with fade
    nvl_narrator "……"
    nvl_narrator "…………"
    nvl_narrator "直到，有一个声音将我拽回现实——"
    nvl clear
    nvl hide
    with dissolve
    voice "audio/voice/007109.ogg"
    l "「……雨潇？」"
    scene bg b05 #湿地公园|夏
    with fade
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    y "「……」"
    y "「芷柔……」"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    voice "audio/voice/007110.ogg"
    l "「我总算找到你了！」"
    show chara lc03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/007111.ogg"
    l "「我给你打了10个电话你都不接，到你家里一问，叔叔阿姨也都不知道你具体在哪儿……」"
    show chara lc08b #梁芷柔立绘|夏季私服|担心2|近
    with dissolve
    voice "audio/voice/007112.ogg"
    l "「呼……吓死我了！我还以为你出什么事了呢……」"
    y "「……」"
    l "「……」"
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve
    voice "audio/voice/007113.ogg"
    l "「你……你还好吧？」"
    y "「……」"
    y "「我没事……没你想的那么夸张。」"
    y "「就是觉得……好窝囊啊……」"
    y "「太他妈窝囊了。」"
    show chara lc07b #梁芷柔立绘|夏季私服|消沉2|近
    with dissolve
    l "「……」"
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve
    voice "audio/voice/007114.ogg"
    l "「到底是……怎么搞的？」"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b05 #湿地公园|夏
    with fade
    show chara lc07b #梁芷柔立绘|夏季私服|消沉2|近
    with dissolve
    y "「就是这样了。」"
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve
    voice "audio/voice/007115.ogg"
    l "「这……」"
    show chara lc02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/007116.ogg"
    l "「怎么会……」"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    "梁芷柔的表情来回变幻了好几次，有迷茫、有紧张、也有纠结，最终糅合成痛苦。"
    show chara lc08b #梁芷柔立绘|夏季私服|担心2|近
    with dissolve
    y "「……」"
    y "「对不起。」"
    y "「我……没有考上樱华。」"
    "我低下头，不太敢直面梁芷柔的视线。"
    "此前的种种约定，在这一刻都已经化为泡影。"
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    with dissolve
    voice "audio/voice/007117.ogg"
    l "「怎么会这样……那这怎么办呢……」"
    y "「我……」"
    "是啊，现在……接下来该怎么办？"
    scene bg b05 #湿地公园|夏
    show chara lc08a #梁芷柔立绘|夏季私服|担心1|近
    nvl show
    nvl_narrator "我不知道。"
    nvl_narrator "是就这样承认自己失败了，然后就此分道扬镳吗？"
    nvl_narrator "——不甘心。"
    nvl clear
    nvl_narrator "可是不甘心又能怎么办呢？"
    nvl_narrator "高考的结果让我们天各一方，空间上的距离让一切言语都变得苍白无力。"
    nvl_narrator "除了放弃，还有什么别的路可走吗？"
    nvl clear
    nvl_narrator "——不要。"
    nvl_narrator "——我这半年多是因为什么才坚持下来的？"
    with vpunch
    nvl_narrator "——现在放弃，岂不是全都变成了笑话？"
    nvl clear
    nvl_narrator "可是……现在这个结果不已经是个笑话了吗？"
    with vpunch
    nvl_narrator "——我不管！"
    nvl_narrator "那到底该怎么办？"
    with vpunch
    nvl_narrator "——不知道！不知道！！不知道！！！"
    nvl clear
    nvl_narrator "……"
    nvl_narrator "…………"
    nvl_narrator "………………"
    nvl clear
    show chara lc07b #梁芷柔立绘|夏季私服|消沉2|近
    with dissolve
    nvl hide
    "偌大的湿地公园，却是静悄悄的，就连水鸟都销声匿迹，不知所踪了。"
    "在接下来的一段时间里，我们谁都没有再说一句话，就只是各自默默地想着心事。"
    "许久之后。"
    "彻底放弃思考的我，一言不发地离开了湿地公园，依赖着自己的本能，摇摇晃晃地朝家的方向挪去。"
    scene bg b04 #滨河路|夏
    with fade
    show chara lc07b #梁芷柔立绘|夏季私服|消沉2|近
    with dissolve
    "而梁芷柔，也就这么一路默默地跟在我的身后，一直跟到了我家楼下。"
    y "「……」"
    l "「……」"
    "我在楼门前站定，面向她，张嘴想说点什么，却依旧是怎么也发不出声音，于是最终也只能闭嘴不谈。"
    "梁芷柔也没有说话，就只是咬着自己的嘴唇，仿佛这一个动作就已经耗尽了她所有的力气。"
    "……{p}…………"
    with fade
    show chara lc07a #梁芷柔立绘|夏季私服|消沉1|近
    with dissolve
    "最后。"
    "红肿着眼睛的梁芷柔抛下一句「我先回去了」，离开了。"
    hide chara
    with dissolve
    y "「……」"
    scene bg b00 #天空
    with fade
    "我们暂时逃避了问题。"
    "我需要一些时间来整理思路，而梁芷柔，看起来也同样没有做好现在就直面这个问题的准备。"
    stop music fadeout 2.5

    "然而，无论如何，我们最终都需要作出决定。"
    "在这个夏天……结束之前。"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t06 #转场 天空
    with fade
    pause

#7月30日。
#收到百薇大学录取通知书。

    scene bg b02 #城区|夏
    with fade
    "过了几天。"
    play sound "audio/sound/ambientnoise05.ogg" fadein 1.5 loop #街道蝉鸣噪音
    scene bg b06 #商业街
    with fade
    y "「……」"
    "从邮局出来，我站在路边，有些不自然地看着手中的信封。"
    "之前因为闷在屋里塞着耳机与世隔绝，没有听到敲门和电话，结果挂号信被退到本地邮局，我只好自己来取一趟。"
    y "「哎……」"
    play audio "audio/sound/effect32.ogg" noloop
    "打开厚厚的信封，检查里面的内容物——"
    "大红色的录取通知书。"
    "蓝色的邮储银行校友卡和用户指南。"
    "像素字体设计的新生入学须知。"
    "国家的高校学生资助政策简介和大学自己的资助、贷款体系介绍手册。"
    "大学新生应征入伍宣传单。"
    "学校的专题特刊杂志。"
    "……{p}…………"
    "林林总总的一大堆文件材料。"
    y "「……」"
    "我打开录取通知书，仔细地看了看。"
    "在录取通知书的最上端，校徽的旁边，清晰地印着「教育部直属国家重点综合性大学」、「国家『211工程』、『985工程』重点建设高校」的字样。"
    "这两行字足以令这座县城里99.9\%的考生羡慕不已，即便是大人们，看到了也是要交口称赞一番的。"
    "我的父母这两天和亲戚朋友打电话的时候仿佛都变成了复读机，翻来覆去就只有一套「惋惜」的说辞——"
    "『哎呀，别提了，小孩子志愿没报好，第一志愿都没考上，只能去读百薇了！』"
    "一点都不考虑儿子的心情，真是亲爹亲妈啊。"
    "我这几天的情绪……在他们看来或许更像是小孩没能达成心愿在闹别扭吧？"
    y "「……唉，不过也难怪。」"
    "父母当初能由着我的性子往樱华报名，这已经是非常支持我了。"
    "没准我第一志愿落榜了他们还更高兴……毕竟百薇的资质好，纸面上排名也高，关键是离家还很近，简直完美。"
    "别说他们了，哪怕是刚才给我拿信的那位邮政员工，在看到信封上寄件方那「百薇大学」四个字之后，再看我的眼神也都变了。"
    with fadehold
    "我将各种文件小心地收回了信封里面。"
    "其实，收到了这封信以后，我就已经可以算是百薇大学的学生了。"
    "只是……"
    "直到现在，我都还不肯接受现实。"
    "其实也确实还有别的路可选。"
    "就算接到了录取通知，也可以不去学校报道。"
    "只要复读就可以了。"
    "复读一年成功考上心仪院校的学生比比皆是，如果不愿意承认自己的高考失败，那么这就是最简单直接的办法。"
    "但是，面临抉择的时候，我却……犹豫了。"
    "俗话说光看贼吃肉不见贼挨打，复读成功的人固然不少，但其实再次失败的也一样到处都是，甚至更多。"
    "而且，复读的过程相当漫长又饱受旁人议论，一旦中途心态崩了，多半连原来的水准都保持不住。"
    "万一再失败了……"
    y "「……」"
    "不敢想了。"
    "摇了摇头，努力让自己不再去这么想。"
    "只是……"
    y "「……」"
    "我再次看了看手中的信封。"
    "前几天我可以不去想，靠逃避问题来麻痹自己。"
    "但是现在——在拿到了这些东西以后——我知道，自己已经没有躲藏的余地了。"
    "我……需要做出决定。"
    y "「……」"
    y "「…………」"
    #老师
    voice "audio/voice/017001.ogg"
    who "「哎？叶雨潇？」"
    y "「啊？」"
    show charaz h01 #老师立绘|夏季|普通
    with dissolve
    "突然被一个熟悉的声音叫了名字，回头一看，居然是班主任老师。"
    show charaz h02 #老师立绘|夏季|微笑
    with dissolve
    voice "audio/voice/017002.ogg"
    z "「哟，还真是你小子啊，干吗呢你这是？」"
    y "「郑老师？您怎么在这儿啊？」"
    show charaz h01 #老师立绘|夏季|普通
    with dissolve
    voice "audio/voice/017003.ogg"
    z "「那要不然呢？」"
    y "「去年这会儿……啊，对哦，这会儿也该放假了。」"
    voice "audio/voice/017004.ogg"
    z "「什么叫该放假了……我早就放假了呀！」"
    y "「哎？」"
    show charaz h03 #老师立绘|夏季|皱眉
    with dissolve
    voice "audio/voice/017005.ogg"
    z "「哎你这琢磨什么哪？我带完你们这届，就要翻回头去带高一了，现在学生都还没有呢，你还不让我放个假啊？」"
    y "「呃……」"
    show charaz h01 #老师立绘|夏季|普通
    with dissolve
    voice "audio/voice/017006.ogg"
    z "「所以……你这到底是在发什么呆哪？大太阳底下晒着，也不知道找个阴凉的地方躲躲？」"
    y "「啊，没什么，没事。就是走神了。」"
    z "「……」"
    "老师用怀疑的目光看着我，最后将视线停留在了我的手上。"
    "显然，作为一中的老师，对于百薇的录取通知书并不会太陌生。"
    show charaz h02 #老师立绘|夏季|微笑
    with dissolve
    voice "audio/voice/017007.ogg"
    z "「呵，是这么回事啊？」"
    voice "audio/voice/017008.ogg"
    z "「还在纠结呢？」"
    y "「……」"
    y "「是。」"
    show charaz h03 #老师立绘|夏季|皱眉
    with dissolve
    voice "audio/voice/017009.ogg"
    z "「你呀……我该怎么说你好啊？」"
    show charaz h01 #老师立绘|夏季|普通
    with dissolve
    voice "audio/voice/017010.ogg"
    z "「你现在，还有别的事吗？」"
    y "「哎？啊，没有……」"
    voice "audio/voice/017011.ogg"
    z "「那……咱俩聊聊？」"
    y "「啊？」"
    show charaz h02 #老师立绘|夏季|微笑
    with dissolve
    voice "audio/voice/017012.ogg"
    z "「放心，你都已经毕业了，我才懒得训你呢。啊，『我也不责备你，小叶雨潇，你自己一定够难受的了。』」"
    y "「喂喂喂，您是英语老师啊，不是法语老师。」"
    voice "audio/voice/017013.ogg"
    z "「嘿，不管是什么语的老师，总归比你岁数要大，这人生经验也要丰富一些，聊一聊没坏处。啊，怎么样啊？」"
    y "「……好。」"
    stop sound fadeout 3.0
    "我没有拒绝老师的好意，实际上，我觉得自己现在也确实需要这样聊一聊。"

    scene bg b07 #快餐店
    with fade
    play audio "audio/sound/effect04.ogg" noloop
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    "我跟着老师进到了旁边的快餐店。"
    play sound "audio/sound/ambientnoise06.ogg" fadein 1.5 loop #快餐店环境噪音
    "这里依然没什么人气，我们随便找了个位子坐下。"
    voice "audio/voice/017014.ogg"
    z "「好了，说说吧，你现在具体是什么地方想不通啊？」"
    y "「那个……」"
    y "「……呃……就是……」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017015.ogg"
    z "「怎么了，这么不痛快呀？」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017016.ogg"
    z "「我替你说了吧——你还没死心，对不对？」"
    y "「……嗯。」"
    show charaz lh04 #老师立绘|夏季|咆哮|近
    with dissolve
    voice "audio/voice/017017.ogg"
    z "「唉！真想一巴掌扇死你。真是，得亏你不是我孩子。」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/017018.ogg"
    z "「你啊，就是算盘打得太好了，但又不去认真想想，万一这事情不按自己想的来，又该怎么办哪？」"
    voice "audio/voice/017019.ogg"
    z "「唉……」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017020.ogg"
    z "「你不死心，那好，那我问你，你想怎么办？」"
    y "「我……」"
    voice "audio/voice/017021.ogg"
    z "「你又能怎么办，啊？都这时候了，你还不想接受的话，那只能去复读了。你想复读吗？」"
    voice "audio/voice/017022.ogg"
    z "「放弃百薇，冒着影响自己一辈子的风险，再去搏这么一次？你愿意吗？」"
    y "「……」"
    y "「我……不知道。」"
    y "「就是不知道，所以才……纠结着呢。」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017023.ogg"
    z "「是吧？但其实你知道，你复读成功的几率不低的，最起码不会比你这次高考的风险更大。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017024.ogg"
    z "「只不过反过来说呢，失败的几率也一样差不多。」"
    voice "audio/voice/017025.ogg"
    z "「所以上回你冲上去了，但这回，你就犹豫了。」"
    y "「……」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/017026.ogg"
    z "「对吧？你也知道了，这有些事情啊，不是光想得好就能行的。」"
    voice "audio/voice/017027.ogg"
    z "「其实现实就是这样，啊，吃一堑长一智。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017028.ogg"
    z "「你赌了一把，失败了，所以就知道求稳的重要性了。」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/017029.ogg"
    z "「但是……」"
    voice "audio/voice/017030.ogg"
    z "「其实求稳不是目的，那是为了实现目的而选择的一种途径。」"
    voice "audio/voice/017031.ogg"
    z "「有必要的时候该赌也得去赌，只要利益足够大，或者风险足够低，那就可以去赌。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017032.ogg"
    z "「你当初就是这么做的，你给自己画了一个足够漂亮的大饼。」"
    voice "audio/voice/017033.ogg"
    z "「我当时之所以会同意啊，就是因为我觉得你小子还是有点想法的，而且也不是没有机会，值得一试。」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/017034.ogg"
    z "「不过呢，现在再看看……啧，我觉得当初有点高估你了。」"
    voice "audio/voice/017035.ogg"
    z "「你想实现的目的到底是什么，我觉得你根本没有真正地想清楚。」"
    y "「我……」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017036.ogg"
    z "「对于你来说，『樱华』，自始至终都是一个抽象的概念，就跟乌托邦一样。」"
    voice "audio/voice/017037.ogg"
    z "「你不知道那边是什么样子，你也不知道樱华和百薇真正的区别在哪，更没有想好你过去了到底做什么、怎么做。」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017038.ogg"
    z "「本来，这也不是什么大问题。你这个岁数嘛，不清楚这些再正常不过了。」"
    voice "audio/voice/017039.ogg"
    z "「而且，你当初说的那些话也不算错，毕竟那边跟咱们这里确实是不一样。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017040.ogg"
    z "「如果你能考过去，有的是时间让你寻找答案。但问题是呢——」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/017041.ogg"
    z "「你没考过去。」"
    voice "audio/voice/017042.ogg"
    z "「你没考过去呢，那你就没有这个答案，你的『目的』就还是虚的。」"
    voice "audio/voice/017043.ogg"
    z "「现在，你其实自己也已经意识到了。所以呢，再要你为了这么一个虚幻的目的，去拿自己的未来赌……」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017044.ogg"
    z "「你就不敢了。」"
    y "「……」"
    "老师说得没有错。"
    "虽然报考樱华并不是我一时冲动的选择，然而有些事……当这样的结果摆在我面前的时候……"
    "我失去了一往无前的勇气。"
    "即便还在不甘心地挣扎，但内心深处，其实已经开始不由自主地退缩了。"
    "这也是这些天，最让我感到自我厌恶的一点。"
    voice "audio/voice/017045.ogg"
    z "「……唉。」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017046.ogg"
    z "「其实要说起来，你已经做得挺不错了。」"
    voice "audio/voice/017047.ogg"
    z "「最后这一年提了一百多分，这一般人可做不到啊。啊，你别看梁芷柔考那么厉害，她也是花了好几年，从初中就开始努力，才慢慢累积成现在这个水平的。」"
    voice "audio/voice/017048.ogg"
    z "「你要是能早点的话……」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017049.ogg"
    z "「唉……」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017050.ogg"
    z "「嗐，现在说这个也没什么意义了。」"
    voice "audio/voice/017051.ogg"
    z "「不过呢，大器晚成的人有的是，啊，只要你是真的认真了，那什么时候开始努力都不算晚。」"
    y "「…………嗯。」"
    y "「谢谢您。」"
    y "「您说的没错，问题在我自己身上……只是……」"
    y "「到了最后，我还是没追上梁芷柔的步伐。还是有点……不甘心。」"
    z "「……」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017052.ogg"
    z "「哎呀……梁芷柔啊……」"
    voice "audio/voice/017053.ogg"
    z "「既然提到了她，我也就索性再多说两句。」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/017054.ogg"
    z "「咱俩当初聊这个问题的时候，我就跟你说过了，你往樱华报可以，但是你得给我一个除了她以外的理由出来。」"
    voice "audio/voice/017055.ogg"
    z "「为什么呢？嘿，我也不怕得罪你，因为感情这个东西啊，不是那么可靠的。」"
    voice "audio/voice/017056.ogg"
    z "「要只有这么一个理由，那万一后来你俩没成，又该怎么办啊？」"
    voice "audio/voice/017057.ogg"
    z "「就拿你现在来说吧，你要是因为对她不死心，去复读了，啊，哪怕你一次就成功，那也要多花一年的时间，是不是？」"
    voice "audio/voice/017058.ogg"
    z "「万一这期间出点什么事，就、就是那个……啊，你明白吧？那样的话你怎么办啊？你是接着考，还是不考了？」"
    y "「……」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017059.ogg"
    z "「而且啊，这又得说回刚才那个问题去了。」"
    voice "audio/voice/017060.ogg"
    z "「咱们有什么说什么，在『去樱华』这个问题上，你跟梁芷柔的情况完全是不一样的。」"
    voice "audio/voice/017061.ogg"
    z "「去樱华呢，除了樱大本身好之外，对个人发展最大的好处是什么啊？机会多，对不对？」"
    voice "audio/voice/017062.ogg"
    z "「啊，这梁芷柔去樱华，那是因为以她现在的水平，能有机会获得一个足够的发展空间，不至于撞上天花板。」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/017063.ogg"
    z "「但是你呢？樱华理工大学当然也不错，但是呢，你无论是去樱华还是百薇，现在的主要问题，是你根本还够不到那个天花板呢。啊，给你那么大的空间，其实不像梁芷柔用处那么大。」"
    voice "audio/voice/017064.ogg"
    z "「当然啦，你之后呢可能还会像前面一年这样的进步，但真到了那时候，可能理工大又反过来成为你的天花板了。」"
    voice "audio/voice/017065.ogg"
    z "「你想去樱华呀，这些都是问题，不是只有『因为梁芷柔去了樱华』这么一个理由就可以的。」"
    voice "audio/voice/017066.ogg"
    z "「反过来说呢，如果你现在，支撑自己去樱华的理由就只剩下梁芷柔这一条了……」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017067.ogg"
    z "「那我劝你放弃。」"
    "老师摊了摊手，下了结论。"
    y "「但……」"
    "虽然下意识地想要反驳，但张了张口，却发现自己无话可说。"
    "我现在……已经没有任何夸下海口的资本了。"
    y "「……我明白了。」"
    y "「您让我再想想。」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    z "「……」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017068.ogg"
    z "「我啊，我的意思呢，其实不是说不想让你去樱华，啊，是不能让你这么不给自己留退路。」"
    voice "audio/voice/017069.ogg"
    z "「就好像之前，我也没不让你去报名，对不对？但那个时候呢，是因为你还有第二志愿可以兜一下。」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/017070.ogg"
    z "「那现在呢？你现在脑子一热，冲上去了，要再出点儿什么差错啊，那可真就是影响你一辈子的事儿了。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017071.ogg"
    z "「有梦想是好事，但是，你也不能不考虑现实，对吧？」"
    voice "audio/voice/017072.ogg"
    z "「大家都年轻过，谁都有过梦想。不止你有啊，我也有。」"
    voice "audio/voice/017073.ogg"
    z "「区别在于，你现在是年轻。而我呢，是年轻过。」"
    voice "audio/voice/017074.ogg"
    z "「明白吗？有梦想，但到了最后，这梦想不一定就是能实现的。」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017075.ogg"
    z "「你啊，就跟你自己说的一样，再好好想想吧，啊！」"
    y "「……是。」"
    y "「……」"
    y "「老师，能再多问您一句吗？」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017076.ogg"
    z "「嗯？你说。」"
    y "「您……以前的梦想，是什么？」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017077.ogg"
    z "「呵……我啊。」"
    voice "audio/voice/017078.ogg"
    z "「你要是想拿我当参考，那你恐怕是打错算盘了。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017079.ogg"
    z "「我毕竟是70后。我们那会儿的想法，跟你们现在可不一样啊。」"
    z "「……」"
    stop sound fadeout 3.0

    voice "audio/voice/017080.ogg"
    z "「嗯，这么说吧。」"

    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.

    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017081.ogg"
    z "「我那会儿啊，想去大山里当老师。」"
    y "「哎？」"
    voice "audio/voice/017082.ogg"
    z "「不奇怪呀。你要知道，我本来是农村人。我小的时候，那上学的条件……嗐，别提了。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017083.ogg"
    z "「我的启蒙老师呢，是个老知青，上山下乡的时候来的。八十年代以后啊也没回老家，就在我们那边扎了根，一直在镇里的小学教书，前两年刚退下来。」"
    voice "audio/voice/017084.ogg"
    z "「他这个人吧，教书也谈不上多好，脾气还暴。那会儿啊，天天打我。你别看我以前老是吼你们啊，那要跟我老师一比，那真是差得远去了。」"
    voice "audio/voice/017085.ogg"
    z "「但是呢，那个时候要是没有他啊，那周围几个村里的孩子，那就真是……现在都得是文盲。」"
    voice "audio/voice/017086.ogg"
    z "「唉，你现在听着可能都没感觉……不过说真的，义务教育可是从1986年才开始的，而且当时只是出了这么个规定，根本没有条件落实。得是到了你们这一代，反正咱们这地方，才算差不多真正能做到这一点。」"
    voice "audio/voice/017087.ogg"
    z "「哎……反正呢，我因为我的老师，有幸读完了小学，然后因为成绩还可以，老师又专门上我家苦口婆心地劝我父母，让我继续读初中。」"
    voice "audio/voice/017088.ogg"
    z "「所以我小的时候啊，最大的愿望，就是能变成像我老师这样的人，到一个没有其他老师愿意去的地方，去教书，教下一个我。」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017089.ogg"
    z "「所以初中毕业的时候，我报了省城的中师，啊就是中等师范学校，现在已经没有了。总之呢，我上完中专，就报名参加了支教，然后去了南边一个省。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017090.ogg"
    z "「我在那儿呆了七年。」"
    voice "audio/voice/017091.ogg"
    z "「你知道吗？我之前以为我家那村里就是最穷的穷乡僻壤了，但等我到了我支教的地方……嘿，我的妈呀，你都想象不到那是个什么地方啊。」"
    voice "audio/voice/017092.ogg"
    z "「那真的就是一座山，就只有山，没有别的啊。那所谓的村，就是山里面找了一块平整一点的地方，搭了点土房出来。」"
    voice "audio/voice/017093.ogg"
    z "「但就是这么个地方，依然有人在，也就有小孩，小孩还想要上学，想学知识。」"
    z "「……」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/017094.ogg"
    z "「所以啊，我一想起你们一天到晚就知道混日子，我就来气！」"
    y "「……呃。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017095.ogg"
    z "「……唉。」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017096.ogg"
    z "「反正呢，我在那个地方教了七年的书。一边教书呢，一边自学，那会儿先考大专嘛，大专考完了又续本。」"
    voice "audio/voice/017097.ogg"
    z "「我呢，一开始真的是想……在大山里面，教上一辈子书。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017098.ogg"
    z "「但是理想是理想，现实是现实啊。」"
    voice "audio/voice/017099.ogg"
    z "「九十年代末那个时候，这各种政策啊是天天改来改去，一点谱都没有。唉，就好像说我支教啊，本来是能解决农转非的，当时传说要取消，还有编制和工龄，也都是说什么的都有，反正啊就是乱成了一锅粥。」"
    voice "audio/voice/017100.ogg"
    z "「那阵子，家里老是催我赶快回去，到县城去上班。这好歹是个铁饭碗嘛，待遇靠得住，也有面子，否则万一政策变了，不管我了，那我就完蛋了。」"
    voice "audio/voice/017101.ogg"
    z "「还有一个关键的，是我……差不多也到岁数了，呵，他们想让我赶紧找个对象。那山里上哪儿找去啊，也没有人会愿意跟我一起去山里，就只能是回家这边来。」"
    voice "audio/voice/017102.ogg"
    z "「反正吧，就这么个意思，每次都催，只要我一回家就催。」"
    voice "audio/voice/017103.ogg"
    z "「我一开始呢，是不想回来的，想坚持一下自己当初的理想。但是时间一久，还是能感觉出来，真的是很难做到啊。」"
    voice "audio/voice/017104.ogg"
    z "「尤其是每次回家，这边就算发展得慢，每年还是会变不少样啊，但是再回到山里……」"
    voice "audio/voice/017105.ogg"
    z "「那山，永远还是那个山。」"
    voice "audio/voice/017106.ogg"
    z "「我其实呢……我挺舍不得那些孩子的，真的。但到了最后两年，我也真的是已经……已经坚持不下去了。好在啊，最后总算是没当逃兵，熬到一个同样愿意来山里支教的人，这么才把我给替回来了。」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017107.ogg"
    z "「这个，就是关于『我的梦想』的故事。」"
    y "「……」"
    voice "audio/voice/017108.ogg"
    z "「呵，是不是觉得没法聊了？」"
    y "「……也不是，就是有点震撼。我都没想到老师您是个这么伟大的人。」"
    voice "audio/voice/017109.ogg"
    z "「嗐，伟大个屁啊。你师爷可以说是伟大，我啊，就是个普通人。」"
    y "「但您还是去了七年啊。」"
    y "「……」"
    y "「老师，那……您说我对樱华没有实际概念，可您当时，也不知道山里的情况吧？怎么还是去了？」"
    voice "audio/voice/017110.ogg"
    z "「因为我知道自己要去做什么。呵，我呀，是把困难想得太简单啦。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017111.ogg"
    z "「而你呢，又不一样。你呀，根本不知道会有什么样的困难。」"
    y "「……」"
    voice "audio/voice/017112.ogg"
    z "「所以说，在这一点上，梁芷柔是做得最好的。」"
    voice "audio/voice/017113.ogg"
    z "「她知道自己要面对什么，然后迎难而上。结果怎么样不好说，但最起码，她的准备是最充分的。」"
    voice "audio/voice/017114.ogg"
    z "「你呢？」"
    y "「……是。我明白了。」"
    y "「那，老师，最后的问题。」"
    y "「您后悔去那七年吗？如果……您就像现在这样，已经知道有那些困难了，您还会去吗？」"
    z "「……」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017115.ogg"
    z "「呵，你小子，在这儿等着我呢？」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017116.ogg"
    z "「嗯，怎么说呢……」"
    voice "audio/voice/017117.ogg"
    z "「人哪，都是会成长的。以前的自己和现在的自己，去看同一件事，角度肯定会不一样。」"
    voice "audio/voice/017118.ogg"
    z "「有些人老是喜欢说什么……啊，『我们都活成了自己最讨厌的样子』……什么的。」"
    voice "audio/voice/017119.ogg"
    z "「呵。不过反过来说，让现在的你再翻回头看看以前的自己，那一样觉得好不到哪去。」"
    voice "audio/voice/017120.ogg"
    z "「年轻、单纯，有的时候啊，甚至有点幼稚。」"
    show charaz lh03 #老师立绘|夏季|皱眉|近
    with dissolve
    voice "audio/voice/017121.ogg"
    z "「我啊，现在的我，可能会觉得以前的自己就是个笨怂，眼界太窄，啥都不知道。」"
    voice "audio/voice/017122.ogg"
    z "「不知道那地方有多苦，不知道自己差点丢掉了什么，也不知道自己不是那块料，根本坚持不到最后。」"
    show charaz lh01 #老师立绘|夏季|普通|近
    with dissolve
    voice "audio/voice/017123.ogg"
    z "「哎。但是吧……」"
    voice "audio/voice/017124.ogg"
    z "「等骂完了，你要问我去不去？」"
    z "「……」"
    show charaz lh02 #老师立绘|夏季|微笑|近
    with dissolve
    voice "audio/voice/017125.ogg"
    z "「能去的话，我还是会去吧。」"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "……{p}…………"
    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音
    scene bg b04 #滨河路|夏
    with fade
    y "「……」"
    y "「…………」"
    scene bg b04 #滨河路|夏
    nvl show
    nvl_narrator "回家的这一路上，我一直在思考老师的话。"
    nvl_narrator "老师和我，在选择目标的时候，都在追随榜样。"
    nvl_narrator "老师追随的是他的老师，而我，则是梁芷柔。"
    nvl clear
    nvl_narrator "只不过，我的目标说是「和梁芷柔一起去樱华」，其实是「『和梁芷柔』一起去樱华」。"
    nvl_narrator "对我来说，去哪里，其实并不是那么重要。如果梁芷柔报考的学校在其他城市，结果也是一样的。"
    nvl_narrator "这也导致……在第一志愿落榜的那一刻，我就已经失去了目标，也迷失了方向。"
    nvl clear
    nvl_narrator "然而，现在问题搞清楚了，答案却还没有找到。"
    nvl_narrator "我甚至不知道该怎么去寻找。"
    nvl_narrator "没有头绪，时间也所剩无几，这眼瞅着就要到8月份了啊……"
    with vpunch
    nvl clear
    nvl hide
    #书店店员
    voice "audio/voice/027001.ogg"
    who "「哎哟！」"
    y "「啊！」"
    "光顾着想事情，没注意看路，结果不小心撞到人了。"
    y "「抱歉抱歉……哎？吴姐？」"
    show charad lg02 #书店店员立绘|惊讶|近
    with dissolve
    voice "audio/voice/027002.ogg"
    d "「啊，小叶？是你啊。」"
    voice "audio/voice/027003.ogg"
    d "「你这是怎么啦，路这么宽都能撞上我。」"
    y "「是，对不起。」"
    show charad lg03 #书店店员立绘|笑容|近
    with dissolve
    voice "audio/voice/027004.ogg"
    d "「哎呀我又没有在怨你，干嘛这么一本正经的呀。」"
    show charad lg01 #书店店员立绘|普通|近
    with dissolve
    voice "audio/voice/027005.ogg"
    d "「哎哎哎，说起来这阵子都没见到你，还没问呢，你考得怎么样啊？」"
    show charad lg04 #书店店员立绘|坏笑|近
    with dissolve
    voice "audio/voice/027006.ogg"
    d "「我记得这两天看新闻说，大学都已经开始录取了？怎么样怎么样，是不是下个月开始你就可以和梁芷柔双宿双飞去啦？」"
    y "「啊，呃……」"
    "所谓哪壶不开提哪壶。"
    "店员小姐显然是没有什么恶意的，倒不如说，她对我还蛮有信心的。"
    "结果…{cps=2}…就{/cps}显得更加扎心了。"
    show charad lg02 #书店店员立绘|惊讶|近
    with dissolve
    voice "audio/voice/027007.ogg"
    d "「嗯？你……这是，怎么了？」"
    y "「……」"
    voice "audio/voice/027008.ogg"
    d "「啊……不是吧？这……」"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b04 #滨河路|夏
    with fade
    show charad g02 #书店店员立绘|惊讶
    with dissolve
    "我把情况简单地向店员小姐说明了一下。"
    y "「……就是这样了。」"
    y "「我真的是……不知道该怎么办了，一点方向都没有。」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/027009.ogg"
    d "「嗯……」"
    "店员小姐罕见地认真了起来，皱着眉头沉吟了一阵。"
    voice "audio/voice/027010.ogg"
    d "「我也不好说你该怎么做，毕竟每个人的情况都不一样。」"
    voice "audio/voice/027011.ogg"
    d "「不过，你说你不知道樱华值不值得你拿一切去再赌一次……那我问你一个问题。」"
    voice "audio/voice/027012.ogg"
    d "「你觉得樱华是一个什么样的地方？」"
    y "「什么样的……」"
    "这问题可谓相当笼统，我一时间有点犹豫，不知道该怎么回答。"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/027013.ogg"
    d "「你就说个大概的感觉？比如，高楼大厦？灯火通明？」"
    y "「我……」"
    y "「我不知道。」"
    y "「我的老师，说我对樱华没有概念。」"
    y "「他也没说错，我确实是没什么概念。」"
    y "「我从来都没有去过樱华——也不用说樱华了，自打我能记事开始，我就没有出过远门……没有去过任何一个大城市。」"
    y "「所以这个问题……我真的是回答不上来。真要是能回答，我也不用再这么犹豫了。」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/027014.ogg"
    d "「对吧，所以说啊……」"
    stop sound fadeout 3.0
    voice "audio/voice/027015.ogg"
    d "「……」"
    play music "audio/music/bgm13.ogg" fadein 10 #With Memories

    voice "audio/voice/027016.ogg"
    d "「我跟你说一下我眼中的樱华吧。」"
    y "「哎？」"
    "店员小姐的话令我有些意外，然而她却没有理会我的惊讶，自顾自地说了下去。"
    scene bg b12 #樱华市
    show memories #回忆滤镜
    with fade
    voice "audio/voice/027017.ogg"
    d "「在我看来，樱华是一个冷漠的地方。」"
    voice "audio/voice/027018.ogg"
    d "「为什么说冷漠呢，就是……你看，一个地方，人来人往的，有很多人在，但是没有人会关心你。」"
    show bg b12a #樱华市|夜晚
    with dissolve
    voice "audio/voice/027019.ogg"
    d "「不管你在大庭广众之下，是开怀大笑，还是号啕痛哭，旁人最多看你一眼就走过去了。连三秒钟都没有，就过去了。」"
    voice "audio/voice/027020.ogg"
    d "「你有一肚子的话想和别人说，周围都是人，但你就是找不到人。」"
    voice "audio/voice/027021.ogg"
    d "「没人有那个闲工夫，陪你笑，听你哭。」"
    scene bg b04 #滨河路|夏
    with fade
    show charad g01 #书店店员立绘|普通
    with dissolve
    "店员小姐不知在想着什么事情，声音有些飘忽。"
    "那感觉……仿佛我就是她话中那些「周围的人」，近在咫尺，却无关。"
    voice "audio/voice/027022.ogg"
    d "「但是……那也是个自由的地方。」"
    voice "audio/voice/027023.ogg"
    d "「规矩清清楚楚，只要你不惹事，想干什么都行，没有人限制你，能限制你的只有你自己。」"
    voice "audio/voice/027024.ogg"
    d "「你正经做事情也好，三天打鱼两天晒网也罢，就算是把自己的头发染成一片蓝一片粉的，也没人会对你大惊小怪。」"
    show charad g04 #书店店员立绘|坏笑
    with dissolve
    "店员小姐指了指自己的脑袋，终于又找回了平时常见的那种笑容。"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/027025.ogg"
    d "「只要你自己能承担结果，就行。」"
    y "「吴姐，您……」"
    voice "audio/voice/027026.ogg"
    d "「呵……对。」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/027027.ogg"
    d "「我15岁那年，读完了初中，勉强算是把义务教育完成了。然后呢，一边做着一夜暴富的白日梦，一边随便选了个大城市，就这么闭着眼睛闷头冲过去了。」"
    voice "audio/voice/027028.ogg"
    d "「……呵。」"
    scene bg b12a #樱华市|夜晚
    show memories #回忆滤镜
    with fade
    voice "audio/voice/027029.ogg"
    d "「樱华啊，当时我出了火车站，只看了一眼，我就明白了，这就是我想要去的地方。」"
    voice "audio/voice/027030.ogg"
    d "「我当时就在心里发誓，我要赌上一切，留下来。」"
    voice "audio/voice/027031.ogg"
    d "「对，就这一眼，让我在那边拼死拼活，拼了好几年。」"
    show bg b12 #樱华市
    with dissolve
    voice "audio/voice/027032.ogg"
    d "「那段日子呀……每天起早贪黑的，干上十几个小时，什么破活烂活都能丢给我，没一天不加班的，还成天挨骂。」"
    show bg b12a #樱华市|夜晚
    with dissolve
    voice "audio/voice/027033.ogg"
    d "「你要说机会，也不是没有，其实还挺多的，但是一个都没有抓住。」"
    show bg b12 #樱华市
    with dissolve
    voice "audio/voice/027034.ogg"
    d "「毕竟……我一个初中生，懂什么呀？想学，也学不出个什么名堂……就没有人会好好教你。」"
    show bg b12a #樱华市|夜晚
    with dissolve
    voice "audio/voice/027035.ogg"
    d "「就这么一天一天地熬，也没个头，熬到最后，终于熬不下去了，呵……」"
    scene bg b04 #滨河路|夏
    show charad g03 #书店店员立绘|笑容
    with fade
    voice "audio/voice/027036.ogg"
    d "「我就灰头土脸地滚回老家来了。」"
    y "「……」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/027037.ogg"
    d "「听着惨吧？是不是感觉……浪费了这么多年，不值？」"
    y "「是……有点。」"
    show charad g04 #书店店员立绘|坏笑
    with dissolve
    voice "audio/voice/027038.ogg"
    d "「可是，惨的可不只是我一个人啊，比我还惨的也多的是呢。但到头来，大家还是前赴后继地往那边去。」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/027039.ogg"
    d "「樱华……那些大城市，就是这样。好，是真的好，总能吸引人去；但苦，也是真的苦，很多人到了最后都是竹篮打水，一场空。」"
    voice "audio/voice/027040.ogg"
    d "「那些付出的代价，值与不值，对每个人来说，感觉都不一样，没有一套绝对的标准。」"
    voice "audio/voice/027041.ogg"
    d "「你不亲自去体会一下，永远不会知道，那是值，还是不值。」"
    y "「……」"
    voice "audio/voice/027042.ogg"
    d "「小叶……现在是你自己想出去看看，对吧？」"
    voice "audio/voice/027043.ogg"
    d "「不单是因为梁芷柔，你自己也在这么想，是不是？」"
    y "「……是。」"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/027044.ogg"
    d "「所以你为什么不真的去一趟呢？」"
    y "「唉？」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/027045.ogg"
    d "「我当年看了那一眼，就让我拼到了最后，一直拼到一点本钱都没有了，才不得不放弃。」"
    voice "audio/voice/027046.ogg"
    d "「你呢……我不知道你现在这个情况，这样有没有用，毕竟咱俩的本钱差得有点远……」"
    "店员小姐看着我手中的录取通知书，轻轻努了努嘴。"
    voice "audio/voice/027047.ogg"
    d "「何况你现在也去不了几天，可能就跟蜻蜓点水似的，帮不到你多少。」"
    show charad g03 #书店店员立绘|笑容
    with dissolve
    voice "audio/voice/027048.ogg"
    d "「但是，哪怕是走马观花呢，总比你留在这里闭门造车强。最起码……」"
    voice "audio/voice/027049.ogg"
    d "「你可以不靠听别人说，不靠自己瞎猜，亲眼去看一看。」"
    voice "audio/voice/027050.ogg"
    d "「看一看你可能的选择……以及梁芷柔的梦想。」"
    show charad g01 #书店店员立绘|普通
    with dissolve
    voice "audio/voice/027051.ogg"
    d "「不是吗？」"
    stop music fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t08 #转场 樱华市
    with fade
    pause

#8月5日。
#樱华市。

    scene bg black #黑屏
    with fade
    voice "audio/voice/147001.ogg"
    m "「旅客朋友，大家好！一路旅行辛苦了！我们的旅行生活已接近尾声，这趟列车由百薇站开出，经过了28小时49分钟的旅行，就要到达终点站樱华站了。」"
    voice "audio/voice/147002.ogg"
    m "「在您即要走下这趟列车与我们分别的时候，我代表列车全体工作人员感谢您对我们工作的支持与协助。同时，也希望下次旅行再乘坐我们这趟列车，愿我们再相逢！」"
    scene bg b12a #樱华市|夜晚
    with fade
#最终需再确认一次BGM
    play music "audio/music/bgm03.ogg" fadein 1.5 #秋～绯月～
    nvl show
    nvl_narrator "顺着人群涌动的方向，走出火车站。"
    nvl_narrator "晚上7点，樱华的天空已经有些暗下来了。"
    nvl_narrator "如果是在老家，距离太阳下山应该还有些时候……然而，此刻的我，已经向东跨越了整整一个时区。"
    nvl clear
    nvl_narrator "在硬座上颠簸了将近2500公里以后，我终于来到了樱华，来到了这座让梁芷柔魂萦梦绕、我却对其知之甚少的巨大都市。"
    nvl_narrator "坐在公交车上的我，靠着车窗，默默地望着外面的繁华世界。"
    nvl_narrator "五光十色的霓虹灯不断在眼前闪现，然后在看清之前就一晃而过，最后留在眼中的只是一道道的残影。"
    nvl_narrator "这许许多多的光影，为无数高楼大厦包裹上了一层金光闪闪的外衣，将因为天色黯淡而被黑暗笼罩的它们重新点亮。"
    nvl clear
    nvl_narrator "然后，迎来人潮。"
    nvl_narrator "在这个老家已该逐渐寂静下来的时刻，对樱华来说，才只是夜生活开始的前奏。"
    nvl_narrator "高节奏高强度工作了一整天的人们，此时终于结束了手头的工作，开始拖着疲惫的身体向家……或者其他的什么地方移动，去享受自己短暂的闲暇时光。"
    nvl clear
    nvl_narrator "望不尽的灯红酒绿、数不完的纸醉金迷。"
    nvl_narrator "华灯初上，夜未央。"
    nvl_narrator "但，这一切都与我毫无关系。"
    nvl clear
    nvl_narrator "我只有从父母那里讨要来的、并不充裕的一点旅费，需要精打细算到每一分。"
    nvl_narrator "我还不属于这座城市，也不知道以后会不会属于这里。"
    nvl_narrator "这些繁华，与现在的我，无关。"
    nvl clear
    nvl_narrator "此时此刻，我正从位于城市边缘的火车站往市中心方向前进。"
    nvl_narrator "而在沿途，那些真正在这座城市中生活的人，却大多是走在与我相反的方向，从市中心往房价便宜的新城区涌动。"
    nvl_narrator "就这样，我用与这座城市格格不入的节奏，一路逆行着闯了进去。"
    nvl clear
    scene bg black #黑屏
    with fade
    nvl hide
    y "「……呼。」"
    with vpunch
    "一进到房间里，我就直挺挺地扑到在床上，一动也不想动了。"
    "无论再怎么年轻力壮，经历了这么长时间的硬座摧残，都注定会让人筋疲力尽、无以为继。"
    y "「……」"
    scene bg b12a #樱华市|夜晚
    with fade
    "勉强翻了个身，抬头仰望着天花板。"
    "窗外依旧灯火辉煌，余光穿透窗帘，在这间半地下室的地板上投出淡淡的亮斑，倒是颇有李白《静思夜》的感觉。"
    "只不过由于多了防盗护栏的影子，或许看上去倒更像是监狱。"
    "老城区的青年旅馆还算便宜，再往前因为靠近一些著名的景区，所以成本会直线拉高。好在这里的交通还算方便，不用担心之后的出行。"
    "晚饭也已经在路上顺便吃过了……无论再怎么奢华的城市，总归还是能够找到物美价廉的食物的。"
    scene bg black #黑屏
    with fade
    y "「……」"
    y "「…………」"
    scene bg b12a #樱华市|夜晚
    with fade
    "只是……明明已经累得不行了，但却偏偏没法很快睡着，大脑还在坚持不懈地进行着各种胡思乱想。"
    "果然……还是紧张啊。"
    "虽然人总算是到了樱华，然而最终结果如何，就完全不得而知了。"
    y "「……呼。」"
    scene bg black #黑屏
    with fade
    "闭上眼睛，强行压下内心的忐忑。"
    "睡吧，养足精神，用最好的状态迎接明天的到来。"
    "抛弃一切借口，也不要再逃避。"
    "去寻找真正的，「我」的答案。"
    stop music fadeout 2.0

    "……{p}…………"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t08 #转场 樱华市
    with fade
    pause

#8月6日。"
#前往樱华大学。"

    play sound "audio/sound/ambientnoise04.ogg" fadein 1.5 loop #白天环境噪音

    scene bg b12 #樱华市
    with fade
    "第二天一早，迎着初升的太阳，我离开旅馆，坐上公交车，向着今天的目的地前进。"
    "路况还算良好，虽然能够明显感觉到街面上的车流在很短的时间内大幅增多了，但由于赶在早高峰之前就出发了，好歹在遇到堵车之前离开了市中心。"
    "离开市中心没多远，公交车途径了一处著名的风景区。"
    "如同紫禁城之于首都一样，眼前的湖泊可以称得上是樱华市的名片。"
    "清晨的湖面上铺着薄薄的雾气，仿佛戴了一层面纱，有着难以形容的朦胧美感。"
    "这幅以前只在电视和图片中看到过的景色，此时此刻，近在眼前。"
    "只可惜，现在的我，无暇在这里多做停留。"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    nvl hide
    "乘坐公交车继续前行，从湖的北岸向西拐了个弯，又开了一段距离，到达了一处公交站。"
    "下了公交车之后，沿着护校河从北往南行进，没过多远，就来到了自己今天的目的地。"
    scene bg b13 #大学校门
    with fade
    play music "audio/music/bgm15.ogg" fadein 1.5 #樱华大学
    "樱华大学。"
    "国内顶尖，世界百强的高等学府。{p}一个梁芷柔已经得偿所愿，但对我而言还只是可望而不可及的地方。"
    "我想到这里来，亲眼看一看。"
    "门口的小广场上伫立着一棵巨大的雪松，相比之下，在它身后的大门本身反倒不是那么显眼了。"
    "然而，当我走到门前的时候，却迅速地感受到了后者的深沉与厚重。"
    "不同于更为常见的烫金色字，樱华大学的校名直接浮刻在石质的校门上方，而在它背后的远方，一座高大的青山隐约可见。"
    "二者浑然一体，仿佛跨过门后，便会是另一方天地。"
    scene bg b14 #大学校区
    with fade
    nvl show
    nvl_narrator "广义上来说，「进入樱大」倒也不难。"
    nvl_narrator "门卫只会对车辆的出入进行登记，对行人则没什么限制。"
    nvl_narrator "不过，进到校区也只是第一步，后面我是一点把握也没有。"
    nvl_narrator "我并非这里的学生，若是里面的管理很严格的话，很多地方大概是进不去的。"
    nvl_narrator "不过事到临头了再想这些也没什么用，只能先走一步算一步了。"
    nvl clear
    nvl_narrator "由于还在放暑假，校园里的人并没有多少。"
    nvl_narrator "绕过正门后面的一小块草坪，周围的建筑逐渐多了起来。"
    nvl_narrator "樱华大学有好几个校区，主校区是其中最老的一个，也正因为此，这里的建筑都颇有些年代感。"
    nvl_narrator "楼房多为四五层的矮楼，以白色为底，在窗台之下间杂着些许砖红色，并不气派，但却敦厚稳重。"
    nvl_narrator "对我来说，这种有些苏联式的建筑甚至还别有一番熟悉感，毕竟老家旧城区里同样风格的楼房可谓数量众多。"
    nvl_narrator "不过……"
    nvl clear
    nvl hide
    with dissolve
    y "「噢噢……」"
    "老家的楼房门口可不会挂着「理学部」、「电子显微镜中心」这样的牌子。"
    y "「说起来……」"
    y "「梁芷柔专业报的是应用数学吧？」"
    "也就是说她以后少不了要路过我现在站的这个位置吧……"
    y "「……」"
    "感觉……有些五味杂陈。"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b14 #大学校区
    with fade
    nvl show
    nvl_narrator "沿着主路继续向前，到达了一片草地广场。"
    nvl_narrator "广场的两侧，繁茂的樟树排列成行，为人们撑起了阴凉。而在西侧大概100米之外，还伫立着一座主席雕像。"
    nvl_narrator "广场上，看不到多少学生模样的人，倒是有不少家长带着孩子在玩耍，还有一些锻炼身体的老人。"
    nvl clear
    nvl_narrator "沿着侧边的道路继续行走，我找到了旁边楼房的大门。"
    nvl_narrator "尽管楼房本身并不多么宏伟，但作为门脸的正门还是经过了一番改造的，中式仿古风格的造型，门上挂着「第一教学楼」的牌匾。"
    nvl_narrator "只不过，虽然大门敞开，但内里却是……"
    nvl_narrator "黑着灯。"
    nvl clear
    nvl hide
    with dissolve
    y "「……」"
    "有些麻烦。"
    "毕竟是暑假，想去蹭个课什么的，恐怕还是不现实的。"
    "看来，要想有点什么近距离的感受，只能是另辟蹊径了。"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b14 #大学校区
    with fade
    nvl show
    nvl_narrator "又向前走了一段距离。"
    nvl_narrator "附近建筑的色彩相较刚才颠倒了一下，变成了砖红色为底、白色为辅。"
    nvl_narrator "除此以外，还出现了一座十分显眼的建筑——"
    nvl clear
    nvl_narrator "图书馆。"
    nvl_narrator "相比一路过来那些沿途的教学楼，图书馆尽管也是老楼，但却更加高大，楼宽约有百米，高度也超过了七层，在门口还树着樱大老校长的雕塑。"
    nvl_narrator "或许这里……是个不错的参考目标？"
    nvl clear
    scene bg black #黑屏
    with fade
    nvl hide
    "……{p}…………"
    scene bg b14 #大学校区
    with fade
    nvl show
    nvl_narrator "虽然此时图书馆刚刚开馆不久，再加上是假期当中，偌大的场馆中并没有几个人，但图书馆的管理员并没有因此偷懒，而是尽职尽责地守在自己的岗位上。"
    nvl_narrator "问过管理员之后，我才明白自己又把问题想简单了。"
    nvl_narrator "尽管樱大的图书馆可以有限度地对外开放，但前提是要办理一大堆的手续，像我这样直愣愣地闯进来的校外人员，肯定是不能进到藏书室的。"
    nvl clear
    nvl_narrator "不过自习室倒是可以自由出入。"
    nvl_narrator "犹豫了一下，我还是进去看了看。"
    nvl_narrator "人数不多，不过每个人倒是都很专注。"
    nvl clear
    nvl_narrator "有的人在抱着某种大部头的书仔细研究。"
    nvl_narrator "有的人拿出纸笔，对照着专业书籍写写画画。"
    nvl_narrator "有的人在默念某种外语，偶尔会不小心念出声来，发觉以后又赶紧压下嗓子。"
    nvl_narrator "不过，会在这个时候到自习室来的人，原本也不太可能是来瞎逛的吧。"
    nvl_narrator "相比之下，两手空空的我就显得十分另类了。"
    nvl clear
    scene bg black #黑屏
    with fade
    nvl hide
    stop music fadeout 2.5
    y "「（……还是离开吧。）」"
    "……{p}…………"
    scene bg b14 #大学校区
    with fade
    play sound "audio/sound/ambientnoise03.ogg" fadein 1.5 loop #傍晚环境噪音
    "当我走出图书馆的时候，时间已经从清晨进入到上午，校园内的人也渐渐多了起来。"
    y "「接下来怎么办……」"
    "继续这样像无头苍蝇一样乱撞显然是不行的，但眼下也实在是没有什么头绪。"
    "总不成在路上直接抓一个学生来求助吧……"
    y "「……」"
    "真到了走投无路的时候，恐怕也就只能这么办了。"
    "希望，到时候能遇到一个好人吧……"
    scene bg black #黑屏
    with fade
    pause 1.0
    scene bg b14 #大学校区
    with fade
    "……{p}…………"
    "一边乱想，一边继续漫步向前。"
    "从图书馆向南拐了个弯，各种建筑的风格开始变得不再统一，名称也逐渐变得晦涩难懂起来。"
    "「信电系」、「高分子系」、「机械设计研究所」……"
    "有的还能理解，有的就需要靠望文生义去猜，还有一些就只能是「虽然不明白你在说什么，但觉得似乎很厉害的样子」了。"
    "而且这些名称似乎也和建筑本身的好坏无关。"
    "有两栋楼，哪怕放在老家都算得上是十分破旧的那种，门口却挂着「省级电池新材料与应用技术研究重点实验室」、「生物质化工教育部重点实验室」之类看上去颇为吓人的牌子。"
    "……{p}…………"
    stop sound fadeout 3.0
    "就这样一路走下来，在又路过一座不知什么实验楼的时候，我突然眼前一亮——"
    play sound "audio/sound/ambientnoise09.ogg" fadein 1.5 loop #人群嘈杂环境噪音
    "一大群看起来和我岁数差不多，穿得也是五花八门看不出规律的学生模样的人，正在往里蜂拥而入。"
    y "「（有机可乘？）」"
    "我紧跑了两步，偷偷混入人群之中。"
    scene bg b15 #实验楼
    with fade
    "从刚到樱大的时候开始，我就一直想要进到这些楼里去参观一下。"
    "无奈看起来似乎并没有机会……要么就是像教学楼那样空无一人，要不就是门口戳着一个虎视眈眈的保安。"
    "不过这里嘛……"
    "虽然这里的门口也有保安，甚至连大门也需要刷卡解禁，但这么多人乱糟糟地往里涌，保安非但没空仔细甄别，反而还需要帮着扶住自动门。"
    y "「（很好！）」"
    "非常顺利地跟着人群进到了楼里。"
    "这帮学生彼此之间似乎也不熟悉，并没有人对我的加入产生疑问。"
    "接下来只要找个机会脱离队伍，就可以自由行动了……"
    voice "audio/voice/137001.ogg"
    stop sound fadeout 3.0
    #工作人员
    who "「好的，来帮忙的同学，我点一下名，叫到名字的跟着负责人走。」"
    y "「……咦？」"
    "我皱起了眉头，终于发现事情似乎并不单纯。"
    "一位看上去像是管理人员之类的中年男子，在学生们全都进来以后，开始照着几张名单点名。"
    "每点几个人，就有一个看起来二三十岁的人将他们领走，向着楼上走去。"

    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    y "「（糟糕，完蛋了！）」"
    "我说这个地方的管理怎么看起来这么松呢！其实是有人在等啊！"
    "这一大票人大概是被拉来帮忙的低年级学生吧？"
    y "「（这可怎么办……）」"
    "被念到的名字越来越多，留下的人越来越少。我心里越来越急，却毫无办法，只能故作镇定地戳在原地。"
    "……{p}…………"
    with fade
    "终于，名单念完了。"
    "所有学生都分配完毕，每一个负责人都领着自己的队伍离开了。"
    h "「……」"
    y "「……」"
    i "「……」"
    "重归平静的一楼大厅，只剩下了那位工作人员、一个保安和我三个人，大眼瞪小眼地互相看。"
    "这就……很尴尬了。"
    "即使楼内的空调开得很足，我脑门上的汗水依然哗哗地往下淌。"
    y "「呃……我……」"
    "组织了半天语言，也不知道该怎么解释才好。"
    stop music fadeout 2.5

    "把心一横……反正大不了就是被轰出去吧，他们总不能吃了我？"
    y "「……嗯……那个……」"
    #李金凡
    voice "audio/voice/037001.ogg"
    who "「哎哟，老杨，给我的志愿者呢？」"
    "突然之间，旁边传来了一个既陌生、又在某个方面有些熟悉的声音。"
    y "「……咦？」"
    show charal i01 #李金凡立绘|普通
    with dissolve
    "我顺着声音望过去，一个看上去文绉绉的三十岁左右的男子，正三步并作两步地从旁边的走廊往这边跑。"
    voice "audio/voice/137002.ogg"
    h "「老李啊？哎，你要过人？」"
    #李金凡
    voice "audio/voice/037002.ogg"
    who "「要过啊。」"
    voice "audio/voice/137003.ogg"
    h "「那怎么没把名单给我啊？你什么时候要的？」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    #李金凡
    voice "audio/voice/037003.ogg"
    who "「早的事了，是他吗？」"
    voice "audio/voice/137004.ogg"
    h "「咳，没给我名单我哪知道啊？那你要人，你刚才怎么不过来啊？」"
    show charal i05 #李金凡立绘|开心
    with dissolve
    #李金凡
    voice "audio/voice/037004.ogg"
    who "「嗐，我这不是现在过来了吗？刚才准备东西呢。」"
    "青年打了个岔，把自己的过失含糊过去，随即转向我这边。"
    show charal i04 #李金凡立绘|微笑
    with dissolve
    voice "audio/voice/037005.ogg"
    who "「你是来做行为识别采样的吧？我是李金凡。」"
    show charal i05 #李金凡立绘|开心
    with dissolve
    voice "audio/voice/037006.ogg"
    j "「来来来，跟我上四楼。」"
    hide charal
    with dissolve
    with vpunch
    "这位不知该算是大哥还是大叔的男子，看来是迫不及待地想把我这个「壮丁」给抓牢了，一边说，一边抓住我的胳膊，开始把我往楼上拖。"
    y "「……」"
    "这倒是救了我一命……虽然依旧是饮鸩止渴。"
    "毕竟我连接下来需要做什么都不知道，说不定一上楼就会露馅。"
    "不过这里还是将错就错吧，最起码，要比现在就被保安和工作人员拿下，还是要强上那么一点的……吧？"
    scene bg b15a #实验楼|二层
    with fade
    show charal i05 #李金凡立绘|开心
    with dissolve
    "我跟着这位自称「李金凡」的男子上了楼。"
    "一边爬楼梯，他还一边很热情地寒暄着。"
    voice "audio/voice/037007.ogg"
    j "「哎呀，这个时候想要找个志愿者过来真是不容易！还好你来了，要不然这事还真是不好办。」"
    show charal i04 #李金凡立绘|微笑
    with dissolve
    voice "audio/voice/037008.ogg"
    j "「发了论坛，布告栏也贴了，就是找不到人，这最后跟辅导员说，他们才说试试看，不过之前都得提前一段时间说，所以也没准。」"
    voice "audio/voice/037009.ogg"
    j "「但是实验又急，哎，真是！啊，这拿我老家的话说就叫做……『人倒霉，鬼吹灯，放屁都砸脚后跟』。」"
    show charal i05 #李金凡立绘|开心
    with dissolve
    voice "audio/voice/037010.ogg"
    j "「这结果呢，没想到他们效率还挺高，昨天说的，今天你就到了。」"
    y "「……」"
    "这个话题还是不要正面回应的好。"
    "不过，我仔细地听过他的话音之后，还是决定说点什么……做个尝试。"
    y "「现在很不好找人吗？」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    voice "audio/voice/037011.ogg"
    j "「是啊……嗯？」"
    "男子露出疑惑的目光。"
    voice "audio/voice/037012.ogg"
    j "「你是……」"
    "我冲他笑笑。"
    show charal i05 #李金凡立绘|开心
    with dissolve
    voice "audio/voice/037013.ogg"
    j "「嗐，老乡啊！」"
    "——果然。"
    "他刚才说那句「家乡话」的时候，我一下子就听出来了——"
    "那正好是我家附近那一带的口音。"
    "我平时虽然都在说普通话，但老家的土话也并非不会说，稍微故意带上一些乡音，立刻就被他听出来了。"
    voice "audio/voice/037014.ogg"
    j "「哈哈，没想到没想到，居然这么巧。」"
    show charal i04 #李金凡立绘|微笑
    with dissolve
    voice "audio/voice/037015.ogg"
    j "「哎呀，在这里能遇到一个老乡不容易啊！」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    voice "audio/voice/037016.ogg"
    j "「这儿倒是也有一些同省的同学，不过大多是从百薇那边过来的。」"
    show charal i05 #李金凡立绘|开心
    with dissolve
    voice "audio/voice/037017.ogg"
    j "「像咱俩挨得这么近的，还真的是少……」"
    scene bg black #黑屏
    with fade
    pause 1.0
    scene bg b15a #实验楼|二层
    with fade
    play music "audio/music/bgm15.ogg" fadein 1.5 #樱华大学
    "一边走，一边聊。"
    "尽管从进门到现在的时间还很短，但不知是这位师兄天生就十分话痨，还是因为见到了老乡所以聊性大发，总之我很快就对他有了初步的了解。"
    "李金凡在八年前考到樱华，从本科读起，目前正在读博。"
    "他并不是我们县的人，家在邻县，不过是在靠近我们县这一侧的交界处，离得不远。"
    "他是他们那个县里第一个考到樱大的人，当时还上了新闻——不过那时候我还在上小学，倒是没什么记忆。"
    "聊天的同时，我顺便观察着沿途大大小小的房间。"
    "「智能交通系统实验室」、「数据采集与监视控制系统实验室」、「机器人实验室」……"
    "和之前看楼名的感觉差不多，基本只能是望文生义去瞎猜用途。"
    "隔着门窗，能看到其中已经有一些人在忙碌了。"
    "这就是……樱华的学生的日常吗？"
    scene bg black #黑屏
    with fade
    pause 1.0
    scene bg b15a #实验楼|二层
    with fade
    show charal i04 #李金凡立绘|微笑
    with dissolve
    voice "audio/voice/037018.ogg"
    j "「……好了，就是这里。」"
    y "「啊……」"
    "李金凡的实验室并不偏僻，很快就到了。"
    y "「『智能监控实验室』？」"
    show charal i01 #李金凡立绘|普通
    with dissolve
    voice "audio/voice/037019.ogg"
    j "「嗯，严格说，这应该算是计算机的课题，不过现在啊，涉及到这个方向的系挺多的，咱们也做。」"
    show charal i05 #李金凡立绘|开心
    with dissolve
    voice "audio/voice/037020.ogg"
    j "「来来来，快进来。」"
    stop music fadeout 2.5

    play sound "audio/sound/ambientnoise13.ogg" fadein 1.5 loop #安静室内噪音
    scene bg b16 #实验室
    with fade
    "进到屋里。"
    "实验室内已经布置出一块空场，铺着绿色的地毯和幕布，还有一圈灯和几个不同角度的摄像头。"
    show charal i04 #李金凡立绘|微笑
    with dissolve
    voice "audio/voice/037021.ogg"
    j "「今天别人都不在，就咱俩。」"
    show charal i05 #李金凡立绘|开心
    with dissolve
    voice "audio/voice/037022.ogg"
    j "「咱们呢，闲话少说，先做实验。做完实验我请你吃饭啊，虽然只是食堂。」"
    show charal i01 #李金凡立绘|普通
    with dissolve
    "一进到实验室，这位李师兄似乎就换了个人，变得有些狂热起来。"
    "也顾不上客套了，三言两语之后，便迫不及待地把我拖到空场中，然后又开始摆弄起周围的灯光。"
    "剩下我手足无措地杵在中间，不敢动弹。"
    y "「……那、那个。」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    voice "audio/voice/037023.ogg"
    j "「嗯？」"
    y "「我待会儿要做什么啊？」"
    voice "audio/voice/037024.ogg"
    j "「哎？辅导员没跟你说吗？」"
    show charal i03 #李金凡立绘|皱眉
    with dissolve
    voice "audio/voice/037025.ogg"
    j "「哦，也是，可能时间太急没跟你仔细说吧。」"
    y "「呃……嗯……」"
    show charal i01 #李金凡立绘|普通
    with dissolve
    voice "audio/voice/037026.ogg"
    j "「这次找你过来，主要是我们做的特定要求下的行为识别系统，需要采集一些针对性的实验数据。」"
    show charal i05 #李金凡立绘|开心
    with dissolve
    voice "audio/voice/037027.ogg"
    j "「不过你也不用紧张，很简单的，不需要什么专业能力，会动就行。」"
    show charal i04 #李金凡立绘|微笑
    with dissolve
    voice "audio/voice/037028.ogg"
    j "「待会儿啊，按照我给你的指示做就行了。」"
    y "「噢噢。」"
    hide charal
    with dissolve
    voice "audio/voice/037029.ogg"
    j "「……好，我们准备，开始了啊！」"
    stop sound fadeout 3.0

    scene bg b16a #实验室|打光
    with dissolve
    nvl show
    nvl_narrator "实验开始了。"
    nvl_narrator "在他的指示下，我开始摆出各种造型，又或者在空场里走来走去。"
    nvl_narrator "李师兄本人则是时而操作电脑，时而调整灯光，偶尔还来掰一掰我的胳膊腿什么的，调整姿势。"
    nvl clear
    nvl_narrator "实验似乎很顺利地进行下去了。"
    nvl_narrator "虽然只是被当做道具摆弄，不过这一切依然让我感到十分新奇。"
    nvl clear
    nvl_narrator "除此以外，还有一点。"
    nvl_narrator "在这位李师兄的脸上，我看到了与梁芷柔如出一辙的……坚定和专注。"
    nvl_narrator "那是已经明确了自己的目标，并一心为之奋斗的人所特有的神情。"
    nvl clear
    nvl hide
    with dissolve

    show charal i01 #李金凡立绘|普通
    with dissolve
    j "「……」"
    show charal i03 #李金凡立绘|皱眉
    with dissolve
    voice "audio/voice/037030.ogg"
    j "「嗯……这一块……应该……」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    voice "audio/voice/037031.ogg"
    j "「……嗯？」"
    play sound "audio/sound/effect03.ogg" noloop
    "李师兄的手机突然响了。"
    show charal i03 #李金凡立绘|皱眉
    with dissolve
    "正巧赶在思索问题的时候，他似乎有些不耐烦，不过看了一眼来电人姓名，还是拧出一个笑脸来接通了电话。"
    stop sound
    play music "audio/music/bgm08.ogg" fadein 1.5 #其乐无穷
    show charal i05 #李金凡立绘|开心
    with dissolve
    voice "audio/voice/037032.ogg"
    j "「哎呀，刘老师啊，谢谢你给我们找人来……」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    voice "audio/voice/037033.ogg"
    j "「……啊？」"
    show charal i03 #李金凡立绘|皱眉
    with dissolve
    voice "audio/voice/037034.ogg"
    j "「什么意思？约的人来不了了？时间太紧张？」"
    show charal i05 #李金凡立绘|开心
    with dissolve
    voice "audio/voice/037035.ogg"
    j "「……没事没事没事，我这边这一个先做着，你也再帮帮忙，想想办法……」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    voice "audio/voice/037036.ogg"
    j "「什么？」"
    voice "audio/voice/037037.ogg"
    j "「……就是说，你那边今天没派人过来？」"
    show charal i03 #李金凡立绘|皱眉
    with dissolve
    voice "audio/voice/037038.ogg"
    j "「不对啊，我这边有人过来了呀？现在正在做着呢。」"
    j "「……」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    voice "audio/voice/037039.ogg"
    j "「是吗？」"
    show charal i01 #李金凡立绘|普通
    with dissolve
    voice "audio/voice/037040.ogg"
    j "「那好吧，我这边确认一下再说吧。」"
    show charal i03 #李金凡立绘|皱眉
    with dissolve
    j "「……」"
    j "「…………」"
    show charal i01 #李金凡立绘|普通
    with dissolve
    "李金凡把手机从耳边拿开，看着屏幕思考了几秒钟，按下了挂断。"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    "随即，又转过头来，用奇怪的表情看向我。"
    j "「……」"
    y "「……」"
    "这就……又很尴尬了。"
    show charal i01 #李金凡立绘|普通
    with dissolve
    voice "audio/voice/037041.ogg"
    j "「呃，那个……」"
    stop music fadeout 2.5

    play sound "audio/sound/ambientnoise13.ogg" fadein 1.5 loop #安静室内噪音
    y "「抱歉！实在对不起！」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    voice "audio/voice/037042.ogg"
    j "「啊……」"
    y "「那个，我其实……不是志愿者。」"
    "在被问到之前，我抢先直截了当地承认自己的身份并道歉。"
    "李师兄问到一半的话被咽了回去。"
    "不过，看他的神色，感觉倒没觉得是在生气，更像是有些疑惑。"
    "在经过了几秒钟的尴尬沉默之后，李师兄再次开口。"
    show charal i03 #李金凡立绘|皱眉
    with dissolve
    voice "audio/voice/037043.ogg"
    j "「……那你来这里干什么？」"
    y "「我今天……只是想来樱华大学看看。」"
    show charal i01 #李金凡立绘|普通
    with dissolve
    voice "audio/voice/037044.ogg"
    j "「看看？」"
    y "「我不是樱大的学生，我今年……刚高考完，还不是大学生。」"
    voice "audio/voice/037045.ogg"
    j "「哦……这样啊。」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    voice "audio/voice/037046.ogg"
    j "「哎，那你既然大老远的跑到这里来……也就是说，你报了这里？」"
    y "「呃……」"
    show charal i05 #李金凡立绘|开心
    with dissolve
    voice "audio/voice/037047.ogg"
    j "「哈哈哈，那也没什么大区别嘛！虽然你现在还不是师弟，但那不就下个月的事情嘛，这有什么大不了的？」"
    show charal i04 #李金凡立绘|微笑
    with dissolve
    voice "audio/voice/037048.ogg"
    j "「没关系没关系，哎呀，倒是我不好意思，还这么使唤你半天。」"
    "李师兄一边笑一边拍了拍我的肩膀，似乎并不介意我偷偷溜进来这事。"
    "惟其如此，更让我觉得不好意思。"
    y "「那个……不，其实……我本来是想要往樱华这里报，但是……差了几分，没考上。」"
    "有些心虚地解释了一句。"
    "我偷换了樱华的概念。我说的樱华是指樱华市，而李师兄大概只会理解成樱华大学吧。"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    j "「……」"
    show charal i03 #李金凡立绘|皱眉
    with dissolve
    voice "audio/voice/037049.ogg"
    j "「这样啊。」"
    "李师兄也一下子沉默了下来，不过很快，他又继续开口。"
    show charal i01 #李金凡立绘|普通
    with dissolve
    voice "audio/voice/037050.ogg"
    j "「好吧，其实一下子我也不知道该说什么好。不过，我想我能理解你的心情。」"
    voice "audio/voice/037051.ogg"
    j "「那你是……还想再考一次吗？」"
    y "「是，有点想。」"
    y "「不过，我也还有点……没太想明白，所以现在很迷茫，才想要来这里亲眼看一看。」"
    show charal i02 #李金凡立绘|疑惑
    with dissolve
    voice "audio/voice/037052.ogg"
    j "「嗯……什么地方没想明白呢？」"
    y "「如果是您，您觉得放弃现有的结果，放弃百薇大学的录取通知书，复读去赌一个重新来过的机会，值得吗？」"
    j "「……」"
    show charal i03 #李金凡立绘|皱眉
    with dissolve
    voice "audio/voice/037053.ogg"
    j "「为什么不值呢？」"
    y "「这……」"
    show charal i01 #李金凡立绘|普通
    with dissolve
    voice "audio/voice/037054.ogg"
    j "「啊，我不是因为已经在这里读书了所以自吹自擂啊，也没有诋毁百薇的意思。」"
    show charal i03 #李金凡立绘|皱眉
    with dissolve
    voice "audio/voice/037055.ogg"
    j "「但是，如果你有这个实力，有这份毅力，又确实想要往这边考的话，为什么会觉得可能不值呢？」"
    y "「……」"
    stop sound fadeout 3.0
    "一时没好意思说出真相的恶果迅速显现出来了，李师兄的思路似乎被我带偏，跑到另外一个角度去了。"
    "不过，虽然前提变了，但问题的核心还是同样成立的。"
    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    y "「我……没搞清楚自己的目的。」"
    y "「我是追随着别人的步伐往樱华报的名，结果失败了。」"
    y "「我的成绩其实没那么好，也就是矬子里拔出来的将军，走到现在这一步已经是竭尽全力了……按说也可以满足了。」"
    y "「这里和百薇，它们都是很优秀的大学，或许樱华这边的条件会更好一些，但是对我来说，它们都已经足够好了。」"
    y "「但我还是觉得……不甘心。」"
    y "「可要说为什么不甘心，我也说不清楚。」"
    y "「仔细想想，我发现我自己其实很多事情根本就没弄明白……」"
    y "「我甚至都搞不清楚如果我真的考到了这里，我能做什么、该怎么做、能不能做到……为什么要这么做。」"
    y "「樱华和百薇的区别究竟在哪？对我来说又有什么不一样？」"
    y "「我究竟是……只是因为看到了一个榜样，所以想跟着去做，还是说我本来就应该这么做？」"
    y "「我挺迷茫的。」"
    y "「我是应该再去考一次？还是就这么认了？」"
    y "「我不知道，所以就来了，想……亲眼看看。」"
    show charal i01 #李金凡立绘|普通
    with dissolve
    voice "audio/voice/037056.ogg"
    j "「……原来如此。」"
    "李师兄点点头，一把搂住我的肩膀，把我拉到了椅子旁边。"
    with hpunch
    "很难相信看上去很瘦弱的他能有这么大的力气。"
    show charal li04 #李金凡立绘|微笑|近
    with dissolve
    voice "audio/voice/037057.ogg"
    j "「来，坐。」"
    "他强行把我按在座椅上，随后自己也坐到了我的旁边。"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037058.ogg"
    j "「我大概明白是什么情况了。」"
    voice "audio/voice/037059.ogg"
    j "「既然今天咱们碰巧这么撞上了，又都是老乡，是个缘分，那我呢，也就斗胆说说我的想法。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037060.ogg"
    j "「按说咱们两个认识的时间还短，有些话我现在说啊，可能有点……交浅言深。要是待会儿哪儿说得过了，说得不合适，你也别往心里去。」"
    y "「哪有……您要是能跟我说一说这些，我是求之不得的。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037061.ogg"
    j "「好吧。但首先需要说的是啊，这个问题，别人的答案始终是别人的，代替不了你自己，不管别人是什么情况，你都只能参考，最后还是得自己做出决断。」"
    voice "audio/voice/037062.ogg"
    j "「每个人的价值观都不一样，因人而异，看你追求什么了。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037063.ogg"
    j "「不过对我来说，我还是刚才那个意思，为什么不呢？」"
    y "「……」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037064.ogg"
    j "「你要说大学和大学之间的区别……嗯，怎么说呢？」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037065.ogg"
    j "「有，也没有。」"
    voice "audio/voice/037066.ogg"
    j "「说有吧，区别是确确实实存在的。」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037067.ogg"
    j "「硬件方面咱们就不提了啊，光说软件，不同大学的师资力量、学习氛围、同学层次，还有诸如一些前沿信息的传递速度、交换留学的机会，包括高校之间的合作项目等等，那这些都是大相径庭的。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037068.ogg"
    j "「这些东西啊，如果展开了说，一点都不夸张，我能跟你说上一整天。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037069.ogg"
    j "「但是呢，也不是所有的方面都是这样。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037070.ogg"
    j "「呃……你说啊，同学都是好学生，其实上课的时候他一样会有人逃课，会找朋友帮忙点名签到，临到考试前才临时抱佛脚也是经常的事。而老师呢，虽然的确有很多都是大牛，但是也不见得给你好好教啊！是吧？」"
    voice "audio/voice/037071.ogg"
    j "「所以这些问题说到最后，归根结底，还是要看你自己的态度，看你够不够努力，会不会争取机会。」"
    voice "audio/voice/037072.ogg"
    j "「无论你最后去了哪所大学，其实都一样。」"
    voice "audio/voice/037073.ogg"
    j "「不过我觉得，对于你刚才的问题来说，这些都不是重点。」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037074.ogg"
    j "「重点是……嗯，怎么说好呢？」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037075.ogg"
    j "「大学的区别，是在你读完大学之后，至少是在本科之后，才能慢慢地感觉出来的。」"
    voice "audio/voice/037076.ogg"
    j "「你现在这种迷茫真的是……再正常不过了。别说你，就算是我前两年，也没有现在这么深的感受。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037077.ogg"
    j "「不过确实，等你从大学里出来以后，开始走向社会的时候，你就会发现，不同学校毕业的学生，那种气质上的差别。」"
    y "「『气质』吗……」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037078.ogg"
    j "「嗯，气质。」"
    voice "audio/voice/037079.ogg"
    j "「就拿樱华来说吧，我们的毕业生，就普遍的比较『坚韧』和『自信』。」"
    voice "audio/voice/037080.ogg"
    j "「换句话说，就是自己能够激励自己，能够持续不断地保持前进的动力。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037081.ogg"
    j "「在做事情的时候，我们会下意识地觉得，『人无我有、人有我优』，别人做不到，我们未必就做不到；别人能做到，我们肯定可以做得更好。」"
    voice "audio/voice/037082.ogg"
    j "「因为这是一种多年养成的、自然而然的习惯，我们不会随便地怀疑自己，也不会轻易地放弃。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037083.ogg"
    j "「这种态度是很重要的，因为在很多的时候，能不能成功就差了这么一点态度。」"
    voice "audio/voice/037084.ogg"
    j "「同样的知识水平，打顺风仗的时候可能都差不多。但是当遇到挫折、遇到不顺利的时候，那点心态上的差距立刻就体现出来了。」"
    voice "audio/voice/037085.ogg"
    j "「这也是为什么名校的毕业生会更受职场欢迎。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037086.ogg"
    j "「因为毕竟，这个世界上恐怕没有多少事是可以轻轻松松、一帆风顺地做成的，你说对吧？」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037087.ogg"
    j "「然后呢，具体到你现在这个情况。」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037088.ogg"
    j "「我问你，你觉得我刚才说的这种『气质』，是怎么养成的？」"
    y "「这个……是因为身边的氛围吗？」"
    y "「因为同学都很优秀，所以也会鞭策自己……这样？」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037089.ogg"
    j "「这算是一方面吧。」"
    voice "audio/voice/037090.ogg"
    j "「但是我的理解啊……这只是一种催化，是加成，而不是根本。」"
    voice "audio/voice/037091.ogg"
    j "「根本在于，来到这里的人，从一开始，就是带着这种气质的。」"
    y "「一开……始？」"
    show charal li04 #李金凡立绘|微笑|近
    with dissolve
    voice "audio/voice/037092.ogg"
    j "「对，一开始。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037093.ogg"
    j "「因为高考，就是这么一种选拔机制。」"
    voice "audio/voice/037094.ogg"
    j "「你看高考每年都有分数线，但这个分数线其实它不是一个绝对值，它是相对的。」"
    voice "audio/voice/037095.ogg"
    j "「这个学校报的人多了，分数线就拉高，人少了呢，就会变低。怎么变化要看名额数量，而不是定死了一个分数。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037096.ogg"
    j "「所以说，虽然学习是自己的事，但考试，本质上还是和别人在竞争。」"
    voice "audio/voice/037097.ogg"
    j "「而竞争，显然就是坚韧和自信的人更有优势。」"
    voice "audio/voice/037098.ogg"
    j "「所谓物以类聚、人以群分，其实不是樱华这样的学校更能培养这种气质，而是有这种气质的人，最后都考上了樱华。」"
    y "「……」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037099.ogg"
    j "「这也是我想跟你说的第一个重点。」"
    voice "audio/voice/037100.ogg"
    j "「我想说的是啊，不管你最终决定是复读还是去百薇，你都需要去尽快地培养这种气质。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037101.ogg"
    j "「你说之前是跟着其他人的步伐走下来的，这很好，榜样的力量是无穷的嘛！身边有这么一个人是很幸运的事，他们就是所谓的自发光体，照亮自己、指引别人。」"
    voice "audio/voice/037102.ogg"
    j "「但是现在，就剩你一个人了。你可能不知道目的地在哪儿、有多远、还有没有机会；你也不知道自己还有多少体力，够不够走得到那里，甚至是够不够从半道折回来。」"
    voice "audio/voice/037103.ogg"
    j "「你越走，就越累，心里也越没谱，然后就越想放弃。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037104.ogg"
    j "「这是人之常情，可能大多数人都是这样。」"
    voice "audio/voice/037105.ogg"
    j "「但是，我认为，你可以换一个角度来看待自己。」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037106.ogg"
    j "「你……真的觉得自己就是那个『大多数人』里面的一员吗？」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037107.ogg"
    j "「你可能自己没意识到这一点啊，尤其是你身边还有个特别厉害的人，可能所有人的注意力都被那个人给吸引了。」"
    voice "audio/voice/037108.ogg"
    j "「但是你想想，你敢往樱华报，甚至非一志愿都能达到百薇的分数线……」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037109.ogg"
    j "「你还能算是普通的考生吗？」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037110.ogg"
    j "「咱们都清楚老家是个什么情况……别说老家了，就算是全国的考生里面，你这个档次，也已经不是一般人了。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037111.ogg"
    j "「所以你为什么会觉得自己不够优秀呢？就像我刚才说的，考试，本质上是竞争，是和别人去比。」"
    voice "audio/voice/037112.ogg"
    j "「你已经很优秀了，为什么不能多一点点自信心呢？为什么不能相信自己可以继续坚持下去呢？」"
    voice "audio/voice/037113.ogg"
    j "「『自发光体』，别人做得，你为什么就做不得？」"
    voice "audio/voice/037114.ogg"
    j "「确实，接下来可能不会再有人继续去照亮你前行的道路了，但你可以自己给自己点上一盏灯啊！不是吗？」"
    voice "audio/voice/037115.ogg"
    j "「就像我刚才说的，我们这类人，优势就在于能拼、能熬，目标明确，想到就做、不懂就问、不对就改，而不是先去担心『我能不能做到』？『我投入了这么多会不会打水漂』？」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037116.ogg"
    j "「但如果你也能做到这些呢？」"
    voice "audio/voice/037117.ogg"
    j "「那样的话，你现在的这些问题，还会是问题吗？」"
    y "「……」"
    y "「嗯……」"
    show charal li05 #李金凡立绘|开心|近
    with dissolve
    voice "audio/voice/037118.ogg"
    j "「行，那这碗鸡汤啊，我就算是给你灌完了。」"
    y "「啊……哈哈。」"
    show charal li04 #李金凡立绘|微笑|近
    with dissolve
    voice "audio/voice/037119.ogg"
    j "「这些话，你可能一时半会消化不完。不过心态这个东西，本来也不是一朝一夕就能扭转得过来的。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037120.ogg"
    j "「但是，这种事，能趁早就一定要趁早，越早调整过来越好。」"
    voice "audio/voice/037121.ogg"
    j "「剩下的，你回头再细想吧，这个问题啊，咱们就先说到这里。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037122.ogg"
    j "「接下来，我再跟你说一些更现实一点的问题。」"
    voice "audio/voice/037123.ogg"
    j "「我为什么推荐你尽量往樱华考。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037124.ogg"
    j "「其实你要说大学的水平，百薇并不差，就算现在落魄了一点，那也得是和『top5』这类学校去比。」"
    show charal li04 #李金凡立绘|微笑|近
    with dissolve
    voice "audio/voice/037125.ogg"
    j "「当然了，说是『top5』，其实全算下来可能有十多所吧。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037126.ogg"
    j "「但总而言之啊，人家也是国内一流的大学，有些专业依然是国内顶尖的，其实比排名靠前的那些大学都更好。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037127.ogg"
    j "「但是，我依然建议你，有机会的话，尽量来樱华。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037128.ogg"
    j "「为什么呢？因为这不单是大学的问题，它更是百薇和樱华两座城市之间的差距问题。」"
    voice "audio/voice/037129.ogg"
    j "「有人可能会觉得这种说法比较嫌贫爱富，不过这就是确实存在的现实啊——」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037130.ogg"
    j "「在樱华，你所能见到的新鲜事物，远比你在百薇要多，要早。」"
    voice "audio/voice/037131.ogg"
    j "「这一点很重要，非常重要。」"
    voice "audio/voice/037132.ogg"
    j "「我可以说，眼界的重要性，远远超出你之前的想象。」"
    y "「『眼界』……」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037133.ogg"
    j "「你觉得人类文明之所以可以不断地进步，依靠的是什么？」"
    y "「啊？」"
    voice "audio/voice/037134.ogg"
    j "「是『归纳』和『演绎』。」"
    voice "audio/voice/037135.ogg"
    j "「人类通过在实践中的积累和总结，抽象出某一类事物的共同特征，再以此为基础，推导出新情况下的结论。」"
    voice "audio/voice/037136.ogg"
    j "「可以说，整个人类就是在不断地重复着『归纳』和『演绎』，才成就了今天的文明。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037137.ogg"
    j "「而『归纳』，就是这里面最重要的第一步。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037138.ogg"
    j "「你看啊，咱们今天做的这个智能监控的采样，就是在收集你的各种姿态，然后通过深度学习来进行归纳，进而追求在未来的应用场景里，可以正确判断任何一个陌生人的行为类型。」"
    voice "audio/voice/037139.ogg"
    j "「当然了，机器学习，无论是什么算法，都是依靠海量的数据样本来提高正确率，而人类的大脑就不用这么多的样本，效率要高很多。」"
    voice "audio/voice/037140.ogg"
    j "「但就算效率再高，也没有高到不需要样本的地步。」"
    voice "audio/voice/037141.ogg"
    j "「而眼界，或者说是见识，就是人所需要的『样本』。」"
    voice "audio/voice/037142.ogg"
    j "「它的开阔与否，决定了你思考问题时的范围。」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037143.ogg"
    j "「嗯……我还是打个比方吧。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037144.ogg"
    j "「你比如说啊，咱们以前会觉得老家的那种生活是天经地义的，就是那种安安稳稳的、慢悠悠的，也感觉不出什么不好，过得很满足。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037145.ogg"
    j "「但当你来到樱华，就会发现这里和老家完全不是一个样子。」"
    voice "audio/voice/037146.ogg"
    j "「你会看到很多人做更大的事情，挣更多的钱，过更多彩的生活。」"
    voice "audio/voice/037147.ogg"
    j "「要是再去一趟首都呢？或者说，有机会出个国，你肯定还会有更多不一样的体验。」"
    voice "audio/voice/037148.ogg"
    j "「而有了这些经历以后，你就会明白：这个世界是多元的，不是只有一种模式。」"
    voice "audio/voice/037149.ogg"
    j "「到那个时候，你再去看其他的城市、其他的国家，视角就不会再受到局限了，可以看得更广，理解得更深。」"
    voice "audio/voice/037150.ogg"
    j "「当你打破了自己的固有思维，思路就会更加地开阔，会发现更多的可能性，更具有创造性。」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037151.ogg"
    j "「所谓一生二，二生三，三生万物。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037152.ogg"
    j "「对吧？这种创造力的高低，将会决定你这个人的上限。」"
    voice "audio/voice/037153.ogg"
    j "「而你越早走出这一步，提升的空间就越大。」"
    voice "audio/voice/037154.ogg"
    j "「所以，虽然说你四年以后，等本科毕业了再来读研也未尝不可，但是如果条件允许的话，我还是觉得你早点来会更好一些。」"
    j "「……」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037155.ogg"
    j "「当然，还有一点。」"
    voice "audio/voice/037156.ogg"
    j "「那就是谁都不知道……你最终能不能达到这个上限，什么时候才能达到这个上限。」"
    voice "audio/voice/037157.ogg"
    j "「有的人一出道就走上巅峰，而大器晚成的人也多得是。」"
    voice "audio/voice/037158.ogg"
    j "「但是，无论是哪一种，他们有一个共同的特点，那就是都提前做好了准备，才能在机遇来的时候，去伸手抓住它。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037159.ogg"
    j "「这里面，『准备』和『机遇』，缺一不可。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037160.ogg"
    j "「所以说为什么大家都喜欢往大城市跑呢？」"
    voice "audio/voice/037161.ogg"
    j "「因为大城市，比方说，樱华，它恰好就是这么一个地方——既能让你做好充分的准备，又能给你提供足够的机遇。」"
    voice "audio/voice/037162.ogg"
    j "「而相比之下，百薇毕竟地处西北，这方面无论如何是不如樱华的。」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037163.ogg"
    j "「我这么说，你能明白吗？」"
    y "「……嗯。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037164.ogg"
    j "「你还有什么疑问吗？」"
    y "「……」"
    y "「有。」"
    show charal li04 #李金凡立绘|微笑|近
    with dissolve
    voice "audio/voice/037165.ogg"
    j "「嗯？你说。」"
    y "「师兄你……当初是为了什么来樱华的呢？」"
    voice "audio/voice/037166.ogg"
    j "「嗯……我啊。」"
    show charal li05 #李金凡立绘|开心|近
    with dissolve
    voice "audio/voice/037167.ogg"
    j "「怎么说呢，我这个人啊，从小就喜欢琢磨东西。小的时候，大人问你长大了想干什么，我永远说是科学家。」"
    show charal li04 #李金凡立绘|微笑|近
    with dissolve
    voice "audio/voice/037168.ogg"
    j "「这一般的孩子，岁数大一点了可能就把小的时候说的这些都给忘光了，但我就比较奇葩，从小说到大，一直都没断过这个念头。」"
    voice "audio/voice/037169.ogg"
    j "「好在我的成绩一直也还不错，别的不敢说，起码在咱们那儿，算是矬子里拔将军了。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037170.ogg"
    j "「就这么着，我考到了这儿。」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037171.ogg"
    j "「你要说那么多大学，为什么我偏偏要选樱华？」"
    show charal li05 #李金凡立绘|开心|近
    with dissolve
    voice "audio/voice/037172.ogg"
    j "「哎，你别看我现在跟你说了这么多啊，好像我有多深思熟虑似的。」"
    voice "audio/voice/037173.ogg"
    j "「其实我当初根本没想那么多，哪有什么为什么啊，我就是报了一个我自己觉得能考上的最好的学校。」"
    show charal li04 #李金凡立绘|微笑|近
    with dissolve
    voice "audio/voice/037174.ogg"
    j "「哎呀，不过也很庆幸，自己当时的选择没有错。」"
    voice "audio/voice/037175.ogg"
    j "「樱华是一个足够广阔的舞台，它能够承载各种各样的人和各种各样的梦想。」"
    voice "audio/voice/037176.ogg"
    j "「虽然，自己现在还是和小时候想象的那种『科学家』不太一样的吧……」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037177.ogg"
    j "「不过我还是可以说，自己走到了这条路上，正在实现自己儿时的梦想。」"
    y "「……嗯。」"
    voice "audio/voice/037178.ogg"
    j "「当然啦，这条路也不是那么好走的。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037179.ogg"
    j "「樱华的机会多，但是竞争也就更激烈，你想啊，千军万马挤独木桥，最后能不能成功，能不能在这里站稳脚跟，都不好说。」"
    voice "audio/voice/037180.ogg"
    j "「但是我提前来了，就多一分准备，多一分优势，也多一分希望。」"
    y "「这样啊……」"
    y "「师兄你也是打算在未来一直留在樱华的吗？」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037181.ogg"
    j "「嗯……当然啊。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037182.ogg"
    j "「有条件的话，当然要留下来。」"
    voice "audio/voice/037183.ogg"
    j "「就像我刚才说的，大城市的优势，始终是小地方，尤其是偏远地区所无法比拟的。」"
    voice "audio/voice/037184.ogg"
    j "「既然已经走到了这里，那当然是要尽可能地跟上队伍，不能又被甩回去。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037185.ogg"
    j "「当然这也很难啊……一个外来者想在这样的大城市扎下根来，那可是需要很多的资源的。」"
    voice "audio/voice/037186.ogg"
    j "「包括时间，包括金钱。」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037187.ogg"
    j "「唉，别的不说了啊，你看我要想留在樱华，房子就先是个大问题。」"
    y "「呃……」"
    show charal li04 #李金凡立绘|微笑|近
    with dissolve
    voice "audio/voice/037188.ogg"
    j "「当然这倒不单是我自己的问题啊，就算是樱华本地人，你让他们再多买一套房，那也是很困难的。」"
    y "「哪怕是您这样的博士？」"
    show charal li05 #李金凡立绘|开心|近
    with dissolve
    voice "audio/voice/037189.ogg"
    j "「对啊。」"
    show charal li04 #李金凡立绘|微笑|近
    with dissolve
    voice "audio/voice/037190.ogg"
    j "「博士也只是个学历，又不能直接变现。」"
    j "「……」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037191.ogg"
    j "「现实啊，是很残酷的。」"
    voice "audio/voice/037192.ogg"
    j "「上一个好的大学，并不是说你就成功了。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037193.ogg"
    j "「就像我刚才说过的那样，你最终能不能达到自己的上限？」"
    voice "audio/voice/037194.ogg"
    j "「除了年少成名、大器晚成这两种情况之外，一辈子籍籍无名，始终怀才不遇的人，那也是多得数不清的。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037195.ogg"
    j "「上大学本身并不是阶层的跨越，它只是支撑你去追求成功的一个基础。」"
    voice "audio/voice/037196.ogg"
    j "「很多时候，其实就只是让你能够找到一份比较体面的工作而已。甚至这几年大学扩招之后，大学生的含金量变低，有些专业连工作都不好找了。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037197.ogg"
    j "「所以到了最后，绕了一圈还是回到了刚才的那个问题。」"
    voice "audio/voice/037198.ogg"
    j "「选拔机制，人和人的竞争。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037199.ogg"
    j "「同样的基本条件，你比别人强在哪里？」"
    voice "audio/voice/037200.ogg"
    j "「你又怎么保障这个『强』能落到实处？」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037201.ogg"
    j "「你早晚要面对这些问题的。所以啊，早做准备。」"
    y "「……嗯。」"
    y "「那，师兄，我能问您最后一个问题吗？」"
    show charal li02 #李金凡立绘|疑惑|近
    with dissolve
    voice "audio/voice/037202.ogg"
    j "「嗯？」"
    y "「这里的竞争这么激烈，您……就一点没考虑过放弃吗？」"
    voice "audio/voice/037203.ogg"
    j "「这个嘛……」"
    show charal li04 #李金凡立绘|微笑|近
    with dissolve
    voice "audio/voice/037204.ogg"
    j "「怎么说呢，心情低落的时候肯定有，胡思乱想的时候也不少，但是等那股劲过去，等我回到正轨来以后……」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037205.ogg"
    j "「没有。」"
    y "「为什么？」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    j "「……」"
    voice "audio/voice/037206.ogg"
    j "「逆水行舟嘛，当然很不容易啊。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037207.ogg"
    j "「来到樱华，和其他先天条件比我们好很多的人竞争，真的是很难。」"
    voice "audio/voice/037208.ogg"
    j "「这个世界上永远不缺少天才和努力的人，甚至努力的天才也很多。」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037209.ogg"
    j "「越是这样的大城市，这样的人就越多，马太效应嘛。」"
    voice "audio/voice/037210.ogg"
    j "「不过虽然很难，但大学……已经是我们这些从小地方出来的人，所能拥有的最好的、也是最公平的起点了。」"
    voice "audio/voice/037211.ogg"
    j "「前面的十八年，我们的起点就是自己的父母，这是先天条件。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037212.ogg"
    j "「但是高考，咱们国家的高考，是你人生中第一次、可能也是最后一次可以让你无视阶层差异的机会。」"
    voice "audio/voice/037213.ogg"
    j "「在这场考试里，只要你足够好，那无论你的竞争对手有什么背景，他最多就是给自己另辟蹊径，新开一条路出来自己走，但他不会强行抢你的路。」"
    voice "audio/voice/037214.ogg"
    j "「这样的机会，为什么不好好把握住呢？」"
    j "「……」"
    show charal li01 #李金凡立绘|普通|近
    with dissolve
    voice "audio/voice/037215.ogg"
    j "「而且，还有一点。」"
    voice "audio/voice/037216.ogg"
    j "「我们的起点是父母，而我们呢，早晚也会为人父母。」"
    voice "audio/voice/037217.ogg"
    j "「虽然说，所谓条条大路通罗马，但有的人需要拼死拼活，而有的人一出生就在『罗马』。」"
    voice "audio/voice/037218.ogg"
    j "「现在，我们拼死拼活，到了『罗马』。」"
    show charal li03 #李金凡立绘|皱眉|近
    with dissolve
    voice "audio/voice/037219.ogg"
    j "「那我为什么不努力留下，好让我的下一代……」"
    voice "audio/voice/037220.ogg"
    j "「也一出生，就在『罗马』呢？」"
    scene bg black #黑屏
    with fade
    pause 1.0
    scene bg b16a #实验室|打光
    with fade
    nvl show
    nvl_narrator "李师兄给我讲了很多。"
    nvl_narrator "而在谈完这些话之后，他倒反而有些不知所措起来，似乎觉得刚才强拖着我来帮忙，不甚合适。"
    nvl_narrator "不过，在我的强烈要求之下，我们还是继续完成了后续的一系列实验。"
    nvl clear
    scene bg b14 #大学校区
    with fade
    nvl_narrator "中午，完成了实验的我们，在樱大的食堂吃了一顿风味十足的便饭。"
    nvl_narrator "有别于西北地区的牛肉面，这里的葱油拌面给我留下了深刻的印象。"
    nvl clear
    nvl_narrator "随后，李师兄带着我在校区里到处参观。有了他的指引，的确是比自己一个人没头苍蝇一般乱转要有效率得多了。"
    nvl_narrator "一路上，我们又聊了很多。"
    nvl_narrator "聊大学，聊樱华，聊家乡……"
    nvl clear
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    nvl hide
    "……{p}…………"

    play sound "audio/sound/ambientnoise03.ogg" fadein 1.5 loop #傍晚环境噪音
    scene bg b13a #大学校门|傍晚
    with fade
    "傍晚，李师兄送我出了学校。"
    "告别之后，我向车站的方向前行。"
    "偶然回头看了一眼，发现留在原地的李师兄，正张开双臂，迎接从另一个方向朝他走去的一位年轻女性。"
    "两人开心地相拥，随后牵着手，朝着与我不同的方向走远了。"
    "那……是他的恋人吧？"
    "他们之间，又会有怎样的故事呢……"
    "我笑了笑，轻轻摇摇头，转身离去。"
    stop sound fadeout 3.0

    scene bg black #黑屏
    with fade
    "……{p}…………"
    play sound "audio/sound/ambientnoise04.ogg" fadein 1.5 loop #白天环境噪音
    scene bg b12 #樱华市
    with fade
    "第三天，也是我在樱华市停留的最后一天。"
    stop sound fadeout 3.0
    "这一天，我去了海边。"
    scene bg b17 #海边
    with fade
    play sound "audio/sound/ambientnoise14.ogg" fadein 1.5 loop #海边环境噪音
    nvl show
    nvl_narrator "这是我人生中第一次面对真实的大海。"
    nvl_narrator "从小在黄河边上生活的我，自诩对水并不陌生，也曾以滚滚东去的黄河自傲。"
    nvl_narrator "惊涛澎湃，万丈狂澜，我曾以为黄河已经足以担得起一切对「水」的形容。"
    nvl_narrator "然而，当我站在大海的脚边时，我才发现，那真的……不一样。"
    nvl_narrator "尽管，眼前的海是那么的平静，但我依然明白，她的体量、她所蕴藏的力量，都远远不是任何江河所能企及的。"
    nvl clear
    scene bg b17 #海边
    nvl hide
    show textblack
    with dissolve
    show text 7-01 at truecenter
    with dissolve
    pause
    hide text
    with dissolve
    hide textblack
    with dissolve
    scene bg b17 #海边
    "大海，无边无垠、烟波浩渺。"
    "而在海天之上，有成群的海鸟，正在自由地翱翔。"
    play audio "audio/sound/effect33.ogg" noloop
    bird2 "「啾——」"
    "偶尔，会有几只降落到我的附近，也得以让我更加清楚地看到它们的细节。"
    y "「……」"
    y "「果然……是不一样的啊。」"
    "海边的鸟，与我所见惯的那些水鸟和林鸟都截然不同。"
    "为了适应海边的生活，它们的进化方向与其他鸟类有着相当巨大的区别。"
    "而这样的进化，也让它们的迁徙，成为普通候鸟难以想象的长途跋涉。"
    "听说，有许多的海鸟，在迁徙的时候，需要跨过大洋、跨过赤道，从北半球飞到南半球去越冬。"
    "其中的佼佼者，甚至会从北极飞到南极，一生往返其间，永无止境地追逐着夏天。"
    with dissolve
    y "「……」"
    "算起来，再过一个月左右，候鸟就该开始南迁了。"
    "冬、夏候鸟可能会在同一个地点交汇的时刻，一年中仅有两次。不知道那个时候，这里会是一个怎样的场面。"
    "但……我等不到候鸟归来的季节了。"
    "明天，我就会离开这里，返回家乡。"
    "而在那时候，会在这里看到这些的，是梁芷柔。"
    "一个月以后的我们，或许还会在同一个时间，朝着同一个方向，目送那些迁徙的候鸟离去。"
    "只是，那时的我们，眼中的风景必然已经不同了。"
    stop sound fadeout 3.0

    scene bg b17 #海边
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
    y "「……」"
    "我闭上眼睛，扪心自问。"
    "如果我这一次退缩了……"
    "那么，在未来，我真的还能鼓起勇气再次前行吗？"
    "等到大学毕业以后？"
    "那个时候的我，就一定能够来到这里吗？"
    "我还会不会想要来这里？"
    "会不会找一个新的借口，再一次，轻易地说服自己留在原地……直到最后，永远地放弃？"
    scene bg b17 #海边
    with fade
    play sound "audio/sound/ambientnoise14.ogg" fadein 1.5 loop #海边环境噪音
    play audio "audio/sound/effect33.ogg" noloop
    bird2 "「啾——」"
    "睁开眼睛，看到身边落下了一只海鸟。"
    y "「咦……」"
    "是个没见过的品种。"
    "不是附近常见的那种海鸟，数量也只有这一只。"
    y "「你是怎么搞的呀？你的同伴呢？」"
    bird2 "「啾——」"
    "小巧的海鸟鸣叫着回应我的问询。"
    "大概是因为我坐着没有动，小鸟似乎并没有太过警觉。"
    "一人一鸟就这样对视了片刻。"
    bird2 "「啾——」"
    "初步判断眼前的灵长类动物没什么威胁，鸟儿开始蹦蹦跳跳地在附近觅起食来。"
    y "「……」"
    "我继续盯着这只与众不同的海鸟。"
    "不是这里的夏候鸟，也不怎么怕人……是留鸟吗？"
    y "「不对……」"
    "数量不对，留鸟通常成群结队生活。"
    "那样的话……"
    y "「是迷鸟，或者……」"
    y "「……是春天的时候，没来得及往北飞的冬候鸟？」"
    scene bg b00 #天空
    with fade
    "偶尔会有这种情况发生。"
    "因为天气恶劣等因素，在迁徙过程中偏离了航线，飞到了陌生地区的候鸟。"
    "或者因为各种原因没能进行迁徙，迫不得已停在原地成为留鸟的。"
    "曾经，这样的鸟儿往往会因为捕食环境的变化而无法继续生存。"
    "不过，如今这个时代，人类城市中的迷鸟想要获得食物并不困难。"
    "只要气候不过于苛刻，它们还是有相当的几率可以活下来的。"
    scene bg b17 #海边
    with fade
    y "「小家伙，你以后打算怎么办啊？」"
    y "「如果你熬过了这个冬天，到了明年，你是会重新走上迁徙的旅途呢，还是就这样继续留在这个衣食无忧的地方呢？」"
    bird2 "「……」"
    play audio "audio/sound/effect33.ogg" noloop
    bird2 "「啾——」"
    scene bg b00a #天空|候鸟"
    with fade
    "海鸟没有理会我的喃喃自语，它像是突然厌倦了在我这样的人的身边，一声长鸣之后，舞动双翼冲向了天空。"
    scene bg b00 #天空
    with dissolve
    "孑然一身，却无所畏惧，一往无前地飞向远方。"
    stop sound fadeout 3.0

    scene bg b17 #海边
    with fade
    "我目送着海鸟的离去。"
    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    "鸟儿不会给我答案，我只能，也必须自己做出回答。"
    "但其实，当我开始不断重复着向自己提出这个问题的时候，内心里那个答案就早已是注定的了。"
    "那个答案，我曾为之迷茫，也曾感到忐忑，乃至未敢直面。"
    "而现在，我已经不可以、也没必要再继续犹豫和拖延下去了。"
    "心中的期望、未来的道路、利弊的权衡，一切都已经清清楚楚地摆在了眼前。"
    "此时此刻，终于到了我必须做出决定的时候了。"
    scene bg black #黑屏
    with fade
    pause 1.5
    scene bg b07 #快餐店
    show charaz lh01 #老师立绘|夏季|普通|近
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/017071.ogg"
    z "「有梦想是好事，但是，你也不能不考虑现实，对吧？」"
    scene bg b05 #湿地公园|夏
    show charad lg01 #书店店员立绘|普通|近
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/027017.ogg"
    d "「在我看来，樱华是一个冷漠的地方。」"
    scene bg b16a #实验室|打光
    show charal li03 #李金凡立绘|皱眉|近
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/037179.ogg"
    j "「樱华的机会多，但是竞争也就更激烈，你想啊，千军万马挤独木桥，最后能不能成功，能不能在这里站稳脚跟，都不好说。」"

    scene bg black #黑屏
    with fade
    pause 1.5

    scene bg b07 #快餐店
    show charaz lh02 #老师立绘|夏季|微笑|近
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/017125.ogg"
    z "「能去的话，我还是会去吧。」"
    scene bg b05 #湿地公园|夏
    show charad g01 #书店店员立绘|普通
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/027045.ogg"
    d "「我当年看了那一眼，就让我拼到了最后，一直拼到一点本钱都没有了，才不得不放弃。」"
    scene bg b16a #实验室|打光
    show charal li01 #李金凡立绘|普通|近
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/037210.ogg"
    j "「不过虽然很难，但大学……已经是我们这些从小地方出来的人，所能拥有的最好的、也是最公平的起点了。」"

    scene bg black #黑屏
    with fade
    pause 1.5

    scene cg08e1 #梁芷柔河边CG-5|顶脑门|微笑|CG08e1
    show memories #回忆滤镜
    with dissolve
    voice "audio/voice/005165.ogg"
    l "「我希望把这一切都烙在自己的记忆里，让我可以在未来回想起这里的时候，浮现出来的是一幅鲜活的画面，而不只是一个朦胧的印象。」"
    voice "audio/voice/005166.ogg"
    l "「在未来……我们一起回忆这段日子的时候。」"

    scene bg black #黑屏
    with fade
    pause 1.5

    scene bg b17 #海边
    with fade
    y "「……呵呵。」"
    "直面本心的这一刻，反而没有想象中的那么艰难。"
    "我甚至忍不住笑了起来。"
    "嘲笑我自己……庸人自扰。"
    scene bg black #黑屏
    with fade
    "……{p}…………"
    scene bg b12 #樱华市
    with fade
    "返乡的火车缓缓地驶离了樱华。"
    "随着时间的推移，窗外的景色不断变换。"
    "从秀美的江南水乡，变为坦荡的中原大地，再到厚重的黄土高坡。"
    scene bg b02 #城区|夏
    with fade
    "在快要回到家的时候，我收到了梁芷柔发来的短信。"
    "「我想和你好好地谈一谈。」"
    "或许是为了避免尴尬，她并没有直接拨打电话过来。"
    "不过，即便如此，我也感到很开心。"
    "至少，我还有机会弥补和修正我的过错。"
    "我飞快地发出了回复，很简单的一个字——"
    stop music fadeout 2.5

    scene bg black #黑屏
    with fade
    "「好」"

    play sound "audio/sound/transition.ogg" noloop
    scene trans t10 #转场 海边
    with fade
    pause

#8月22日。"
#梁芷柔前往樱华。"

    scene bg b18 #火车站
    with fade
    play music "audio/music/bgm01.ogg" fadein 1.5 #春～樱飞～
    "……"
    show chara f06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    voice "audio/voice/007118.ogg"
    l "「……哎！」"
    show chara f10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/007119.ogg"
    l "「这边这边！」"
    y "「哟！」"
    show chara f04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/007120.ogg"
    l "「哟什么哟啊，说了不让你来送了，还非来。」"
    y "「哎，这么重要的日子，我还是来吧。」"
    show chara f02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    voice "audio/voice/007121.ogg"
    l "「多麻烦啊，你还得专门跑到省城来……而且，亏你还能进得了站台？我爸妈都没进来。」"
    y "「这个嘛，我买了张最近一站的车票。」"
    show chara f04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/007122.ogg"
    l "「唉……你啊，让我说你什么好。」"
    show chara f05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/007123.ogg"
    l "「聪明劲全都用在奇怪的地方了。」"
    "面对大言不惭的我，梁芷柔一幅又好气又好笑的样子。"
    scene bg b00a #天空|候鸟"
    with fade
    "一晃时间到了八月下旬，今天是梁芷柔出发前往樱华市的日子。"
    "距离开学其实还有一个礼拜左右的时间，不过因为要配合樱华大学做宣传，梁芷柔的行程要略微提前几天。"
    scene bg b18 #火车站
    show chara f11 #梁芷柔立绘|夏季私服|微笑
    with fade
    y "「怎么样，要不要我帮忙放行李？」"
    voice "audio/voice/007124.ogg"
    l "「算了吧！总共也没多少东西，一个箱子就够了，我自己没问题的。」"
    y "「这么少啊，女生出门一般不都喜欢大包小包一大堆的吗？」"
    show chara f08a #梁芷柔立绘|夏季私服|担心1
    with dissolve
    voice "audio/voice/007125.ogg"
    l "「毕竟……不是只去一天两天啊。不可能什么都从这边准备。」"
    y "「……也是。」"
    y "「那，你……自己保重。」"
    show chara f05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/007126.ogg"
    l "「嗯。」"
    y "「车还有多久开？」"
    show chara f11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007127.ogg"
    l "「马上了，就这几分钟。」"
    y "「嗯……那你就上车吧。」"
    show chara f13a #梁芷柔立绘|夏季私服|疑惑1
    with dissolve
    voice "audio/voice/007128.ogg"
    l "「哎？嘻嘻……我还以为你既然买了票，会索性送我一站地呢，结果不是啊？」"
    y "「我倒是想，可惜这一站就要开一个多小时，返程的车还要等到下午，那样的话我今天就回不去县里了。」"
    show chara f04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/007129.ogg"
    l "「所以说啦，你这么大费周章地跑过来就是为了见这么一面啊，何苦呢？」"
    y "「是啊……」"
    y "「……」"
    show chara f13b #梁芷柔立绘|夏季私服|疑惑2
    with dissolve
    l "「……」"
    show chara f12a #梁芷柔立绘|夏季私服|羞涩1
    with dissolve
    voice "audio/voice/007130.ogg"
    l "「干……干嘛啦，这么盯着看。」"
    y "「就是想要来看看你啊……」"
    y "「毕竟，接下来这一年，恐怕都再见不到你了。」"
    show chara f12b #梁芷柔立绘|夏季私服|羞涩2
    with dissolve
    voice "audio/voice/007131.ogg"
    l "「啊……」"
    show chara f12a #梁芷柔立绘|夏季私服|羞涩1
    with dissolve
    voice "audio/voice/007132.ogg"
    l "「……嗯。」"
    "梁芷柔有些黯然地点点头。"
    scene bg black #黑屏
    with fade
    pause 1.0
    scene bg b05 #湿地公园|夏
    show chara c07b #梁芷柔立绘|夏季私服|消沉2
    show memories #回忆滤镜"
    with fade
    "回到县城以后，我和梁芷柔长谈了一次。"
    "看得出，梁芷柔是抱着几乎绝望的心态过来的。"
    "毕竟，在这之前的这么长时间里，我一直都处于杳无音信的状态，任谁都会觉得我是已经自暴自弃了。"
    "不过这一次，我开门见山的一句话，就堵住了梁芷柔之后的所有话语。"
    y "「我准备复读。」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    l "「——！」"
    y "「我不是在逞强，也不是一时的冲动。」"
    y "「这两天，我去了一趟樱华。」"
    y "「也去了樱华大学。」"
    y "「我见到了一些人，也亲身体会过了一些事情。」"
    y "「我认认真真地考虑过了。」"
    y "「我会再次以樱华为目标，而且不只是去到樱华这个地方，我要追求更高的目标。」"
    y "「如果，我是说如果，顺利的话……」"
    y "「一年以后……」"
    y "「你愿意再给我一次机会吗？」"
    y "「给这样的我一个机会……与你一起，追逐同一个梦想？」"
    scene bg b18 #火车站
    with fade
    y "「呵呵……」"
    show chara f04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/007133.ogg"
    l "「喂喂，想什么哪？笑得贼兮兮的。」"
    y "「呵……没什么。来，你也笑一笑嘛。」"
    show chara f13b #梁芷柔立绘|夏季私服|疑惑2
    with dissolve
    voice "audio/voice/007134.ogg"
    l "「嗯？为什么啊？」"
    y "「你还是笑起来最漂亮了，笑一个好不好？」"
    y "「我想记住你最漂亮的样子。」"
    show chara f12a #梁芷柔立绘|夏季私服|羞涩1
    with dissolve
    voice "audio/voice/007135.ogg"
    l "「啊……」"
    l "「……」"
    show chara f03 #梁芷柔立绘|夏季私服|生气
    with dissolve
    voice "audio/voice/007136.ogg"
    l "「哼！不要！」"
    y "「哎？为什么啊……」"
    show chara f04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/007137.ogg"
    l "「你说让我笑我就笑啊？你现在可还不是我的男朋友呢，我干嘛要听你的？」"
    y "「我还不是啊？」"

    show chara f03 #梁芷柔立绘|夏季私服|生气
    with dissolve
    voice "audio/voice/007138.ogg"
    l "「当然不是啦！我说的可是『给你一个机会』！」"
    stop music fadeout 2.5

    # TODO
    $ config.keymap = keymap_end
    $ renpy.clear_keymap_cache()
    $ renpy.run(Preference("auto-forward", "enable"))
    $ _dismiss_pause = False
    $ _skipping = False
    $ _rollback = False
    scene bg black #黑屏
    with fade
    pause 1.0
    scene bg b05 #湿地公园|夏
    show chara c05b #梁芷柔立绘|夏季私服|苦笑2
    show memories #回忆滤镜"
    with fade
    play music "audio/music/themepiano.ogg" fadein 1.5 #梦想天空 piano ver.
    voice "audio/voice/007139.ogg"
    l "「男生啊……有的时候真是，喜欢瞎钻牛角尖。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007140.ogg"
    l "「这还需要问吗？」"
    show chara c12b #梁芷柔立绘|夏季私服|羞涩2
    with dissolve
    voice "audio/voice/007141.ogg"
    l "「在你真正做出决定的那一刻，我的答案也就已经确定了呀。」"
    show chara c12a #梁芷柔立绘|夏季私服|羞涩1
    with dissolve
    l "「……」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007142.ogg"
    l "「你说，我要是高考发挥失常了，你觉得我会怎么做？你会因为我落榜而因此看不上我了吗？」"
    y "「这……」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/007143.ogg"
    l "「就是这样……就是这么简单的道理。」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007144.ogg"
    l "「嗳，雨潇。」"
    voice "audio/voice/007145.ogg"
    l "「你抬头。」"
    y "「嗯？」"
    scene bg b00a #天空|候鸟"
    show memories #回忆滤镜"
    with fade
    voice "audio/voice/007146.ogg"
    l "「看，有候鸟。」"
    y "「……嗯。」"
    voice "audio/voice/007147.ogg"
    l "「候鸟……夏候鸟和冬候鸟……」"
    voice "audio/voice/007148.ogg"
    l "「它们生活在同一片天空下，只是时间不同，难以相聚。」"
    scene bg b05 #湿地公园|夏
    show chara c01b #梁芷柔立绘|夏季私服|普通|侧面
    show memories #回忆滤镜"
    with fade
    l "「……」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007149.ogg"
    l "「我呢，曾经以为自己可能只是一只夏候鸟。」"
    show chara c05a #梁芷柔立绘|夏季私服|苦笑1
    with dissolve
    voice "audio/voice/007150.ogg"
    l "「而你，也曾经……甚至现在还在觉得自己可能只是一只夏候鸟。」"
    show chara c01b #梁芷柔立绘|夏季私服|普通|侧面
    with dissolve
    voice "audio/voice/007151.ogg"
    l "「虽然我们的确是从夏候鸟的起点去出发，但是……」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007152.ogg"
    l "「只有自己，才能决定自己究竟是什么。」"
    voice "audio/voice/007153.ogg"
    l "「你知道吗？除了夏候鸟和冬候鸟以外，这世界上还有一类候鸟。」"
    voice "audio/voice/007154.ogg"
    l "「它们可以和冬候鸟在一起繁殖，再去和夏候鸟一起过冬。」"
    voice "audio/voice/007155.ogg"
    l "「它们是……过境鸟。」"
    show chara c01b #梁芷柔立绘|夏季私服|普通|侧面
    with dissolve
    l "「……」"
    voice "audio/voice/007156.ogg"
    l "「我已经决定好，不只做一只夏候鸟，而是让自己成为过境鸟。」"
    voice "audio/voice/007157.ogg"
    l "「而你呢？」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007158.ogg"
    l "「你相信自己是和我一样的过境鸟吗？」"
    y "「我……」"
    show chara c10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/007159.ogg"
    l "「我相信喔！」"
    show chara c11 #梁芷柔立绘|夏季私服|微笑
    with dissolve
    voice "audio/voice/007160.ogg"
    l "「我，相信你。」"
    scene bg black #黑屏
    with fade
    pause 1.0
    scene bg b18 #火车站
    show chara f03 #梁芷柔立绘|夏季私服|生气
    with fade
    y "「哎呀，求求你了，听我的，笑一笑，好不好？」"
    voice "audio/voice/007161.ogg"
    l "「不好！」"
    y "「那你说，我怎么做才能让你笑一个？」"
    show chara f04 #梁芷柔立绘|夏季私服|无奈
    with dissolve
    voice "audio/voice/007162.ogg"
    l "「怎么都不能。如果现在就给你甜头的话，会让你怠惰的。」"
    show chara f09 #梁芷柔立绘|夏季私服|坏笑
    with dissolve
    voice "audio/voice/007163.ogg"
    l "「所以要放到一年以后。等到明年的这个时候，我们在樱华再讨论这个话题吧！」"
    show chara f10 #梁芷柔立绘|夏季私服|开心
    with dissolve
    voice "audio/voice/007164.ogg"
    l "「就像我们约好的那样，好不好？」"
    y "「啊……」"
    y "「……嗯。」"
    y "「是啊，约好的。」"
    "对着梁芷柔饱含期待的目光，我一边点头回应，一边却又感到稍许黯淡。"
    y "「一年，以及……」"
    y "「……就只等我『一』年。」"
    show chara f06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    l "「——！」"
    stop music fadeout 2.5

    "是的。"
    "我在向她提出请求的同时，也为自己的这个请求加上了一个限制。"
    scene bg b05 #湿地公园|夏
    show chara c12a #梁芷柔立绘|夏季私服|羞涩1
    show memories #回忆滤镜"
    with fade
    y "「请你等我一年，但……」"
    y "「如果……我这一次还是失败了……」"
    y "「那就，请你忘掉我吧。」"
    show chara c06 #梁芷柔立绘|夏季私服|吃惊
    with dissolve
    pause 0.5
    scene bg black #黑屏
    with fade
    pause 1.0
    scene bg b18 #火车站
    show chara f06 #梁芷柔立绘|夏季私服|吃惊
    with fade
    "这是我必须要做的一个决断。"
    "既是为了她，也是为了我自己。"
    "一方面，我不可能去让她年复一年地等我。"
    "这不光是我脸皮够不够厚的问题。毕竟，从实际角度来说，这本来也不可能做得到。"
    "而另一方面，则是我给自己的一个鞭策——"
    "一年之后，不成功、便成仁。"
    show chara f02 #梁芷柔立绘|夏季私服|皱眉
    with dissolve
    l "「……」"
    show chara f03 #梁芷柔立绘|夏季私服|生气
    with dissolve
    voice "audio/voice/007165.ogg"
    l "「你怎么又说这种话！？」"
    y "「因为……」"
    show chara lf02 #梁芷柔立绘|夏季私服|皱眉|近
    with dissolve
    voice "audio/voice/007166.ogg"
    l "「我不管，反正你不许再说这个了！」"
    y "「呃……」"
    "不过，这句话貌似是把梁芷柔刺激得不轻。"
    "在河边的时候，就差点情绪失控，当时还用力捶了我一顿。"
    "虽然已经过去几天了，看她这意思，是又要爆炸啊……"
    y "「可是……」"
    show chara lf03 #梁芷柔立绘|夏季私服|生气|近
    with dissolve
    voice "audio/voice/007167.ogg"
    l "「没有可是！你一定能做到，我相信你！所以！」"
    y "「是，我知道，可是凡事都有意外，就好像我这次高考一样……」"
    voice "audio/voice/007168.ogg"
    l "「你还说！是不是又想让我打你一顿啊？」"
    y "「那个，不是，我……」"
    "原本还想要再解释两句，结果看到梁芷柔的巴掌都抬起来了。"
    "——这是真的要打啊？"
    scene bg black #黑屏
    with fade
    "下意识地闭上了眼睛。"
    "梁芷柔的手掌印在了我的脸颊上。然而，却不是预想之中的痛感。"
    "而是，温柔地……轻轻抚住。"
    play music "audio/music/theme.ogg" fadein 5 noloop #梦想天空 人声 ver.
    scene cg11 #火车站吻别CG|CG11
    with fade
    l "「……」"
    y "「……」"
    "嘴唇……传来了温软的触感。"
    "大脑一片空白。"
    "一时间，根本没法理解眼前发生的事情。"
    voice "audio/voice/007169.ogg"
    l "「……嘤。」"
    y "「……」"
    scene bg b18 #火车站
    with fade
    show chara lf12b #梁芷柔立绘|夏季私服|羞涩2|近
    with dissolve
    l "「……」"
    y "「……你，你这是……」"
    show chara lf12a #梁芷柔立绘|夏季私服|羞涩1|近
    with dissolve
    voice "audio/voice/007170.ogg"
    l "「这样就可以了。」"
    y "「什……」"
    voice "audio/voice/007171.ogg"
    l "「我给你下了一个诅咒。」"
    voice "audio/voice/007172.ogg"
    l "「就像你说的那样，一年以后，如果你没有来樱华找我的话，我会想办法忘掉你。」"
    show chara lf01a #梁芷柔立绘|春季私服|普通|正面|近
    with dissolve
    voice "audio/voice/007173.ogg"
    l "「我会忘掉有关你的一切，努力学习、努力工作、努力生活，努力过好属于我的每一天。」"
    voice "audio/voice/007174.ogg"
    l "「我说到做到。」"
    y "「……」"
    voice "audio/voice/007175.ogg"
    l "「但是，留在这里的你，会被这个诅咒缠住，永远都没办法忘掉我。」"
    voice "audio/voice/007176.ogg"
    l "「哪怕是到了很多年以后，也会让你偶尔回想起来，想着『如果当年自己可以更努力一点……』什么的。」"
    show chara lf04 #梁芷柔立绘|春季私服|无奈|近
    with dissolve
    voice "audio/voice/007177.ogg"
    l "「……让你后悔一辈子。」"
    voice "audio/voice/007178.ogg"
    l "「所以。」"
    show chara lf01a #梁芷柔立绘|春季私服|普通|正面|近
    with dissolve
    voice "audio/voice/007179.ogg"
    l "「不想变成这个样子的话，你就不可以失败。」"
    voice "audio/voice/007180.ogg"
    l "「你一定能追上我，你一定要追上我……一定会追上我的。」"
    voice "audio/voice/147003.ogg"
    m "「本次列车即将离开百薇东站，请您再次检查自己的车票是否与本次列车相符，带小孩的旅客，请照看好孩子，注意安全。列车就要开车了。」"
    y "「……」"
    l "「……」"
    show chara lf11 #梁芷柔立绘|春季私服|微笑|近
    with dissolve
    voice "audio/voice/007181.ogg"
    l "「我……在那里……」"
    scene bg black #黑屏
    with fadehold
    voice "audio/voice/007182.ogg"
    show text 7-02 at truecenter
    with dissolve
    stop music fadeout 2.5
    pause 0.5 # pause
    scene bg black #黑屏
    with fade
    pause 5.0
    if not debug:
        $ config.keymap = keymap_release
    else:
        $ config.keymap = keymap_debug
    $ renpy.clear_keymap_cache()
    $ renpy.run(Preference("auto-forward", "disable"))
    $ _dismiss_pause = True
    $ _skipping = True
    $ _rollback = True

#尾声

    play sound "audio/sound/ambientnoise01.ogg" fadein 1.5 loop #河边环境噪音

    scene cg12a #叶雨潇打电话CG-1|CG12a"
    with fade
    "漫步河滨，放眼望去，但见河水滔滔，奔流而下，裹挟着泥沙，仿佛要将天地间的一切都染作昏黄。"
    "然而，在这其中，却有一片湿地居于岸边，为这无尽的昏黄，增添了一抹鲜艳的绿色。"
    "数不清的草甸、芦苇，以及槐树、柳树和白杨。"
    "在这个夏末秋初的时节，它们用尽全力展现着自己的活力。"
    "随手捡起一片落叶，仰望天空。"

    scene bg b00 #天空
    with fade

    "青空如洗，白云如练。"
    "空气中卷着些许潮湿的味道。"
    "江浪声，风声，草木枝叶的哗哗声。"
    stop sound fadeout 3.0

    scene cg12a2 #叶雨潇打电话CG-1|手机|CG12a2
    with fade
    "掏出手机，打开通讯录。"
    scene cg12a3 #叶雨潇打电话CG-1|手机|通讯录|CG12a3
    with dissolve
    "在许许多多的人名中，翻出其中的一条。"
    scene cg12a4 #叶雨潇打电话CG-1|手机|通讯录|梁芷柔|CG12a4
    with dissolve
    "「梁芷柔」"
    "我凝视着这个名字，片刻。"
    "然后——"
    play sound "audio/sound/effect34.ogg" noloop
    pause 5.0
    stop sound

    voice "audio/voice/007183.ogg"
    "电话：「……喂？」"
    y "「是我——」"
    y "「我来了。」"

    scene cg12a1 #叶雨潇打电话CG-1|候鸟|CG12a1
    with dissolve
    "忽然，有一声嘶鸣，自天空响彻四野。"
    "我抬起头，看到有一道白影，从眼前一晃而过，朝着正南的方向，义无反顾地飞去。"
    "那是一只候鸟。"

    $ persistent.game_clear_times += 1

    scene bg black #黑屏
    with fade
    pause 3.0

    return
