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

            var start_date = '2020-03-28';
            var end_date = '2020-04-03';
            form.val('example', {
                "start_date": start_date // "name": "value"
                , "end_date": end_date
            });

            function swInit(input_date) {
                var index = layer.load(1);
                console.log(input_date.field);
                $.post("/data_api/search_problem_count_v2/",
                    input_date.field,
                    function (data, status) {
                        console.log("Data: " + data + "\nStatus: " + status);
                        console.log(data);

                        index_1(data);
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
                            data: ['解答', '录入', '评论']
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
                                data: data.oper_all_sum.map(function (item, i) {
                                    return item.first_name;
                                })
                            }
                        ],
                        series: [
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
                        ]
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