#ifndef __CRAWLER_WEIBO_ICE__
#define __CRAWLER_WEIBO_ICE__

module com {
    module bfd {
        module crawler {
            interface weiboControl{
                string addTask(string request);
                string queryTask(string request);
                string delTask(string request);
            };
        };
    };
};

#endif