package com.sfu.dior.pojo;
import javax.persistence.*;
import java.sql.Date;


@Entity
@IdClass(InterviewId.class)
@Table(name = "interview")
public class Interview {
    @Id
    @Column(name = "comp_id")
    private String compId;

    @Id
    @Column(name = "job_id")
    private int jobId;

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "interview_id")
    private int interviewId;

    @Column(name = "date")
    private Date date;

    @Column(name = "question")
    private String question;

    public String getCompId() {
        return compId;
    }

    public void setCompId(String compId) {
        this.compId = compId;
    }

    public int getJobId() {
        return jobId;
    }

    public void setJobId(int jobId) {
        this.jobId = jobId;
    }

    public Date getDate() {
        return date;
    }

    public void setDate(Date date) {
        this.date = date;
    }


    public int getInterviewId() {
        return interviewId;
    }

    public void setInterviewId(int interviewId) {
        this.interviewId = interviewId;
    }


    public String getQuestion() {
        return question;
    }

    public void setQuestion(String question) {
        this.question = question;
    }
}
