# 这里可以define staff的角色

define temp = Character("叶雨潇", color="#ffffff", ctc_pause="ctc_pause_icon", ctc="ctc_icon")

# 这里是Staff剧情

label staff:

$ achievement.Sync()
$ persistent.chpt_staff_clear = True
if not achievement.has('CHPT_STAFF_CLEAR'):
    $ achievement.grant('CHPT_STAFF_CLEAR')

    # scene bg migrant #候鸟封面|调色
    scene bg migrant_old #候鸟封面|未调色
    with fade
    nvl show

    play music "audio/music/themepiano.ogg" fadein 5.0 #梦想天空 piano ver.

    nvl_narrator "您好，我们是KID Fans Club。"
    nvl_narrator "在这个部分，我们会向您介绍一些「候鸟」制作幕后的故事，以及部分主创人员的制作感言，希望能够借此让您更加全面地了解这部作品。"
    nvl_narrator "当然，首先还是要感谢您完整地读完了这个故事。不知道您对这部作品的评价如何呢？"
    nvl_narrator "如您所见，「候鸟」是一部现实主义题材的作品，这是我们在经历过一段时间的摸索过后，给这部作品定下的基调。这种比较偏向于写实的风格，往往会因为玩家的过往经历，而产生不同的感受——也许会觉得代入感很强，但也可能会完全无法产生共鸣，不知道您属于哪一种？但无论如何，您坚持读到了最后，这本身就是对我们的鼓励。"
    nvl clear
    nvl_narrator "那么，接下来就是正题了。"
    nvl_narrator "访谈的部分主要分为三块：第一部分由本作的主催「苍蓝的风」来向大家介绍「候鸟」制作幕后的故事，当然，也包括他挖坑多年的心路历程与最终完坑的感想；第二部分由原案「小雨潇潇」向大家介绍这个故事最初的创作经历；最后一部分则是由本作女主角的配音演员「酒儿」来给大家讲述她对角色的理解与认识，谈一谈是如何给梁芷柔这个角色注入灵魂的。"
    nvl clear

label choice:

    # scene bg migrant #候鸟封面|调色
    scene bg migrant_old #候鸟封面|未调色
    with dissolve
    nvl hide
    "现在，您可以通过我们在正篇中根本没有启用（笑）的选项功能，来选择您感兴趣的访谈内容："

menu:

    "主催「苍蓝的风」":
        jump blovewind

    "原案「小雨潇潇」":
        jump rain

    "配音演员「酒儿」":
        jump jiuer

    "退出访谈":
        jump end

