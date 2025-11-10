class Solution {
    public int[] solution(String[] wallpaper) {
        int[] result = new int[4];
        int minx=Integer.MAX_VALUE;
        int miny=Integer.MAX_VALUE;

        int maxx=Integer.MIN_VALUE;
        int maxy=Integer.MIN_VALUE;

        for(int i=0; i<wallpaper.length; i++)
        {
            for(int j=0; j<wallpaper[i].length(); j++)
            {
                if(wallpaper[i].charAt(j)=='#')
                {
                    if(minx > i)
                    {
                         minx=i;
                    }
                    if(miny>j)
                    {
                        miny=j;
                    }

                    if(maxy<=j)
                    {
                        maxy = j+1;
                    }
                    if(maxx<=i)
                    {
                        maxx=i+1;
                    }
                }
            }
        }
        result[0]=minx;
        result[1]=miny;
        result[2]=maxx;
        result[3]=maxy;
        return result;

    }
}