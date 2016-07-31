/**
 * Created by peter on 2015/8/14.
 */
var token = '2a5ee64c-35cd-11e5-88fc-ecf4bbd6bc40';
var base_url = 'http://api.nlp.baifendian.com';
var CONFIG = {
    "sentiment_weibo": "/sentiment_weibo",
    "sentiment_auto": "/sentiment_auto",
    "sentiment_news": "/sentiment_news",
    "sentiment_finance": "/sentiment_finance",
    "auto_summary": "/auto_summary",
    "result_url": "result",
    "keywords_url": "/keywords",
    "media_label": "/media_label",
    "item_label": "/item_label",
    "reputation": "/reputation",
    "crawle_weibo": "/crawle_weibo",
    "crawle_media": "/crawle_media"

};
//默认的口碑按钮
var repu_module = 'mobile';
//默认的情感按钮
var SENTIMENT_MODULE = 'sentiment_weibo';

//标签提取默认按钮
var LABEL_MODULE = 'media_label';

// 去除字符串首尾空格
function trimStr(str) {
    return str.replace(/(^\s*)|(\s*$)/g,"");
}

function getData() {
    var ds = $("#datasource").val();
    console.log(ds);
    if (ds == "nods") {

    } else if (ds == "weibo") {
        getDataFromWeibo();
    } else if (ds == "url") {
        getDataFromUrl();
    }

}

//定义图表颜色，按照顺序0,1,2,3,4    top5
COLOR_DICT = {
    "0": "#0099fe",
    "1": "#e75b8d",
    "2": "#53a93f",
    "3": "#fb6e52",
    "4": "#2de1e8"
}

//单文本模式single
//多文本模式multiple
var mode = 'multiple';
function showPanel(pid) {
    if (pid == "sentiment_result") {
        $('#compare_result').hide();
        $('#sentiment_result').tab('show');
        mode = 'multiple';
        $('#' + pid).show();
    } else if (pid == "compare_result") {
        $('#sentiment_result').hide();
        $('#compare_result').tab('show');
        mode = 'single';
        $('#' + pid).show();
    } else if (pid == "single") {
        mode = 'single';
    } else if (pid == "multiple") {
        mode = 'multiple';
    }
}



//商品标签
function item_label(t) {
    $('#tags_result').empty();
    changeButtonColor(t);
    LABEL_MODULE='item_label';
    var url = $("#tags_url").val();

    // 加载抓取的内容
    $.post(CONFIG.crawle_media, {'token': token, 'url': url}, function (data) {
        var result = eval(data);
	var title = result.title;
        if (result.status == '10'){
            $("#tags_content").text('提示：链接无效');
            return;
        }

        $("#tags_content").text('标题：'+title);

        //提取商品标签
        var num = 10;
        var title = $("#tags_content").text();
        $.post(CONFIG.item_label, {'token': token, "title": title}, function (data) {
            var result = eval(data);
            // console.log(result);
            //添加商品类别
            $('#tags_result').append('<div style="width:100%;" id="item_category">');
            $('#item_category').append('<div class="panel-title">所属类别</div>');
            //遍历类别
            $.each(result.category, function (i, v) {
                $('#item_category').append('<div class="ants-tag"><span class="num">' + i + '</span><span class="desc">' + v + '</span> </div>');
            });
            //添加标签属性
            //$('#tags_result').append('<div style="width:100%;" id="tag_props">');
            //$('#tag_props').append('<div class="panel-title">标签属性</div>');
            //$.each(result.attr, function (i, v) {
            //    $('#tag_props').append('<div class="ants-label-tag"> <span class="ants-label">'+i+'</span> <span class="ants-name">'+v+'</span> </div>');
            //});

            //添加标签属性
            //$('#tags_result').append('<div style="width:100%;" id="tag_props">');
            //$('#tag_props').append('<div class="panel-title">标签属性</div>');
            if(result.attr != null) {
                $('#tags_result').append('<div style="width:100%;" id="tag_props">');
                $('#tag_props').append('<div class="panel-title">标签属性</div>');
                $.each(result.attr, function (i, v) {
                    $('#tag_props').append('<div class="ants-label-tag"><span class="ants-label">' + i + '</span><span class="ants-name">' + v + '</span></div>');
                });
            }

        });
        $('#auto_summary_input').val(title);
    });
}

