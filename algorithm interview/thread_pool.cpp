/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * class HtmlParser {
 *   public:
 *     vector<string> getUrls(string url);
 * };
 */
class Solution {
    
    struct ThreadPool{
        int n = 1;
        vector<thread> m_workers;
        unordered_set<string> m_set;
        mutex m;
        condition_variable cv;
        queue<string> q;
        bool done = false;
        
        HtmlParser *htmlParser;
        int working = 0;
        string host;
        string getHost(string url){
            size_t pos = url.find('/',7);
            if(pos != string::npos){
                string host = url.substr(0,pos);

                return host;
            }else return url;
        }
        ThreadPool(int num, HtmlParser &htmlParser, string url){
            n = num;
            host = getHost(url);
            m_set.insert(url);
            q.push(url);
            
            this->htmlParser = &htmlParser;
            for(int i = 0; i < num; i++){
                m_workers.push_back(thread(&ThreadPool::start, this));
            }
        }
        void start(){
            while(true){
                unique_lock lck(m);
                cv.wait(lck, [&](){return q.size() > 0|| done == true;});
                if(done == true)break;
                string url = q.front();
                q.pop();
                working++;
               
                lck.unlock();
                vector<string> urls = htmlParser->getUrls(url);
                lck.lock();
                for(string str: urls){
                    if(getHost(str) == host && m_set.insert(str).second)
                        q.push(str);
                }
                working--;
               
                
                if(working == 0 && q.size() == 0){
                    done = true;
                }
                cv.notify_all();
            }
            
            
        }
    };
public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        ThreadPool pool(thread::hardware_concurrency(), htmlParser, startUrl);
        for(int i = 0; i < pool.m_workers.size(); i++){
            pool.m_workers[i].join();
        }
        vector<string> result;
        for(auto str: pool.m_set)
            result.push_back(str);
        return result;
    }
};
