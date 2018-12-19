package com.sfu.dior.pojo;
import javax.persistence.*;

@Entity
@IdClass(CompanyReviewId.class)
@Table(name = "company_review")
public class CompanyReview {
    @Id
    @Column
    private String compId;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column
    private int reviewId;

    @Column(name = "reviewer_title")
    private String reviewerTitle;
    
    @Column(name = "score")
    private String score;

    @Column(name = "pros")
    private String pros;

	@Column(name = "cons")
    private String cons;

    public String getCompId() {
        return compId;
    }

    public void setCompId(String compId) {
        this.compId = compId;
    }

    public int getReviewId() {
        return reviewId;
    }

    public void setReviewId(int reviewId) {
        this.reviewId = reviewId;
    }

    public String getReviewerTitle() {
		return reviewerTitle;
	}

	public void setReviewerTitle(String reviewerTitle) {
		this.reviewerTitle = reviewerTitle;
	}
	
    public String getScore() {
        return score;
    }

    public void setScore(String score) {
        this.score = score;
    }

    public String getPros() {
        return pros;
    }

    public void setPros(String pros) {
        this.pros = pros;
    }

    public String getCons() {
        return cons;
    }

    public void setCons(String cons) {
        this.cons = cons;
    }
}
