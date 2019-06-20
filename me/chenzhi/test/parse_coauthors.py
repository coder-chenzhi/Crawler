from collections import Counter

coauthors = \
    """
Wei Yang, Xusheng Xiao, Dengfeng Li, Huoran Li, Xuanzhe Liu, Haoyu Wang, Yao Guo, Tao Xie
Xuan Li, Zerui Wang, Qianxiang Wang, Shoumeng Yan, Tao Xie, Hong Mei
Xuan Lu, Xuanzhe Liu, Huoran Li, Tao Xie, Qiaozhu Mei, Dan Hao, Gang Huang, Feng Feng
Sihan Li, Xusheng Xiao, Blake Bassett, Tao Xie, Nikolai Tillmann
Tao Xie, Nikolai Tillmann, Pratap Lakshman
Xuan Lu, Xuanzhe Liu, Huoran Li, Tao Xie, Qiaozhu Mei, Dan Hao, Gang Huang, Feng Feng
Tao Xie, William Enck
Benjamin Andow, Adwait Nadkarni, Blake Bassett, William Enck, Tao Xie
Dongmei Zhang, Tao Xie
Dan Hao, Lu Zhang, Lei Zang, Yanbo Wang, Xingxia Wu, Tao Xie
Xuanzhe Liu, Yun Ma, Yunxin Liu, Tao Xie, Gang Huang
Kai Pan, Xintao Wu, Tao Xie
Yuan Yao, Hanghang Tong, Tao Xie, Leman Akoglu, Feng Xu, Jian Lu
Xusheng Xiao, Nikolai Tillmann, Manuel Fahndrich, Jonathan de Halleux, Michal Moskal, Tao Xie
Tao Xie
Huoran Li, Xuanzhe Liu, Tao Xie, Kaigui Bian, Xuan Lu, Felix Xiaozhu Lin, Qiaozhu Mei, Feng Feng
Rui Ding, Hucheng Zhou, Jian-Guang Lou, Hongyu Zhang, Qingwei Lin, Qiang Fu, Dongmei Zhang, Tao Xie
Yun Ma, Shuhui Zhang, Xuanzhe Liu, Ruirui Xiang, Yunxin Liu, Tao Xie
Wei Yang, Xusheng Xiao, Benjamin Andow, Sihan Li, Tao Xie, William Enck
Judith Bishop, Nigel Horspool, Tao Xie, Nikolai Tillmann, Jonathan de Halleux
Tao Xie, Judith Bishop, Nikolai Tillmann, Jonathan de Halleux
Tao Xie, Judith Bishop, R. Nigel Horspool, Nikolai Tillmann, Jonathan de Halleux
Tao Xie, Nikolai Tillmann, Jonathan de Halleux, Judith Bishop
Tao Xie, Lu Zhang, Xusheng Xiao, Yingfei Xiong, Dan Hao
Kai Pan, Xintao Wu, Tao Xie
Dongmei Zhang, Shi Han, Jian-Guang Lou, Yingnong Dang, Haidong Zhang, Tao Xie
Qiang Liu, Qianxiang Wang, Tao Xie
John Slankas, Xusheng Xiao, Laurie Williams, Tao Xie
Yuan Yao, Hanghang Tong, Tao Xie, Leman Akoglu, Feng Xu, Jian Lu
Rui Ding, Qiang Fu, Jian-Guang Lou, Qingwei Lin, Dongmei Zhang, Tao Xie
Xiao Yu, Shi Han, Dongmei Zhang, Tao Xie
Dongmei Zhang, Tao Xie
William Enck, Tao Xie
Nikolai Tillmann, Jonathan de Halleux, Tao Xie
Nikolai Tillmann, Jonathan de Halleux, Tao Xie, Judith Bishop
Qiang Fu, Jieming Zhu, Wenlu Hu, Jian-Guang Lou, Rui Ding, Qingwei Lin, Dongmei Zhang, Tao Xie
Wei Yang, Xusheng Xiao, Rahul Pandita, William Enck, Tao Xie
Nikolai Tillmann, Jonathan de Halleux, Tao Xie, Judith Bishop
Qianxiang Wang, Wenxin Li, Tao Xie
Nikolai Tillmann, Jonathan de Halleux, Judith Bishop, Tao Xie, Nigel Horspool, Daniel Perelman
Nikolai Tillmann, Judith Bishop, Nigel Horspool, Daniel Perelman, Tao Xie
Dongmei Zhang, Shi Han, Yingnong Dang, Jian-Guang Lou, Haidong Zhang, Tao Xie
Xiaoyin Wang, Lu Zhang, Tao Xie, Hong Mei, Jiasu Sun
Xusheng Xiao, Sihan Li, Tao Xie, Nikolai Tillmann
Sihan Li, Tao Xie, Nikolai Tillmann
Guangtai Liang, Qianxiang Wang, Tao Xie, Hong Mei
Rahul Pandita, Xusheng Xiao, Wei Yang, William Enck, Tao Xie
Ruowen Wang, Peng Ning, Tao Xie, Quan Chen
Xusheng Xiao, Shi Han, Tao Xie, Dongmei Zhang
Qian Wu, Ling Wu, Guangtai Liang, Qianxiang Wang, Tao Xie, Hong Mei
Jue Wang, Yingnong Dang, Hongyu Zhang, Kai Chen, Tao Xie, Dongmei Zhang
Qiang Fu, Jian-Guang Lou, Qingwei Lin, Rui Ding, Dongmei Zhang, Tao Xie
Wei Yang, Mukul Prasad, Tao Xie
Hao Zhong, Suresh Thummalapenta, Tao Xie
Jian-Guang Lou, Qingwei Lin, Rui Ding,  Qiang Fu, Dongmei Zhang, Tao Xie
Nikolai Tillmann, Jonathan de Halleux, Tao Xie, Judith Bishop
Sihan Li, Tian Xiao, Hucheng Zhou, Haoxiang Lin, Haibo Lin, Wei Lin, Tao Xie
Dongmei Zhang, Tao Xie
Nikolai Tillmann, Jonathan De Halleux, Tao Xie, Sumit Gulwani, Judith Bishop
Dongmei Zhang, Tao Xie
Eric Anderson, Sihan Li, Tao Xie
Tao Xie, Nikolai Tillmann, Jonathan de Halleux
Kai Pan, Xintao Wu, Tao Xie
Tao Xie
John J. Majikes, Rahul Pandita, Tao Xie
Sihan Li, Tao Xie, Nikolai Tillmann
Hong Mei, Gang Huang, Tao Xie
Fei Chen, Alex X. Liu, JeeHyun Hwang, Tao Xie
JeeHyun Hwang, Tao Xie, Fei Chen, Alex X. Liu
Linghao Zhang, Xiaoxing Ma, Jian Lu, Tao Xie, Nikolai Tillmann, Jonathan de Halleux
Shing-chi Cheung, Tao Xie, Donggang Cao, Lu Zhang
Yingnong Dang, Dongmei Zhang, Song Ge, Chengyun Chu, Yingjun Qiu, Tao Xie
Xusheng Xiao, Amit Paradkar, Suresh Thummalapenta, Tao Xie
Yida Tao, Yingnong Dang, Tao Xie, Dongmei Zhang, Sunghun Kim
Xiaoyin Wang, Lu Zhang, Tao Xie, Yingfei Xiong, Hong Mei
Qiang Fu, Jian-Guang Lou, Qing-Wei Lin, Rui Ding, Zihao Ye, Dongmei Zhang, Tao Xie
Tao Xie
Jeehyun Hwang, Tao Xie, Donia Elkateb, Tejeddine Mouelhi, Yves Le Traon
Rui Ding, Qiang Fu, Jian-guang Lou, Qingwei Lin, Dongmei Zhang, Jiajun Shen, Tao Xie
Rahul Pandita, Xusheng Xiao, Hao Zhong, Tao Xie, Stephen Oney, Amit Paradkar
Shi Han, Yingnong Dang, Song Ge, Dongmei Zhang, Tao Xie
Donia Elkateb, Tejeddine Mouelhi, Yves Le Traon, Jeehyun Hwang, Tao Xie
Laleh Shikh Gholamhossein Ghandehari, Yu Lei, Tao Xie, D. Richard Kuhn, Raghu Kacker
Nikolai Tillmann, Michal Moskal, Jonathan de Halleux, Manuel Fahndrich, Judith Bishop, Arjmand Samuel, Tao Xie
Dongmei Zhang, Tao Xie
Ahmed E. Hassan, Tao Xie
Dongmei Zhang, Yingnong Dang, Shi Han, Tao Xie
Nikolai Tillmann, Jonathan de Halleux, Tao Xie, Judith Bishop
Nikolai Tillmann, Michal Moskal, Jonathan de Halleux, Manuel Fahndrich, Tao Xie
Nikolai Tillmann, Michal Moskal, Jonathan de Halleux, Manuel Fahndrich, Tao Xie
JeeHyun Hwang, Vincent Hu, Tao Xie
Tao Xie, Suresh Thummalapenta
Kiran Shakya, Tao Xie, Nuo Li, Yu Lei, Raghu Kacker, Richard Kuhn
Xusheng Xiao, Suresh Thummalapenta, Tao Xie
Alex X. Liu, Fei Chen, JeeHyun Hwang, Tao Xie
Vincent Hu, Richard Kuhn, Tao Xie, JeeHyun Hwang
Hao Zhong, Lu Zhang, Tao Xie, Hong Mei
Suresh Thummalapenta, Tao Xie
Kai Pan, Xintao Wu, Tao Xie
Qian Wu, Guangtai Liang, Qianxiang Wang, Tao Xie, Hong Mei
Wujie Zheng, Hao Ma, Michael R. Lyu, Tao Xie, Irwin King
Suresh Thummalapenta, Tao Xie, Nikolai Tillmann, Jonathan de Halleux, Zhendong Su
Kunal Taneja, Mark Grechanik, Rayid Ghani, Tao Xie
Kunal Taneja, Tao Xie, Nikolai Tillmann, Jonathan de Halleux
Yitao Ni, Lu Zhang, Zhongjie Li, Tao Xie, Hong Mei
Xusheng Xiao, Tao Xie, Nikolai Tillmann, Jonathan de Halleux
Suresh Thummalapenta, Madhuri Marri, Tao Xie, Nikolai Tillmann, Jonathan de Halleux
Lin Shi, Hao Zhong, Tao Xie, Mingshu Li
Dongmei Zhang, Tao Xie
Judith Bishop, Jonathan de Halleux, Nikolai Tillmann, Nigel Horspool, Don Syme, Tao Xie
Lin Tan, Tao Xie
Xusheng Xiao, Tao Xie, Nikolai Tillmann, Jonathan de Halleux
Xi Ge, Kunal Taneja, Tao Xie, Nikolai Tillmann
Ahmed E. Hassan, Tao Xie
Nikolai Tillmann, Jonathan de Halleux, Tao Xie
Dongmei Zhang, Yingnong Dang, Jian-Guang Lou, Shi Han, Haidong Zhang, Tao Xie
Kai Pan, Xintao Wu, Tao Xie
Hyun Cho, Jeff Gray, Yuanfang Cai, Sonny Wong, Tao Xie
Mithun Acharya, Tao Xie
Suresh Thummalapenta, Tao Xie, Madhuri R. Marri
Nikolai Tillmann, Jonathan de Halleux, Tao Xie
Xusheng Xiao, Amit Paradkar, Tao Xie
Nuo Li, Tao Xie, Maozhong Jin, Chao Liu
Dan Hao, Tao Xie, Lu Zhang, Xiaoyin Wang, Jiasu Sun, Hong Mei
Xiaoyin Wang, Lu Zhang, Tao Xie, Hong Mei, Jiasu Sun
Fei Chen, Alex X. Liu, JeeHyun Hwang, Tao Xie
Guangtai Liang, Ling Wu, Qian Wu, Qianxiang Wang, Tao Xie, Hong Mei
Kunal Taneja, Yi Zhang, Tao Xie
Kunal Taneja, Nuo Li, Madhuri Marri, Tao Xie, Nikolai Tillmann
Wujie Zheng, Qirun Zhang, Michael Lyu, Tao Xie
LiGuo Huang, Daniel Port, Liang Wang, Tao Xie, Tim Menzies
Rahul Pandita, Tao Xie, Nikolai Tillmann, Jonathan de Halleux
Lingming Zhang, Tao Xie, Lu Zhang, Nikolai Tillmann, Jonathan de Halleux, Hong Mei
Hojun Jaygarl, Sunghun Kim, Tao Xie, Carl K. Chang
JeeHyun Hwang, Tao Xie, Vincent Hu, Mine Altunay
Hao Zhong, Suresh Thummalapenta, Tao Xie, Lu Zhang, Qing Wang
Lu Zhang, Shan-Shan Hou, Jun-Jue Hu, Tao Xie, Hong Mei
Michael Gegick, Pete Rotella, Tao Xie
Wei Jin, Alex Orso, Tao Xie
Tao Xie, Nikolai Tillmann, Jonathan de Halleux, Wolfram Schulte
Ahmed E. Hassan, Tao Xie
Wei Jin, Alex Orso, Tao Xie
Tao Xie, Jonathan de Halleux, Nikolai Tillmann, Wolfram Schulte
JeeHyun Hwang, Tao Xie, Vincent Hu, Mine Altunay
Yoonki Song, Xiaoyin Wang, Tao Xie, Lu Zhang, Hong Mei
Nikolai Tillmann, Jonathan de Halleux, Tao Xie
Ahmed E. Hassan, Tao Xie
JeeHyun Hwang, Evan Martin, Tao Xie, Vincent C. Hu
Xusheng Xiao, Tao Xie, Nikolai Tillmann, Peli de Halleux
Tao Xie, Suresh Thummalapenta, David Lo, Chao Liu
Stephen Thomas, Laurie Williams, Tao Xie
Dan Hao, Lu Zhang, Tao Xie, Hong Mei, Jia-Su Sun
Suresh Thummalapenta, Tao Xie
Hao Zhong, Lu Zhang, Tao Xie, Hong Mei
Nuo Li, Tao Xie, Nikolai Tillmann, Jonathan de Halleux, Wolfram Schulte
JeeHyun Hwang, Tao Xie, Fei Chen, Alex X. Liu
Suresh Thummalapenta, Tao Xie, Nikolai Tillmann, Peli de Halleux, Wolfram Schulte
Lu Zhang, Shan-Shan Hou, Chao Guo, Tao Xie, Hong Mei
JeeHyun Hwang, Tao Xie, Vincent C. Hu
Hao Zhong, Tao Xie, Lu Zhang, Jian Pei, Hong Mei
Tao Xie, Nikolai Tillmann, Peli de Halleux, Wolfram Schulte
Suresh Thummalapenta, Tao Xie
Xiaoyin Wang, Lu Zhang, Tao Xie, Hong Mei, Jiasu Sun
Mithun Acharya, Tao Xie
Mark Harman, Fayezin Islam, Tao Xie, Stefan Wappler
Nikolai Tillmann, Jonathan de Halleux, Tao Xie, Wolfram Schulte
Lingshuang Shao, Junfeng Zhao, Tao Xie, Lu Zhang, Bing Xie, Hong Mei
Wujie Zheng, Michael R. Lyu, Tao Xie
Kunal Taneja, Tao Xie, Nikolai Tillmann, Jonathan de Halleux, Wolfram Schulte
Xiaoyin Wang, Lu Zhang, Tao Xie, Hong Mei, Jiasu Sun
Nikolai Tillmann, Jonathan de Halleux, Tao Xie, Wolfram Schulte
Tao Xie, Ahmed E. Hassan
Madhuri R Marri, Tao Xie, Nikolai Tillmann, Jonathan de Halleux, Wolfram Schulte
Madhuri R Marri, Suresh Thummalapenta, Tao Xie
Tao Xie, Nikolai Tillmann, Jonathan de Halleux, Wolfram Schulte
Ting Yu, Dhivya Sivasubramanian, Tao Xie
Tao Xie
Christoph Csallner, Yannis Smaragdakis, Tao Xie
Vincent Hu, Richard Kuhn, Tao Xie
Evan Martin, JeeHyun Hwang, Tao Xie, Vincent Hu
Prasanth Anbalagan, Tao Xie
JeeHyun Hwang, Tao Xie, Fei Chen, Alex X. Liu
Shan-Shan Hou, Lu Zhang, Tao Xie, Jia-Su Sun
Suresh Thummalapenta, Tao Xie
Kobi Inkumsah, Tao Xie
Kunal Taneja, Tao Xie
Alex X. Liu, Fei Chen, JeeHyun Hwang, Tao Xie
Xiaoyin Wang, Lu Zhang, Tao Xie, John Anvik, Jiasu Sun
Lingshuang Shao, Lu Zhang, Tao Xie, Junfeng Zhao, Bing Xie, Hong Mei
Tevfik Bultan, Tao Xie
Suresh Thummalapenta, Tao Xie
Ahmed E. Hassan, Tao Xie
Alessandro Orso, Tao Xie
Nuo Li, JeeHyun Hwang, Tao Xie
Tao Xie, Nikolai Tillmann, Jonathan de Halleux, Wolfram Schulte
Tao Xie, Mithun Acharya, Suresh Thummalapenta, Kunal Taneja
Suresh Thummalapenta, Tao Xie
Kunal Taneja, Danny Dig, Tao Xie
Kobi Inkumsah, Tao Xie
Yuanfang Cai, Sunny Huynh, Tao Xie
Shan-Shan Hou, Lu Zhang, Tao Xie, Hong Mei, Jia-Su Sun
Mithun Acharya, Tao Xie, Jian Pei, Jun Xu
Prasanth Anbalagan, Tao Xie
Evan Martin, Tao Xie
Chao Liu, Tao Xie, Jiawei Han
Evan Martin, Suranjana Basu, Tao Xie
Tao Xie, Jian Pei, Ahmed E. Hassan
Evan Martin, Suranjana Basu, Tao Xie
Yoonki Song, Suresh Thummalapenta, Tao Xie
Vincent C. Hu, Evan Martin, JeeHyun Hwang, Tao Xie
Evan Martin, Tao Xie
Tao Xie, Kunal Taneja, Shreyas Kale, Darko Marinov
Tao Xie, Jianjun Zhao
Suresh Thummalapenta, Tao Xie
Tao Xie, David Notkin
Evan Martin, Tao Xie, Ting Yu
Mithun Acharya, Tao Xie, Jun Xu
Tao Xie, Jianjun Zhao, Darko Marinov, David Notkin
Marcelo d'Amorim, Carlos Pacheco, Tao Xie, Darko Marinov, Michael D. Ernst
Mithun Acharya, Tanu Sharma, Jun Xu, Tao Xie
Tao Xie
Tao Xie, Jianjun Zhao
Prasanth Anbalagan, Tao Xie
Evan Martin, Tao Xie
Yonghee Shin, Laurie Williams, Tao Xie
Tao Xie
Tao Xie, Jian Pei
Tao Xie, Evan Martin, Hai Yuan
Evan Martin, Tao Xie
Prasanth Anbalagan, Tao Xie
Evan Martin, Suranjana Basu, Tao Xie
Prasanth Anbalagan, Tao Xie
Jianjun Zhao, Tao Xie, Nan Li
Evan Martin, Tao Xie
Tao Xie, Jian Pei
Hai Yuan, Tao Xie
Yonghee Shin, Laurie Williams, Tao Xie
Tao Xie, David Notkin
Tao Xie, David Notkin
Amir Michail, Tao Xie
Tao Xie, Darko Marinov, Wolfram Schulte, David Notkin
Hai Yuan, Tao Xie
Tao Xie, Jianjun Zhao, Darko Marinov, David Notkin
Tao Xie
Tao Xie
Tao Xie, David Notkin
Tao Xie, Darko Marinov, David Notkin
Tao Xie, David Notkin
Tao Xie
Tao Xie, David Notkin
Tao Xie, Darko Marinov, David Notkin
Tao Xie, David Notkin
Tao Xie, David Notkin
Tao Xie, David Notkin
Tao Xie
Hong Mei, Tao Xie, Fuqing Yang
Tao Xie, David Notkin
Tao Xie, David Notkin
Hong Mei, Tao Xie, Wanghong Yuan, Fuqing Yang
Tao Xie, Wanghong Yuan, Hong Mei, Fuqing Yang
Hong Mei, Tao Xie, Fuqing Yang
Wanghong Yuan, Xiangkui Chen, Tao Xie, Hong Mei, Fuqing Yang
Tao Xie
"""
authors = []
for line in coauthors.split("\n"):
    authors.extend(line.split(", "))
cnt = Counter(authors)
for author in cnt.most_common():
    print author[0] + "\t" + str(author[1])