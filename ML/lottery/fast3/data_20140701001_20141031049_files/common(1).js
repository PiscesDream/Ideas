function isIE() { 
	//indexOf() ���ҵ�, ���ش���0; ��û���ҵ�,�򷵻� -1 ��
    if (window.navigator.userAgent.toString().toLowerCase().indexOf("msie") >= 1)
        return true;
    else
        return false;
}

//firefox innerText define
if (!isIE()) {   
	HTMLElement.prototype.__defineGetter__( "innerText",
		function () {
			var anyString = "";
			var childS = this.childNodes;
			for(var i = 0; i < childS.length; i++) {
				//����հ��ַ�
				if(childS[i].nodeType == 1)
					anyString += childS[i].tagName == "BR" ? '\n' : childS[i].innerText;
				else if(childS[i].nodeType == 3)
					anyString += childS[i].nodeValue;
			}
			return anyString;
		}
	);
	HTMLElement.prototype.__defineSetter__( "innerText",
		function (sText) {
			this.textContent = sText;
		}
	);
}
//��¼��ǰҳ��������߶�
var currentClientHeight = 0;
//��¼��ǰҳ����������
var currentClientWidth = 0;
/* ����3D */
function onLoadLine(tbodyId, startIndex, len, cssName) {
 
    if (currentClientHeight == document.documentElement.clientHeight
        && currentClientWidth == document.documentElement.clientWidth) {
��������return;
����}
����currentClientHeight = document.documentElement.clientHeight;
    currentClientWidth = document.documentElement.clientWidth;

    oZXZ.clear(); 
    
    //��������
    var indexParam = getArrayFormString(startIndex);     
    var lenParam = getArrayFormString(len);
    var cssParam = getCssArrayFormString(cssName);
    
    //������
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

//��������
function getArrayFormString(param) {
    //��������
    var returnArray = new Array();
    if (param != "" && param != undefined) {
        //���ߵ����
        if (param.indexOf(",") > 0) {
             //�ж����ߵ����
             returnArray = param.split(",");
        } else {
             //ֻ��һ���ߵ����
             returnArray[0] = param;
        }
    }
    return returnArray;
}

//����CSS
function getCssArrayFormString(param) {
    //��������
    var returnArray = new Array();
    var cssParamTemp = new Array();
    if (param != "" && param != undefined) {
        //���ߵ����
        if (param.indexOf(",") > 0) {
             //�ж����ߵ����
             cssParamTemp = param.split(",");
        } else {
         //ֻ��һ���ߵ����
         cssParamTemp[0] = param;
        }
    }
    countIndex = 0;
    for (var i = 0; i < cssParamTemp.length; i++) {
        returnArray[countIndex] = cssParamTemp[i];
        countIndex = countIndex + 1;
        returnArray[countIndex] = "backChange " + cssParamTemp[i];
        countIndex = countIndex + 1;
    }
    return returnArray;
}