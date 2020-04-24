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

            var start_date = "2020-03-21";
            var end_date = '2020-03-27';

            form.val('example', {
                "start_date": start_date // "name": "value"
                , "end_date": end_date
            });

            function swInit(data) {
                line_left1(data);
                bar_left2(data.list_bank_big_count);
                bar_7(data.list_bank_cz_count);

                bar_left3(data.list_oper_count_HX, data.list_oper_count_max);
                bar_left4(data.list_oper_count_GL, data.list_oper_count_max);
                bar_left5(data.list_oper_count_JG, data.list_oper_count_max);
                bar_6(data.list_oper_count_KF, data.list_oper_count_max);


                bar_right1(data.list_bank_count);
                bar_right2(data.list_bank_count2);
                bar_right3(data.list_group_count);

                //bar_6(data, 10);
            }

            var index = layer.load(1);
            $.post("/data_api/qq_data_count/",
                {start_date: start_date, end_date: end_date},
                function (data, status) {
                    console.log("Data: " + data + "\nStatus: " + status);
                    console.log(data);
                    console.log(data.count_date);
                    test = data.count_date.map(function (item, i) {
                        return item.date;
                    });
                    console.log(test);

                    swInit(data);

                    // bar_left4(data);


                    layer.close(index);
                }
            );

            //监听提交
            form.on('submit(demo1)', function (data) {
                console.log(data.field);
                var index = layer.load(1);
                $.post("/data_api/qq_data_count/",
                    data.field,
                    function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                        console.log(data);
                        console.log(data.count_date);
                        test = data.count_date.map(function (item, i) {
                            return item.date;
                        });
                        console.log(test);

                        swInit(data);

                        // bar_left4(data);


                        layer.close(index);
                    }
                );
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
                            text: 'QQ活跃度趋势',
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
                                type: 'category',
                                boundaryGap: false,
                                //data: ['周X', '周二', '周三', '周四', '周五', '周六', '周日']
                                data: data.count_date.map(function (item, i) {
                                    return item.date;
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
                                name: 'QQ活跃度',
                                type: 'line',
                                //data: [11, 11, 15, 13, 12, 13, 10],
                                data: data.count_date.map(function (item, i) {
                                    return item.sum;
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
                    , elemnormline = $('#LAY-index-line-left1').children('div')
                    , rendernormline = function (index) {
                    echnormline[index] = echarts.init(elemnormline[index], layui.echartsTheme);
                    echnormline[index].setOption(normline[index]);
                    window.onresize = echnormline[index].resize;
                };
                if (!elemnormline[0]) return;
                rendernormline(0);

            });
        }


        function bar_left2(data) {
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
                            text: '大客户活跃排行',
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
                    , elemNormbar = $('#LAY-index-bar-left2').children('div')
                    , renderNormbar = function (index) {
                    echnormbar[index] = echarts.init(elemNormbar[index], layui.echartsTheme);
                    echnormbar[index].setOption(normbar[index]);
                    window.onresize = echnormbar[index].resize;
                };
                if (!elemNormbar[0]) return;
                renderNormbar(0);


            });
        }


        function bar_left3(data, max) {
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
                            text: '核心渠道',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            show: false,
                            data: ['QQ活跃度']
                        },
                        calculable: true,
                        xAxis: [
                            {
                                type: 'value',
                                max: max,
                                // show: false,
                                boundaryGap: [0, 0.01]
                            }
                        ],
                        yAxis: [
                            {
                                type: 'category',
                                //data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口(万)']
                                data: data.data.map(function (item, i) {
                                    return item.first_name;
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
                                data: data.data.map(function (item, i) {
                                    return item.sum;
                                })
                            }
                        ]
                    }
                ]
                    , elemNormbar = $('#LAY-index-bar-left3').children('div')
                    , renderNormbar = function (index) {
                    echnormbar[index] = echarts.init(elemNormbar[index], layui.echartsTheme);
                    echnormbar[index].setOption(normbar[index]);
                    window.onresize = echnormbar[index].resize;
                };
                if (!elemNormbar[0]) return;
                renderNormbar(0);


            });
        }

        function bar_left4(data, max) {
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
                            show: true,
                            text: '管理产品',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            show: false,
                            data: ['QQ活跃度']
                        },
                        calculable: true,
                        xAxis: [
                            {
                                type: 'value',
                                max: max,
                                // show: false,
                                boundaryGap: [0, 0.01]
                            }
                        ],
                        yAxis: [
                            {
                                type: 'category',
                                //data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口(万)']
                                data: data.data.map(function (item, i) {
                                    return item.first_name;
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
                                data: data.data.map(function (item, i) {
                                    return item.sum;
                                })
                            }
                        ]
                    }
                ]
                    , elemNormbar = $('#LAY-index-bar-left4').children('div')
                    , renderNormbar = function (index) {
                    echnormbar[index] = echarts.init(elemNormbar[index], layui.echartsTheme);
                    echnormbar[index].setOption(normbar[index]);
                    window.onresize = echnormbar[index].resize;
                };
                if (!elemNormbar[0]) return;
                renderNormbar(0);


            });
        }

        function bar_left5(data, max) {
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
                            show: true,
                            text: '监管产品',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            show: false,
                            data: ['QQ活跃度']
                        },
                        calculable: true,
                        xAxis: [
                            {
                                type: 'value',
                                max: max,
                                // show: false,
                                boundaryGap: [0, 0.01]
                            }
                        ],
                        yAxis: [
                            {
                                type: 'category',
                                //data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口(万)']
                                data: data.data.map(function (item, i) {
                                    return item.first_name;
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
                                data: data.data.map(function (item, i) {
                                    return item.sum;
                                })
                            }
                        ]
                    }
                ]
                    , elemNormbar = $('#LAY-index-bar-left5').children('div')
                    , renderNormbar = function (index) {
                    echnormbar[index] = echarts.init(elemNormbar[index], layui.echartsTheme);
                    echnormbar[index].setOption(normbar[index]);
                    window.onresize = echnormbar[index].resize;
                };
                if (!elemNormbar[0]) return;
                renderNormbar(0);


            });
        }

        function bar_right1(data) {
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
                            text: '合作行活跃TOP10',
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
                    , elemNormbar = $('#LAY-index-bar-right1').children('div')
                    , renderNormbar = function (index) {
                    echnormbar[index] = echarts.init(elemNormbar[index], layui.echartsTheme);
                    echnormbar[index].setOption(normbar[index]);
                    window.onresize = echnormbar[index].resize;
                };
                if (!elemNormbar[0]) return;
                renderNormbar(0);


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
                            text: '合作行不活跃TOP20',
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
                                axisLabel: {
                                    interval: 0
                                    , fontSize: 8
                                },
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


        function bar_right3(data, max) {
            layui.use(['carousel', 'echarts'], function () {
                var $ = layui.$
                    , echarts = layui.echarts
                    , carousel = layui.carousel;

                //console.log(data.list_bank_count);
                //console.log(data.list_bank_count.slice(-5,-1));
                //标准条形图
                var myColor = ['#1089E7', '#F57474', '#9717eb', '#F8B448', '#8B78F6'];

                var echnormbar = [], normbar = [
                    {
                        title: {
                            text: '团队统计',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            show: false,
                            data: ['QQ活跃度']
                        },
                        calculable: true,
                        xAxis: [
                            {
                                type: 'category',
                                //data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口(万)']
                                data: data.map(function (item, i) {
                                    return item.name;
                                })


                            }
                        ],
                        yAxis: [
                            {
                                type: 'value',
                                //max: max,
                                // show: false,
                                boundaryGap: [0, 0.01]
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
                                //itemStyle: {normal: {label: {show: true, position: 'top'}}},

                                //data: [18203, 23489, 29034, 104970, 131744, 630230]
                                itemStyle: {
                                    normal: {
                                        barBorderRadius: 10,
                                        label: {show: true, position: 'top'},
                                        color: function (params) {
                                            var num = myColor.length;
                                            return myColor[params.dataIndex % num]
                                        },
                                    }
                                },
                                data: data.map(function (item, i) {
                                    return item.sum;
                                })
                            }
                        ]
                    }
                ]
                    , elemNormbar = $('#LAY-index-bar-right3').children('div')
                    , renderNormbar = function (index) {
                    echnormbar[index] = echarts.init(elemNormbar[index], layui.echartsTheme);
                    echnormbar[index].setOption(normbar[index]);
                    window.onresize = echnormbar[index].resize;
                };
                if (!elemNormbar[0]) return;
                renderNormbar(0);


            });
        }

        function bar_6(data, max) {
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
                            show: true,
                            text: '客服专员&生产调度',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            show: false,
                            data: ['QQ活跃度']
                        },
                        calculable: true,
                        xAxis: [
                            {
                                type: 'value',
                                max: max,
                                // show: false,
                                boundaryGap: [0, 0.01]
                            }
                        ],
                        yAxis: [
                            {
                                type: 'category',
                                //data: ['巴西', '印尼', '美国', '印度', '中国', '世界人口(万)']
                                data: data.data.map(function (item, i) {
                                    return item.first_name;
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
                                data: data.data.map(function (item, i) {
                                    return item.sum;
                                })
                            }
                        ]
                    }
                ]
                    , elemNormbar = $('#LAY-index-bar-6').children('div')
                    , renderNormbar = function (index) {
                    echnormbar[index] = echarts.init(elemNormbar[index], layui.echartsTheme);
                    echnormbar[index].setOption(normbar[index]);
                    window.onresize = echnormbar[index].resize;
                };
                if (!elemNormbar[0]) return;
                renderNormbar(0);


            });
        }

        function bar_7(data) {
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
                            text: '村镇重点客户',
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
                    , elemNormbar = $('#LAY-index-bar-7').children('div')
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
        exports('qq_data', {})

    }
);