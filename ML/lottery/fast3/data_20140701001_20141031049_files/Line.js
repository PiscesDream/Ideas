ESUNChart={};
ESUNChart.previewCode=[];
ESUNChart.on=function(o,type,fn){o.attachEvent?o.attachEvent('on'+type,function(){fn.call(o)}):o.addEventListener(type,fn,false);};
/* ȫ�ֿ��� */
ESUNChart.ini={
	default_has_line:true,
	map:[],/* ���ֵ��ַ�ӳ�� */
	initShow:'',/* �Ƿ��ʼ��ʱ��ʾ�غŻ�����������,��ʽΪ��ѡ��ID+,�� "c_tb,c_v,c_v3,c_h,c_h3,c_x,c_x3" */
	stop_buy_re:/sina|tenpay|paipai|youa/ /* ��ֹ���ֹ���ť�İ���վ����� */
};

ESUNChart.CSS=function(obj,v){
	var _style=obj.style;
	if (_style[v])return _style[v];  
    if (obj.currentStyle) return obj.currentStyle[v]
    if (document.defaultView && document.defaultView.getComputedStyle){ 
            v = v.replace(/([A-Z])/g,"-$1").toLowerCase();
            var s = document.defaultView.getComputedStyle(obj,""); 
            return s && s.getPropertyValue(v); 
    }
    return null; 
}
ESUNChart.stop= function(e) {
	if (e.stopPropagation) {
		e.stopPropagation();
		e.preventDefault();
	} else {
		e.cancelBubble = true;
		e.returnValue = false;
	};
};
ESUNChart.insertAfter=function(newElement,targetElement){
	var parent=targetElement.parentNode;
	if(parent.lastChild==targetElement){
		return parent.appendChild(newElement);
	}else{
		return parent.insertBefore(newElement,targetElement.nextSibling);
	};
}

