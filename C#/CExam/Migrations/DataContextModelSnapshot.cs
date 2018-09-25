﻿// <auto-generated />
using CExam.Data;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Infrastructure;
using Microsoft.EntityFrameworkCore.Metadata;
using Microsoft.EntityFrameworkCore.Migrations;
using MySql.Data.EntityFrameworkCore.Storage.Internal;
using System;

namespace CExam.Migrations
{
    [DbContext(typeof(DataContext))]
    partial class DataContextModelSnapshot : ModelSnapshot
    {
        protected override void BuildModel(ModelBuilder modelBuilder)
        {
#pragma warning disable 612, 618
            modelBuilder
                .HasAnnotation("ProductVersion", "2.0.3-rtm-10026");

            modelBuilder.Entity("CExam.Models.Act", b =>
                {
                    b.Property<int>("ActId")
                        .ValueGeneratedOnAdd();

                    b.Property<int>("ActDuration");

                    b.Property<string>("ActName");

                    b.Property<string>("ActTime");

                    b.Property<DateTime>("Date");

                    b.Property<string>("Description");

                    b.Property<int>("UserId");

                    b.HasKey("ActId");

                    b.HasIndex("UserId");

                    b.ToTable("Acts");
                });

            modelBuilder.Entity("CExam.Models.Join", b =>
                {
                    b.Property<int>("JoinId")
                        .ValueGeneratedOnAdd();

                    b.Property<int>("ActId");

                    b.Property<int>("UserId");

                    b.HasKey("JoinId");

                    b.HasIndex("ActId");

                    b.HasIndex("UserId");

                    b.ToTable("Joins");
                });

            modelBuilder.Entity("CExam.Models.User", b =>
                {
                    b.Property<int>("UserId")
                        .ValueGeneratedOnAdd();

                    b.Property<string>("Email");

                    b.Property<string>("FirstName");

                    b.Property<string>("LastName");

                    b.Property<string>("Password");

                    b.HasKey("UserId");

                    b.ToTable("Users");
                });

            modelBuilder.Entity("CExam.Models.Act", b =>
                {
                    b.HasOne("CExam.Models.User", "User")
                        .WithMany("Acts")
                        .HasForeignKey("UserId")
                        .OnDelete(DeleteBehavior.Cascade);
                });

            modelBuilder.Entity("CExam.Models.Join", b =>
                {
                    b.HasOne("CExam.Models.Act", "Act")
                        .WithMany("Joins")
                        .HasForeignKey("ActId")
                        .OnDelete(DeleteBehavior.Cascade);

                    b.HasOne("CExam.Models.User", "User")
                        .WithMany("Joins")
                        .HasForeignKey("UserId")
                        .OnDelete(DeleteBehavior.Cascade);
                });
#pragma warning restore 612, 618
        }
    }
}
