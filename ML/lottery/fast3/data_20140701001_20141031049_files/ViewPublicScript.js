// ͼ��ҳ���ú���
//***************************************************************************
//                  ��ʽ����
//***************************************************************************

//������ʽ
function LoadCss()
{
    var css=request("css");
    if(css != "")
    {
        try
        {
            Style(css);
        }
        catch(e)
        {
            Style("orange");
        }
    }
}
// ��ȡ��ʽ����
function request(paras)
{  
    var url = location.href;   
    var paraString = url.substring(url.indexOf("?")+1,url.length).split("&");   
    var paraObj = {}   
    for (i=0; j=paraString[i]; i++){   
        paraObj[j.substring(0,j.indexOf("=")).toLowerCase()] = j.substring(j.indexOf 
        ("=")+1,j.length);   
    }   
    var returnValue = paraObj[paras.toLowerCase()];   
    if(typeof(returnValue)=="undefined"){   
        return "css=";   
    }else{   
        return returnValue;   
    }   
}

// ѡ����ʽ��
function Style(i)
{
    var css=document.getElementById('userStyle');

    css.href="../CSS/"+i+"/"+i+'.css'; 
    css.rel="stylesheet"; 
    css.type="text/css"; 
}

// ***************************************************************************
// ��ʾ�ʾ����ṩ����
function UrlLink()
{
    document.write("<span class='Url'>�ṩ����2000������,��ͼ���ṩ��:  <a style='color:Red' href='http://www.cjcp.com.cn' target=_blank> �ʾ���</a></span>");
}
// **********************************************************************
// �ƶ���SCRIPT
// **********************************************************************
// �����ƶ�������ƶ�����
var Mouse_Obj="none",_x,_y;
// �϶�������(�Զ�)
function DivMoving()
{
	if(Mouse_Obj!=="none")
	{
	    document.getElementById(Mouse_Obj).style.left=_x+event.x;
	    document.getElementById(Mouse_Obj).style.top=_y+event.y;
	    event.returnValue=false;
	}
}
// ֹͣ�϶�����(�Զ�)
function DivMoveStop()
{
	Mouse_Obj="none";
}
// ȷ�����϶������� oΪ���϶�����
function DivMoveStart(obj)
{
	Mouse_Obj=obj;
	_x=parseInt(document.getElementById(Mouse_Obj).style.left)-event.x;
	_y=parseInt(document.getElementById(Mouse_Obj).style.top)-event.y;
}

// ***************�߼�ɸѡ
function HighJqChange(obj)
{
    var HighSelectJQ=document.getElementById("HighSelectJQ");
    HighSelectJQ.value=obj.options[obj.selectedIndex].value;
}
function MainClean()
{
    var objQishuEnd=document.getElementById("QishuEndSelect");
    objQishuEnd.value="-1";
    CleanSelect("MonthDiv","HighSelectMonth");
    CleanSelect("YangLiDiv","HighSelectYangLi");
    CleanSelect("YinLiDiv","HighSelectYinLi");
    CleanSelect("WeekDiv","HighSelectWeek");
    CleanHiddenValue("HighSelectQishuEnd");
    CleanSelect("QishuEndDiv","HighSelectQishujo");
    CleanHiddenValue("HighSelectJQ");
}
// ��ʾ���ظ߼�DIV
function Display(id)
{
    var obj=document.getElementById(id);
    var objmain=document.getElementById("HighSelectMain");
    if(obj.style.display=="none")
    {
        objmain.style.display="none";
        obj.style.display="block";
    }
    else
    {
        obj.style.display="none";
        objmain.style.display="block";
    }
    var Hselect=document.getElementById("HighSelect");
    HighSelectTopLeft(Hselect);
}

function QishuEndSelectChange(objselect)
{
    var obj=document.getElementById("HighSelectQishuEnd");
    var result=objselect.value;
    var arr;
    switch(result)
    {
        case "1":
        CleanSelect("QishuEndDiv","HighSelectQishuEnd");
        ListSelect("HighSelectQishuEnd","5,6,7,8,9","QishuEnd");
        break;
        case "2":
        CleanSelect("QishuEndDiv","HighSelectQishuEnd");
        ListSelect("HighSelectQishuEnd","0,1,2,3,4","QishuEnd");
        break;
        case "3":
        CleanSelect("QishuEndDiv","HighSelectQishuEnd");
        ListSelect("HighSelectQishuEnd","1,3,5,7,9","QishuEnd");
        break;
        case "4":
        CleanSelect("QishuEndDiv","HighSelectQishuEnd");
        ListSelect("HighSelectQishuEnd","0,2,4,6,8","QishuEnd");
        break;
        case "5":
        arr=GetPrime(0,9);
        CleanSelect("QishuEndDiv","HighSelectQishuEnd");
        ListSelect("HighSelectQishuEnd","0,1,2,3,5,7","QishuEnd");
        break;
        case "6":
        arr=GetComposite(0,9);
        CleanSelect("QishuEndDiv","HighSelectQishuEnd");
        ListSelect("HighSelectQishuEnd","4,6,8,9","QishuEnd");
        break;
        case "7":
        arr=GetZero(0,9);
        CleanSelect("QishuEndDiv","HighSelectQishuEnd");
        ListSelect("HighSelectQishuEnd",arr,"QishuEnd");
        break;
        case "8":
        arr=GetOne(0,9);
        CleanSelect("QishuEndDiv","HighSelectQishuEnd");
        ListSelect("HighSelectQishuEnd",arr,"QishuEnd");
        break;
        case "9":
        arr=GetTwo(0,9);
        CleanSelect("QishuEndDiv","HighSelectQishuEnd");
        ListSelect("HighSelectQishuEnd",arr,"QishuEnd");
        break;
    }
}

// ������ѡ��
function CleanYearSelect()
{
    var obj=document.getElementById("YearDiv");
    var objinput=obj.getElementsByTagName("div");
    for(var i=0;i<objinput.length;i++)
    {
        objinput[i].className="button_ha";
    }
    CleanHiddenValue("HighSelectYear");
}
// ���������ѡ��
function YearSelectChange()
{
    var objselect=document.getElementById("YearSelect");
    var result=objselect.value;
    switch(result)
    {
        case "1":
        CleanYearSelect();
        ListSelect("HighSelectYear","2003,2005,2007","Year");
        break;
        case "2":
        CleanYearSelect();
        ListSelect("HighSelectYear","2002,2004,2006,2008","Year");
        break;
        case "3":
        CleanYearSelect();
        ListSelect("HighSelectYear","2002,2003,2005,2007","Year");
        break;
        case "4":
        CleanYearSelect();
        ListSelect("HighSelectYear","2004,2006,2008","Year");
        break;
        case "5":
        CleanYearSelect();
        ListSelect("HighSelectYear","2003,2006","Year");
        break;
        case "6":
        CleanYearSelect();
        ListSelect("HighSelectYear","2004,2007","Year");
        break;
        case "7":
        CleanYearSelect();
        ListSelect("HighSelectYear","2002,2005,2008","Year");
        break;
    }
}