function load_label(){

    var btn = $('#btn_'+LABEL_MODULE);
    // var media = $('#btn_media_label').hasClass('light_btn2');
    // var item = $('#btn_item_label').hasClass('light_btn2');

    // validate: url mustn't empty
    var url = $('#tags_url').val();
    url = trimStr(url);
    if('' == url){
        $("#tags_content").html('提示：请输入要提取标签的URL地址！');
        return false;
    }

    // // validate: must be choose one of media and item
    // if(false == media && false == item){
    //    $("#tags_content").html('提示：请选择需要提取的文本属于"媒体"类型，还是“商品”类型！');
    //    return false;
    // }

    // validate: url must be avaliable
    $("#tags_content").html('');
    if(LABEL_MODULE == 'media_label'){
    	media_label(btn);
    } else {
        item_label(btn);
    }

}

//媒体标签
function media_label(t) {
    $('#tags_result').empty();
    changeButtonColor(t);
    var url = $("#tags_url").val();
    $("#tags_content").text();
    LABEL_MODULE = 'media_label';

    $.post(CONFIG.crawle_media, {'token': token, 'url': url}, function (data) {
        var result = eval(data);
	var content = result.result;
        if (result.status == '10'){
            $("#tags_content").text('提示：链接无效');
            return;
        }

        $("#tags_content").text(content);

        //提取媒体标签
        var content = $("#tags_content").text();
        var num = 10;
        $('#tags_result').empty();
        $.post(CONFIG.media_label, {'token': token, "num": num, 'content': content}, function (data) {
            var result = eval(data);
            console.log(result);

            $('#tags_result').append('<div style="width:100%;" id="item_category">');
            $('#item_category').append('<div class="panel-title">品类</div>');
            $('#item_category').append('<div class="ants-tag"><span class="num">1</span><span class="desc">'+ result.category+'</span> </div>');


            //$('#tags_result').append('<span>品类</span>');
            //$('#tags_result').append('<button class="btn btn-sm"   data-toggle="buttons">' + result.category + '</button></br>');
            //$('#tags_result').append('<span>关键字:</span>');
    //添加标签属性
            $('#tags_result').append('<div style="width:100%;" id="tag_props">');
            $('#tag_props').append('<div class="panel-title">标签属性</div>');
            $.each(result.keywords, function (i, v) {
            	$('#tags_result').append('<button class="btn btn-sm" data-toggle="buttons">' + v + '</button>');
            });
        });
        $('#auto_summary_input').val(content);
    });
}

//情感分析提交
function get_sentiment(){
    getSentiment(SENTIMENT_MODULE);
}


function changeButtonColor(t){
    $(t).parent().siblings('div').children().removeClass('light_btn2');
    $(t).addClass('light_btn2');
}


function changeColor(t){
    $(t).siblings('button').removeClass('light_btn2');
    $(t).addClass('light_btn2');
}

//// 去除字符串首尾空格
//function trimStr(str) {
//    return str.replace(/(^\s*)|(\s*$)/g,"");
//}

