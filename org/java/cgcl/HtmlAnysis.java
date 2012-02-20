package org.java.cgcl;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class HtmlAnysis {
	
	public static void main(String args[]) {
      //  String html = "<title>ABCD</title>gsdggas<title></title>jkll<title>005</title>";
		String html1 = "<title>ABCD</title>gsdggas<title></title>jkll<title>00i5</title>";
		String html = "<td width=\"*\" align=\"left\" valign=\"center\" class=\"briefcitDetail \"> "+
"<!--{nohitmsg}--> <span class=\"briefcitTitle\">" +
" <a href=\"/search~S0*chx?/Xmpi&amp;SORT=D/Xmpi&amp;SORT=D&amp;SUBKEY=mpi/1%2C14%2C14%2CB/frameset&amp;FF=Xmpi&amp;SORT=D&amp;1%2C1%2C\">" +
"MPI并行程序设计实例教程 Mpi Bing Xing Cheng Xu She Ji Shi Li Jiao Cheng 张武生 ... [等] 编著</a>" +
"</span> <br /> <span class=\"briefcitDetail\">" +
" 张武生<br /> <span class=\"briefcitDetail\"> " +
"北京 清华大学出版社 2009" +
"<br /> <br /> <span class=\"briefcitDetail\">" +
" <br /> &nbsp;</span></span></span></td>";
		String test = "“This is a <EM>first</EM> test";
        // 简单示例，相当于String html=getHtml(String urlString);
        List resultList = getContext(html1);
        for (Iterator iterator = resultList.iterator(); iterator.hasNext();) {
            String context = (String) iterator.next();
            System.out.println(context);
        }
    }
    
    /**
     * 提取"<title>XXXX</title>"中的文字XXXX
     * @param html 要解析的html文档内容
     * @return 解析结果，可以多次匹配，每次匹配的结果按文档中出现的先后顺序添加进结果List
     */
    public static List getContext(String html) {
        List resultList = new ArrayList();
        String pattern = ">([^<]*)";
        String pattern1 = "<title>([^</title>]*)";
        String pattern2 = "<.+>";
        Pattern p = Pattern.compile(pattern1);//匹配<title>开头，</title>结尾的文档
        Matcher m = p.matcher(html );//开始编译
        
        while (m.find()) {
        	System.out.println(m.group(1));
            //resultList.add(m.group(1));//获取被匹配的部分
        }
        return resultList;
    }
}