// ����·�ѡ��
function CleanSelect(DivId,HiddenId)
{
    var obj=document.getElementById(DivId);
    var objinput=obj.getElementsByTagName("div");
    for(var i=0;i<objinput.length;i++)
    {
        objinput[i].className="button_ha";
    }
    CleanHiddenValue(HiddenId);
}

// �·�������ѡ��
function MonthSelectChange()
{
    var objselect=document.getElementById("MonthSelect");
    var result=objselect.value;
    switch(result)
    {
        case "1":
        CleanSelect("MonthDiv","HighSelectMonth");
        ListSelect("HighSelectMonth","1,3,5,7,9,11","Month");
        break;
        case "2":
        CleanSelect("MonthDiv","HighSelectMonth");
        ListSelect("HighSelectMonth","2,4,6,8,10,12","Month");
        break;
        case "3":
        CleanSelect("MonthDiv","HighSelectMonth");
        ListSelect("HighSelectMonth","1,2,3,5,7,11","Month");
        break;
        case "4":
        CleanSelect("MonthDiv","HighSelectMonth");
        ListSelect("HighSelectMonth","4,6,8,9,10,12","Month");
        break;
        case "5":
        CleanSelect("MonthDiv","HighSelectMonth");
        ListSelect("HighSelectMonth","3,6,9,12","Month");
        break;
        case "6":
        CleanSelect("MonthDiv","HighSelectMonth");
        ListSelect("HighSelectMonth","1,4,7,10","Month");
        break;
        case "7":
        CleanSelect("MonthDiv","HighSelectMonth");
        ListSelect("HighSelectMonth","2,5,8,11","Month");
        break;
    }
}
// ����������ѡ��
function YangLiSelectChange()
{
    var objselect=document.getElementById("YangLiSelect");
    var result=objselect.value;
    var arr;
    switch(result)
    {
        case "1":
        CleanSelect("YangLiDiv","HighSelectYangLi");
        arr=GetOdd(1,31);
        ListSelect("HighSelectYangLi",arr,"YangLi");
        break;
        case "2":
        CleanSelect("YangLiDiv","HighSelectYangLi");
        arr=GetEven(1,31);
        ListSelect("HighSelectYangLi",arr,"YangLi");
        break;
        case "3":
        CleanSelect("YangLiDiv","HighSelectYangLi");
        arr=GetPrime(1,31);
        ListSelect("HighSelectYangLi",arr,"YangLi");
        break;
        case "4":
        arr=GetComposite(1,31);
        CleanSelect("YangLiDiv","HighSelectYangLi");
        ListSelect("HighSelectYangLi",arr,"YangLi");
        break;
        case "5":
        arr=GetZero(1,31);
        CleanSelect("YangLiDiv","HighSelectYangLi");
        ListSelect("HighSelectYangLi",arr,"YangLi");
        break;
        case "6":
        arr=GetOne(1,31);
        CleanSelect("YangLiDiv","HighSelectYangLi");
        ListSelect("HighSelectYangLi",arr,"YangLi");
        break;
        case "7":
        arr=GetTwo(1,31);
        CleanSelect("YangLiDiv","HighSelectYangLi");
        ListSelect("HighSelectYangLi",arr,"YangLi");
        break;
    }
}

// ����������ѡ��
function YinLiSelectChange()
{
    var objselect=document.getElementById("YinLiSelect");
    var result=objselect.value;
    var arr;
    switch(result)
    {
        case "1":
        CleanSelect("YinLiDiv","HighSelectYinLi");
        arr=GetOdd(1,30);
        ListSelect("HighSelectYinLi",arr,"YinLi");
        break;
        case "2":
        CleanSelect("YinLiDiv","HighSelectYinLi");
        arr=GetEven(1,30);
        ListSelect("HighSelectYinLi",arr,"YinLi");
        break;
        case "3":
        CleanSelect("YinLiDiv","HighSelectYinLi");
        arr=GetPrime(1,30);
        ListSelect("HighSelectYinLi",arr,"YinLi");
        break;
        case "4":
        arr=GetComposite(1,30);
        CleanSelect("YinLiDiv","HighSelectYinLi");
        ListSelect("HighSelectYinLi",arr,"YinLi");
        break;
        case "5":
        arr=GetZero(1,30);
        CleanSelect("YinLiDiv","HighSelectYinLi");
        ListSelect("HighSelectYinLi",arr,"YinLi");
        break;
        case "6":
        arr=GetOne(1,30);
        CleanSelect("YinLiDiv","HighSelectYinLi");
        ListSelect("HighSelectYinLi",arr,"YinLi");
        break;
        case "7":
        arr=GetTwo(1,30);
        CleanSelect("YinLiDiv","HighSelectYinLi");
        ListSelect("HighSelectYinLi",arr,"YinLi");
        break;
    }
}

// ���ÿؼ���ʽ�б�
function ListSelect(id,strList,strID)
{
    var obj=document.getElementById(id);
    var arrID=strList.split(',');
    for(var i=0;i<arrID.length;i++)
    {
        var cr=document.getElementById(strID+arrID[i]);// ���ÿؼ�״̬��ʽ
        cr.className="button_hb";
    }
    
    obj.value=strList;
}

// ���������ֵ
function CleanHiddenValue(id)
{
    var obj=document.getElementById(id);
    obj.value="";
}

function Select(id,str,obj)
{
    if(obj.className=="button_ha")
    {
        obj.className="button_hb";
    }
    else
    {
        obj.className="button_ha";
    }
    InsertValueHidden(id,str);
}

// ��ǰֵ����������
function InsertValueHidden(id,str)
{
    var obj=document.getElementById(id);
    if(obj.value=="")
    {
        obj.value=str;
        return;
    }
    var arr=obj.value.split(',');
    var index=-1;
    for(var i=0;i<arr.length;i++)
    {
        if(arr[i]!==""&&arr[i]==str)
        {
            index=i;
        }
    }
    if(index==-1)
    {
        arr.push(str); 
    }
    else
    {
        arr.splice(index,1);
    }
    obj.value=arr.join();
	
}

