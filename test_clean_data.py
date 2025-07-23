#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import importlib.util
import sys

# 动态导入 clean-data.py 模块
spec = importlib.util.spec_from_file_location("clean_data", "clean-data.py")
clean_data = importlib.util.module_from_spec(spec)
spec.loader.exec_module(clean_data)


def test_clean_web_content():
    """测试网页内容清洗功能"""
    
    # 测试数据
    test_data = """
\\n                                   \\n          如何1年内把1万变成114亿？\\n            \\n                东方财富网\\n               \\n                2024-12-23\\n               \\n            已关注\\n           　　内容仅供娱乐，开心就好!　　假设2024年初我们拿着1万块入市，每个月都买最牛的那只股票，现在手里能有多少钱？　　在连续买入月度“涨幅王”的设定下，我们的本金将在3月份突破10万元，4月份突破100万元，7月份突破1000万元，9月份突破1亿元,10月份突破10亿元,12月突破100亿元。截至12月23日收盘，我们的资产将变成114亿元，完成114个“小目标”。　　既然连续买入月度最牛股，资产能膨胀到114亿元，那么换个角度，假设回到2024年初，我们连续买入的都是月度最熊股，资产会萎缩到多少？　　在连续买入月度“跌幅王”的设定下，我们1万块的本金将在1月份末宣告腰斩，在4月份跌破1000元，在7月份跌破100元，在11月份跌破10元。截至12月23日收盘，我们1万元的本金将只剩下3.61元，相较年初累计下跌99.96%。　　连续买入2024年月度最牛股和月度最熊股，最终资产分别为114亿元与3.61元，两者之间差了近32亿倍，属实是天差地别。当然，上述资产变动情况仅限于理论状态，现实中不可能实现。我们从中可以看到的是，在决策连续成功/失败的情况下，我们资产的变动幅度将会异常巨大，投资者在交易中需要更为审慎。（文章来源：东方财富研究中心）  \\n            * 相关产品如下，点击可了解详情 ↓↓\\n            \\n              谈股论市\\n             \\n            阅读 7555\\n                  \\n        免责声明\\n       \\n        版权申明\\n       \\n        关注平安银行\\n       \\n        长按识别二维码进行关注\\n         \\n          设置字体大小\\n          小 标准 大 特大         \\n      相关产品\\n        \\n            商品\\n                  合格投资者确认  本人确认符合监管部门最新规定的“合格投资者”条件： 1、具有相应风险识别能力和风险承担能力； 2、具有2年以上投资经历，且满足以下条件之一： 家庭金融净资产不低于300万元； 家庭金融资产不低于500万元； 最近三年个人年均收入不低于40万元。            \\n        确定\\n            \\n      金币已装入口袋中\\n     \\n      关注成功\\n     \\n      您可以勾选APP（平安口袋银行）通知获取最新资讯推送。\\n     \\n          APP通知\\n         \\n          微信通知\\n         \\n        看看其他\\n       \\n        我知道了\\n         window.__NUXT__=(function(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p){i.allowComment=\\\"2\\\";i.author=\\\"SYSTEM\\\";i.columnInfo=f;i.contentHtml=\\\"\\\\u003Cp\\\\u003E　　\\\\u003Cstrong\\\\u003E内容仅供娱乐，开心就好!\\\\u003C\\\\u002Fstrong\\\\u003E\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Ccenter\\\\u003E\\\\u003Cimg src=\\\\\\\"https:\\\\u002F\\\\u002Fnp-newspic.dfcfw.com\\\\u002Fdownload\\\\u002FD25730774900815789399_w1563h5643_o.jpg\\\\\\\" width=\\\\\\\"580\\\\\\\" style=\\\\\\\"border:#d1d1d1 1px solid;padding:3px;margin:5px 0;\\\\\\\" \\\\u002F\\\\u003E\\\\u003C\\\\u002Fcenter\\\\u003E\\\\u003Cp\\\\u003E　　假设2024年初我们拿着1万块入市，每个月都买最牛的那只股票，现在手里能有多少钱？\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp\\\\u003E　　在连续买入月度“涨幅王”的设定下，我们的本金将在3月份突破10万元，4月份突破100万元，7月份突破1000万元，9月份突破1亿元,10月份突破10亿元,12月突破100亿元。截至12月23日收盘，我们的资产将变成114亿元，完成114个“小目标”。\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp\\\\u003E　　既然连续买入月度最牛股，资产能膨胀到114亿元，那么换个角度，假设回到2024年初，我们连续买入的都是月度最熊股，资产会萎缩到多少？\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp\\\\u003E　　在连续买入月度“跌幅王”的设定下，我们1万块的本金将在1月份末宣告腰斩，在4月份跌破1000元，在7月份跌破100元，在11月份跌破10元。截至12月23日收盘，我们1万元的本金将只剩下3.61元，相较年初累计下跌99.96%。\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp\\\\u003E　　连续买入2024年月度最牛股和月度最熊股，最终资产分别为114亿元与3.61元，两者之间差了近32亿倍，属实是天差地别。当然，上述资产变动情况仅限于理论状态，现实中不可能实现。我们从中可以看到的是，在决策连续成功\\\\u002F失败的情况下，我们资产的变动幅度将会异常巨大，投资者在交易中需要更为审慎。\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp style=\\\\\\\"text-align:center;\\\\\\\"\\\\u003E\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp class=\\\\\\\"em_media\\\\\\\"\\\\u003E（文章来源：东方财富研究中心）\\\\u003C\\\\u002Fp\\\\u003E\\\";i.contentTagList=j;i.contentText=a;i.coverPhoto=a;i.customersLabel=a;i.digest=c;i.digestShow=g;i.focusPhoto=\\\"https:\\\\u002F\\\\u002Fcdn.sdb.com.cn\\\\u002Fapp_upload\\\\u002Fbrop-mop\\\\u002Fnews\\\\u002Fdefault\\\\u002FfocusPhoto\\\\u002F00000015.jpg\\\";i.hostType=\\\"03\\\";i.id=e;i.infoType=\\\"4\\\";i.isAuth=d;i.isShare=d;i.isShowSDK=g;i.labelId=a;i.leftButtonContent=a;i.leftButtonUrl=a;i.multipleThumbnails=f;i.pcUrl=\\\"https:\\\\u002F\\\\u002Febank.pingan.com.cn\\\\u002Finfo\\\\u002Fzixun\\\\u002Fdetail.shtml?id=003905212&outerSource=zxpt_2412_022462\\\";i.pdfUrl=a;i.posterImg=a;i.publishTime=\\\"2024-12-23 17:11:05\\\";i.readings=k;i.rightButtonContent=a;i.rightButtonUrl=a;i.serviceInfo=l;i.serviceNoThumbnail=n;i.shareContent=a;i.sharePic=a;i.shareTitle=a;i.shareVisitCard=d;i.showStyle=a;i.sign=a;i.source=h;i.tagName=a;i.targetGroupCategory=g;i.thumbnail=n;i.title=c;i.typeContent=\\\"快讯\\\";i.url=\\\"https:\\\\u002F\\\\u002Fb.pingan.com.cn\\\\u002Fnode-ssr\\\\u002Fbase\\\\u002Fbrop-cmp\\\\u002Fssr\\\\u002Fugc\\\\u002Fdetails\\\\u002F003905212\\\\u002F?outerSource=zxpt_2412_022462&tempType=bank\\\";i.windowContent=a;i.publishTimeFrom=\\\"2024-12-23\\\";i.readingsForm=k;i.contentHtmlFormArr=[{type:a,content:a,itemContent:\\\"\\\\u003Cp data-height-pushed=\\\\\\\"00\\\\\\\" olabel=\\\\\\\"003905212-段落995280\\\\\\\"\\\\u003E　　\\\\u003Cstrong\\\\u003E内容仅供娱乐，开心就好!\\\\u003C\\\\u002Fstrong\\\\u003E\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Ccenter\\\\u003E\\\\u003Cimg alt=\\\\\\\"东方财富网\\\\\\\"  src=\\\\\\\"https:\\\\u002F\\\\u002Fnp-newspic.dfcfw.com\\\\u002Fdownload\\\\u002FD25730774900815789399_w1563h5643_o.jpg\\\\\\\" width=\\\\\\\"580\\\\\\\" style=\\\\\\\"border:#d1d1d1 1px solid;padding:3px;margin:5px 0;\\\\\\\" \\\\u002F\\\\u003E\\\\u003C\\\\u002Fcenter\\\\u003E\\\\u003Cp data-height-pushed=\\\\\\\"00\\\\\\\" olabel=\\\\\\\"003905212-段落995281\\\\\\\"\\\\u003E　　假设2024年初我们拿着1万块入市，每个月都买最牛的那只股票，现在手里能有多少钱？\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp data-height-pushed=\\\\\\\"00\\\\\\\" olabel=\\\\\\\"003905212-段落995282\\\\\\\"\\\\u003E　　在连续买入月度“涨幅王”的设定下，我们的本金将在3月份突破10万元，4月份突破100万元，7月份突破1000万元，9月份突破1亿元,10月份突破10亿元,12月突破100亿元。截至12月23日收盘，我们的资产将变成114亿元，完成114个“小目标”。\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp data-height-pushed=\\\\\\\"00\\\\\\\" olabel=\\\\\\\"003905212-段落995283\\\\\\\"\\\\u003E　　既然连续买入月度最牛股，资产能膨胀到114亿元，那么换个角度，假设回到2024年初，我们连续买入的都是月度最熊股，资产会萎缩到多少？\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp data-height-pushed=\\\\\\\"00\\\\\\\" olabel=\\\\\\\"003905212-段落995284\\\\\\\"\\\\u003E　　在连续买入月度“跌幅王”的设定下，我们1万块的本金将在1月份末宣告腰斩，在4月份跌破1000元，在7月份跌破100元，在11月份跌破10元。截至12月23日收盘，我们1万元的本金将只剩下3.61元，相较年初累计下跌99.96%。\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp data-height-pushed=\\\\\\\"00\\\\\\\" olabel=\\\\\\\"003905212-段落995285\\\\\\\"\\\\u003E　　连续买入2024年月度最牛股和月度最熊股，最终资产分别为114亿元与3.61元，两者之间差了近32亿倍，属实是天差地别。当然，上述资产变动情况仅限于理论状态，现实中不可能实现。我们从中可以看到的是，在决策连续成功\\\\u002F失败的情况下，我们资产的变动幅度将会异常巨大，投资者在交易中需要更为审慎。\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp data-height-pushed=\\\\\\\"00\\\\\\\" olabel=\\\\\\\"003905212-段落995286\\\\\\\" style=\\\\\\\"text-align:center;\\\\\\\"\\\\u003E\\\\u003C\\\\u002Fp\\\\u003E\\\\u003Cp data-height-pushed=\\\\\\\"00\\\\\\\" olabel=\\\\\\\"003905212-段落995287\\\\\\\" class=\\\\\\\"em_media\\\\\\\"\\\\u003E（文章来源：东方财富研究中心）\\\\u003C\\\\u002Fp\\\\u003E\\\",itemType:\\\"rich\\\"}];j[0]={category:a,source:\\\"DQ\\\",tagCode:\\\"CLS_A20202012\\\",tagName:\\\"谈股论市\\\",urlHttpsTagList:\\\"https:\\\\u002F\\\\u002Frsb.pingan.com.cn\\\\u002Fbrop\\\\u002Fmop\\\\u002Fadms\\\\u002Fcust\\\\u002Fadmssf\\\\u002Fuc\\\\u002Finformation\\\\u002Fnews\\\\u002Ftag\\\\u002Flist?tagCode=CLS_A20202012&tagFlag=TAG_ALL&pageNo=1&pageSize=30\\\",urlTagList:\\\"\\\\u002Fbrop\\\\u002Fmop\\\\u002Fadms\\\\u002Fcust\\\\u002Fadmssf\\\\u002Fuc\\\\u002Finformation\\\\u002Fnews\\\\u002Ftag\\\\u002Flist?tagCode=CLS_A20202012&tagFlag=TAG_ALL&pageNo=1&pageSize=30\\\",urlTagPath:\\\"\\\\u002Fuc\\\\u002Finformation\\\\u002Fnews\\\\u002Ftag\\\\u002Flist\\\",weight:62.99,tagNameEncode:\\\"%E8%B0%88%E8%82%A1%E8%AE%BA%E5%B8%82\\\"};l.description=\\\"提供7*24小时财经资讯及全球金融市场报价\\\";l.icon=\\\"https:\\\\u002F\\\\u002Fcdn.sdb.com.cn\\\\u002Fapp_upload\\\\u002Fbrop-mop\\\\u002Fservice\\\\u002Fhead\\\\u002F301b8b5b49ea4b1491df653b01e78007_100_100.jpg\\\";l.infoId=e;l.serviceName=h;l.serviceNo=m;l.serviceType=\\\"01\\\";l.status=d;l.url=\\\"https:\\\\u002F\\\\u002Fb.pingan.com.cn\\\\u002Finfo\\\\u002Fzixun\\\\u002Fservice\\\\u002Fnews.shtml?serviceId=ZX_FWH_1064\\\";return {layout:\\\"default\\\",data:[{detailId:e,detailData:{responseCode:\\\"000000\\\",responseMsg:\\\"成功\\\",currentTime:\\\"2025-07-23 15:59:36\\\",info:i},seoObj:{title:c,description:c,keywords:\\\"平安口袋银行,平安头条,天天有料,东方财富网,谈股论市\\\"},contentVote:[],contentYinji:[],pagemakerCard:[],isQueryQualified:b,serviceNo:m,serviceName:h,detailDataInfo:i,serviceInfo:l,detailLabel:j,ableShowProduct:b}],fetch:{},error:f,state:{pageTraceNo:\\\"772124\\\",notLogin:b,httpError:b,httpErrorMessage:a,httpServerTimeout:b,httpServerTimeoutList:[],body:{},firstScreenload:b,goNewPage:b,cookie:void 0,communityIndex:{msgCapsuleObj:{}},details:{audioStatusId:a,isOpenComment:b,countData:o,isShowMarketIcon:b,isShowMarketDialog:b,isQueryQualifiedinvestor:b,isShowKypProductInfos:b,isShowAttentDialog:b,isLnbBigfont:b,isCanComment:p},newsDetails:{isOpenComment:b,countData:o}},serverRendered:p,routePath:\\\"\\\\u002Fdetails\\\\u002F003905212\\\\u002F\\\",config:{_app:{basePath:\\\"\\\\u002Fnode-ssr\\\\u002Fbase\\\\u002Fbrop-cmp\\\\u002Fssr\\\\u002Fugc\\\\u002F\\\",assetsPath:\\\"\\\\u002F\\\",cdnURL:\\\"https:\\\\u002F\\\\u002Fcdn.sdb.com.cn\\\\u002Fnode-ssr\\\\u002Fbase\\\\u002Fbrop-cmp\\\\u002Fssr\\\\u002Fugc\\\\u002F_nuxt\\\\u002F\\\"}}}}(\\\"\\\",false,\\\"如何1年内把1万变成114亿？\\\",\\\"1\\\",\\\"003905212\\\",null,\\\"0\\\",\\\"东方财富网\\\",{},Array(1),7555,{},\\\"ZX_FWH_1064\\\",\\\"https:\\\\u002F\\\\u002Fcdn.sdb.com.cn\\\\u002Fbrcp\\\\u002Fwefiles\\\\u002Fcdn\\\\u002FopenDownload\\\\u002FF07d1a2c0a08e46fea8e68c7758de54a1\\\",0,true));\\n\\n\\n\\n
"""    

    print("🧪 开始测试网页内容清洗功能...")
    print("=" * 60)
    
    # 调用清洗函数
    result = clean_data.clean_web_content(test_data)
    
    # 输出结果
    print("📋 清洗结果:")
    print(f"标题: {result['title']}")
    print(f"内容长度: {len(result['content'])} 字符")
    print(f"图片数量: {len(result['image_urls'])} 张")
    
    if result['image_urls']:
        print("🖼️  提取到的图片URL:")
        for i, url in enumerate(result['image_urls'], 1):
            print(f"  {i}. {url}")
    else:
        print("❌ 未提取到图片URL")
    
    print("\n📄 文章内容预览 (前200字符):")
    print("-" * 40)
    print(result['content'][:200] + "..." if len(result['content']) > 200 else result['content'])
    print("-" * 40)
    
    # 验证结果
    print("\n✅ 验证结果:")
    
    # 验证标题
    expected_title = "如何1年内把1万变成114亿？"
    if result['title'] == expected_title:
        print(f"✅ 标题提取正确: {result['title']}")
    else:
        print(f"❌ 标题提取错误: 期望 '{expected_title}', 实际 '{result['title']}'")
    
    # 验证图片URL
    expected_image_url = "https://np-newspic.dfcfw.com/download/D25730774900815789399_w1563h5643_o.jpg"
    if expected_image_url in result['image_urls']:
        print(f"✅ 图片URL提取正确: {expected_image_url}")
    else:
        print(f"❌ 图片URL提取失败: 期望包含 '{expected_image_url}'")
        print(f"   实际提取到的URL: {result['image_urls']}")
    
    # 验证内容
    if "内容仅供娱乐" in result['content'] and "（文章来源：东方财富研究中心）" in result['content']:
        print("✅ 文章内容提取正确")
    else:
        print("❌ 文章内容提取错误")
    
    print("\n" + "=" * 60)
    print("🎉 测试完成!")

if __name__ == "__main__":
    test_clean_web_content() 