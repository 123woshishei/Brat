
// =======模板===================================================================================================================

$("#muban_top").mouseenter(function () {
    $("#muban_menu").slideDown(100);
});
$('#muban_menu').mouseleave(function () {
    $("#muban_menu").delay(500).slideUp();
});


// var sdf = document.referrer;
// console.log('location.href',sdf);


$("#muban_menu_collection").on('click',function () {
    // location.href = document.referrer;
    location.href = location.href.slice(0,54);
});

$("#muban_menu_wenhao").on('click',function () {
   window.open("http://brat.nlplab.org/manual.html");
});



// 获取指定名称的cookie值：getCookie(name) 该函数返回名称为name的cookie值，如果不存在则返回空
function getCookie(name){
     var strCookie=document.cookie;
     var arrCookie=strCookie.split("; ");
     for(var i=0;i<arrCookie.length;i++){
           var arr=arrCookie[i].split("=");
           if(arr[0]==name)return arr[1];
     }
     return "";
}
var csrftoken = getCookie('csrftoken');
console.log('csrftoken',csrftoken);

 function csrfSafeMethod(method) {
     // these HTTP methods do not require CSRF protection(这些HTTP方法不需要CSRF保护。)
     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
 }
$.ajaxSetup({
     crossDomain: false, // obviates need for sameOrigin test(消除对同一来源测试的需要)
     beforeSend: function(xhr, settings) {
         if (!csrfSafeMethod(settings.type)) {
             xhr.setRequestHeader("X-CSRFToken", csrftoken);
         }
     }
 });

// ======蒙板============================================================================================================

$("#mengban_shuoming_ok").on('click',function () {
   $("#mengban_shuoming").css('display','none');
   $("#mengban_open").css('display','block');
});
$("#mengban_shuoming_x").on('click',function () {
   $("#mengban_shuoming").css('display','none');
   $("#mengban_open").css('display','block');
});


$(".mengban_open_tr").on('click',function () {
   $(this).css('backgroundColor','rgb(193,193,193)');
   $('.mengban_open_tr').not($(this)).css('backgroundColor','#fcfdfd');
   var inputValue = $(this).children().eq(1).html();
   $("#mengban_open_path").val(inputValue);
});


// $(".mengban_open_return").dblclick(function () {
//    alert(location.href);
// });


$(".mengban_open_tr").dblclick(function () {
    var inputValue = $(this).children().eq(1).html();
    console.log('inputValue',inputValue);
    location.href = inputValue;
    // $('#mengban_open_path').val(inputValue);
    // if(inputValue == 'one/'){
    //     $('#mengban_open_tbody').load('one/',{pat:inputValue},function () {
    //         // $result = $(result);
    //         // $result.find('script').appendTo('#document_one');
    //        // alert(location.href+inputValue);
    //     });
    // }else if(inputValue == 'two/'){
    //     $('#mengban_open_tbody').load('two/',function () {
    //        // alert(location.href+inputValue);
    //     });
    // }

});

$('#mengban_open_x').on('click',function () {
    location.href = 'http://'+location.host+'/cancel/';
});

$('#mengban_open_cancel').on('click',function () {
   location.href = 'http://'+location.host+'/cancel/';
});

$(document).ready(function () {
   var a = location.href.split('/');
   var b = a[(a.length - 2)];
   console.log(b);
   var c = document.referrer;
   console.log(c);
   if(b != 'mengban.html'){
        $("#mengban_shuoming").css('display','none');
        $("#mengban_open").css('display','block');
   }else {

   }
});

//
// // 获取指定名称的cookie值：getCookie(name) 该函数返回名称为name的cookie值，如果不存在则返回空
// function getCookie(name){
//      var strCookie=document.cookie;
//      var arrCookie=strCookie.split("; ");
//      for(var i=0;i<arrCookie.length;i++){
//            var arr=arrCookie[i].split("=");
//            if(arr[0]==name)return arr[1];
//      }
//      return "";
// }
//
// var csrftoken = getCookie('csrftoken');
// console.log(csrftoken);
// // console.log(getCookie('shiti'));
