var getRight_4Option=function(data){


    // rsv1=30  邯郸网联
    // rsv2=100-rsv1 兴业网联占比
    xydlwl_tot=data.xydlwl_tot
    hddlwl_tot=data.hddlwl_tot
    rsv1=(hddlwl_tot/(xydlwl_tot+hddlwl_tot)*100).toFixed(0)

    rsv2=100 -rsv1
    // rsv1=30
    // rsv2=50



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
            fontSize: '24',
            fontWeight: 'normal',
            color: '#fff'
        }
    }
};


option = {
    //backgroundColor: '#142058',
    //     tooltip: {
    //     trigger: 'item',
    //     // formatter: '邯郸总量:'+hddlwl_tot+'</br>'+'兴业总量'+xydlwl_tot,
    // },
    title: [
        {
        text: '平台交易占比',
        x: 10,
        y: 10,
        textStyle: {
            color: '#fff',
            fontSize: 16
        }
    },{
        text: '兴业邯郸网联',
        left: '23%',
        top: '75%',
        textAlign: 'center',
        textStyle: {
            fontWeight: 'normal',
            fontSize: '16',
            color: '#fff',
            textAlign: 'center',
        },
    }, {
        text: '兴业代理网联',
        left: '73%',
        top: '75%',
        textAlign: 'center',
        textStyle: {
            color: '#fff',
            fontWeight: 'normal',
            fontSize: '16',
            textAlign: 'center',
        },
    }],
    series: [
        {
            type: 'pie',
            hoverAnimation: false, //鼠标经过的特效
            radius: ['35%', '50%'],
            center: ['25%', '50%'],
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
            tooltip:{
                trigger:'item'


            },
            data: [{
                    value: rsv1,
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
                    value: rsv2,
                    itemStyle: placeHolderStyle,
                },

            ]
        },
        {
            type: 'pie',
            hoverAnimation: false,
            radius: ['35%', '50%'],
            center: ['75%', '50%'],
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
                    value: rsv2,
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
                    value: rsv1,
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
            center: ['25%', '50%'],
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
                    value: rsv1,
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
                    value: rsv2,
                    itemStyle: placeHolderStyle,
                },

            ]
        },
        {
            type: 'pie',
            hoverAnimation: false,
            radius: ['50%', '52%'],
            center: ['75%', '50%'],
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
                    value: rsv1,
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
                    value: rsv2,
                    itemStyle: placeHolderStyle,
                },

            ]
        },
    ]
};
return option;
}