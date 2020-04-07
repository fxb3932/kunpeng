

var getLeft_1Option=function(){


var colors = ['#008cff','#00da9c','#c4e300'];
var city=['13:00','13:01','13:02','13:03','13:04','13:05','13:06','13:07','13:08','13:09','13:10','13:11','13:12','13:13','13:14','13:15','13:16','13:17','13:18','13:19','13:20','13:21','13:22','13:23','13:24','13:25','13:26','13:27','13:28','13:29','13:30','13:31','13:32','13:33','13:34','13:35','13:36','13:37','13:38','13:39','13:40','13:41','13:42','13:43','13:44','13:45','13:46','13:47','13:48','13:49','13:50','13:51','13:52','13:53','13:54','13:55','13:56','13:57','13:58','13:59'];
var data1=[3293,3302,3262,3291,3278,3193,3268,3200,3259,3186,3188,3274,3121,3196,3156,3278,3222,3204,3185,3177,3142,3122,3135,3213,3154,3151,3160,3112,3178,3132,3117,3125,3165,3164,3093,3126,3102,3149,3111,3018,3144,3269,3163,3177,3152,3163,3142,3259,3176,3295,3162,3179,3023,3126,3092,3043,3205,3178,3170,3083];
var data2=[4590,4569,4505,4476,4496,4521,4548,4428,4458,4425,4402,4526,4363,4445,4409,4431,4408,4334,4427,4368,4385,4385,4353,4422,4351,4352,4388,4272,4352,4365,4419,4279,4343,4353,4285,4297,4274,4332,4356,4195,4328,4424,4397,4371,4370,4341,4314,4466,4332,4431,4327,4388,4217,4282,4227,4306,4341,4383,4273,4202];
var data3=[1271,1238,1209,1154,1181,1305,1255,1200,1179,1216,1191,1223,1226,1222,1225,1132,1156,1113,1220,1168,1218,1238,1191,1188,1171,1175,1199,1138,1148,1207,1279,1123,1149,1166,1169,1146,1142,1151,1209,1158,1158,1136,1209,1166,1189,1148,1143,1182,1133,1111,1131,1186,1164,1124,1103,1232,1102,1178,1079,1097];
option = {
     title: {
        text: 'POS通当日交易量',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
    },
    color: colors,
    tooltip: {
        trigger: 'axis',
        axisPointer: {type: 'cross'}
    },
     grid: {
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },    
   
     legend: {
        data:['微信','支付宝','银联二维码'],
        align: 'right',
        top:40,
        right: 10,
        textStyle: {
            color: "#fff"
        },
        itemWidth: 10,
        itemHeight: 10,
        itemGap: 10
    },
    xAxis: [
        {
            type: 'category',
            
            axisTick: {
                alignWithLabel: true
            },
             axisLabel: {
            show: true,
            textStyle: {
                color: "#00c7ff",
            }
        },
            data: city
        }
    ],
    yAxis: [
        
        {
            splitLine: {show: false},
            type: 'value',
            //name: '交易笔数',
            min: 0,
            max: 12000,
            position: 'left',
             axisLine: {
            show: true,
            lineStyle: {
                color: "#00c7ff",
                width: 1
                
            },
        },
            axisLabel: {
                formatter: '{value} '
            }
        }],
        
    series: [{
            name:'微信',
            stack: '总量',
            type:'bar',
            barWidth : 2,
            data:data1
        },
        {
            name:'支付宝',
            stack: '总量',
            type:'bar',
            data:data2
        },
        {
            name:'银联二维码',
            stack: '总量',
            type:'bar',
            data:data3
        }]
};

return option;
}
