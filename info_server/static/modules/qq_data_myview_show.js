/**

 @Name：layuiAdmin Echarts集成
 @Author：star1029
 @Site：http://www.layui.com/admin/
 @License：GPL-2

 */


layui.define(function (exports) {
        //区块轮播切换
        layui.use(['laydate', 'form'], function () {
            var $ = layui.$
                , laydate = layui.laydate
                , form = layui.form;


            laydate.render({
                elem: '#start_date'
            });
            laydate.render({
                elem: '#end_date'
            });

            var start_date = '2020-02-21';
            var end_date = '2020-03-20';
            form.val('example', {
                "start_date": start_date // "name": "value"
                , "end_date": end_date
            });

            function swInit(input_date){
                var index = layer.load(1);
                console.log(input_date.field);
                $.post("/data_api/qq_data_count/myview_show/",
                    input_date.field,
                    function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                        console.log(data);

                        line_left1(data);
                        line_left2(data);

                        bar_right1(data);


                        layer.close(index);
                    }
                );
            }

            swInit({field: {start_date:start_date, end_date:end_date}});
            //监听提交
            form.on('submit(demo1)', function (data) {
                console.log(data.field);
                swInit(data);
                return false;
            });

        });


        function line_left1(data) {
            //标准折线图
            layui.use(['carousel', 'echarts'], function () {
                var $ = layui.$
                    , echarts = layui.echarts
                    , carousel = layui.carousel;
                var echnormline = [], normline = [
                    {
                        title: {
                            text: '鲲鹏运维管理平台',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            data: ['PV']
                        },
                        calculable: true,
                        xAxis: [
                            {
                                type: 'category',
                                boundaryGap: false,
                                //data: ['周X', '周二', '周三', '周四', '周五', '周六', '周日']
                                data: data.data.map(function (item, i) {
                                    return item.CreateTime;
                                })
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                axisLabel: {
                                    formatter: '{value}'
                                }
                            }
                        ],
                        series: [
                            {
                                name: 'PV',
                                type: 'line',
                                //data: [11, 11, 15, 13, 12, 13, 10],
                                data: data.data.map(function (item, i) {
                                    return item.count;
                                }),
                                markPoint: {
                                    data: [{type: 'max', name: '最大值'}, {type: 'min', name: '最小值'}]
                                },
                                markLine: {
                                    data: [{type: 'average', name: '平均值'}]
                                }
                            }/*,
                                {
                                    name: '最低气温',
                                    type: 'line',
                                    data: [1, -2, 2, 5, 3, 2, 0],
                                    markPoint: {
                                        data: [{name: '周最低', value: -2, xAxis: 1, yAxis: -1.5}]
                                    },
                                    markLine: {
                                        data: [{type: 'average', name: '平均值'}]
                                    }
                                }*/
                        ]
                    }
                ]
                    , elemnormline = $('#LAY-index-left1').children('div')
                    , rendernormline = function (index) {
                    echnormline[index] = echarts.init(elemnormline[index], layui.echartsTheme);
                    echnormline[index].setOption(normline[index]);
                    window.onresize = echnormline[index].resize;
                };
                if (!elemnormline[0]) return;
                rendernormline(0);

            });
        }


        function line_left2(data) {
            //标准折线图
            layui.use(['carousel', 'echarts'], function () {
                var $ = layui.$
                    , echarts = layui.echarts
                    , carousel = layui.carousel;
                var echnormline = [], normline = [
                    {
                        title: {
                            text: '自动化软件下发',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            data: ['普通版本', '紧急版本']
                        },
                        color: ['#168a76','#f51346'],
                        calculable: true,
                        xAxis: [
                            {
                                type: 'category',
                                boundaryGap: false,
                                //data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']

                                data: data.data2.map(function (item, i) {
                                    return item.CreateTime;
                                })


                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                axisLabel: {
                                    formatter: '{value}'
                                }
                            }
                        ],
                        series: [
                            {
                                name: '普通版本',
                                type: 'line',
                                //data: [11, 11, 15, 13, 12, 13, 10],
                                data: data.data2.map(function (item, i) {
                                    return item.count;
                                }),
                                markPoint: {
                                    data: [{type: 'max', name: '最大值'}]
                                },
                                markLine: {
                                    data: [{type: 'average', name: '平均值'}]
                                }
                            },
                            {
                                name: '紧急版本',
                                type: 'line',
                                // data: [1, 2, 2, 5, 3, 2, 0],
                                data: data.data3.map(function (item, i) {
                                    return item.count;
                                }),
                                markPoint: {
                                    data: [{type: 'max', name: '最大值'}]
                                },
                                markLine: {
                                    data: [{type: 'average', name: '平均值'}]
                                }
                            }
                        ]
                    }
                ]
                    , elemnormline = $('#LAY-index-left2').children('div')
                    , rendernormline = function (index) {
                    echnormline[index] = echarts.init(elemnormline[index], layui.echartsTheme);
                    echnormline[index].setOption(normline[index]);
                    window.onresize = echnormline[index].resize;
                };
                if (!elemnormline[0]) return;
                rendernormline(0);

            });
        }


        function bar_left3(data) {
            layui.use(['carousel', 'echarts'], function () {
                var $ = layui.$
                    , carousel = layui.carousel
                    , echarts = layui.echarts;

                //标准柱状图
                var echnormcol = [], normcol = [
                    {
                        title: {
                            text: '人员运营分析',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },

                        legend: {
                            data: ['KPI']
                        },


                        //vlegend: new_data.legend,
                        calculable: true,
                        xAxis: [
                            {
                                type: 'category',
                                // data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
                                data: data.map(function (item, i) {
                                    return item.first_name;
                                })
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value'
                            }
                        ],
                        series: [
                            {
                                name: 'KPI',
                                type: 'bar',
                                // data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                                data: data.map(function (item, i) {
                                    return item.sum;
                                }),
                                markPoint: {
                                    data: [
                                        {type: 'max', name: '最大值'},
                                        {type: 'min', name: '最小值'}
                                    ]
                                },
                                markLine: {
                                    data: [{type: 'average', name: '平均值'}]
                                }
                            }
                        ]
                    }
                ]
                    , elemNormcol = $('#LAY-index-bar-left3').children('div')
                    , renderNormcol = function (index) {
                    echnormcol[index] = echarts.init(elemNormcol[index], layui.echartsTheme);
                    echnormcol[index].setOption(normcol[index]);
                    window.onresize = echnormcol[index].resize;
                };
                if (!elemNormcol[0]) return;
                renderNormcol(0);
            });
        }

        function bar_left4(data) {
            layui.use(['carousel', 'echarts'], function () {
                var $ = layui.$
                    , carousel = layui.carousel
                    , echarts = layui.echarts;

                //标准柱状图
                var echnormcol = [], normcol = [
                    {
                        title: {
                            text: '某地区蒸发量和降水量',
                            subtext: '纯属虚构'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            data: ['蒸发量', '降水量']
                        },
                        calculable: true,
                        xAxis: [
                            {
                                type: 'category',
                                data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value'
                            }
                        ],
                        series: [
                            {
                                name: '蒸发量',
                                type: 'bar',
                                data: [2.0, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                                markPoint: {
                                    data: [
                                        {type: 'max', name: '最大值'},
                                        {type: 'min', name: '最小值'}
                                    ]
                                },
                                markLine: {
                                    data: [{type: 'average', name: '平均值'}]
                                }
                            },
                            {
                                name: '降水量',
                                type: 'bar',
                                data: [2.6, 5.9, 9.0, 26.4, 28.7, 70.7, 175.6, 182.2, 48.7, 18.8, 6.0, 2.3],
                                markPoint: {
                                    data: [
                                        {name: '年最高', value: 182.2, xAxis: 7, yAxis: 183, symbolSize: 18},
                                        {name: '年最低', value: 2.3, xAxis: 11, yAxis: 3}
                                    ]
                                },
                                markLine: {
                                    data: [
                                        {type: 'average', name: '平均值'}
                                    ]
                                }
                            }
                        ]
                    }
                ]
                    , elemNormcol = $('#LAY-index-bar-left4').children('div')
                    , renderNormcol = function (index) {
                    echnormcol[index] = echarts.init(elemNormcol[index], layui.echartsTheme);
                    echnormcol[index].setOption(normcol[index]);
                    window.onresize = echnormcol[index].resize;
                };
                if (!elemNormcol[0]) return;
                renderNormcol(0);
            });
        }

        function bar_right1(data) {
            layui.use(['carousel', 'echarts'], function () {
                var $ = layui.$
                    , carousel = layui.carousel
                    , echarts = layui.echarts;

                //标准柱状图
                var echnormcol = [], normcol = [
                    {
                        title: {
                            text: '人员运营分析',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },

                        legend: {
                            data: ['KPI']
                        },


                        //vlegend: new_data.legend,
                        calculable: true,
                        xAxis: [
                            {
                                type: 'category',
                                data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
                                // data: data.map(function (item, i) {
                                //     return item.first_name;
                                // })
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value'
                            }
                        ],
                        series: [
                            {
                                name: 'KPI',
                                type: 'bar',
                                data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                                // data: data.map(function (item, i) {
                                //     return item.sum;
                                // }),
                                markPoint: {
                                    data: [
                                        {type: 'max', name: '最大值'},
                                        {type: 'min', name: '最小值'}
                                    ]
                                },
                                markLine: {
                                    data: [{type: 'average', name: '平均值'}]
                                }
                            }
                        ]
                    }
                ]
                    , elemNormcol = $('#LAY-index-right1').children('div')
                    , renderNormcol = function (index) {
                    echnormcol[index] = echarts.init(elemNormcol[index], layui.echartsTheme);
                    echnormcol[index].setOption(normcol[index]);
                    window.onresize = echnormcol[index].resize;
                };
                if (!elemNormcol[0]) return;
                renderNormcol(0);
            });
        }

        function bar_right2(data) {
            layui.use(['carousel', 'echarts'], function () {
                var $ = layui.$
                    , echarts = layui.echarts
                    , carousel = layui.carousel;

                //console.log(data.list_bank_count);
                //console.log(data.list_bank_count.slice(-5,-1));
                //标准条形图

                var echnormbar = [], normbar = [
                    {
                        title: {
                            text: '合作行不活跃TOP10',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            data: ['QQ活跃度']
                        },
                        calculable: true,
                        xAxis: [
                            {
                                type: 'value',
                                boundaryGap: [0, 0.01]
                            }
                        ],
                        yAxis: [
                            {
                                type: 'category',
                                //data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口(万)']
                                data: data.map(function (item, i) {
                                    return item.group;
                                })
                            }
                        ],
                        dataZoom: [
                            {
                                show: true,
                                start: 0,
                                end: 100
                            },
                            {
                                type: 'inside',
                                start: 94,
                                end: 100
                            },
                            {
                                show: true,
                                yAxisIndex: 0,
                                filterMode: 'empty',
                                width: 30,
                                height: '50%',
                                showDataShadow: false,
                                left: '93%'
                            }
                        ],
                        series: [
                            {
                                name: 'QQ活跃度',
                                type: 'bar',
                                itemStyle: {normal: {label: {show: true, position: 'right'}}},

                                //data: [18203, 23489, 29034, 104970, 131744, 630230]
                                data: data.map(function (item, i) {
                                    return item.sum;
                                })
                            }
                        ]
                    }
                ]
                    , elemNormbar = $('#LAY-index-bar-right2').children('div')
                    , renderNormbar = function (index) {
                    echnormbar[index] = echarts.init(elemNormbar[index], layui.echartsTheme);
                    echnormbar[index].setOption(normbar[index]);
                    window.onresize = echnormbar[index].resize;
                };
                if (!elemNormbar[0]) return;
                renderNormbar(0);


            });
        }


        //区块轮播切换
        layui.use(['admin', 'carousel'], function () {
            var $ = layui.$
                , admin = layui.admin
                , carousel = layui.carousel
                , element = layui.element
                , device = layui.device();


            //轮播切换
            $('.layadmin-carousel').each(function () {
                var othis = $(this);
                carousel.render({
                    elem: this
                    , width: '100%'
                    , arrow: 'none'
                    , interval: othis.data('interval')
                    , autoplay: othis.data('autoplay') === true
                    , trigger: (device.ios || device.android) ? 'click' : 'hover'
                    , anim: othis.data('anim')
                });
            });

            element.render('progress');

        });
        exports('senior', {})

    }
);