// ����
function GetOdd(start,end)
{
    var arr=new Array();
    for(var i=start;i<=end;i++)
    {
        if(i%2==1)
        {
            arr.push(i);
        }
    }
    return arr.join();
}
// ż��
function GetEven(start,end)
{
    var arr=new Array();
    for(var i=start;i<=end;i++)
    {
        if(i%2==0)
        {
            arr.push(i);
        }
    }
    return arr.join();
}
// ����
function GetPrime(start,end)
{
    var i,k;
    var arr = [];
    for(i=start; i<=end; i++){
      arr.push(i);
    }
    for(i=0; i<arr.length; i++){
      for(k=i+1; k<arr.length; k++){
        if(arr[k]%arr[i]==0&&i!=0){
          arr.splice(k,1);
        }
      }
    }
    return arr.join();
}
// ����
function GetComposite(start,end)
{
    var i,k;
    var arr = [];
    var newarr=[];
    for(i=start; i<=end; i++){
      arr.push(i);
    }
    for(i=0; i<arr.length; i++){
      for(k=i+1; k<arr.length; k++){
        if(arr[k]%arr[i]==0&&i!=0){
          newarr.push(arr.splice(k,1));
        }
      }
    }
    return newarr.join();
}

// 0·
function GetZero(start,end)
{
    var arr=new Array();
    for(var i=start;i<=end;i++)
    {
        if(i%3==0)
        {
            arr.push(i);
        }
    }
    return arr.join();
}
// 1·
function GetOne(start,end)
{
    var arr=new Array();
    for(var i=start;i<=end;i++)
    {
        if(i%3==1)
        {
            arr.push(i);
        }
    }
    return arr.join();
}
// 2·
function GetTwo(start,end)
{
    var arr=new Array();
    for(var i=start;i<=end;i++)
    {
        if(i%3==2)
        {
            arr.push(i);
        }
    }
    return arr.join();
}


// �ײ���ʾ��ʷ����������ͳ��
function showshiorcurrdata2(temp){
	if(temp.id=="lishi"){
		document.getElementById("yilouceng").style.display="none";
		document.getElementById("lishiyilouceng").style.display="";
		}else{
			document.getElementById("yilouceng").style.display="";
			document.getElementById("lishiyilouceng").style.display="none";
			}
	   // �������ʾ��������
	  if(document.getElementById("lqfbxs").checked==true){
	        if(temp.value=="1"){
				areaDisplayOrnot('t',34,clonum,endclum+1,endclum+5,2);
	            areaDisplayOrnot('t',34,clonum,endclum-4,endclum,1); 
	        }else{
	            areaDisplayOrnot('t',34,clonum,endclum+1,endclum+5,1);
				areaDisplayOrnot('t',34,clonum,endclum-4,endclum,2);
	        }
	        
	    }else{	    
	        // ����ʾ��������
	            areaDisplayOrnot('t',34,clonum,endclum-4,endclum,2); 
	            areaDisplayOrnot('t',34,clonum,endclum+1,endclum+5,2);
	    }
	    
}

//function moxuan(obj1){
//	obj=document.getElementById("moxuan");
//	if(obj.style.display==""){
//		obj.style.display="none";
//	}else{
//		obj.style.display=""
//	}
//	if(obj1.className == "mx_open"){
//		obj1.className = "mx_close";
//	}else if(obj1.className == "mx_close"){
//		obj1.className = "mx_open";
//	}
//	parent.SetCwinHeight(parent.document.getElementById("cwin"));
//	}
// ����ť����
function paixu1(img_obj){
     
	obj=document.getElementById("paixu_img");

	if(obj.value==""){		
		// alert("xia");
		window.location.href="?paixu=xia";	
        //document.getElementById("paixu_img").value = "xia";	
	}else{
		window.location.href="?paixu=";	
        //document.getElementById("paixu_img").value = "";    		
	}
    //document.thirdD.action="3dtubiao.php";
    //document.thirdD.submit();
}
function fan_qishu_img(obj,div_id){
	
	if(obj.src.indexOf("bg1.jpg")==-1){
		
		obj.src="../imgs/zoushi/bg1.jpg"
		
		}
		else{
			
			obj.src="../imgs/zoushi/bg2.jpg";
			}
	// alert(div_id);
	var menu=document.getElementById(div_id)
// if ( menu.style.display == "")
// {
// menu.style.display = "none"
// }
// else {
// menu.style.display = "inline"
// }
// }
	if   (   menu.style.display   ==   "inline")
    {   
    menu.style.display   =   "none"   
    }   
    else   {   
    menu.style.display   =   "inline"
    } 
	}

// ģ��ѡ�Ű�ťλ�ó�ʵ��
function mn_weizhi(){
	 document.getElementById("mn").style.left=document.getElementById("t").offsetWidth-23;
}

// �ںż�ͷ��ʼ��
function qh_jiantou(){
	var obj= new Array();
	obj=document.getElementsByName("img1");
	arrlenth=document.getElementsByName("img1").length;
	if(obj[0].style.display==""){
		for(i=0;i<arrlenth;i++){
			obj[i].style.display="none";
		}		
	}else{
		for(i=0;i<arrlenth;i++){
			obj[i].style.display="";
		}
	}
}

// ͼ�����ȸ�ֵ
function tb_width(t_width){
	var obj;
	obj=document.getElementById("t");
	// alert(screen.width );
	if(screen.width!=1440){
		obj.setAttribute("width",t_width); 
	}
	
}
// �����Ч����������
/*
 * ����˵�� No1���ؼ������ƣ���Ҫ��һ�������Ӷ��ٸ�����ϲ�� No2:�ؼ���ʼʱ��topֵ
 * No3:�ؼ���ʼʱ��leftֵ����ֵΪ������left������Ϊ����ұߵ�ֵ new couplet("id",14,24);
 */