/* ������  --------------------------------------------------------------------*/
JoinLine=function(color,size){
	this.color=color||"#000000";
	this.size=size||1;
	this.lines=[];
	this.tmpDom=null;
	this.visible=true;
    var cenbox=document.getElementById('container');//for center div
    this.box=document.body;
    if(cenbox){//���ݾ���div
        this.wrap=cenbox.getElementsByTagName('DIV')[0];
        if(this.wrap){
            this.box=this.wrap
            this.wrap.style.position='relative';
        }
    };
};
JoinLine.prototype={
	show:function(yes){
		for(var i=0;i<this.lines.length;i++)
			this.lines[i].style.visibility=yes?"visible":"hidden";		
	},
	remove:function(){
		for(var i=0;i<this.lines.length;i++)
			this.lines[i].parentNode.removeChild(this.lines[i]);
		this.lines=[];		
	},
	join:function(objArray,hide,fn){
		this.remove();
		this.visible=hide?"visible":"hidden";
		this.tmpDom=document.createDocumentFragment();
		for(var i=0;i<objArray.length-1;i++){
			var a=this.pos(objArray[i]);
			var b=this.pos(objArray[i+1]);
            //alert("A.x*: " + a.x + " * A.y*: " + a.y + " *B.x*: " + b.x + " *B.y*: " + b.y);
			/* ͨ���ȶ�����ֵ�����߻������ */
			if(fn&&fn(a,b)===false)continue;
			if(document.all && !(navigator.appName == "Microsoft Internet Explorer" 
                                && (navigator.appVersion.match(/9./i)=="9." || document.documentMode == 10))){
				this.IELine(a.x,a.y,b.x,b.y)
				
			}else{
				this.FFLine(a.x,a.y,b.x,b.y)
			};
		};
		this.box.appendChild(this.tmpDom);		
	},
	 pos:function(obj){
        //alert(obj.offsetWidth);
	 	if(obj.nodeType==undefined)return obj;// input {x:x,y:y} return;
		var pos={x:0,y:0},a=obj;
		for(;a;a=a.offsetParent){pos.x+=a.offsetLeft;pos.y+=a.offsetTop;if(this.wrap&&a.offsetParent===this.wrap)break};// ���ݾ���div
		pos.x+=parseInt(obj.offsetWidth/2);
		pos.y+=parseInt(obj.offsetHeight/2);
		return pos;
	},
	_oldDot:function (x,y,color,size){
		var dot=document.createElement("DIV");
		dot.style.cssText="position: absolute; left: "+x+"px; top: "+y+"px;background: "+color+";width:"+size+"px;height:"+size+"px;font-size:1px;overflow:hidden";
		dot.style.visibility=this.visible;
		this.lines.push(this.tmpDom.appendChild(dot));
	},
	_oldLine:function(x1,y1,x2,y2){
		var r=Math.floor(Math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)));
		var theta=Math.atan((x2-x1)/(y2-y1));
		if(((y2-y1)<0&&(x2-x1)>0)||((y2-y1)<0&&(x2-x1)<0))	theta=Math.PI+theta;
		var dx=Math.sin(theta),dy=Math.cos(theta),i=0;
		do{this.FFDot(x1+i*dx,y1+i*dy,this.color,this.size)}while(i++<r);
	},
	FFLine:function(x1,y1,x2,y2){
		if(Math.abs(y1-y2)<(JoinLine.indent*2)&&x1==x2)return;//�Զ�ȷ��ͬ�е��Ƿ�����		
		var np=this.nPos(x1,y1,x2,y2,JoinLine.indent);//����������������ֹ������
		x1=np[0];y1=np[1];x2=np[2];	y2=np[3];
		var cvs=document.createElement("canvas");
		cvs.style.position="absolute";
		cvs.style.visibility=this.visible;
		cvs.width=Math.abs(x1-x2)||this.size;
		cvs.height=Math.abs(y1-y2)||this.size;
		var newY=Math.min(y1,y2);
		var newX=Math.min(x1,x2);
		cvs.style.top=newY+"px";
		cvs.style.left=newX+"px";
		var FG=cvs.getContext("2d");
		FG.save();//������ʷ����
		FG.strokeStyle=this.color;
		FG.lineWidth=this.size;
		//FG.globalAlpha=0.5;//͸���ȣ�	
		FG.beginPath(); 
		FG.moveTo(x1-newX,y1-newY);
		FG.lineTo(x2-newX,y2-newY);
		FG.closePath();
		FG.stroke();
		FG.restore();//�ָ���ʷ����
		this.lines.push(cvs);
		this.tmpDom.appendChild(cvs);		
	},	
	IELine:function(x1,y1,x2,y2){
		if(Math.abs(y1-y2)<(JoinLine.indent*2)&&x1==x2)return;//�Զ�ȷ��ͬ�е��Ƿ�����
		var np=this.nPos(x1,y1,x2,y2,JoinLine.indent);//����������������ֹ������
		x1=np[0];y1=np[1];x2=np[2];	y2=np[3];		
		var line = document .createElement( "<v:line></v:line>" );
		line.from=x1+","+y1;
		line.to=x2+","+y2;
		line.strokeColor=this.color;
		line.strokeWeight=this.size+"px";
		line.style.cssText="position:absolute;z-index:999;top:0;left:0";
		line.style.visibility=this.visible;
		line.coordOrigin="0,0";
		this.lines.push(line);
		this.tmpDom.appendChild(line);
	},
	nPos:function(x1, y1, x2, y2, r){
		var a = x1 - x2, b = y1 - y2;
		var c = Math.round(Math.sqrt(Math.pow(a, 2) + Math.pow(b, 2)));
		var x3, y3, x4, y4;
		var _a = Math.round((a * r)/c);
		var _b = Math.round((b * r)/c);
		return [x2 + _a, y2 + _b, x1 - _a, y1 - _b]; 
	}
};

JoinLine.indent=8;