//情感分析
function getSentiment(module) {
    changeButtonColor($('#btn_'+module));
    SENTIMENT_MODULE = module;
    var url = CONFIG.sentiment_weibo;
    if (module == 'sentiment_weibo') {
        url = CONFIG.sentiment_weibo;
    } else if (module == 'sentiment_news') {
        url = CONFIG.sentiment_news;
    } else if (module == 'sentiment_auto') {
        url = CONFIG.sentiment_auto;
    } else if (module == 'sentiment_finance') {
        url = CONFIG.sentiment_finance;
    }

    //处理单行文本
    if (mode == 'single') {
        var content = $('#sentiment_input_data').val();
        var content = trimStr(content);
	if('' == content){
	    // alert(content);
            $('#compare_result').html("提示：文本输入不能为空!");
	    return false;
        }
	$("#emotion_positive").html("");
	$("#emotion_negitive").html("");
	// alert(content);
       $.post(url, {'token': token, 'content': content,'mode':mode}, function (data) {
          var $t = $('#compare_result') ;
            var result =eval(data);
            var str = ''; posImg = 0 ; negImg = 0;
            $('#compare_result').empty();
            //var res =result.result || 100;
            var res =result.result;
            var pos ,neg;
            if(url=='/sentiment_finance'){
                if(res<0){
                    res = 0 ;

                }else if(res > 0){
                    res =100;
                }else{

                    res = 50;
                }
            }
            pos = res*($t.width()-40-3)/2/100;
            neg = ($t.width()-40-3)/2 -pos;
            posImg = (pos-21) > 0 ? (pos-21)  : 0;
            negImg = (neg-21) > 0 ? (neg-21) : 0;

            str = '<div style="width:'+($t.width())+'px;text-align:center;height:50px;margin:150px 20px 0px 20px;">'
                  + '<div class="ants-positive" style="width: '+($t.width()-40-3)/2+'px;height: 20px;float: left;text-align: center;" >'
                  + '<img src="/static/images/icon_face_2.png"  style="right:'+0+'px;">'
                  +'<div class="pos-percent" style="right: 0px;width:'+pos+'px;" ></div>'
                  +'</div>'
                  + '<div style="width: 3px;height: 40px;float: left;" ></div>'
                  + '<div class="ants-negtive" style="width: '+($t.width()-40-3)/2+'px;height: 20px;float: left; text-align: center;" >'
                  + '<img src="/static/images/icon_face_1.png" style="left:'+0+'px;">'
                  + '<div class="neg-percent" style="left: 0px;width:'+neg+'px;"></div>'
                  + '</div>'
                  + '</div>'
                  + '<div class="show-band" style="margin:30px 20px 0px 20px;"><span  style="color:#DF0615;width:'+($t.width()-40-3)/2+'px;">正面 <em>'+res+'%</em></span><span style="color:#0099FE;width:'+($t.width()-40-3)/2+'px;">负面<em>'+(100-res)+'%</em></span></div>';
                  $('#compare_result').html(str);
                  setTimeout(function(){

                    $t.find(".ants-positive img").css({"right":posImg+'px'});

                    $t.find(".ants-negtive img").css({"left":negImg+'px'});

                  }, 500);
            });

        //同步内容到热点分析
        $('#keywords_input_data').val(content);

        //微博抓取多行文本
    } else if (mode == 'multiple') {
        var content = $('#sentiment_crawle_data').val();
        var content = trimStr(content);
        if('' == content){
            // alert(content);
            $('#emotion_positive').html("提示：抓取系统内容不能为空!");
            return false;
        }
        $('#emotion_positive').html("");
        $('#emotion_negitive').html("");
        $.post(url, {'token': token, 'content': content, 'mode': mode}, function (data) {
            $('#emotion_positive').append('<table width="100%" cellpadding="5" style="color:#555; font-size:13px;" id="ul_emotion_positive">');
            $('#emotion_negitive').append('<table width="100%" cellpadding="5" style="color:#555; font-size:13px;" id="ul_emotion_negitive">');
            console.log(data);
            $('#ul_emotion_positive').empty();
            $('#ul_emotion_negitive').empty();
            var result = eval(data);
            if (typeof result.pos_result != "undefined" ){
            $.each(result.pos_result, function (i, v) {
                $('#ul_emotion_positive').append('<tr><td><div id="pos_tag_' + i + '" style="width:55px;height:55px;"></div></td><td>' + v.text + '</td></tr>');
                $('#pos_tag_' + i).radialIndicator({
                    barColor: COLOR_DICT[i],
                    radius: 26,
                    barWidth: 3,
                    fontSize: 20,
                    initValue: v.weight,
                    roundCorner: true,
                    percentage: true
                });
            });
            }
            if (typeof result.neg_result != "undefined" ){
             $.each(result.neg_result, function (i, v) {
                 var v_weight = 100 - v.weight;
                $('#ul_emotion_negitive').append('<tr><td><div id="neg_tag_' + i + '" style="width:55px;height:55px;"></div></td><td>' + v.text + '</td></tr>');
                $('#neg_tag_' + i).radialIndicator({
                    barColor: COLOR_DICT[4 - i],
                    radius: 26,
                    barWidth: 3,
                    fontSize: 20,
                    initValue: v_weight,
                    roundCorner: true,
                    percentage: true
                });
            });
            $('#emotion_positive').append('</table>');
            $('#emotion_negitive').append('</table>')
            }
        });


    }
}


//自动摘要
function auto_summary() {
    var auto_summary_input = $("#auto_summary_input").val();
    console.log(auto_summary_input);
    $("#auto_summary_result").empty();
    
    auto_summary_input = trimStr(auto_summary_input);
    if('' == auto_summary_input){
        $("#auto_summary_result").html('提示：请输入自动摘要文本！');
        return false;
    }
 
    // window.sessionStorage.setItem('token', '2222');
    //var t = window.sessionStorage.getItem("token");
    //alert(token);
    //if(null != t){
    //    token = t;
    //    alert("if");
    //} else {
    //    token = token;
    //    alert("else");
    //}
    //alert("token: "+token);

    $.post(CONFIG.auto_summary, {
        'token': token,
        'content': auto_summary_input,
        'language': 'chinese'
    }, function (data) {
        console.log(data);

        $("#auto_summary_result").empty();
        $("#auto_summary_result").append('<p>' + data + '</p>');
    });
}