function couplet(){
	if(arguments.length>=1) this.objID = document.getElementById(arguments[0]);
	if(arguments.length>=2) this.divTop = arguments[1]-145;
	if(arguments.length>=3) this.divPlane = arguments[2];
	if(arguments.length>=4) this.scrollDelay = arguments[4];
	if(arguments.length>=5) this.waitTime = arguments[5];
	if(!this.objID){
	alert("��������"+ arguments[0] +"����Ч�������޷���ʼ����������������Ƿ���ȷ��");
	this.objID = null; return;
	}else{
	this.objID.style.position="absolute";
	this.objID.style.display="block";
	this.objID.style.zIndex=9999;
	}
	if("" == this.objID.style.top){
	if(isNaN(this.divTop)){
	alert("����ֱλ��(top)��������Ϊ���֡�"); return;
	}else{
	this.objID.style.top = this.divTop+"px";
	}
	}
	if("" == this.objID.style.left && "" == this.objID.style.right){
	if(isNaN(this.divPlane)){
	alert("����ˮƽλ��(left||right)��������Ϊ���֡�"); return;
	}
	if(this.divPlane>0) this.objID.style.left = this.divPlane+"px";
	if(this.divPlane<0) this.objID.style.right = Math.abs(this.divPlane)+"px";
	}
	if(this.scrollDelay<15 || isNaN(this.scrollDelay)) this.scrollDelay = 15;
	if(this.waitTime<500 || isNaN(this.waitTime)) this.waitTime = 500;
	if(arguments.length>=1) this.start();
	}
	couplet.prototype.start = function(){
	if(null == this.objID) return;
	var objCouplet = this;
	timer = this.scrollDelay;
	objCouplet.lastScrollY = 0;
	objCouplet.timerID = null;
	objCouplet.startID = function(){
	if("block" == objCouplet.objID.style.display){
	objCouplet.run();
	}else{
	clearInterval(objCouplet.timerID);
	}
	}
	objCouplet.Begin = function(){
	objCouplet.timerID = setInterval(objCouplet.startID,timer);
	}

	setTimeout(objCouplet.Begin,this.waitTime);
	}
	couplet.prototype.run = function(){
	if(parent.document.documentElement && parent.document.documentElement.scrollTop){
	uu_scrY = parseFloat(parent.document.documentElement.scrollTop);
		if(uu_scrY>1114){
			uu_scrY=1114;
		}
	}else if(parent.document.body){
	uu_scrY = parseFloat(parent.document.body.scrollTop);
		if(uu_scrY>1114){
			uu_scrY=1114;
		}
	}
	uu_divX = parseFloat(this.objID.style.top.replace("px",""));
	uu_curTop = .1 * (uu_scrY - this.lastScrollY);
	uu_curTop = uu_curTop>0?Math.ceil(uu_curTop):Math.floor(uu_curTop);
	this.objID.style.top = parseFloat(uu_divX + uu_curTop) + "px";
	this.lastScrollY += uu_curTop;
	}
	
	var updateTR="";
// ������б�ɫ
	function overClass1(trName) {
		
		
		 if (updateTR != "") {
			 
			 var tn1 = document.getElementById(updateTR);

			 var tdlength1 = tn1.cells.length;
					 for (var i = 0; i < tdlength1; i++) {
					 var className = tn1.cells[i].className;
					 tn1.cells[i].className = className.replace("backChange ", "");
					 
					 }
			 }
		
		 var tn = document.getElementById(trName);
		 var tdlength = tn.cells.length;
		 for (var i = 0; i < tdlength; i++) {
		
		 tn.cells[i].className ="backChange " + tn.cells[i].className ;
		 }
		 updateTR = trName;
		}
	
function overClassDLC(trName) {
		 if (updateTR != '') {
		 var tn1 = document.getElementById(updateTR);
		 var tdlength1 = tn1.cells.length;
		 if(fenceng==1){
		 for (var i = 0; i < tdlength1; i++) {
		 var className = tn1.cells[i].className;
		 if(className ==" b10 "){
		 tn1.cells[i].style.backgroundColor="";
		 tn1.cells[i].style.backgroundColor="#d6e1f6";
		 }else if(tn1.cells[i].className =="borbottom b10 "){
		 tn1.cells[i].style.backgroundColor="";
		 tn1.cells[i].style.backgroundColor="#d6e1f6";
		 }else{
		 var className = tn1.cells[i].className;
		 tn1.cells[i].className = className.replace("backChange", "");
		
		 }
		
		 }
		 }else{
		 for (var i = 0; i < tdlength1; i++) {
		 var className = tn1.cells[i].className;
		 if(className ==" b10 "){
		 tn1.cells[i].style.backgroundColor="";
		 tn1.cells[i].style.backgroundColor="#FFF3E2";
		 }else if(tn1.cells[i].className =="borbottom b10 "){
		 tn1.cells[i].style.backgroundColor="";
		 tn1.cells[i].style.backgroundColor="#FFF3E2";
		 }else{
		 tn1.cells[i].className = className.replace("backChange", "");
		 }
		 }
		
		 }
		
		 }
		 var tn = document.getElementById(trName);
		 var tdlength = tn.cells.length;
		
		 for (var i = 0; i < tdlength; i++) {
		 if(tn.cells[i].className==" b10 "){
		 tn.cells[i].style.backgroundColor="";
		 tn.cells[i].style.backgroundColor="#DDDDDD";
		 }else if(tn.cells[i].className =="borbottom b10 "){
		 tn.cells[i].style.backgroundColor="";
		 tn.cells[i].style.backgroundColor="#DDDDDD";
		 }else{
		 tn.cells[i].className = tn.cells[i].className + " backChange";
		 }
		 }
		
		
		 updateTR = trName;
		} 
		
function dangqian_lishi(obj){
			 var tongji = document.getElementById('tongji');
			var tongji2 = document.getElementById('tongji2');
			if(obj.value==0){
				tongji.style.display="";
				tongji2.style.display="none";		
				}else if(obj.value==1){
					tongji.style.display = "none";
					tongji2.style.display= "";
					}
			 }
             
// Ԥ������Ŀ���             
function docopy(){
    var Url2=document.getElementById("copytext");
    Url2.select();
    document.execCommand("Copy"); //ִ���������������
}

// ͼ��Ƕ�׵�Ԥ��            
function doPreview(){
    window.open("preview.html","","");//��Ԥ������
}

//����js����
function killErrors() {
	return true;
}
window.onerror = killErrors;
    
//3D JavaScript by zhouec 2010/06/07
function Checkvalue(searchType)
{   
    var frm1=document.getElementById("startqi");
    var frm2=document.getElementById("endqi");
    var pageHtml = document.getElementById("pageHtml").value;
    var result=frm1.value;
    var result2=frm2.value;

    var regex=new RegExp("[0-9]{7}");
    if(!regex.test(result))
    {
        alert("����Ŀ�ʼ��������ȷ������������");
        frm1.focus();
        return false;
    }
    if(!regex.test(result2))
    {
        alert("����Ľ�����������ȷ������������");
        frm2.focus();
        return false;
    }
    
    document.getElementById("searchType").value=searchType;  
    window.location.href = pageHtml + '-1-' + result + '-' +  result2 + '-' + searchType + '.html';
}