label blovewind:

    # scene bg migrant #候鸟封面|调色
    # scene bg migrant_old #候鸟封面|未调色
    nvl_narrator "大家好，我是KID Fans Club站长、原创游戏组负责人苍蓝的风。"
    nvl_narrator "作为「候鸟」的主要制作人，我承担了主催、剧本、演出、配音导演等几方面工作，可以说，游戏里的每一份素材都有我的参与，也正因为如此，对于「候鸟」，对于这部自己投入了如此之多心血的作品，我其实很难在有限的篇幅里把对她的感想总结出来。"
    nvl_narrator "无论如何，还是让我从一切的开始说起吧。"
    nvl clear
    nvl_narrator "KID Fans Club是一个颇具年头的同人社团了，诞生于2002年，而作为它的创始人，我接触Galgame的时间还要更早一些。在那个资源和渠道尚不丰富、语言障碍几乎坚不可摧的年代，嗷嗷待哺的玩家是不挑食的，也几乎不存在什么「冷门作品」。但凡是代理商引入的作品，玩家们都进行了超饱和的咀嚼、乃至反刍，但即便如此，中文化的作品数量还是因为数量太过有限，根本不能满足玩家的需求。"
    nvl_narrator "汉化组也在如雨后春笋般诞生，但产能依旧跟不上。"
    nvl_narrator "于是，在这个时候，作为一个从初中开始写同人文的人，我那高涨的创作欲便开始蠢蠢欲动了——"
    nvl_narrator "我不想只等待别人的投喂，我想自己有产出，我想创作出一样的、乃至更好的……属于我们本土文化的作品。"
    nvl clear
    nvl_narrator "抱着这样的念头，我和伙伴们开始了一步一步的尝试。"
    nvl_narrator "最初是在2006年，我们打算循序渐进，先尝试制作一部KID作品的二创同人游戏，后来因为种种原因，拖了一年左右，最后无疾而终了。"
    nvl_narrator "第一次尝试的结果固然不尽人意，但我们也并没有就此浅尝辄止，反倒是更来劲了，打算吸取失败的经验，再接再厉，而且这次还要索性一步到位，直接上原创。"
    nvl_narrator "时任论坛管理员的小雨潇潇以他高中时期的一些亲身经历，改编出了「候鸟」的原案并交给了我，我也毫不客气地整理出了粗略的剧本大纲，然后在那个智能手机都还没有普及的年代，我俩顶着惊人的漫游费，利用长途电话沟通好了这部作品最初的基调，然后……就这样，开启了一场我们都始料未及的长征。"
    nvl clear
    nvl_narrator "是的，长征。"
    nvl_narrator "人生总是充满意外。"
    nvl_narrator "我俩谁都没想到这个坑会挖这么多年，更没想到的是，拖了这么多年之后，我俩居然还真的一起把这个坑给填上了。"
    nvl_narrator "「候鸟」最初创作的时候，我们其实只是想写一个几万字的小剧本，来一篇轰轰烈烈但没什么结果的青春伤痛恋爱文学，与其说是故事，不如说是散文。然而这个目标在最初的时候就出现了偏差——"
    nvl clear
    nvl_narrator "小雨潇潇写「候鸟」原案的时候，他是听了SHE的同名歌曲而诞生的灵感；但如果说到一首叫做「候鸟」的歌曲，对15年前的我而言，我当时根本就不听SHE，脑海里第一个浮现出来的，其实是王杰的那个版本，而王杰这个人的曲风吧……嗯，就很……苦逼。"
    nvl_narrator "于是在写「候鸟」初稿的时候，我基本上整个人都是陷于苦逼状态之中难以自拔的，而且我本身属于非常不喜欢也不擅长写Bad End的，这稿子写得就非常难受，怎么都抓不住那种感觉。开场的序幕因为有真实故事原型还算是写得比较顺畅，但没过多久就卡了壳，再难寸进，继而就陷入了长时间的停滞。"
    nvl clear
    nvl_narrator "现在想想，倒是不难明白问题在哪里——当时满脑子想的都是情绪表达，结果就是想写的东西全在天上飘着，根本落不了地，找不到足以用来承载和表演这些情绪的基石。这种情况下，能写得出来才怪。"
    nvl_narrator "总而言之，这坑就这么拖下去了。"
    nvl_narrator "好在我们手头也不是只有这一件事，社团的日常活动还在继续，不至于散伙。另外，随着年龄的逐渐增长，现实中牵扯的精力也越来越多，「候鸟」这个坑尽管一直都挂在心上，有时闲暇下来，还会再试图啃上那么几下，但在这种不得章法的状态下，终究还是难有进度，经常是搞两下搞不动，就又只能先放下了。"
    nvl clear
    nvl_narrator "这样，一直到了2013年。"
    nvl_narrator "那年，单位组织活动，拖着我们去看了一场电影，一场爱情电影。"
    nvl_narrator "这类题材我不怎么感兴趣，而且这部电影整体来说也确实很一般，本来我是昏昏欲睡的，但电影里突然出现了一个很小的桥段，一下子把我给触动了。"
    nvl_narrator "那就是一个特别贴近候鸟原案的桥段。如果原案故事正常结束，那么，后续的发展，几乎必然是电影中的那个桥段所展现出来的样子。"
    nvl_narrator "以往虚无缥缈、只存在于大纲设定之中的「候鸟」，在这个瞬间，突然就有了鲜明、清晰，乃至如同现实一般的画面感。"
    nvl clear
    nvl_narrator "从那一刻开始，我终于知道「候鸟」该怎么去写了。"
    nvl_narrator "大家所见到的现在这个「候鸟」的偏写实风格正是从这个时候开始定下的。而这个故事所要讲述的重点，也从这个时候开始有了根本的改变。"
    nvl_narrator "如前所述，我希望有朝一日能够写出属于我们自己的、本土文化的作品，而「候鸟」的故事大背景——高考，其实恰好就是这么一个绝佳的「本土文化」舞台。"
    nvl clear
    nvl_narrator "作为一个重要的分水岭，高考承载着近半数中、青年人的共同记忆，同时又是各地发展不平衡的一次集中展示。之前想要写的那种「毕业即分手」的伤痛，归根结底还是难以克服的「异地恋」与「前途差异」的一种体现。"
    nvl_narrator "但在最初几年，我其实一直在试图剥离这种大背景，把重点全都放在叶雨潇和梁芷柔两个人之间，想要细致入微地描写一个二人世界，这种思路之下，总会朝着无病呻吟的方向扭曲，不说南辕北辙吧，也终究「味儿不对」。"
    nvl_narrator "而自这次观影之后，我开始尝试着将他们融入这个舞台之中。表演的依旧是他们，但讲述的却是这个大背景——换句话说，这虽然依然是一个Galgame，但本质上，没准会更接近……传统文学？"
    nvl clear
    nvl_narrator "除了剧本之外，我对美术素材的需求也在这个阶段发生了改变。"
    nvl_narrator "在最早的计划中，梁芷柔的校服其实是非常标准的日式水手服——对，甚至都不是现在比较普遍的那种小西服，而是要更复古一些，更加接近那种昭和时代才常见的水手服，可以说是对二次元女高中生根深蒂固的刻板印象了。"
    nvl_narrator "而在创作方向发生改变以后，我也开始重新审视这些设定。恰好，在那之后不久，就有一部产生了很大影响的国产校园青春动画发布了预告样片，里面的人物，虽然脸是日系的画法，但衣着打扮却是典型的中国式校服，而且组合起来感觉还挺不错的。看过之后，我认真思考了一段时间，最终决定全盘重塑人物的形象。于是，梁芷柔的校服就变成了现在的这个样子。"
    nvl clear
    nvl_narrator "总而言之，从2013年开始，「候鸟」的创作才算是真正开始启动。"
    nvl_narrator "不过，哪怕找到了方向，想要写出能够让自己基本满意的作品，依旧是一件非常困难的事。倒不如说，因为这个大方向起得太高，写作的难度也随之增加上去了，还不如原来写卿卿我我来得容易。何况，三次元的干扰也一直都存在，甚至还在逐渐加大力度。"
    nvl_narrator "种种因素糅杂起来的结果就是，「候鸟」的初稿我磕磕绊绊写了三年才写完，而这第一版稿子，也基本是一个不可用的状态。"
    nvl_narrator "毕竟「候鸟」初稿中最早的文字甚至都是七八年前写的了，二十几岁到三十岁又是一个人文风比较容易变化的时候，结果就是剧本前后差异过大，完全搭不到一起，再加上经验不足，故事结构有不少问题，整体看下来就比较凌乱。"
    nvl clear
    nvl_narrator "这样不行，老老实实从头开始改吧。"
    nvl_narrator "于是三年之后又三年，花了与初稿几乎相同的时间，逐字逐句把剧本推翻重走了一遍之后，目前这一版「候鸟」的剧本终于基本定稿了。"
    nvl_narrator "新稿大刀阔斧地删改了不少东西，有一部分是直接砍掉了，有一部分则是重写。总的来说，主要调整了事件链结构，进一步捋顺了故事逻辑，并且大幅强化了配角们的作用——郑老师、书店店员和李金凡的戏份原本其实都比现在少很多，但在修订稿里则全部提到了比较重要的推动剧情的位置上，而哪怕是原本只有一两句台词的那些龙套，也都在修改过程中尽量让他们的谈吐变得更像是一个活生生的「人」。"
    nvl clear
    nvl_narrator "除了这些技术上的修订之外，还有一些则是因为这个坑拖得太久，乃至于现实政策都发生了巨大变化所不得不做出的改变。就比如最要命的一点，在故事原案诞生的年代，高考还是估分报志愿，但到了剧本写出来的时候，全国上下都已经完全变为了知分报志愿，整个结局部分的故事逻辑都要重写，就颇有一种「大人，食大便了」的悲痛感。"
    nvl_narrator "这么一路删删改改下来，剧本不减反增，从原案计划的几万字，到初稿完成时的12万字，再到终稿完成时的15万余字。最后，终于在2019年的双11那天，候鸟的剧本整体定稿了。"
    nvl clear
    nvl_narrator "剧本定稿之后，真正的考验才刚刚开始。"
    nvl_narrator "原因无他——该花钱了。"
    nvl_narrator "在2019年，BBS的时代早已过去，KID Fans Club在微博和B站开设了账号，但日常的业务主要还是做一些翻译方面的事，几乎没有什么原创方面的人才储备，曾经的人脉在经历了多年的消磨之后，也已经寥寥无几，靠原本的社团模式做同人游戏显然是不现实的，这种情况下只能全面转向商业约稿。"
    nvl_narrator "于是，喜忧参半的局面出现了：好消息是我和小雨潇潇都工作了不少年，总还算有点余财，不至于过分捉襟见肘；坏消息则是这钱该花多少，该怎么花，着实是两眼一抹黑，就感觉周围处处藏坑，指不定在哪儿就会踩上那么一脚。"
    nvl clear
    nvl_narrator "但……事到如今，也没什么好办法了，只能在危险的边缘疯狂试探。"
    nvl_narrator "然后就真的踩坑了。"
    nvl_narrator "而且还不止一次，可以说是一个接一个地踩，把一个萌新创作者可能因为经验不足踩到的坑，挨着个地趟了一遍——"
    nvl_narrator "CG约到过一张大翻车的邪神，自己作为审核未能及时调整，责任起码要扛一半；场景约得早了，后面因为人物画师变了几次，风格过于不搭，不得不换人重绘了一整套；与最初联络的CV在沟通方面出现了巨大的问题，最后只能分道扬镳，重新选人；压力过大导致一段时间失去画面感，根本写不出美术需求，耽误了工期；BGM约少了，不得不死线赶稿临时追加需求……"
    nvl_narrator "一路下来花了不少冤枉钱，还留下了一些精神创伤，可谓血泪史了。"
    nvl clear
    nvl_narrator "但，我终究还是坚持着走下来了，走到了最后，做完了这部作品。"
    nvl_narrator "就如同最开始说的那样，对于「候鸟」，我投入了太多的心血，但「候鸟」并不是只有我自己一个人的心血。在制作期间，有很多伙伴都给予了我巨大的帮助——感谢九九一木在我长时间失去状态期间的耐心等待、感谢aaaaki对场景精益求精的追求、感谢酒儿和闲踏梧桐对配音的专业态度、感谢拾九子不厌其烦地帮我处理各种零碎的美术素材、感谢木之为我提供了宝贵的学霸经验……感谢所有参与了「候鸟」制作的朋友们，「候鸟」的完成离不开你们费心费力的投入，谢谢！"
    nvl clear
    nvl_narrator "当然，候鸟也并不完美。"
    nvl_narrator "从理智上讲，我知道她依然还有许许多多可以更进一步的地方，比如全程几乎站桩输出的演出效果、比如一些囿于旧稿未能尽改的剧本设计……还有其他很多没有做到位的地方。"
    nvl_narrator "不过，话虽如此，但从情感来说，我已经是竭尽全力，在力所能及的范围内，做出了最大的投入、最细致的打磨，把能顾及到的方面做到了最好，可以说一句「我的生涯一片无悔」了。"
    nvl_narrator "仍不免存有遗憾，然而技止于此，无可奈何。"
    nvl_narrator "不过，正所谓青山不改，绿水长流。「候鸟」的故事结束了，我们却还要在创作之路上继续走下去，让我们在下一部作品里再见吧！"
    nvl clear
    nvl_narrator "以上，就是「候鸟」的幕后故事了。"
    nvl_narrator "总之，感谢您读完了「候鸟」正篇的故事，也感谢您能够听我唠叨完这些年来的心路历程。"
    nvl_narrator "再一次感谢您对本作的支持，也希望今您后还能够继续支持我们。"
    nvl_narrator "我是KID Fans Club的站长苍蓝的风，是一个坚持了20年没有退圈、直到现在依然还热爱着并且创作着二次元作品的人，我会一如既往地坚持走下去的。"
    nvl_narrator "谢谢！"
    nvl clear

    scene bg migrant_old #候鸟封面|未调色
    with dissolve
    nvl hide
    "主催「苍蓝的风」的访谈到此就结束了。接下来，您可以选择其他感兴趣的访谈内容："

