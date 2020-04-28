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


            form.val('example', {
                "start_date": start_date // "name": "value"
                , "end_date": end_date
            });

            var options = {
                useEasing: true,  // 过渡动画效果，默认ture
                useGrouping: true,  // 千分位效果，例：1000->1,000。默认true
                separator: ',',   // 使用千分位时分割符号
                decimal: '.',   // 小数位分割符号
                prefix: '',    // 前置符号
                suffix: ''    // 后置符号，可汉字
            };

            var tmp_num = 0;

            function swInit(input_date) {
                var index = layer.load(1);
                console.log(input_date.field);
                $.post("/data_api/search_problem_count_v2/",
                    input_date.field,
                    function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                        console.log(data);

                        var num1 = new CountUp('card1_info_count', tmp_num, data.data0.card1_info_count, 0, 1, options);
                        num1.start();
                        tmp_num = data.data0.card1_info_count

                        $("p#card1_answer_suc").text('解答率：' + data.data0.card1_answer_suc + '%');
                        $("p#card1_auth_suc").text('认证率：' + data.data0.card1_auth_suc + '%');

                        $("p#card2_input_count").text('录入：' + data.data0.card2_input_count);
                        $("p#card2_answer_count").text('解答：' + data.data0.card2_answer_count);
                        $("p#card2_comments_count").text('评论：' + data.data0.card2_comments_count);
                        $("p#card2_auth_count").text('认证：' + data.data0.card2_auth_count);


                        index_1(data);
                        index_2(data);
                        index_3(data);
                        // line_left2(data);

                        // bar_right1(data);


                        layer.close(index);
                    }
                );
            }

            swInit({field: {start_date: start_date, end_date: end_date}});
            //监听提交
            form.on('submit(demo1)', function (data) {
                console.log(data.field);
                swInit(data);
                return false;
            });

        });


        function index_1(data) {
            //标准折线图
            layui.use(['carousel', 'echarts'], function () {
                var $ = layui.$
                    , echarts = layui.echarts
                    , carousel = layui.carousel;

                var myColor = ['#1089E7', '#F57474', '#9717eb', '#F8B448', '#8B78F6'];
                var echheapbar = [], heapbar = [
                    {
                        title: {
                            text: '综合排行榜',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            }
                        },
                        legend: {
                            data: data.data1.list_dict_series.map(function (item, i) {
                                return item.name;
                            })
                        },
                        calculable: true,
                        grid: {y: 70},
                        xAxis: [
                            {
                                position: 'top',
                                type: 'value'

                            }
                        ],
                        yAxis: [
                            {
                                type: 'category',
                                axisLabel: {
                                    interval: 0
                                    , fontSize: 8
                                },
                                //data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                                data: data.data1.list_first_name.map(function (item, i) {
                                    return item.first_name;
                                })
                            }
                        ],
                        series: data.data1.list_dict_series
                        /*[
                        {
                            name: '解答',
                            type: 'bar',
                            stack: '总量',
                            itemStyle: {normal: {label: {show: true, position: 'insideLeft'}, color: '#168a76'}},
                            // data: [320, 302, 301, 334, 390, 330, 320]
                            data: data.oper_all_sum.map(function (item, i) {
                                return item.answer_sum;
                            })
                        },
                        {
                            name: '录入',
                            type: 'bar',
                            stack: '总量',
                            itemStyle: {normal: {label: {show: true, position: 'insideLeft'}, color: '#2bb1c2'}},
                            // data: [120, 132, 101, 134, 90, 230, 210]
                            data: data.oper_all_sum.map(function (item, i) {
                                return item.input_sum;
                            })
                        },
                        {
                            name: '评论',
                            type: 'bar',
                            stack: '总量',
                            itemStyle: {normal: {label: {show: true, position: 'right'}, color: '#e74732'}},
                            // data: [220, 182, 191, 234, 290, 330, 310]
                            data: data.oper_all_sum.map(function (item, i) {
                                return item.comments_sum;
                            })
                        }
                    ]*/
                    }
                ]
                    , elemheapbar = $('#LAY-index-1').children('div')
                    , renderheapbar = function (index) {
                    echheapbar[index] = echarts.init(elemheapbar[index], layui.echartsTheme);
                    echheapbar[index].setOption(heapbar[index]);
                    window.onresize = echheapbar[index].resize;
                };
                if (!elemheapbar[0]) return;
                renderheapbar(0);

            });
        }

        function index_2(data) {
            layui.use(['carousel', 'echarts'], function () {
                var $ = layui.$
                    , carousel = layui.carousel
                    , echarts = layui.echarts;

                //标准柱状图
                var echnormcol = [], normcol = [
                    {
                        title: {
                            text: '每日统计',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },

                        legend: {
                            data: ['录入']
                        },


                        //vlegend: new_data.legend,
                        calculable: true,
                        xAxis: [
                            {
                                type: 'category',
                                // boundaryGap: false,
                                // data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
                                data: data.index_2.data.map(function (item, i) {
                                    return item.date;
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
                                name: '录入',
                                type: 'bar',
                                // data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                                data: data.index_2.data.map(function (item, i) {
                                    return item.count;
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
                    , elemNormcol = $('#LAY-index-2').children('div')
                    , renderNormcol = function (index) {
                    echnormcol[index] = echarts.init(elemNormcol[index], layui.echartsTheme);
                    echnormcol[index].setOption(normcol[index]);
                    window.onresize = echnormcol[index].resize;
                };
                if (!elemNormcol[0]) return;
                renderNormcol(0);
            });
        }

        function index_3(data) {
            layui.use(['carousel', 'echarts'], function () {
                var $ = layui.$
                    , carousel = layui.carousel
                    , echarts = layui.echarts;

                //堆积折线图
                var echheapline = [], heapline = [
                    {
                        title: {
                            // text: '每日统计',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },
                        legend: {
                            // data: ['邮件营销', '联盟广告']
                            data: data.index_3.series.map(function (item, i) {
                                return item.name;
                            }),
                        },
                        calculable: true,
                        xAxis: [
                            {
                                type: 'category',
                                boundaryGap: false,
                                // data: ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
                                data: data.index_3.list
                            }
                        ],
                        yAxis: [
                            {
                                type: 'value'
                            }
                        ],
                        series: data.index_3.series
                        /* [
                        {
                            name: '邮件营销',
                            type: 'line',
                            stack: '总量',
                            data: [120, 132, 101, 134, 90, 230, 210]
                        },
                        {
                            name: '联盟广告',
                            type: 'line',
                            stack: '总量',
                            data: [220, 182, 191, 234, 290, 330, 310]
                        }
                    ]*/
                    }
                ]
                    , elemheapline = $('#LAY-index-3').children('div')
                    , renderheapline = function (index) {
                    echheapline[index] = echarts.init(elemheapline[index], layui.echartsTheme);
                    echheapline[index].setOption(heapline[index]);
                    window.onresize = echheapline[index].resize;
                };
                if (!elemheapline[0]) return;
                renderheapline(0);
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
        exports('qq_data_search_problem', {})

    }
);