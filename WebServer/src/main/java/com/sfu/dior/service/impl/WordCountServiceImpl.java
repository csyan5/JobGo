package com.sfu.dior.service.impl;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

import org.apache.spark.api.java.JavaSparkContext;
import org.apache.spark.sql.Dataset;
import org.apache.spark.sql.RelationalGroupedDataset;
import org.apache.spark.sql.Row;
import org.apache.spark.sql.SparkSession;
import org.slf4j.Logger;

import static org.apache.spark.sql.functions.col;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.sfu.dior.service.WordCountService;
import com.sfu.dior.utils.CommonUtils;
import com.sfu.dior.utils.Count;
import com.sfu.dior.utils.Word;

@Service
public class WordCountServiceImpl implements WordCountService{
	@Autowired
    private JavaSparkContext javaSparkContext;
    @Autowired
    private SparkSession sparkSession;
    
    private Logger logger = CommonUtils.getLogger();
	@Override
	public List<Count> wordCount(String words) {
		// TODO Auto-generated method stub
		String[] word_set = words.split(" ");
		List<Word> wordList = Arrays.stream(word_set).map(Word::new).collect(Collectors.toList());
		Dataset<Row> dataFrame = sparkSession.createDataFrame(wordList,Word.class);
        
        RelationalGroupedDataset groupedDataset = dataFrame.groupBy(col("word"));
        List<Row> rows = groupedDataset.count().collectAsList();
        
        List<Count> res = new ArrayList<>();
        for (Row row : rows) {
        	res.add(new Count(row.getString(0), row.getLong(1)));
        }
        dataFrame.show();
        
        return res;
	}

}
