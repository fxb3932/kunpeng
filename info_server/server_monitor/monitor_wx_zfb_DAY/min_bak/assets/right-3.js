var getRight_3Option=function(){
var placeHolderStyle = {
    normal: {
        label: {
            show: false
        },
        labelLine: {
            show: false
        },
        color: "rgba(0,0,0,0)",
        borderWidth: 0
    },
    emphasis: {
        color: "rgba(0,0,0,0)",
        borderWidth: 0
    }
};


var dataStyle = {
    normal: {
        formatter: '{c}%',
        position: 'center',
        show: true,
        textStyle: {
            fontSize: '28',
            fontWeight: 'normal',
            color: '#fff'
        }
    }
};


option = {
    //backgroundColor: '#142058',
    title: [
        {
        text: '双中心交易占比',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
    },{
        text: '上海运行中心',
        left: '23%',
        top: '80%',
        textAlign: 'center',
        textStyle: {
            fontWeight: 'normal',
            fontSize: '16',
            color: '#fff',
            textAlign: 'center',
        },
    }, {
        text: '武汉运行中心',
        left: '73%',
        top: '80%',
        textAlign: 'center',
        textStyle: {
            color: '#fff',
            fontWeight: 'normal',
            fontSize: '16',
            textAlign: 'center',
        },
    }],
    series: [{
            type: 'pie',
            hoverAnimation: false, //鼠标经过的特效
            radius: ['35%', '50%'],
            center: ['25%', '60%'],
            startAngle: 225,
            labelLine: {
                normal: {
                    show: false
                }
            },
            label: {
                normal: {
                    position: 'center'
                }
            },
            data: [{
                    value: 75,
                    itemStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: '#99da69'
                            }, {
                                offset: 1,
                                color: '#01babc'
                            }]),
                        }
                    },
                    label: dataStyle,
                }, {
                    value: 25,
                    itemStyle: placeHolderStyle,
                },

            ]
        },
        {
            type: 'pie',
            hoverAnimation: false,
            radius: ['35%', '50%'],
            center: ['75%', '60%'],
            startAngle: 225,
            labelLine: {
                normal: {
                    show: false
                }
            },
            label: {
                normal: {
                    position: 'center'
                }
            },
            data: [{
                    value: 25,
                    itemStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: '#9f3edd'
                            }, {
                                offset: 1,
                                color: '#4897f6'
                            }]),
                        }
                    },
                    label: dataStyle,
                }, {
                    value: 75,
                    itemStyle: placeHolderStyle,
                },

            ]
        },
        
        //外圈的边框
        {
            // name: '总人数',
            type: 'pie',
            hoverAnimation: false, //鼠标经过的特效
            radius: ['50%', '52%'],
            center: ['25%', '60%'],
            startAngle: 225,
            labelLine: {
                normal: {
                    show: false
                }
            },
            label: {
                normal: {
                    position: 'center'
                }
            },
            data: [{
                    value: 75,
                    itemStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: '#01babc'
                            }, {
                                offset: 1,
                                color: '#99da69'
                            }]),
                        }
                    },
                }, {
                    value: 25,
                    itemStyle: placeHolderStyle,
                },

            ]
        },
        {
            type: 'pie',
            hoverAnimation: false,
            radius: ['50%', '52%'],
            center: ['75%', '60%'],
            startAngle: 225,
            labelLine: {
                normal: {
                    show: false
                }
            },
            label: {
                normal: {
                    position: 'center'
                }
            },
            data: [{
                    value: 75,
                    itemStyle: {
                        normal: {
                            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                                offset: 0,
                                color: '#4897f6'
                            }, {
                                offset: 1,
                                color: '#9f3edd'
                            }]),
                        }
                    },
                }, {
                    value: 25,
                    itemStyle: placeHolderStyle,
                },

            ]
        },
    ]
};
return option;
}