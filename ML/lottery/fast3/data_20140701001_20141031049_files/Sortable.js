/*
* ����������
* ����ǰҳ�����������
* ������
*   tbodyId: ��ǰ����TBody��ID
*   startIndex: ����ʱ����ʼ��Ԫ�����飬����ж����ߣ���","�ָ������û���ߣ��ÿ��ַ���""
*   len: ����ʱ�����ߵ�Ԫ��ĳ��ȣ�����ж����ߣ���","�ָ������û���ߣ��ÿ��ַ���""
*/  
function sortAble(tbodyId, startIndex, len, cssName){
    
     var tbody = document.getElementById(tbodyId);
     var colRows = tbody.rows;      
     var aTrs = new Array;
     
     //��������
     var indexParam = getArrayFormString(startIndex);     
     var lenParam = getArrayFormString(len);
     var cssParam = getCssArrayFormString(cssName);
     
     //ѭ�����е���
     for (var i = 0; i < colRows.length; i++) { 
          
          //ȡ�ø������ݣ���ֵ������
          aTrs[i] = colRows[i];  
          
          //���Ƹ����ߵ���ʽ
          if (aTrs[i].className == "z_tr_hui_top") {
              aTrs[i].className = "z_tr_hui_bottom";
          } else if (aTrs[i].className == "tdbckno_top") {
              aTrs[i].className = "tdbckno_bottom";  
          } else if (aTrs[i].className == "z_tr_hui_bottom") {
              aTrs[i].className = "z_tr_hui_top";  
          } else if (aTrs[i].className == "tdbckno_bottom") {
              aTrs[i].className = "tdbckno_top";  
          }
     } 
     
     if(aTrs != null && aTrs.length > 0){
         
         //��ת����
         aTrs.reverse();
         
         var strSrc = document.getElementById("imgSort").src;
         var srcArray = strSrc.split("/");
         //alert(srcArray[srcArray.length - 1]);  
         if (srcArray[srcArray.length - 1] == "sort_xia.gif") {
             document.getElementById("imgSort").src = "../CSS/" + srcArray[srcArray.length - 2] + "/sort_shang.gif"; 
         } else {
             document.getElementById("imgSort").src = "../CSS/" + srcArray[srcArray.length - 2] + "/sort_xia.gif"; 
         }
         
         var oFragment = document.createDocumentFragment();     
         for (var i=0; i < aTrs.length; i++) {
             oFragment.appendChild(aTrs[i]);
         }
         tbody.appendChild(oFragment);
     }
     
     if (startIndex != "" && startIndex != undefined && startIndex != null) {   
         //��ҳ���ϵ������
         oZXZ.clear();
         if (document.getElementById("dzx").checked == true) {
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
}

/*
* ������������������� innerHTML ����
* �������� HTML �����а��� script �� style
* ������
*   el: DOM ���еĽڵ㣬�������� innerHTML
*   htmlCode: ����� HTML ����
* �����Ե��������ie5+, firefox1.5+, opera8.5+
*/
var set_innerHTML = function (el, htmlCode){
    var ua = navigator.userAgent.toLowerCase();
    if (ua.indexOf('msie') >= 0 && ua.indexOf('opera') < 0) 
    {
        htmlCode = '<div style="display:none">for IE</div>' + htmlCode;
        htmlCode = htmlCode.replace(/<script([^>]*)>/gi,'<script$1 defer="true">');
        el.innerHTML = htmlCode;
        el.removeChild(el.firstChild);
    } else {
        var el_next = el.nextSibling;
        var el_parent = el.parentNode;
        el_parent.removeChild(el);
        el.innerHTML = htmlCode;
        if (el_next)
           el_parent.insertBefore(el, el_next)
        else
           el_parent.appendChild(el); 
    }
}