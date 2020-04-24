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


            function swInit(input_date) {
                var index = layer.load(1);
                console.log(input_date.field);
                $.post("/data_api/search_problem/score/count/",
                    input_date.field,
                    function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                        console.log(data);

                        index_1(data.data1);
                        index_2(data.data3);
                        // line_left2(data);

                        // bar_right1(data);
                        $("p#val_score_all").text(data.data2.val_score_all);
                        $("span#var_score_day").text(data.data2.var_score_day);


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

                console.log(data);
                console.log(data.list_first_name);
                var myColor = ['#1089E7', '#F57474', '#9717eb', '#F8B448', '#8B78F6'];
                var echheapbar = [], heapbar = [
                    {
                        title: {
                            text: '',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis',
                            axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                type: 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                            }
                        },
                        legend: {
                            //data: ['解答', '录入', '评论']
                            data: data.list_dict_series.map(function (item, i) {
                                return item.name;
                            })
                        },
                        calculable: true,
                        xAxis: [
                            {
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
                                data: data.list_first_name.map(function (item, i) {
                                    return item.first_name;
                                })
                            }
                        ],
                        series: data.list_dict_series
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
                            text: '日积分量统计',
                            subtext: '数据来自小鲲数据中台'
                        },
                        tooltip: {
                            trigger: 'axis'
                        },

                        legend: {
                            data: ['日积分量']
                        },


                        //vlegend: new_data.legend,
                        calculable: true,
                        xAxis: [
                            {
                                type: 'category',
                                // data: ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月']
                                data: data.map(function (item, i) {
                                    return item.DATE;
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
                                name: '日积分量',
                                type: 'bar',
                                // data: [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3],
                                data: data.map(function (item, i) {
                                    return item.score__sum;
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
        exports('qq_data_search_problem_score', {})

    }
);