// ��ʾ���ظ߼�ɸѡDIV
function DisplayHighSelect(temp1,temp2,lishiqihao,lotteryType)
{  
    //alert(temp1); 
    var typeId = document.getElementById("typeId").value; 
    document.searchform.action=temp2+"?searchType=gaoji&typeId=" + typeId+"&lotteryType="+lotteryType;
    //�����������߼�ɸѡҳ����
    document.getElementById("Qishu").value=temp1;
    //��ʷ�ϵĽ���--�ں�
    //document.getElementById("lishi_qishu").value=lishiqihao;
    
    var Hselect=document.getElementById("HighSelect");
    
    if(Hselect.style.display=="none")
    {
        Hselect.style.display="block";
    }
    else
    {
        Hselect.style.display="none";
    }
    HighSelectTopLeft(Hselect);  
}

function HighSelectTopLeft(Hselect)
{
    var bodyhh=document.body.clientHeight;
    var bodyww=document.body.clientWidth;
    var objhh=Hselect.clientHeight;
    var objww=Hselect.clientWidth;
    Hselect.style.top=250;
    Hselect.style.left=(bodyww-objww)/2;
}

// ģ��ѡ�ŵ���ʾ����
function moxuan(obj1){
    obj=document.getElementById("moxuan");
    if(obj.style.display==""){
        obj.style.display="none";
    }else{
        obj.style.display=""
    }
    
    if(obj1.className == "mx_open"){
        obj1.className = "mx_close";
    }else if(obj1.className == "mx_close"){
        obj1.className = "mx_open";
    }
}

// ��ʷͳ�ƺ͵�ǰͳ�Ƶ���ʾ����
function showshiorcurrdata(value){
    for (var i = 0; i < 5; i++) {
        if (value == "0") {
            document.getElementById("current" + i).style.display="none";
            document.getElementById("history" + i).style.display="";
        } else {
            document.getElementById("current" + i).style.display="";
            document.getElementById("history" + i).style.display="none";
        }
    }
}

/*
* ��������©�ֲ�  zhouec 2010/06/10
* ����ǰҳ�����©�ֲ�
* ������
*   tbodyId: ��ǰ����TBody��ID
*   startIndex: �ֲ�����Ŀ�ʼλ��  
*               ����ֲ�Ϊһ������5,20��,startIndex:'5', ����ֲ�Ϊ�������5,20��,��25,45��,��60,75��,startIndex:'5,25,60'
*   endIndex:   �ֲ�����Ľ���λ��
*               ����ֲ�Ϊһ������5,20��,startIndex:'20', ����ֲ�Ϊ�������5,20��,��25,45��,��60,75��,startIndex:'20,45,75'
*   cssStyle: ���⴦��ĵ�Ԫ�����ʽ���ַ��� �磺"backChange z_bg_06, backChange z_bg_17, backChange z_bg_18"
*/ 
function showdata(tbodyId, startIndex, endIndex, cssStyle){
    
    var tbody = document.getElementById(tbodyId);
    var trs = tbody.rows;
    
    //��������
    var startParam = new Array(); 
    var endParam = new Array();     
    if (startIndex != "" && startIndex != undefined) {
        //��©�ֲ�����


        if (startIndex.indexOf(",") > 0) {
            //��©�ֲ㲻���������
            startParam = startIndex.split(","); 
            endParam = endIndex.split(","); 
        } else {
            //��©�ֲ����������


            startParam[0] = startIndex;
            endParam[0] = endIndex;  
        }
    }
    
    //ȡ�õ�ǰ������
    var isSort = isSortOrNot(tbodyId);
    
    if (!isSort) {
        if(document.getElementById("bdylsj").checked == true){
            //������©����
            var k = 0;
            my_array=new Array();
            for(var i = 0; i < trs.length; i++){
                for (var n = 0; n < startParam.length; n++) {   
                    for (var j = parseInt(startParam[n]); j < parseInt(endParam[n]); j++) {
                        var tmp = trs[i].cells[j];
                        //�ж��Ƿ���һ����
                        if(cssStyle.indexOf(tmp.className) < 0){
                            continue;
                        }else{
                            k++;
                            tdAreaDisplayOrnot(tbodyId, i, j, 1, k);
                        }
                    }
                }
            }
        }else{
            var k=0;
            for(var i = 0; i < trs.length; i++){
                for (var n = 0; n < startParam.length; n++) {   
                    for (var j = parseInt(startParam[n]); j < parseInt(endParam[n]); j++) {
                        var tmp = trs[i].cells[j];
                        if(cssStyle.indexOf(tmp.className) < 0){
                            continue;
                        }else{
                            k++;
                            tdAreaDisplayOrnot(tbodyId, i, j, 2, k);
                        }
                    }
                }
            } 
        } 
    } else { 
        if(document.getElementById("bdylsj").checked == true){
            //������©����
            var k = 0;
            my_array=new Array();
            for(var i = trs.length - 1; i >= 0; i--){
                for (var n = 0; n < startParam.length; n++) {   
                    for (var j = parseInt(startParam[n]); j < parseInt(endParam[n]); j++) {
                        var tmp = trs[i].cells[j];
                        //�ж��Ƿ���һ����
                        if(cssStyle.indexOf(tmp.className) < 0){
                            continue;
                        }else{
                            k++;
                            tdAreaDisplayOrnot(tbodyId, i, j, 1, k);
                        }
                    }
                }
            }
        }else{
            var k=0;
            for(var i = trs.length - 1; i >= 0; i--){ 
                for (var n = 0; n < startParam.length; n++) {   
                    for (var j = parseInt(startParam[n]); j < parseInt(endParam[n]); j++) {
                        var tmp = trs[i].cells[j];
                        if(cssStyle.indexOf(tmp.className) < 0){
                            continue;
                        }else{
                            k++;
                            tdAreaDisplayOrnot(tbodyId, i, j, 2, k);
                        }
                    }
                }
            } 
        }
    }
    
    /*if(document.getElementById("bdylsj").checked == true){
        //������©����
        var k = 0;
        my_array=new Array();
        for(var i = trs.length - 1; i >= 0; i--){
            for (var n = 0; n < startParam.length; n++) {   
                for (var j = parseInt(startParam[n]); j < parseInt(endParam[n]); j++) {
                    var tmp = trs[i].cells[j];
                    //�ж��Ƿ���һ����
                    if(cssStyle.indexOf(tmp.className) < 0){
                        continue;
                    }else{
                        k++;
                        tdAreaDisplayOrnot(tbodyId, i, j, 1, k);
                    }
                }
            }
        }
    }else{
        var k=0;
        for(var i = trs.length - 1; i >= 0; i--){ 
            for (var n = 0; n < startParam.length; n++) {   
                for (var j = parseInt(startParam[n]); j < parseInt(endParam[n]); j++) {
                    var tmp = trs[i].cells[j];
                    if(cssStyle.indexOf(tmp.className) < 0){
                        continue;
                    }else{
                        k++;
                        tdAreaDisplayOrnot(tbodyId, i, j, 2, k);
                    }
                }
            }
        } 
    }*/
}