/* �����������߲����� --------------------------------------------------------------------*/
LG=function(table,_x,_y,width,margin_bottom,css_name,fn_check){
	var rect={x:_x||0,y:_y||0,w:width||0,oh:margin_bottom||0};
	var trs;
    if (isIE()) {
        trs=document.getElementById(table).rows;
    } else {
        trs = (document.getElementById("table3d").getElementsByTagName("tbody"))[1] . rows; 
    }
	var row_start=rect.y<0?(trs.length+rect.y):rect.y;
	var row_end=trs.length-rect.oh;
	var col_start=rect.x<0?(trs[row_start].cells.length+rect.x):rect.x;
	var col_end=parseInt(col_start)+parseInt(rect.w);
	if(col_end>trs[row_start].cells.length)col_end=trs[row_start].cells.length;	
	if(rect.w==0)col_end=trs[row_start].cells.length;	
	this.g=[];
	//alert([row_start,row_end,col_start,col_end]);
	for(var i=row_start;i<row_end;i++){/* each and grouping */
		var tr=trs[i].cells;
		for(var j=col_start;j<col_end;j++){
			var td=tr[j];
			/* ��������ؾ�����ʱ����Ԫ��ű���ӵ��� */
			if(td){
				if(fn_check(td,css_name,j,i)===true)this.g.push(td);
			}
		};
	};
	if(LG.autoDraw)this.draw();
};
//LG.color='#E4A8A8';
LG.color='#898989';
LG.size=2;
LG.autoDraw=true;/* Ĭ���Զ����� */
LG.isShow=true;
LG.filter=function(){};
LG.prototype={
	draw:function(color,size,fn){
		this.line=new JoinLine(color||LG.color,size||LG.size);
		if(!fn)fn=LG.filter;
		this.line.join(this.g,LG.isShow,fn);
	},
	clear:function(){
		this.line.remove();
	},
	show:function(yes){this.line.show(yes)}
}

/* �������߶��� -----------------------------------------------------------------------------------
���ñ��
���ÿ��أ�
���ü�⺯����
��ӿ飻x�����0��ʼ
��ʾ��
�޸�ģʽ��
��ӣ�
����ʾ��
error:�����⺯����һ����ʾ��Ч���ڶ��λᱻ���ǵ�
*/
oZXZ={
	vg:[],
	lg:[],
	_vg:[],
	_lg:[],
    css_name:[],
	table:false,
	check:function(td,cssName){
        for (var i = 0; i < cssName.length; i++) {
            if (td.className == cssName[i]) {
                return true;
            }
        }
        return false;
	},
	on_off:true,
	_on:true,/* ���ط����� */
	novl:false,/* ���Դ�ֱ�� */
	bind:function(tid,_css_name,_on_off){
		this.table=tid;
        for(var i=0;i<_css_name.length;i++){this.css_name.push(_css_name[i])};
		this.on_off=_on_off;
		return this;
	},
	color:function(c){
		LG.color=c;
		return this;
	},
	newCheck:function(fn){
		this.check=fn;
		return this;
	},	
	draw:function(yes){
		if(!this.table)return;
		if(yes){
			var qL=this.vg.length;
			for(var i=0;i<qL;i++){
				var it=this.vg[i];
				LG.color=it.color;
				JoinLine.indent=it.indent;
				this.novl=it.novl;
				if(this.novl)LG.filter=function(a,b){return !(a.x==b.x)};
				this.lg.push(new LG(this.table,it[0],it[1],it[2],it[3],this.css_name,this.check));
			}
		}
		if(this.on_off){
			var _this=this;
			$=document.getElementById(this.on_off);
			if($)$.onclick=function(){
				var yes=_this._on?this.checked:!this.checked;
				_this.show(yes);
			};	
		}
		/* ת���������ʷ��¼���ȴ���һ����� */
		this._vg=this._vg.concat(this.vg);
		this.vg=[];
		this._lg=this._lg.concat(this.lg);
		this.lg=[];
		return this;
	},
	show:function(yes){
		/* ���û�������ػ�һ�� */
		if(this._lg.length==0)this.redraw();
		var qL=this._lg.length;
		for(var i=0;i<qL;i++){this._lg[i].show(yes)};
	},
	/*
	x,y,w,-bottom
	*/
	add:function(x,y,w,mb){//��ÿһ�������������
		this.vg.push([x,y,w,mb]);
		/* ��¼������������ɫ */
		this.vg[this.vg.length-1].color=LG.color;
		this.vg[this.vg.length-1].indent=JoinLine.indent;
		this.vg[this.vg.length-1].novl=this.novl;
		return this;
	},
	clear:function(){
		for(var i=0;i<this._lg.length;i++)
			this._lg[i].clear();
		return this;
	},
	redraw:function(){
		this.clear();
		this.vg=this.vg.concat(this._vg);
		this._vg=[];
		this.draw(true);
	},
	newCheck:function(fn){
		this.check=fn;
		return this;
	},	
	setvl:function(v){
		this.novl=v;
		return this;
	},
	indent:function(v){
		JoinLine.indent=v;
		return this;
	}
}

