
var getLeft_5Option=function(){
 /*---------------------数据----------------------------*/
var echartData = [{
    value: 100,//时间
    name: '健康度'
}, {
   
}];


/*---------------------颜色变量----------------------------*/
//蓝色
var innerColor = '#2bff8f'; //内层颜色
var outColor = "#50e0ff"; //外层边框色粗
var textColor = '#50e0ff'; //文字颜色
var startColor = 'rgba(73,223,240,0.1)'; //中间饼图渐变开始颜色
var endColor = 'rgba(73,223,240,0.8)'; //中间饼图渐变结束颜色
//绿色
// var innerColor = '#50e0ff'; //内层颜色
// var outColor = "#2bff8f"; //外层边框色粗
// var textColor = '#50e0ff'; //文字颜色
// var startColor = 'rgba(43,255,143,0.1)'; //中间饼图渐变开始颜色
// var endColor = 'rgba(43,255,143,0.8)'; //中间饼图渐变结束颜色


/*---------------------缩放----------------------------*/
var scale = 1;


/*---------------------颜色配置----------------------------*/
var color = [{
    type: 'linear',
    x: 0,
    y: 0,
    x2: 0,
    y2: 1,
    colorStops: [{
        offset: 0,
        color: startColor // 0% 处的颜色
    }, {
        offset: 1,
        color: endColor // 100% 处的颜色
    }],
    globalCoord: false // 缺省为 false
}, 'none'];
/*---------------------富文本----------------------------*/
var rich = {
    time: {
        color: innerColor,
        fontSize: 32 * scale,
        padding: [0, 0],
        fontWeight:'bold'
    },
    unit:{
        color: innerColor,
        fontSize: 14 * scale,
        padding: [0,0,0, 0],
        verticalAlign:'bottom',
    }
}


option = {
   // backgroundColor: '#031f2d',
    title: [{
        text: '运行监控',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        },
    }],
  
 
    series: [
        //内圈圆环
        {
            name: '系统健康度',
            type: 'pie',
            clockWise: false, //顺时加载
            hoverAnimation: false, //鼠标移入变大
            center: ['50%', '25%'],
            radius: ['60%', '62%'],
            itemStyle: {
                normal: {
                    color: innerColor,
                }
            },
            data: [{
            value: 10,
            label: {
                normal: {
                    formatter: '100%',
                     position: 'center',
                    textStyle: {
                        color: '#fff',
                        fontSize: 20
                    }
                }
            }
        }, {
            tooltip: {
                show: false
            },
            label: {
                normal: {
                    formatter: '\n公网POS',
                    position: 'center',
                    textStyle: {
                        color: innerColor,
                        fontSize: 8
                    }
                }
            }
        }]
        
        },
        //中间圆环
        {
            name: '系统健康度2',
            type: 'pie',
            clockWise: false, //顺时加载
            hoverAnimation: false, //鼠标移入变大
            center: ['50%', '25%'],
            radius: ['66%', '80%'],
            color: color,
            itemStyle: {
                normal: {
                    label: {
                        show: false,
                        
                    },
                    labelLine: {
                        show: false
                    },
                }
            },
             
            data:echartData,
            
        },
        //外层圆环
        {
            name: '系统健康度3',
            type: 'pie',
            clockWise: false, //顺时加载
            hoverAnimation: false, //鼠标移入变大
            center: ['50%', '25%'],
            radius: ['80%', '80%'],
            itemStyle: {
                normal: {
                    borderWidth: 2* scale,
                    borderColor: outColor,
                    label: {
                        show: true
                    },
                    labelLine: {
                        show: false
                    },
                }
            },
            
            data: [{
                value: 100,
                name: '',

            }]
        },
        
    //----------第二个圆---------------    
        
     //内圈圆环
        {
            name: '应用健康度',
            type: 'pie',
            clockWise: false, //顺时加载
            hoverAnimation: false, //鼠标移入变大
            center: ['50%', '55%'],
            radius: ['60%', '62%'],
            itemStyle: {
                normal: {
                    color: '#08B6E6',
                }
            },
            data: [{
            value: 10,
            label: {
                normal: {
                    formatter: '100%',
                     position: 'center',
                    textStyle: {
                        color: '#fff',
                        fontSize: 20
                    }
                }
            }
        }, {
            tooltip: {
                show: false
            },
            label: {
                normal: {
                    formatter: '\n商踪密',
                    position: 'center',
                    textStyle: {
                        color: '#08B6E6',
                        fontSize: 8
                    }
                }
            }
        }]
       
        },
        //中间圆环
        {
            name: '应用健康度2',
            type: 'pie',
            clockWise: false, //顺时加载
            hoverAnimation: false, //鼠标移入变大
            center: ['50%', '55%'],
            radius: ['66%', '80%'],
            color: color,
            itemStyle: {
                normal: {
                    label: {
                        show: false,
                        
                    },
                    labelLine: {
                        show: false
                    },
                }
            },
             
            data:echartData,
            
        },
        //外层圆环
        {
            name: '应用健康度3',
            type: 'pie',
            clockWise: false, //顺时加载
            hoverAnimation: false, //鼠标移入变大
            center: ['50%', '55%'],
            radius: ['80%', '80%'],
            itemStyle: {
                normal: {
                    borderWidth: 2* scale,
                    borderColor: outColor,
                    label: {
                        show: true
                    },
                    labelLine: {
                        show: false
                    },
                }
            },
            
            data: [{
                value: 100,
                name: '',

            }]
        } ,
        
      //-------第三个圆----------  
       //内圈圆环
        {
            name: '网络健康度',
            type: 'pie',
            clockWise: false, //顺时加载
            hoverAnimation: false, //鼠标移入变大
            center: ['50%', '85%'],
            radius: ['60%', '62%'],
            itemStyle: {
                normal: {
                    color: '#827BF8',
                }
            },
            data: [{
            value: 10,
            label: {
                normal: {
                    formatter: '100%',
                     position: 'center',
                    textStyle: {
                        color: '#fff',
                        fontSize: 20
                    }
                }
            }
        }, {
            tooltip: {
                show: false
            },
            label: {
                normal: {
                    formatter: '\nPOS通',
                    position: 'center',
                    textStyle: {
                        color: '#827BF8',
                        fontSize: 8
                    }
                }
            }
        }]
       
        },
        //中间圆环
        {
            name: '网络健康度2',
            type: 'pie',
            clockWise: false, //顺时加载
            hoverAnimation: false, //鼠标移入变大
            center: ['50%', '85%'],
            radius: ['66%', '80%'],
            color: color,
            itemStyle: {
                normal: {
                    label: {
                        show: false,
                        
                    },
                    labelLine: {
                        show: false
                    },
                }
            },
             
            data:echartData,
            
        },
        //外层圆环
        {
            name: '网络健康度3',
            type: 'pie',
            clockWise: false, //顺时加载
            hoverAnimation: false, //鼠标移入变大
            center: ['50%', '85%'],
            radius: ['80%', '80%'],
            itemStyle: {
                normal: {
                    borderWidth: 2* scale,
                    borderColor: outColor,
                    label: {
                        show: true
                    },
                    labelLine: {
                        show: false
                    },
                }
            },
            
            data: [{
                value: 100,
                name: '',

            }]
        } 
        
        
        
        
    ],
};

return option;
}