/*
* ��������©�ֲ�
* ����ǰҳ�����©�ֲ�
* ������
*   tbodyId: ��ǰ����TBody��ID
*   startIndex: �ֲ�����Ŀ�ʼλ��  
*               ����ֲ�Ϊһ������5,20��,startIndex:'5', ����ֲ�Ϊ�������5,20��,��25,45��,��60,75��,startIndex:'5,25,60'
*   endIndex:   �ֲ�����Ľ���λ��
*               ����ֲ�Ϊһ������5,20��,startIndex:'20', ����ֲ�Ϊ�������5,20��,��25,45��,��60,75��,startIndex:'20,45,75'
*   cssStyle: ���⴦��ĵ�Ԫ�����ʽ���ַ��� �磺"backChange z_bg_06, backChange z_bg_17, backChange z_bg_18"
*/ 
function yiloufenceng(tbodyId, startIndex, endIndex, cssStyle){
    //ȡ��ǰ��TBody
    var  vtablebb =document.getElementById(tbodyId);
    
    //ȡ�õ�ǰ������
    var isSort = isSortOrNot(tbodyId);
    
    //��������
    var startParam = new Array(); 
    var endParam = new Array();     
    if (startIndex != "" && startIndex != undefined) {
        //��©�ֲ�����
        if (startIndex.indexOf(",") > 0) {
            //��©�ֲ㲻���������
            startParam = startIndex.split(","); 
            endParam = endIndex.split(","); 
        } else {
            //��©�ֲ����������
            startParam[0] = startIndex;
            endParam[0] = endIndex;  
        }
    }
    
    if(document.getElementById("ylfc").checked == true){
        //��ʼ��,������,�Ƿ�Check,�Ƿ����� 
        ylfcDisplayOrnot(tbodyId, startParam, endParam, 1, isSort, cssStyle);    
    }else{
        ylfcDisplayOrnot(tbodyId, startParam, endParam, 2, isSort, cssStyle);
    } 
}

//���ػ���ʾ������
function showspaceLine(tbodyId, startIndex, len, cssName){
    var trs =document.getElementById(tbodyId).rows;
    if(document.getElementById("fzx").checked == true){
        spaceLineshow=0;
    }else{
        spaceLineshow=1;
    }
    
    //ȡ�õ�ǰ������

    var isSort = isSortOrNot(tbodyId);
    if (!isSort) {
        for (var i = 0; i < trs.length; i++) {   
            if(trs[i].className == 'z_tr_hui_top' || trs[i].className == 'tdbckno_top'){
                if(spaceLineshow == 1){
                    lineDisplayOrnot(tbodyId,i,i,1,"top");
                }else{
                    lineDisplayOrnot(tbodyId,i,i,2,"top");
                }
            }
        } 
    } else {
        for (var i = trs.length - 1; i >= 0; i--) {   
            if(trs[i].className == 'z_tr_hui_top' || trs[i].className == 'tdbckno_top' ||
               trs[i].className == 'z_tr_hui_bottom' || trs[i].className == 'tdbckno_bottom') {
                if(spaceLineshow == 1){
                    lineDisplayOrnot(tbodyId,i,i,1,"bottom");
                }else{
                    lineDisplayOrnot(tbodyId,i,i,2,"bottom");
                }
            }
        } 
    }
    //��������
    var indexParam = getArrayFormString(startIndex);     
    var lenParam = getArrayFormString(len);
    var cssParam = getCssArrayFormString(cssName);
    
    if (document.getElementById("dzx").checked == true
     && startIndex != "" && startIndex != undefined && startIndex != null) {    
        //��ҳ���ϵ������
        oZXZ.clear();
        //���¼�����
        objectZXZ = oZXZ.bind(tbodyId, cssParam);
        for (var i = 0; i < indexParam.length; i++) {
            objectZXZ.add(indexParam[i], 0, lenParam[i], 0);
            //����߿�ʼ�ڼ�����Ԫ��
            //���ϱ߿�ʼ�ڼ�����Ԫ��
            //��Ԫ�����
            //�����������(0�������һ��)
        }
        objectZXZ.draw(ESUNChart.ini.default_has_line);
    }
}

//���ػ���ʾ����
function showbrokenLine(tbodyId, startIndex, len, cssName){

    if(document.getElementById("dzx").checked == true){
        spaceLineshow=0;
    }else{
        spaceLineshow=1;
    }
    
    //��������
    var indexParam = getArrayFormString(startIndex);     
    var lenParam = getArrayFormString(len);
    var cssParam = getCssArrayFormString(cssName);
    
    if (spaceLineshow == 0) {
        //��ʾ��
        oZXZ.clear();
        //���¼�����
        objectZXZ = oZXZ.bind(tbodyId, cssParam);
        for (var i = 0; i < indexParam.length; i++) {
            objectZXZ.add(indexParam[i], 0, lenParam[i], 0);
            //����߿�ʼ�ڼ�����Ԫ��
            //���ϱ߿�ʼ�ڼ�����Ԫ��
            //��Ԫ�����
            //�����������(0�������һ��)
        }
        objectZXZ.draw(ESUNChart.ini.default_has_line);
    } else {
        //������
        oZXZ.clear();
    }
}

//�ж��Ƿ��������ǽ��� 
//����ֵ�� true:����false:����
function isSortOrNot(tbodyId) {
    var tbody =document.getElementById(tbodyId);
    var isSort = false;
    if (tbody.rows.length > 0) {
        var value = tbody.rows[0].cells[0].innerText; 
        if (value == "1") {
            //ֵΪ1ʱ���ǽ���

            isSort = false;
        } else {
            //ֵ��Ϊ1ʱ��������

            isSort = true;
        }
    }
    return isSort;
}

