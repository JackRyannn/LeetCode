//计算最短路径的方法 DJ算法
public class Main {
    public static void main(String[] args) {
        int MAX = 65535;
//        目标点
        int D = 1;
        int N = 5;
        int i = 0;
        int[] tmpv = new int[5];
//        距离0点最近的嘛，所以把0点先标记一下。0是未标记，1是标记
        tmpv[D] = 1;
        int[][] edgeform = {{MAX, 2, 5, MAX, 3},
                            {2, MAX, MAX, 4, MAX},
                            {5, MAX, MAX, MAX, 5},
                            {MAX, 4, MAX, MAX, 2},
                            {3, MAX, 5, 2, MAX}};

        int[] weight = edgeform[D];
        int[] path = new int[5];
//        循环五次，每次找到距离 点0 (除去已经走过的点）最近的点
        for(i=0;i<N-1;i++){
            int min = MAX;
//            k为选中的权值最小的路径的点
            int k = -1;
            for(int j = 0;j<N;j++){
                if(tmpv[j] == 0 && weight[j]<min){
                    min = weight[j];
                    k = j;
                }
            }
            tmpv[k] = 1;
//            由于k点的改变，weight和path也要随之更新
            for(int j = 0;j<N;j++){
                for(int p = 0;p<N;p++){
                    if(tmpv[p] == 0 && weight[k] + edgeform[k][p] < weight[p]){
                        weight[p] = weight[k] + edgeform[k][p];
                    }
                }
            }
        }
        for(int w :weight){

            System.out.println(w);
        }

    }
}