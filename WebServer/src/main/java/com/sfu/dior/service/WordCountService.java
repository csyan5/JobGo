package com.sfu.dior.service;

import java.util.List;

import com.sfu.dior.utils.Count;

public interface WordCountService {
	List<Count> wordCount(String words);
}