// ������б�ɫ
function overClass(trName) {
    
    if (updateTR != "") {
        var tn1 = document.getElementById(updateTR);
        var tdlength1 = tn1.cells.length;
        for (var i = 0; i < tdlength1; i++) {
            var className = tn1.cells[i].className;
            tn1.cells[i].className = className.replace("backChange ", "");
        }
    }

    var tn = document.getElementById(trName);
    var tdlength = tn.cells.length;
    for (var i = 0; i < tdlength; i++) {
        if ("z_bg_16" != tn.cells[i].className) {
            tn.cells[i].className ="backChange " + tn.cells[i].className ;
        }
    }
    updateTR = trName;
}

//����  �����0��ʼ���� 
function clickshulian(temp, tbodyId, sartColIndex, endColIndex){  
    var tbody = document.getElementById(tbodyId);
    if (temp.value >= 2) {
        clearlian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_ligtred', 'z_font_red');
        zhilian(tbodyId,sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_ligtred', 'z_font_ligtred', temp.value);
    } else {
        clearlian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_ligtred', 'z_font_red');  
    }
}

//б��
function clickxielian(temp, tbodyId, sartColIndex, endColIndex){
    var tbody = document.getElementById(tbodyId);   
    if(temp.value>=2){
        //��ʼ��,������,��ʼ��,������ /ԭ������ʽ,Ҫ�滻����ʽ
        clearlian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_purple', 'z_font_red');
        xielian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_purple', 'z_font_purple', temp.value);
    }else{
        clearlian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_purple', 'z_font_red');
    }
}

//����б��
function clickoddlian(temp, tbodyId, sartColIndex, endColIndex) {  
    var tbody = document.getElementById(tbodyId);     
    if (temp.value >= 2) {
        //���Ǹ��п�ʼ����һ�н���
        clearlian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_darkblue', 'z_font_red');
        OddEvenlian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_darkblue', 'z_font_darkblue', 1, temp.value);
    } else {
        clearlian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_darkblue','z_font_red');
    }
}

//ż��б�� 
function clickevenlian(temp, tbodyId, sartColIndex, endColIndex){  
    var tbody = document.getElementById(tbodyId);     
    if (temp.value >= 2) {
        clearlian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_evendarkblue','z_font_red');
        OddEvenlian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_evendarkblue', 'z_font_evendarkblue', 0, temp.value);
    }else{
        clearlian(tbodyId, sartColIndex, endColIndex, 0, tbody.rows.length - 1, 'z_font_evendarkblue','z_font_red'); 
    }
}

/*
���������
tableid:���id
begincol:��ʼ��
endcol:������
beginclum:��ʼ��
endclum:������
oldclsnam:���滻classname
newclsnam:�����滻��classname
*/
function clearlian(tableid,begincol,endcol,beginclum,endclum,oldclsnam,newclsnam){
    var vtable = document.getElementById(tableid);
    for(i=beginclum;i<=endclum;i++){
        for(j=begincol;j<=endcol;j++){
            var tmpa = vtable.rows[i].cells[j];
            var tmpacn = CertainBeBall(tmpa.className);
            //alert("new"+tmpacn);
            //alert(oldclsnam);
            if(tmpacn==oldclsnam){
                tmpH = tmpa.className;
                if(tmpa.id.indexOf("Gray") < 0) {
                    tmpa.className = tmpH.replace(CertainBeBall(tmpH),newclsnam);
                    tmpa.className=newclsnam; 
                } else {
                    tmpa.className = tmpH.replace(CertainBeBall(tmpH),"z_font_hs");
                    tmpa.className="z_font_hs";
                }
            }
        }
    }
}

//ÿλ��N��������
function chushuSubmit(tbodyId, pageId) {
    //��ȡҳ���ϳ�����ֵ 
    document.getElementById("searchType").value = "chushu";
    //form���ύ��ʽΪ"POST"  
    document.thirdD.method = "POST";
    //form�ύ��ҳ��   
    document.thirdD.action = pageId;
    document.thirdD.submit();
}

//��������JS
function zxfsSubmit(pageId) {
    
    var temaNum = document.getElementById("temaNum").value;
    if (temaNum.length == 0) {
        alert("���������֣�");
        document.getElementById("temaNum").focus();
        return false;
    }
    var re = /^[0-9]*$/;    
    if (!re.test(temaNum)) {
        alert("������0-9�����֣�");
        document.getElementById("temaNum").select();
        return false;
    }
    for (var i = 0; i < 10; i++) {
        var tempStr = temaNum.replace(new RegExp(i + "", "gm"), "");
        if (!(tempStr.length == temaNum.length || tempStr.length == temaNum.length - 1)) {
            alert("��������ֲ����ظ���");
            document.getElementById("temaNum").select();
            return false;
        }
    } 
    
    //��ȡҳ���ϳ�����ֵ 
    document.getElementById("searchType").value = "chushu";
    //form���ύ��ʽΪ"POST"  
    document.thirdD.method = "POST";
    //form�ύ��ҳ��   
    document.thirdD.action = pageId;
    document.thirdD.submit();
}

//�����ʷ�ϵĽ���İ�ť
function lishiSubmit(type,pageId) {
    var pageHtml = document.getElementById("pageHtml").value; 
    var typeId = document.getElementById("typeId").value;
    if ("qishu" == type) {
        var lishi_qishu = document.getElementById("lishi_qishu").value;
        var re = /^[0-9]*$/;            
        if (!re.test(lishi_qishu)) {
            alert("������0-9�����֣�");
            document.getElementById("lishi_qishu").select();
            return false;
        }  
        window.location.href = pageHtml + '-2-4-' + lishi_qishu + '.html';
    } else if ("riqi" == type) {
        var month = document.getElementById("lishi_yue").value;
        var day = document.getElementById("lishi_ri").value;
        var lishi_riqi = month + "-" + day; 
        window.location.href = pageHtml + '@2@5@' + lishi_riqi + '.html';
    } else if ("xingqi" == type) {
        var xingqiji = new Array("һ", "��", "��", "��", "��", "��", "��");    
        var lishi_xingqi = document.getElementById("lishi_xingqi").value; 
        var index = 0;
        for (var i = 0; i < xingqiji.length; i++) {
            if (lishi_xingqi == xingqiji[i]) {
                index = i;
                break;
            }
        }
        window.location.href = pageHtml + '-2-6-' + index + '.html';
    } else if ("yinli_riqi" == type) {
        var lishi_yinli_yue = document.getElementById("lishi_yinli_yue").selectedIndex + 1;
        var lishi_yinli_ri = document.getElementById("lishi_yinli_ri").selectedIndex + 1;
        window.location.href = pageHtml + '-7-'+lishi_yinli_yue+'-' + lishi_yinli_ri + '.html';
    }
}

//�µ�������
function monthChangedEvent() {
 
    var year = document.getElementById("lishi_nian").value;
    var month = document.getElementById("lishi_yue").value;
    
    var riArray = Array("01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31");
    var tempArray = new Array("04", "06", "09", "11");
    
    var count = riArray.length;
    var isXiaoYue = false;
    for (var i = 0; i < tempArray.length; i++) {
        if (month == tempArray[i]) {
            isXiaoYue = true;
            break;
        }
    }
    if (isXiaoYue) {
        //30����µļ���
        count = riArray.length - 1;
    } else if (month == "02") {
        //2�µļ���
        if (year % 400 == 0 || (year % 4 == 0 && year % 100 != 0)) {
            //����
            count = riArray.length - 2;  
        } else {
            count = riArray.length - 3;  
        }
    }
    document.getElementById("lishi_ri").options.length = 0;
    for(var i = 0; i < count; i++){
        var item = document.createElement("OPTION"); 
        item.value = riArray[i];   
        item.text = riArray[i];
        document.getElementById("lishi_ri").options.add(item); 
    }
}

// ģ��ѡ�ŵ���ʾ����
function moxuan_label_xia(xia){
    if (xia == "1") {
        document.getElementById("mo3").style.display="";
        document.getElementById("mo4").style.display="";
        document.getElementById("mo5").style.display="";
        document.getElementById("moxuan2").style.display = "none";
    } else {
        document.getElementById("mo3").style.display="none";
        document.getElementById("mo4").style.display="none";
        document.getElementById("mo5").style.display="none";
        document.getElementById("moxuan2").style.display = "";
    }     
}

// Ԥ������ʽ�����
function css(td,css1,css2)
{
    if(td.className==css1)
    {
        td.className=css2;
    }
    else
    {
        td.className=css1;
    }
    int_blue1=Number(document.getElementById("m1_blue").innerText);
    int_blue2=Number(document.getElementById("m2_blue").innerText);  
    int_blue3=Number(document.getElementById("m3_blue").innerText);  
    int_blue4=Number(document.getElementById("m4_blue").innerText);  
    int_blue5=Number(document.getElementById("m5_blue").innerText);
    
    int_yellow1=Number(document.getElementById("m1_yellow").innerText);
    int_yellow2=Number(document.getElementById("m2_yellow").innerText);
    int_yellow3=Number(document.getElementById("m3_yellow").innerText);
    int_yellow4=Number(document.getElementById("m4_yellow").innerText);
    int_yellow5=Number(document.getElementById("m5_yellow").innerText);
    
    int_red1=Number(document.getElementById("m1_red").innerText);
    int_red2=Number(document.getElementById("m2_red").innerText); 
    int_red3=Number(document.getElementById("m3_red").innerText);  
    int_red4=Number(document.getElementById("m4_red").innerText);  
    int_red5=Number(document.getElementById("m5_red").innerText);
    
    for (var i = 1; i <= 5; i++) {
        if (td.parentNode.id == ("mo" + i)) {
            if (td.className == "q_blue") {
                if (i == 1) {
                    int_blue = int_blue1 + 1;          
                } else if (i == 2) {
                    int_blue = int_blue2 + 1;          
                } else if (i == 3) {
                    int_blue = int_blue3 + 1;          
                } else if (i == 4) {
                    int_blue = int_blue4 + 1;          
                } else if (i == 5) {
                    int_blue = int_blue5 + 1;          
                }
                document.getElementById("m" + i + "_blue").innerText = int_blue;
                
            } else if (td.className == "q_yellow") {
                if (i == 1) {
                    int_yellow = int_yellow1 + 1;          
                } else if (i == 2) {
                    int_yellow = int_yellow2 + 1;          
                } else if (i == 3) {
                    int_yellow = int_yellow3 + 1;          
                } else if (i == 4) {
                    int_yellow = int_yellow4 + 1;          
                } else if (i == 5) {
                    int_yellow = int_yellow5 + 1;          
                }                   
                document.getElementById("m" + i + "_yellow").innerText = int_yellow;
                
            } else if (td.className == "q_red") {
                if (i == 1) {
                    int_red = int_red1 + 1;          
                } else if (i == 2) {
                    int_red = int_red2 + 1;          
                } else if (i == 3) {
                    int_red = int_red3 + 1;          
                } else if (i == 4) {
                    int_red = int_red4 + 1;          
                } else if (i == 5) {
                    int_red = int_red5 + 1;          
                }                   
                document.getElementById("m" + i + "_red").innerText = int_red;
            
            } else if(td.className == "SelectHtml1_blue") {
                if (i == 1) {
                    int_blue = int_blue1 - 1;          
                } else if (i == 2) {
                    int_blue = int_blue2 - 1;          
                } else if (i == 3) {
                    int_blue = int_blue3 - 1;          
                } else if (i == 4) {
                    int_blue = int_blue4 - 1;          
                } else if (i == 5) {
                    int_blue = int_blue5 - 1;          
                }                    
                document.getElementById("m" + i + "_blue").innerText = int_blue;
                
            } else if(td.className == "SelectHtml1_yellow") {
                if (i == 1) {
                    int_yellow = int_yellow1 - 1;          
                } else if (i == 2) {
                    int_yellow = int_yellow2 - 1;          
                } else if (i == 3) {
                    int_yellow = int_yellow3 - 1;          
                } else if (i == 4) {
                    int_yellow = int_yellow4 - 1;          
                } else if (i == 5) {
                    int_yellow = int_yellow5 - 1;          
                }                   
                document.getElementById("m" + i + "_yellow").innerText = int_yellow;
                  
            } else if(td.className == "SelectHtml1_red") {
                if (i == 1) {
                    int_red = int_red1 - 1;          
                } else if (i == 2) {
                    int_red = int_red2 - 1;          
                } else if (i == 3) {
                    int_red = int_red3 - 1;          
                } else if (i == 4) {
                    int_red = int_red4 - 1;          
                } else if (i == 5) {
                    int_red = int_red5 - 1;          
                }                   
                document.getElementById("m" + i + "_red").innerText = int_red;
            }
        }
    }
}