/* ������е�ȫ�ֳ�ʼ������
------------------------------------------------------------------------------------------*/
ESUNChart.init=function(){
	/* ��λ��ѡ�� */
	var inputs=document.getElementsByTagName("INPUT");
	for(var i=0;i<inputs.length;i++){
		var it=inputs[i];
		if(it.type.toLowerCase()=="checkbox")it.checked=false;
	}
	if(!ESUNChart.ini.default_has_line)return;
	var on_off=document.getElementById("has_line");
	if(!on_off)return;
	on_off.checked='checked';
};

/* ��дfw.onReady �ӳ�ִ�е�window.onload */
if(typeof fw =='undefined')fw={};
fw.onReady=function(fn){
	ESUNChart.on(window,'load',fn);
}

ESUNChart.on(window,'load',function(){// foot scroll AD
	var sys=document.getElementById('foot_scroll_txt');
	if(!sys)return;
	//sys.style.overflow='hidden';
	//sys.style.height='38px'
	var go_go=function(outer,inShell,goUnit,stopTime,speed,dir){
		var $=function (id){return document.getElementById(id)},dir=dir||-1;
		var outer=$(outer),inShell=$(inShell),H=inShell.offsetHeight;
		outer.appendChild(inShell.cloneNode(true));
		(function (){
			H=H||inShell.offsetHeight;
			var m=(outer.scrollTop-1)%goUnit?(speed||13):stopTime;//get timer speed;
			var ed=outer.scrollTop;
			if(go_go.stop!=true)
			if(dir==-1){
				outer.scrollTop=ed==H+1?0:++ed;
			}else{
				outer.scrollTop=ed==0?H-1:--ed;
			}
			setTimeout(arguments.callee,m);
		})()
		return arguments.callee;
	};
	go_go('foot_scroll_txt','foot_scroll_shell',19,3000,10,-1);
	sys.onmouseover=function(){go_go.stop=true};
	sys.onmouseout=function(){go_go.stop=false};
});

function addReferrer(from){
    var links=document.links;
    for(var i=0,j;j=links[i++];)
        j.href+=(j.href.indexOf('?')==-1?'?':'&')+'from='+from
};
function isStopBuySite(){
	var from=document.referrer,local=location.href,search=location.search;
    var param=search.match(/\bfrom=([^&?]+)\b/);
    if(param)from=param[1]
    //addReferrer(from);
	if(ESUNChart.ini.stop_buy_re!==null)
	    return ESUNChart.ini.stop_buy_re.test(from);
	return false;    	
};

ESUNChart.on(window,'load',function(){ // show hide foot ad and buy button
	var noBuy=isStopBuySite();
    if(noBuy)return;
    function getID(o){return document.getElementById(o)}
    //��ʾԤѡ��
    for (var i=0;i<6;++i ) {
        var el=getID('selLine'+i);
        if(el)el.style.display='';
    };
    el=getID('selMaskBox');
    if(el)el.style.display='none';
    //��ʾ��ť
    var spans=getID('chartbottom').getElementsByTagName('span');
    for(var i=0,l=spans.length;i<l;i++){
        var j=spans[i];
        if(j.className=='intro_right ssq_ad')j.style.display='block';        
    };
    //��ʾ����
    var spans=getID('chartbottom').getElementsByTagName('DIV');
    for(var i=0,l=spans.length;i<l;i++){
        var j=spans[i];
        if(j.className=='latest')j.style.display='block';        
    };
});

/*
Ԥѡ�¼�
*/

ESUNChart.onPreviewAreaClick=function(){}

/*
ȫ������
*/

/*
������Чԭ��
1.δ��VML��ʽ
2.���x,y��λ����ʹ���û��ȫ������
3.ȱ�ٱ�ҪID
*/

/*
line Color:
����ɫ:#C5C50A;
��ɫ:#FF9916;
���:#FB9D82;
*/