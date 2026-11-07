 বৈদেশিক কর্মসংস্থান ও অভিবাসী আইন, ২০১৩ | ১৪ক। সাব-এজেন্ট বা প্রতিনিধি নিয়োগ, ইত্যাদি 
    .navbar-left ul
    {
      padding-left: 0px;
    }
             <img class="img-responsive logo"
                                           src="/resources/website/assets/img/laws-of-bangadesh-logo-bn.png"
                                           alt="bangladesh -logo"> 
                            <input id="search-click" name="q"
                                   value="" class="form-control"
                                   placeholder="টেক্সট অনুসারে অনুসন্ধান করুন"/>
                         <i
                                class="fa fa-search">  
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                 Toggle navigation 
                  হোম   
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">লজ অব বাংলাদেশ
                          কালানুক্রমিক সূচী   
                          বর্ণানুক্রমিক সূচী   
                          আইন অনুসন্ধান  
                  সংশ্লিষ্ট সংযোগ 
                  যোগাযোগ/অভিমত   
                  পূর্বতন ওয়েবসাইট  
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">সাহায্য    
                          অনুসন্ধান   
                          প্রিন্ট   
                          শব্দকোষ   
                          রোমান সংখ্যা   
                          যোগাযোগ/অভিমত  
                      বাংলা   |  English    
    .print-only{
        display: none;
        visibility: hidden;
    }
    @media print {
        .no-print {
            display: none;
        }
        .print-only{
            display: none;
            visibility: hidden;
        }
    }
<a target="_blank" href="/act-print-1131/section-print-52936.html" class="pull-right no-print" style="width: 72px;height: 80px;margin-right: -50px;
margin-bottom: 7px;"> 
    <p class="pull-right" style="margin-right: -40px;
margin-bottom: 7px;color:#FF3399">প্রিন্ট ভিউ 
            <p class="pull-right" style="margin-right: -100px;