//关键字提取

function get_keywords() {
    var hot_text_input = '';
    var info = '';
    if (mode == 'multiple') {
        hot_text_input = $('#keywords_crawle_data').val();
        info = '提示：抓取系统内容不能为空！';
    } else if (mode == 'single') {
        hot_text_input = $('#keywords_input_data').val();
        info = '提示：文本输入内容不能为空！';
        $('#sentiment_input_data').val(hot_text_input);
    }
    
    var hot_text_input = trimStr(hot_text_input);
    if('' == hot_text_input){
        // alert(content);
        $('#hot_words').html(info);
        return false;
    }
    $('#hot_words').html("");

    $.post(CONFIG.keywords_url, {'token': token, 'content': hot_text_input, 'num': 30}, function (data) {
        result = eval(data)
        $("#hot_words").empty();
         autoResize: true
        $("#hot_words").jQCloud(result.result,{ autoResize: true});
    });

}


var reputation_result;
//口碑分析
function changeData(module) {
    $('#reputation_tags').empty();
    $('#reputation_lists').empty();
    //var current_task_id = $('#current_task_id').val();

    $.post(CONFIG.reputation, {'token': token, 'module': repu_module}, function (data) {
        var result = eval(data)
        var reputation_input_text ='';
        $.each(result['input_data'],function(i, v){
            var inx = i+1
            reputation_input_text  += inx+'.'+v+'\n';
        });
        $('#reputation_input_text').val(reputation_input_text);

        reputation_result = result['result'];
        $.each(reputation_result, function (i, v) {
            $('#reputation_tags').append('<button class="btn btn-sm" data-toggle="buttons" onclick="load_reputation(event)">' + i + '</button>');
        });
        $('#reputation_tags:first-child').children("button").first().click();

    });
}

function load_reputation(event) {
    $('#reputation_lists').empty();
    var btdata = $(event.target).text();
    changeColor(event.target);
    $.each(reputation_result[btdata], function (i, v) {
        $('#reputation_lists').append('<li class="list-group-item">' + v + '</li>');
    })
}


function load_repuation_data(mod) {
    repu_module = mod;
    changeButtonColor($('#btn_reputation_'+mod))
    changeData(repu_module);
}


function crawler_sentiment() {
    var sentiment_keywords = $('#sentiment_keywords').val();
    $('#hotwords_keywords').val(sentiment_keywords);

    $.post(CONFIG.crawle_weibo, {'keyword': sentiment_keywords}, function (data) {
        var result = eval(data)
        console.log(result);
        reputation_result = result['result'];
        console.log(reputation_result);
        var input_data = '';
        $.each(reputation_result, function (i, v) {
            input_data += removeHTMLTag(v) + '\n';
        });
        $('#sentiment_crawle_data').val(input_data);
        $('#keywords_crawle_data').val(input_data);
    });
}

function crawler_hotwords() {
    var hotwords_keywords = $('#hotwords_keywords').val();
    $('#sentiment_keywords').val(hotwords_keywords);
    $.post(CONFIG.crawle_weibo, {'keyword': hotwords_keywords}, function (data) {
        var result = eval(data)
        reputation_result = result['result'];
        console.log(reputation_result);
        var input_data = '';
        $.each(reputation_result, function (i, v) {
            input_data += removeHTMLTag(v) + '\n';
        });
        $('#sentiment_crawle_data').val(input_data);
        $('#keywords_crawle_data').val(input_data);

    });
}

function removeHTMLTag(str) {
            str = str.replace(/<\/?[^>]*>/g,''); //去除HTML tag
            str = str.replace(/[ | ]*\n/g,'\n'); //去除行尾空白
            //str = str.replace(/\n[\s| | ]*\r/g,'\n'); //去除多余空行
            str=str.replace(/&nbsp;/ig,'');//去掉&nbsp;
            return str;
    }



//token调用次数统计
function tokenCounts(){
    var username = $('#username').val();
    $.post('tokenCounts', {'username': username}, function (data) {
        var result = eval(data)
        tkCounts = result['result'];
        $.each(tkCounts, function (i, v) {
            console.log(v);
        });
    });
}

