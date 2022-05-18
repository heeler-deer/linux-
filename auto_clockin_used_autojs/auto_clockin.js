auto;
//开启无障碍服务






sleep(2500);



// 解锁屏幕

function unlock()

{

if(!device.isScreenOn())

{

device.wakeUp();

sleep(1000);

swipe(100,

2000,

100,

1000,

210);

sleep(1000);

var password = "xxxxxx" //这里输入你手机的密码

for(var i = 0; i < password.length; i++)

{

var p = text(password[i

].toString()).findOne().bounds();

click(p.centerX(), p.centerY());

sleep(100);

}

}

}



unlock();










//打开微信

var packageName = getPackageName("微信"); //得到微信的包名


openAppSetting(packageName); //打开微信的设置页用于关闭微信


var close = className("android.widget.Button").id("right_button").findOne().click(); //通过控件找到强行停止，并点击


sleep(500);


var cl2 = className("android.widget.Button").text("强行停止").findOne().click(); //通过控件找到强行停止，并点击


sleep(500);


launchApp("微信"); //打开微信


sleep(4000)






//依次点击最终找到疫情防控

//通讯录->公众号->湖南大学->功能服务->疫情防控




var ling = className("android.widget.TextView").text("通讯录").findOne(2000);


log(ling);


if(ling==null){ //找不到退出


toast("找不到通讯录");


exit();

}



click(ling.bounds().centerX(),ling.bounds().centerY());


sleep(4000);


var ling = className("android.widget.TextView").text("公众号").findOne(2000);


log(ling);


if(ling==null){ //找不到退出


toast("找不到公众号");


exit();

}


click(ling.bounds().centerX(),ling.bounds().centerY());


sleep(4000);


var ling = className("android.widget.TextView").text("湖南大学").findOne(2000);


log(ling);


if(ling==null){ //找不到退出


toast("找不到湖南大学");


exit();

}


click(ling.bounds().centerX(),ling.bounds().centerY());


sleep(4000);


var ling = className("android.widget.TextView").text("功能服务").findOne(2000);


log(ling);


if(ling==null){ //找不到退出


toast("找不到功能服务");


exit();

}


click(ling.bounds().centerX(),ling.bounds().centerY());


sleep(4000);


var ling= className("android.widget.TextView").text("疫情防控").findOne(2000);


log(ling);


if(ling==null){


toast("找不到疫情防控");


exit();

}


click(ling.bounds().centerX(),ling.bounds().centerY());


sleep(4000);


var ling = className("android.widget.TextView").text("确认").findOne(2000);


log(ling);


if(ling==null){


toast("找不到确认");

}

else{

click(ling.bounds().centerX(),ling.bounds().centerY());

}




sleep(2500);



//打卡选项



//由于我太菜
//因此下面采用的是绝对位置进行点击
//不同手机绝对位置不同
//因此不能直接用
click(27,1804,132,1860);
sleep(4000);
click(27,2014,170,2071);
sleep(4000);



swipe(100,

2000,

100,

1500,

210);


sleep(4000);
click(153,1320,261,1377);
sleep(4000);

click(153,1531,261,1588);
sleep(8000);

click(27,2044,132,2101);
sleep(4000);

click(153,2346,261,2401);
sleep(4000);

swipe(100,

2000,

100,

1500,

210);


sleep(4000);

click(153,1652,261,1712);
sleep(4000);


swipe(100,

2000,

100,

1000,

210);

sleep(8000);
click(0,2281,1080,2401);