margin-bottom: 7px;margin-top:15px;">[সেকশন সূচি]
                        বৈদেশিক কর্মসংস্থান ও অভিবাসী আইন, ২০১৩
                              (
                                        ২০১৩ সনের ৪৮ নং
                                            আইন
                                )
                     <i class="fa fa-arrow-left" title="Back"
                                                                                 aria-hidden="true">   
                    [ ২৭ অক্টোবর, ২০১৩  ]
    <section
            class="padding-bottom-20  ">
                            তৃতীয় অধ্যায়
                            রিক্রুটিং এজেন্ট, লাইসেন্স, ইত্যাদি
                         সাব-এজেন্ট বা প্রতিনিধি নিয়োগ, ইত্যাদি
                     1    [১৪ক।  কোন রিক্রুটিং এজেন্ট, বিধি দ্বারা নির্ধারিত পদ্ধতিতে, নিবন্ধিত কোন ব্যক্তিকে সাব-এজেন্ট বা প্রতিনিধি নিয়োগ করিতে পারিবে এবং সাব-এজেন্ট বা প্রতিনিধির দায়িত্ব ও কর্তব্য বিধি দ্বারা নির্ধারিত হইবে।] 
                    1   ধারা ১৪ক  বৈদেশিক কর্মসংস্থান ও অভিবাসী (সংশোধন) আইন, ২০২৩  (২০২৩ সনের ৪১ নং আইন) এর ৪ ধারাবলে সন্নিবেশিত। 
         Copyright  ©  2019, Legislative and Parliamentary Affairs Division  
         Ministry of Law, Justice and Parliamentary Affairs 
    function onSubmit(token) {
        document.getElementById("recaptchaForm").submit();
    }
        $(document).ready(function() {
            $('.test-tooltip').tooltip();
            // find tags and remove
            // remove empty p tag
            $('p').each(function () {
                var $this = $(this);
                if ($this.html().replace(/\s| /g, '').length == 0)
                    $this.remove();
            });
            $(document).on('click','.advancedSearch',function (event) {
                console.log(event);
                $('.advancedSearchForm').toggle("slow");
            })
            $('[data-toggle="tooltip"]').tooltip();
            String.prototype.bn_number = function(){
                var b = String (this);
                var c = b.replace(/0/g,'০')
                        .replace(/1/g,'১')
                        .replace(/2/g,'২')
                        .replace(/3/g,'৩')
                        .replace(/4/g,'৪')
                        .replace(/5/g,'৫')
                        .replace(/6/g,'৬')
                        .replace(/7/g,'৭')
                        .replace(/8/g,'৮')
                        .replace(/9/g,'৯');
                //console.log(c);
                return c;
            }
            String.prototype.en_number = function(){
                var b = String (this);
                var c = b.replace(/০/g,'0')
                        .replace(/১/g,'1')
                        .replace(/২/g,'2')
                        .replace(/৩/g,'3')
                        .replace(/৪/g,'4')
                        .replace(/৫/g,'5')
                        .replace(/৬/g,'6')
                        .replace(/৭/g,'7')
                        .replace(/৮/g,'8')
                        .replace(/৯/g,'9');
                //console.log(c);
                return c;
            }
            $(document).on("keyup","[data-td-index]",function () {
                var table = $(".table-search");
                var filter = [];
                $(this).parents("form").find("[data-td-index]").each(function (index){
                    if ($(this).val().trim()!="" && $(this).val()!=null){
                        filter.push(
                                {
                                    "bn": $(this).val().trim().toUpperCase().bn_number(),
                                    "en": $(this).val().trim().toUpperCase().en_number(),
                                    "td": $(this).data("td-index")
                                }
                        )
                     }
                })
                var trs = table.find("tbody tr");
                $.each(trs, function (index, tr) {
                    var rowShow = true;
                    $.each(filter, function (ind, val){
                        console.log(val);
                        var td = $(tr).find("td").get(val["td"]);
                        var text = $(td).text();
                        if (text.toUpperCase().indexOf(val["en"]) > -1
                        || text.toUpperCase().indexOf(val["bn"]) > -1){
                            rowShow = rowShow && true;
                        }else{
                            rowShow = false;
                        }
                    })
                    if (rowShow==true){
                        $(tr).show();
                    }else{
                        $(tr).hide();
                    }
                } )
            })
            $(document).on("keyup","[data-search]",function () {
                var searchContent = $(this).data("search");
                var filter1 = $(this).val().trim().toUpperCase().bn_number();
                var filter2 = $(this).val().trim().toUpperCase().en_number();
                var rows = $(document).find(searchContent);
                // Loop through all table rows, and hide those who don't match the search query
                for (i = 0; i < rows.length; i++) {
                    var row = rows[i];
                    if (row) {
                        if ($(row).text().toUpperCase().indexOf(filter1) > -1
                                ||$(row).text().toUpperCase().indexOf(filter2) > -1
                        ) {
                            $(row).show();
                        } else {
                            $(row).hide();
                        }
                    }
                }
            })
            $(document).find(".removableRowTable").each(function (index) {
                console.log($(this).find("tbody tr").length);
                $(this).find("tbody").each(function () {
                    if ($(this).find("tr").length<=1){
                        $(this).remove();
                    }
                })
            })
            $(document).on("reset","form",function () {
                var table = $(".table-search");
                var tr = table.find("tbody tr");
                // Loop through all table rows, and hide those who don't match the search query
                for (i = 0; i < tr.length; i++) {
                    tr[i].style.display = "";
                }
            })
        });
        $(document).ready(function($) {
            $('body').scrollToTop({
                distance: 200,
                speed: 1000,
                easing: 'linear',
                animation: 'fade', // fade, slide, none
                animationSpeed: 500,
                mobile: {
                    width: 768,
                    distance: 100,
                    speed: 1000,
                    easing: 'easeInOutElastic',
                    animation: 'slide',
                    animationSpeed: 200
                },
                trigger: null, // Set a custom triggering element. Can be an HTML string or jQuery object
                target: null, // Set a custom target element for scrolling to. Can be element or number
                text: '  Top', // Text for element, can contain HTML
                skin: null,
                throttle: 250,
                namespace: 'scrollToTop'
            });
        });
        function validateForm(){
            var name=document.contactUsForm.name.value;
            var message=document.contactUsForm.message.value;
            var email=document.contactUsForm.email.value;
            if (name==null || name==""){
                alert("Name can't be blank");
                return false;
            }else if(email==null || email==""){
                alert("Email can't be blank");
                return false;
            }
            else if(message==null || message==""){
                alert("Message can't be blank");
                return false;
            }
        }
    /*    $(document).ready(function(){
            loopcounter('first-counter');
            loopcounter('second-counter');
        });*/
                      সংশ্লিষ্ট সংযোগ   
                               বাংলাদেশ সরকার এর অফিসিয়াল ওয়েবসাইট  
                               লেজিসলেটিভ ও সংসদ বিষয়ক বিভাগ  
                               সংসদ সচিবালয়  
                               আইন কমিশন  
                               জাতীয় মানবাধিকার কমিশন  
                      যোগাযোগ/অভিমত   
                        লেজিসলেটিভ ও সংসদ বিষয়ক বিভাগ  
                        আইন, বিচার ও সংসদ বিষয়ক মন্ত্রণালয়  
                        বাংলাদেশ সচিবালয়, ঢাকা-১০০০, বাংলাদেশ।  
                        কপিরাইট © ২০১৯, লেজিসলেটিভ ও সংসদ বিষয়ক বিভাগ,আইন, বিচার ও সংসদ বিষয়ক মন্ত্রণালয়
                            ডিজাইন  এবং  ডেভেলপড
                                বেইজ লিমিটেড