menu:

    "主催「苍蓝的风」":
        jump blovewind

    "原案「小雨潇潇」":
        jump rain

    "配音演员「酒儿」":
        jump jiuer

    "退出访谈":
        jump end

label rain:

    # scene bg migrant #候鸟封面|调色
    # scene bg migrant_old #候鸟封面|未调色
    nvl_narrator "大家好，我是KIDFansClub汉化组、B站及新浪微博官号负责人，同时也是「候鸟」的原案作者小雨潇潇。"
    nvl_narrator "虽然提供了原案，但实际上我参与「候鸟」制作的部分很少，大部分都是苍蓝一人包揽了，我除了做了点微小的协助工作外，也就是掏了点银子而已，因为我平时的工作重点在汉化及新闻宣传方面。不过，我也愿意从另一个角度来给大家分享下「候鸟」自原案诞生到制作出成品的这十八年来的点点滴滴。"
    nvl clear
    nvl_narrator "时间要回到2006年初，当时的KFC在经历了分家之后重振旗鼓，并且制定了一条即使放到现在来看也很有效的发展路线，即「汉化——同人——原创」，通过三步走的方式完成一蜕变。当然了，理想很丰满，现实很骨感，当年的网络与资源渠道并不像现在这样发达，什么东西都是信手拈来的，加上大家虽然是热血青年，但毕竟没有经验，一切都是从零开始，汉化和同人这两条路在一阵折腾之后，因为种种原因无疾而终了，特别是年末KID公司宣布破产倒闭，基本把这条路封死了。"
    nvl_narrator "按理说，这时候的我们应该选择一条横向发展的道路，就是说，KID公司没了，可以汉化其他公司的游戏，KID的同人做不了了，可以做其他公司的。结果苍蓝和我直接一步到位，「啪」地就将原创游戏立项提上了议程，而这款原创游戏，就是大家今天所见到的「候鸟」。"
    nvl clear
    nvl_narrator "「候鸟」的原案最初是一篇散文，是我在2005年秋季迈入大学校门时，给学校的文学社投的一篇「投名状」，当然我也顺利靠着这篇作品加入了社团。它的构思也很简单，我在当年听了SHE的歌曲「候鸟」之后，结合自己高中时期的一些情感经历，联想到大家在高中毕业后各奔东西，从此再不相见，就以倒叙为开头，中间穿插了两个人在四季时看到河岸边候鸟时的不同感想，写出了这篇称之为「青春伤痛文学」风格的作品，这种风格在本世纪初很流行，以新概念作文比赛中脱颖而出的那批新锐作家，如韩寒、郭敬明、安妮宝贝为代表，所以当年也很吃得香。如今大家玩了游戏后也能够清晰地感受到，「候鸟」的时间框架结构依然参考了当年的原案，但是结尾的风格有了改变。"
    nvl_narrator "所以说，这篇作为雏形的原案也诞生于十八年前，与游戏开头时的文字「纪念十八岁的我们」形成了异曲同工之妙，而做出成品又是十八年。"
    nvl clear
    nvl_narrator "在这篇散文完成一年之后，当我们在KFC之前的发展道路上遇到挫折时，我突发奇想地将这篇散文翻了出来交给了苍蓝，并阐述了我的观点，让他看看能否以这篇散文为大纲，拓展出一个原创的国产Galgame剧本。而苍蓝在听了我的描述之后便立刻理解到了我想要表达的意思，就这么办。"
    nvl_narrator "按照苍蓝的说法：「我俩顶着惊人的漫游费，利用长途电话沟通好了这部作品最初的基调。」这话没错，我当年上大学时，手机还有长途漫游费的，但是宿舍里有两部固定电话，一部电信一部铁通，需要购买电话卡才能使用，但是价格还算便宜，10元的面值只卖6.5元，且不同的电话卡之间可以充值累计在一个账号上，一张卡基本能打一个小时。宿舍那时候除了周末，每晚11点半准时停电熄灯，所以也不能在电脑上聊天。所以我一般都是在每晚11点半熄灯之后，待舍友们都睡着时，才打电话给苍蓝。现在想想，我那几位舍友没有因此嫌我打扰睡觉，真的是万分感谢。后来毕业前，我清点了当年用掉的电话卡，差不多有三百多张，这还不包括中间丢弃的一部分。不过我俩的沟通也主要集中在06年这一年，而之后发生的事，甚至让我一度有了离开的念头。"
    nvl clear
    nvl_narrator "从2007年开始，随着同类新兴论坛以及其他媒体平台的崛起，在丧失了汉化与同人两条道路之后的KFC已经没有什么产能了，变成了一个纯粹的交流论坛，没有优势之后，人员也就不可避免地会出现流失。虽然「候鸟」此时已立项，但苍蓝在一开始便卡壳了，当时的我们谁也无法预料到这个项目什么时候能完成，就算完成后，KFC是否还活着。到了2008年，KFC接连遭受服务器硬盘故障和域名丢失两大打击，以至于很长时间内，大家都以为我们不复存在了。这期间的我正好也面临着考研和毕业的双重抉择，和家里人在这方面产生了矛盾，心烦意乱之下，我一度不再过问论坛事物，逐渐疏远了这里。而苍蓝此时也跟我一样，甚至有了另起炉灶的想法。"
    nvl_narrator "幸运的是，冥冥之中，我俩谁也没有选择轻易放弃。"
    nvl clear
    nvl_narrator "时间来到了2009年后半年，大学毕业后的我顺利就业，虽然离开了家里，但是经济独立，加上有了属于自己的私人时间，终于得以静下心来重新回到KFC收拾残局了。这段时间，虽然对KFC之前缺失的东西做了些恢复完善，但此时已经明显看到端倪，随着新兴的网络传播平台出现，原有的BBS已经逐渐失去了优势，周围的一些友情链接论坛已经出现了关闭的迹象。很不幸，KFC在刚刚恢复没多久之后，就面临着再一次的转型。"
    nvl_narrator "这时候，我们的一位老会员给我们提出了一个新的发展方向：主动出击，入驻刚刚诞生没多久的新浪微博，适应新时代的网络平台，同时延续以前的传统。这个思路其实是这么多年以来，KFC的管理层一直欠缺的。以往我们想的都是如何把人员吸引到自己的平台上来，但如果平台自己的优势开始丧失时，人气流失就是不可避免的。与其如此，还不如自己主动走出去，在新的网络平台传播自己的影响力，至于观众在哪里听到，并不重要。时代变了，不能只守着自己的一亩三分地了。"
    nvl clear
    nvl_narrator "于是，在这股思想的影响之下，除了新浪微博外，KFC先后在A、B站注册了账号，利用之前积累下的信息资料，开始在新的网络平台逐渐扩大影响，并且吸引了一部分新人加入，而这带来的结果，就是汉化组的重组。11年的9月，某位成员在看到「Ever17」的漫画后，抱着试试看的心态，与其他人商量做个汉化试试，没想到一发不可收拾，在那之后，漫画，视频，游戏，新闻，几乎全部有了我们的汉化踪迹。相信有些玩家也看过我们的汉化作品，当然其中最著名的就是「近月少女的系列」六部曲了，可以说，正是这一步「走出去」的战略，彻底激活了KFC的汉化计划。"
    nvl_narrator "但是我很清楚，靠着别人的东西，不是长久之计，我们自己的原创游戏，我们的「候鸟」必须要搞出来。"
    nvl clear
    nvl_narrator "好在，虽然经历了多年的蛰伏，但苍蓝并没有彻底，几乎是在KFC重启汉化Galgame的同一年，他在受到一部电影的启发之后，突然意识到该如何下笔了。之后的事情可以去看苍蓝的自述了，而我在这期间就在帮他打下手，比如对台词、查资料、听试音、看画稿、跑测试等。期间的起起落落也如同苍蓝所说，我们虽然踩了几个坑，但是好歹挺过来了，并且真的填完了这部作品。"
    nvl_narrator "后来我和苍蓝开玩笑地说，咱们无论是做汉化还是做原创，都是一出新手村就去打世界级BOSS。才做了几部漫画热了个身，就去挑战了近月六部曲；同人夭折了，结果直接搞起了原创。但是，我们也庆幸，这些作品的完成时间，不是十多年前，而是现在。岁月的沧桑赋予了我们智慧与耐心，让我们在不断学习之中逐渐成熟，结出了丰硕的果实。虽然完成时，我们已人到中年，但是不后悔。"
    nvl clear
    nvl_narrator "现在，经历了十八年的蛰伏，候鸟终于再次展翅翱翔，不论结果如何，我们都希望它们能飞得更远更高。同时我们也知道，这不是我们的终点，破晓之后迎来的，是无比绚烂的朝阳。在梦想的天空下，我们的脚步还能走得更远，更长。而你，原意与我们继续携手前行吗？"
    nvl_narrator "我是KIDFansClub汉化组、B站及新浪微博官号负责人，同时也是「候鸟」的原案作者小雨潇潇，希望在下一个梦想集结处，能够看到你的身影，下次见！"
    nvl clear

    scene bg migrant_old #候鸟封面|未调色
    with dissolve
    nvl hide
    "原案「小雨潇潇」的访谈到此就结束了。接下来，您可以选择其他感兴趣的访谈内容："

