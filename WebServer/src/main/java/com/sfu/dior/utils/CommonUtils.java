package com.sfu.dior.utils;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CommonUtils {
	
	public static Logger getLogger() {
		StackTraceElement[] stackTrace = Thread.currentThread().getStackTrace();
        String callersClassName = stackTrace[2].getClassName();
        return LoggerFactory.getLogger(callersClassName);
	}
	
	public static String trimSingleQuote(String str) {
		if (str != null) {
			String tmp = str;
			try {
				if (str.startsWith("\'")) {
					str = str.substring(1);
				}
				if (str.endsWith("\'")) {
					str = str.substring(0, str.length()-1);
				}
			}catch(Exception e) {
				str = tmp;
			}
		}
		
		return str;
	}
	
	public static Map<String, Integer> sortMapByValue(Map<String, Integer> passedMap) {
    	Map<String, Integer> ret = new LinkedHashMap<>();
    	
    	// 升序比较器
        Comparator<Map.Entry<String, Integer>> valueComparator = new Comparator<Map.Entry<String,Integer>>() {
            @Override
            public int compare(Map.Entry<String, Integer> o1,
            		Map.Entry<String, Integer> o2) {
                // TODO Auto-generated method stub
                return o2.getValue()-o1.getValue();
            }
        };

        // map转换成list进行排序
        List<Map.Entry<String, Integer>> list = new ArrayList<Map.Entry<String,Integer>>(passedMap.entrySet());

        // 排序
        Collections.sort(list,valueComparator);

        for (Map.Entry<String, Integer> entry : list) {
            ret.put(entry.getKey(), entry.getValue());
        }
        return ret;
    }
	
	public static String convertJobType(String jobType) {
		if ("Data Analysis".equals(jobType) || "Data Science".equals(jobType) || "Data Mining".equals(jobType) || "ML/AI".equals(jobType)) {
			jobType = "Data Science";
		} else if ("Software Development".equals(jobType) || "Operating System".equals(jobType) || "Database".equals(jobType)) {
			jobType = "Software Development";
		}
		return jobType;
	}
}
