# -*- coding: cp936 -*-
import re
from bs4 import BeautifulSoup
import xlwt

html = '''<div class="zm-item-comment" data-id="69285090">
<a class="zg-anchor-hidden" name="comment-69285090"></a>
<a title="易有"
data-tip="p$t$yi-you-11"
class="zm-item-link-avatar"
href="/people/yi-you-11">
<img src="http://pic3.zhimg.com/a94edcdf0f1feacce655be7c450a4afa_s.jpg" class="zm-item-img-avatar">
</a>
<div class="zm-comment-content-wrap">
<div class="zm-comment-hd">
<a data-tip="p$t$yi-you-11" href="http://www.zhihu.com/people/yi-you-11" class="zg-link" title="易有">易有</a>

</div>
<div class="zm-comment-content">
首赞！
</div>
<div class="zm-comment-ft">
<span class="date">2015-02-10</span>


<a href="#" class="reply zm-comment-op-link" name="reply_comment">
<i class="zg-icon zg-icon-comment-reply"></i>回复</a>


<a href="#" class="like zm-comment-op-link " name="like_comment">
<i class="zg-icon zg-icon-comment-like"></i>赞</a>
<span class="like-num  " data-tip="s$r$121 人觉得这个很赞">
<em>121</em> <span>赞</span></span>


<a href="#" name="report" class="report zm-comment-op-link needsfocus">
<i class="zg-icon z-icon-no-help"></i>举报</a>


</div>
</div>
</div>

<div class="zm-item-comment" data-id="69285399">
<a class="zg-anchor-hidden" name="comment-69285399"></a>
<a title="whorlf"
data-tip="p$t$whorlf"
class="zm-item-link-avatar"
href="/people/whorlf">
<img src="http://pic4.zhimg.com/8cf13c0759712406dbb072c457d9509b_s.jpg" class="zm-item-img-avatar">
</a>
<div class="zm-comment-content-wrap">
<div class="zm-comment-hd">
<a data-tip="p$t$whorlf" href="http://www.zhihu.com/people/whorlf" class="zg-link" title="whorlf">whorlf</a>

</div>
<div class="zm-comment-content">
凡所有相，皆是虚妄！
</div>
<div class="zm-comment-ft">
<span class="date">2015-02-10</span>


<a href="#" class="reply zm-comment-op-link" name="reply_comment">
<i class="zg-icon zg-icon-comment-reply"></i>回复</a>


<a href="#" class="like zm-comment-op-link " name="like_comment">
<i class="zg-icon zg-icon-comment-like"></i>赞</a>
<span class="like-num  " data-tip="s$r$953 人觉得这个很赞">
<em>953</em> <span>赞</span></span>


<a href="#" name="report" class="report zm-comment-op-link needsfocus">
<i class="zg-icon z-icon-no-help"></i>举报</a>


</div>
</div>
</div>
'''

soup = BeautifulSoup(html)
b = soup.contents[0].contents[5]
c = b.contents[1]
#print b

print c