menu:

    "主催「苍蓝的风」":
        jump blovewind

    "原案「小雨潇潇」":
        jump rain

    "配音演员「酒儿」":
        jump jiuer

    "退出访谈":
        jump end

label jiuer:

    # scene bg migrant #候鸟封面|调色
    # scene bg migrant_old #候鸟封面|未调色
    play sound "<from 1 to 89>audio/sound/impressions.ogg"
    nvl_narrator "大家好，我是酒儿，为「候鸟」的女主角梁芷柔配音。{p=7.0}{p=0.1}设定上说她是一位十全十美的美少女学霸，但其实从第一视角很难感受到一个学霸的从容，反而是站得越高，越能感受到自己的渺小。她有非常远大的理想，但没有一个特别好的学习环境，在叶雨潇觉醒之前，她的努力其实都是很模糊很吃力的。随着他们的相处，那个理想的指示灯才在某一刻「叮」地亮了起来。{p=33}{p=0.1}没错，理想的指示灯，不是爱情的火花儿。从我的角度几乎没有感受到爱情的火花儿，大家学习地太投入了。爱情嘛——应该是这个故事结束之后的事情。高三太特殊了，它是一种，至少对我来说是一种人生烙印。「候鸟」对高三氛围的营造，非常细节。吹着空调还会流汗的黏腻的夏天，水低石现干燥坚硬的冬天，你都能够很清晰地感受到。在这种氛围下——"
    stop sound
    nvl clear
    play sound "<from 89 to 178>audio/sound/impressions.ogg"
    nvl_narrator "只想学习哈哈哈哈哈，不会太想其他的东西。但那个人也和学习一起烙在了人生当中，还是挺美好的。这才是中国特色的高中生活！没有去拯救世界，没有青春酷炫的社团，就只有路在脚下，落子无悔，努力本身就是一件很酷的事情啊。通过「候鸟」和我一起做一个很酷的人吧！{p=28.0}{p=0.1}录制「候鸟」的时候是苍蓝老师在直播间现场监工，虽然是线上录制，但像在录音棚里一样，可以即时碰撞出很多东西。比如社戏的时候，是「候鸟」里比较少有的小甜戏，是我非常非常非常非常不擅长的桥段。感觉尺度很难把握，两个人的关系其实还没有那么亲近，但又有一些小感觉，很、很……就那种「噫」～的感觉。多亏了甲方爸爸现场护航，在大家的鼓励下，终于是完成了。我很喜欢这种录制方式！很Nice的甲方～很有审美！{p=50.0}{p=0.1}综上所诉，感谢你们听到这里~希望你们喜欢这个故事。"
    stop sound
    nvl clear
    play sound "<from 179 to 265>audio/sound/impressions.ogg"
    nvl_narrator "诶？不到800字，虽然说作为Freetalk来说已经足够长了，但缺少了一点纪念意义，我可以稍微凑一点。讲讲刚拿到剧本的时候，就被「候鸟」比较贴近生活的质感吸引了，而且听说它的原型是甘肃的一个县城，我甚至一度想要去看一看，差一点就投入到乡村振兴事业中去了。然后和苍蓝老师商量配音风格，商量需要写实到什么程度，什么电影感啊、电视剧的感觉啊，想要贴近生活，但太生活了又会缺少浪漫和遐想，就会削减了一个虚拟的纸片人形象可以承载的魅力。但「十全十美」这种标签又很容易缺乏个性。最后在表演上，借鉴了一点「狼与香辛料」里赫萝的形象，会面对很多日常小事，但是聪明伶俐想得开，我把这样的性格作为一个高不可攀的可怕学霸外表下的本质，让表演更有趣了。{p=71.0}{p=0.1}这篇「录制候鸟有感」文体不限，不低于800字的作文完成了！你会打几分呢～"
    stop sound
    nvl clear

    scene bg migrant_old #候鸟封面|未调色
    with dissolve
    nvl hide
    "配音演员「酒儿」的访谈到此就结束了。接下来，您可以选择其他感兴趣的访谈内容："

menu:

    "主催「苍蓝的风」":
        jump blovewind

    "原案「小雨潇潇」":
        jump rain

    "配音演员「酒儿」":
        jump jiuer

    "退出访谈":
        jump end

label end:

    return
