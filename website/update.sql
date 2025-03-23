BEGIN TRANSACTION;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 5) WHERE
pokedex_nbr = 113 OR pokedex_nbr = 440;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 10) WHERE
pokedex_nbr = 242;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 15) WHERE
pokedex_nbr = 63 OR pokedex_nbr = 172 OR pokedex_nbr = 174 OR pokedex_nbr = 238;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 20) WHERE
pokedex_nbr = 39 OR pokedex_nbr = 318 OR pokedex_nbr = 349 OR pokedex_nbr = 746 
OR pokedex_nbr = 824 OR pokedex_nbr = 921;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 23) WHERE
pokedex_nbr = 293;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 25) WHERE
pokedex_nbr = 50 OR pokedex_nbr = 280 OR pokedex_nbr = 960;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 28) WHERE
pokedex_nbr = 173 OR pokedex_nbr = 827;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 30) WHERE
pokedex_nbr = 13 OR pokedex_nbr = 21 OR pokedex_nbr = 64 OR pokedex_nbr = 92
OR pokedex_nbr = 163 OR pokedex_nbr = 165 OR pokedex_nbr = 191 OR pokedex_nbr = 228 
OR pokedex_nbr = 270 OR pokedex_nbr = 276 OR pokedex_nbr = 278 OR pokedex_nbr = 296 
OR pokedex_nbr = 396 OR pokedex_nbr = 731 OR pokedex_nbr = 734 OR pokedex_nbr = 859 
OR pokedex_nbr = 885 OR pokedex_nbr = 946 OR pokedex_nbr = 955;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 31) WHERE
pokedex_nbr = 789;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 32) WHERE
pokedex_nbr = 283 OR pokedex_nbr = 522;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 33) WHERE
pokedex_nbr = 694;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 34) WHERE
pokedex_nbr = 161 OR pokedex_nbr = 403 OR pokedex_nbr = 425;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 35) WHERE
pokedex_nbr = 10 OR pokedex_nbr = 19 OR pokedex_nbr = 41 OR pokedex_nbr = 52
OR pokedex_nbr = 56 OR pokedex_nbr = 69 OR pokedex_nbr = 72 OR pokedex_nbr = 124
OR pokedex_nbr = 223 OR pokedex_nbr = 235 OR pokedex_nbr = 236 OR pokedex_nbr = 252
OR pokedex_nbr = 261 OR pokedex_nbr = 265 OR pokedex_nbr = 281 OR pokedex_nbr = 320
OR pokedex_nbr = 325 OR pokedex_nbr = 353 OR pokedex_nbr = 406 OR pokedex_nbr = 418
OR pokedex_nbr = 551 OR pokedex_nbr = 704 OR pokedex_nbr = 714 OR pokedex_nbr = 753
OR pokedex_nbr = 821 OR pokedex_nbr = 848 OR pokedex_nbr = 872 OR pokedex_nbr = 940
OR pokedex_nbr = 944 OR pokedex_nbr = 948;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 37) WHERE
pokedex_nbr = 239 OR pokedex_nbr = 240 OR pokedex_nbr = 509 OR pokedex_nbr = 795;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 38) WHERE
pokedex_nbr = 170 OR pokedex_nbr = 659 OR pokedex_nbr = 761;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 39) WHERE
pokedex_nbr = 504 OR pokedex_nbr = 669;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 40) WHERE
pokedex_nbr = 15 OR pokedex_nbr = 16 OR pokedex_nbr = 25 OR pokedex_nbr = 32
OR pokedex_nbr = 37 OR pokedex_nbr = 60 OR pokedex_nbr = 167 OR pokedex_nbr = 179
OR pokedex_nbr = 187 OR pokedex_nbr = 218 OR pokedex_nbr = 220 OR pokedex_nbr = 255
OR pokedex_nbr = 274 OR pokedex_nbr = 298 OR pokedex_nbr = 309 OR pokedex_nbr = 311
OR pokedex_nbr = 319 OR pokedex_nbr = 322 OR pokedex_nbr = 331 OR pokedex_nbr = 399
OR pokedex_nbr = 408 OR pokedex_nbr = 446 OR pokedex_nbr = 447 OR pokedex_nbr = 453
OR pokedex_nbr = 529 OR pokedex_nbr = 535 OR pokedex_nbr = 570 OR pokedex_nbr = 572
OR pokedex_nbr = 577 OR pokedex_nbr = 602 OR pokedex_nbr = 613 OR pokedex_nbr = 617
OR pokedex_nbr = 653 OR pokedex_nbr = 656 OR pokedex_nbr = 664 OR pokedex_nbr = 725
OR pokedex_nbr = 742 OR pokedex_nbr = 744 OR pokedex_nbr = 757 OR pokedex_nbr = 767
OR pokedex_nbr = 813 OR pokedex_nbr = 816 OR pokedex_nbr = 846 OR pokedex_nbr = 868
OR pokedex_nbr = 915 OR pokedex_nbr = 919 OR pokedex_nbr = 922 OR pokedex_nbr = 935
OR pokedex_nbr = 951 OR pokedex_nbr = 963;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 41) WHERE
pokedex_nbr = 263 OR pokedex_nbr = 401 OR pokedex_nbr = 938;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 42) WHERE
pokedex_nbr = 198 OR pokedex_nbr = 415 OR pokedex_nbr = 431 OR pokedex_nbr = 969;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 43) WHERE
pokedex_nbr = 4 OR pokedex_nbr = 155 OR pokedex_nbr = 294 OR pokedex_nbr = 339
OR pokedex_nbr = 527 OR pokedex_nbr = 661;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 44) WHERE
pokedex_nbr = 23 OR pokedex_nbr = 390 OR pokedex_nbr = 426 OR pokedex_nbr = 427;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 45) WHERE
pokedex_nbr = 40 OR pokedex_nbr = 58 OR pokedex_nbr = 65 OR pokedex_nbr = 84 
OR pokedex_nbr = 93 OR pokedex_nbr = 96 OR pokedex_nbr = 147 OR pokedex_nbr = 177
OR pokedex_nbr = 193 OR pokedex_nbr = 194 OR pokedex_nbr = 225 OR pokedex_nbr = 253
OR pokedex_nbr = 291 OR pokedex_nbr = 292 OR pokedex_nbr = 300 OR pokedex_nbr = 315
OR pokedex_nbr = 321 OR pokedex_nbr = 328 OR pokedex_nbr = 412 OR pokedex_nbr = 420
OR pokedex_nbr = 439 OR pokedex_nbr = 441 OR pokedex_nbr = 443 OR pokedex_nbr = 498
OR pokedex_nbr = 501 OR pokedex_nbr = 506 OR pokedex_nbr = 517 OR pokedex_nbr = 552
OR pokedex_nbr = 554 OR pokedex_nbr = 566 OR pokedex_nbr = 588 OR pokedex_nbr = 590
OR pokedex_nbr = 736 OR pokedex_nbr = 850 OR pokedex_nbr = 854 OR pokedex_nbr = 856
OR pokedex_nbr = 860 OR pokedex_nbr = 912 OR pokedex_nbr = 917 OR pokedex_nbr = 924
OR pokedex_nbr = 928 OR pokedex_nbr = 957 OR pokedex_nbr = 974 OR pokedex_nbr = 996
OR pokedex_nbr = 1012;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 46) WHERE
pokedex_nbr = 291;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 47) WHERE
pokedex_nbr = 434 OR pokedex_nbr = 670 OR pokedex_nbr = 793;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 48) WHERE
pokedex_nbr = 35 OR pokedex_nbr = 54 OR pokedex_nbr = 132 OR pokedex_nbr = 201 
OR pokedex_nbr = 360 OR pokedex_nbr = 422 OR pokedex_nbr = 511 OR pokedex_nbr = 513 
OR pokedex_nbr = 515 OR pokedex_nbr = 672 OR pokedex_nbr = 708 OR pokedex_nbr = 762;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 49) WHERE
pokedex_nbr = 1 OR pokedex_nbr = 404 OR pokedex_nbr = 878;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 50) WHERE
pokedex_nbr = 12 OR pokedex_nbr = 14 OR pokedex_nbr = 48 OR pokedex_nbr = 51
OR pokedex_nbr = 66 OR pokedex_nbr = 70 OR pokedex_nbr = 88 OR pokedex_nbr = 100
OR pokedex_nbr = 133 OR pokedex_nbr = 164 OR pokedex_nbr = 166 OR pokedex_nbr = 183
OR pokedex_nbr = 188 OR pokedex_nbr = 209 OR pokedex_nbr = 216 OR pokedex_nbr = 229
OR pokedex_nbr = 246 OR pokedex_nbr = 258 OR pokedex_nbr = 267 OR pokedex_nbr = 271
OR pokedex_nbr = 273 OR pokedex_nbr = 312 OR pokedex_nbr = 329 OR pokedex_nbr = 347
OR pokedex_nbr = 361 OR pokedex_nbr = 363 OR pokedex_nbr = 386 OR pokedex_nbr = 397
OR pokedex_nbr = 414 OR pokedex_nbr = 433 OR pokedex_nbr = 458 OR pokedex_nbr = 459
OR pokedex_nbr = 510 OR pokedex_nbr = 519 OR pokedex_nbr = 548 OR pokedex_nbr = 574
OR pokedex_nbr = 578 OR pokedex_nbr = 580 OR pokedex_nbr = 582 OR pokedex_nbr = 585
OR pokedex_nbr = 592 OR pokedex_nbr = 595 OR pokedex_nbr = 615 OR pokedex_nbr = 619
OR pokedex_nbr = 622 OR pokedex_nbr = 627 OR pokedex_nbr = 633 OR pokedex_nbr = 666
OR pokedex_nbr = 698 OR pokedex_nbr = 726 OR pokedex_nbr = 732 OR pokedex_nbr = 759
OR pokedex_nbr = 810 OR pokedex_nbr = 833 OR pokedex_nbr = 835 OR pokedex_nbr = 837
OR pokedex_nbr = 864 OR pokedex_nbr = 886 OR pokedex_nbr = 894 OR pokedex_nbr = 895 
OR pokedex_nbr = 961;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 51) WHERE
pokedex_nbr = 402 OR pokedex_nbr = 931;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 52) WHERE
pokedex_nbr = 29 OR pokedex_nbr = 391 OR pokedex_nbr = 430 OR pokedex_nbr = 657 
OR pokedex_nbr = 695 OR pokedex_nbr = 751;

UPDATe pokedex SET stats = json_set(stats, '$[2].value', 53) WHERE
pokedex_nbr = 106 OR pokedex_nbr = 316 OR pokedex_nbr = 393 OR pokedex_nbr = 686
OR pokedex_nbr = 705 OR pokedex_nbr = 799 OR pokedex_nbr = 806;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 54) WHERE
pokedex_nbr = 677 OR pokedex_nbr = 728 OR pokedex_nbr = 906;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 55) WHERE
pokedex_nbr = 11 OR pokedex_nbr = 17 OR pokedex_nbr = 26 OR pokedex_nbr = 43
OR pokedex_nbr = 46 OR pokedex_nbr = 77 OR pokedex_nbr = 83 OR pokedex_nbr = 86
OR pokedex_nbr = 120 OR pokedex_nbr = 129 OR pokedex_nbr = 180 OR pokedex_nbr = 190
OR pokedex_nbr = 192 OR pokedex_nbr = 215 OR pokedex_nbr = 266 OR pokedex_nbr = 268
OR pokedex_nbr = 307 OR pokedex_nbr = 343 OR pokedex_nbr = 370 OR pokedex_nbr = 419
OR pokedex_nbr = 495 OR pokedex_nbr = 499 OR pokedex_nbr = 528 OR pokedex_nbr = 532
OR pokedex_nbr = 536 OR pokedex_nbr = 555 OR pokedex_nbr = 605 OR pokedex_nbr = 607
OR pokedex_nbr = 636 OR pokedex_nbr = 662 OR pokedex_nbr = 722 OR pokedex_nbr = 755
OR pokedex_nbr = 817 OR pokedex_nbr = 819 OR pokedex_nbr = 822 OR pokedex_nbr = 831
OR pokedex_nbr = 845 OR pokedex_nbr = 876 OR pokedex_nbr = 958 OR pokedex_nbr = 987;

UPDATE pokedex SET stats = json_set(Stats, '$[2].value', 56) WHERE
pokedex_nbr = 456;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 57) WHERE
pokedex_nbr = 33 OR pokedex_nbr = 125 OR pokedex_nbr = 126 OR pokedex_nbr = 702
OR pokedex_nbr = 739;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 58) WHERE
pokedex_nbr = 5 OR pokedex_nbr = 156 OR pokedex_nbr = 171 OR pokedex_nbr = 202 
OR pokedex_nbr = 654 OR pokedex_nbr = 667 OR pokedex_nbr = 828 OR pokedex_nbr = 877;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 59) WHERE
pokedex_nbr = 543 OR pokedex_nbr = 909;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 60) WHERE
pokedex_nbr = 20 OR pokedex_nbr = 49 OR pokedex_nbr = 53 OR pokedex_nbr = 57 
OR pokedex_nbr = 94 OR pokedex_nbr = 118 OR pokedex_nbr = 134 OR pokedex_nbr = 135
OR pokedex_nbr = 136 OR pokedex_nbr = 196 OR pokedex_nbr = 200 OR pokedex_nbr = 231 
OR pokedex_nbr = 256 OR pokedex_nbr = 275 OR pokedex_nbr = 277 OR pokedex_nbr = 285
OR pokedex_nbr = 287 OR pokedex_nbr = 297 OR pokedex_nbr = 310 OR pokedex_nbr = 327
OR pokedex_nbr = 332 OR pokedex_nbr = 333 OR pokedex_nbr = 335 OR pokedex_nbr = 336
OR pokedex_nbr = 359 OR pokedex_nbr = 371 OR pokedex_nbr = 400 OR pokedex_nbr = 409
OR pokedex_nbr = 429 OR pokedex_nbr = 502 OR pokedex_nbr = 530 OR pokedex_nbr = 546
OR pokedex_nbr = 571 OR pokedex_nbr = 573 OR pokedex_nbr = 587 OR pokedex_nbr = 596
OR pokedex_nbr = 608 OR pokedex_nbr = 610 OR pokedex_nbr = 620 OR pokedex_nbr = 665
OR pokedex_nbr = 676 OR pokedex_nbr = 682 OR pokedex_nbr = 690 OR pokedex_nbr = 720
OR pokedex_nbr = 735 OR pokedex_nbr = 743 OR pokedex_nbr = 758 OR pokedex_nbr = 814
OR pokedex_nbr = 829 OR pokedex_nbr = 836 OR pokedex_nbr = 847 OR pokedex_nbr = 852
OR pokedex_nbr = 873 OR pokedex_nbr = 891 OR pokedex_nbr = 897 OR pokedex_nbr = 903 
OR pokedex_nbr = 929 OR pokedex_nbr = 941 OR pokedex_nbr = 942 OR pokedex_nbr = 953
OR pokedex_nbr = 956 OR pokedex_nbr = 971 OR pokedex_nbr = 978 OR pokedex_nbr = 980
OR pokedex_nbr = 994;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 61) WHERE
pokedex_nbr = 264;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 62) WHERE
pokedex_nbr = 234 OR pokedex_nbr = 284 OR pokedex_nbr = 520 OR pokedex_nbr = 568 
OR pokedex_nbr = 673 OR pokedex_nbr = 674 OR pokedex_nbr = 692 OR pokedex_nbr = 747;

UPDATe pokedex SET stats = json_set(stats, '$[2].value', 63) WHERE
pokedex_nbr = 2 OR pokedex_nbr = 295 OR pokedex_nbr = 512 OR pokedex_nbr = 514 
OR pokedex_nbr = 516 OR pokedex_nbr = 523 OR pokedex_nbr = 581 OR pokedex_nbr = 777 
OR pokedex_nbr = 907 OR pokedex_nbr = 965;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 64) WHERE
pokedex_nbr = 158 OR pokedex_nbr = 162 OR pokedex_nbr = 387 OR pokedex_nbr = 432;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 65) WHERE
pokedex_nbr = 7 OR pokedex_nbr = 22 OR pokedex_nbr = 61 OR pokedex_nbr = 71
OR pokedex_nbr = 73 OR pokedex_nbr = 79 OR pokedex_nbr = 119 OR pokedex_nbr = 122
OR pokedex_nbr = 142 OR pokedex_nbr = 143 OR pokedex_nbr = 148 OR pokedex_nbr = 152
OR pokedex_nbr = 175 OR pokedex_nbr = 203 OR pokedex_nbr = 254 OR pokedex_nbr = 282
OR pokedex_nbr = 301 OR pokedex_nbr = 326 OR pokedex_nbr = 337 OR pokedex_nbr = 341
OR pokedex_nbr = 354 OR pokedex_nbr = 407 OR pokedex_nbr = 444 OR pokedex_nbr = 454
OR pokedex_nbr = 461 OR pokedex_nbr = 475 OR pokedex_nbr = 500 OR pokedex_nbr = 507
OR pokedex_nbr = 550 OR pokedex_nbr = 567 OR pokedex_nbr = 583 OR pokedex_nbr = 637
OR pokedex_nbr = 650 OR pokedex_nbr = 700 OR pokedex_nbr = 745 OR pokedex_nbr = 775
OR pokedex_nbr = 782 OR pokedex_nbr = 808 OR pokedex_nbr = 818 OR pokedex_nbr = 851
OR pokedex_nbr = 855 OR pokedex_nbr = 857 OR pokedex_nbr = 861 OR pokedex_nbr = 902
OR pokedex_nbr = 913 OR pokedex_nbr = 945 OR pokedex_nbr = 949 OR pokedex_nbr = 952
OR pokedex_nbr = 967 OR pokedex_nbr = 975;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 66) WHERE
pokedex_nbr = 424 OR pokedex_nbr = 631 OR pokedex_nbr = 684 OR pokedex_nbr = 997 
OR pokedex_nbr = 1015;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 67) WHERE
pokedex_nbr = 30 OR pokedex_nbr =  435 OR pokedex_nbr = 466 OR pokedex_nbr = 467 
OR pokedex_nbr = 556 OR pokedex_nbr = 658 OR pokedex_nbr = 688 OR pokedex_nbr = 803;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 68) WHERE
pokedex_nbr = 394 OR pokedex_nbr = 423 OR pokedex_nbr = 671;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 69) WHERE
pokedex_nbr = 24 OR pokedex_nbr = 505 OR pokedex_nbr = 729 OR pokedex_nbr = 879;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 70) WHERE
pokedex_nbr = 20 OR pokedex_nbr = 42 OR pokedex_nbr = 44 OR pokedex_nbr = 67 
OR pokedex_nbr = 78 OR pokedex_nbr = 81 OR pokedex_nbr = 85 OR pokedex_nbr = 97 
OR pokedex_nbr = 101 OR pokedex_nbr = 116 OR pokedex_nbr = 137 OR pokedex_nbr = 168 
OR pokedex_nbr = 178 OR pokedex_nbr = 189 OR pokedex_nbr = 206 OR pokedex_nbr = 226 
OR pokedex_nbr = 247 OR pokedex_nbr = 257 OR pokedex_nbr = 259 OR pokedex_nbr = 262 
OR pokedex_nbr = 269 OR pokedex_nbr = 272 OR pokedex_nbr = 323 OR pokedex_nbr = 351 
OR pokedex_nbr = 352 OR pokedex_nbr = 364 OR pokedex_nbr = 398 OR pokedex_nbr = 417 
OR pokedex_nbr = 421 OR pokedex_nbr = 448 OR pokedex_nbr = 474 OR pokedex_nbr = 478 
OR pokedex_nbr = 482 OR pokedex_nbr = 540 OR pokedex_nbr = 559 OR pokedex_nbr = 575 
OR pokedex_nbr = 586 OR pokedex_nbr = 591 OR pokedex_nbr = 593 OR pokedex_nbr = 599 
OR pokedex_nbr = 603 OR pokedex_nbr = 611 OR pokedex_nbr = 624 OR pokedex_nbr = 634 
OR pokedex_nbr = 641 OR pokedex_nbr = 642 OR pokedex_nbr = 706 OR pokedex_nbr = 710 
OR pokedex_nbr = 741 OR pokedex_nbr = 749 OR pokedex_nbr = 779 OR pokedex_nbr = 811 
OR pokedex_nbr = 849 OR pokedex_nbr = 905 OR pokedex_nbr = 908 OR pokedex_nbr = 923 
OR pokedex_nbr = 925 OR pokedex_nbr = 926 OR pokedex_nbr = 947 OR pokedex_nbr = 981 
OR pokedex_nbr = 999;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 71) WHERE
pokedex_nbr = 392 OR pokedex_nbr = 663 OR pokedex_nbr = 796 OR pokedex_nbr = 1005;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 72) WHERE
pokedex_nbr = 455 OR pokedex_nbr = 640 OR pokedex_nbr = 655 OR pokedex_nbr = 668
OR pokedex_nbr = 683 OR pokedex_nbr = 699 OR pokedex_nbr = 899 OR pokedex_nbr = 964;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 73) WHERE
pokedex_nbr = 36 OR pokedex_nbr = 340 OR pokedex_nbr = 804 OR pokedex_nbr = 976;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 74) WHERE
pokedex_nbr = 730 OR pokedex_nbr = 973;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 75) WHERE
pokedex_nbr = 18 OR pokedex_nbr = 38 OR pokedex_nbr = 89 OR pokedex_nbr = 108
OR pokedex_nbr = 186 OR pokedex_nbr = 210 OR pokedex_nbr = 214 OR pokedex_nbr = 217
OR pokedex_nbr = 224 OR pokedex_nbr = 243 OR pokedex_nbr = 302 OR pokedex_nbr = 308
OR pokedex_nbr = 313 OR pokedex_nbr = 314 OR pokedex_nbr = 460 OR pokedex_nbr = 496
OR pokedex_nbr = 537 OR pokedex_nbr = 539 OR pokedex_nbr = 549 OR pokedex_nbr = 579
OR pokedex_nbr = 606 OR pokedex_nbr = 628 OR pokedex_nbr = 629 OR pokedex_nbr = 701
OR pokedex_nbr = 723 OR pokedex_nbr = 724 OR pokedex_nbr = 733 OR pokedex_nbr = 786
OR pokedex_nbr = 807 OR pokedex_nbr = 815 OR pokedex_nbr = 843 OR pokedex_nbr = 866
OR pokedex_nbr = 869 OR pokedex_nbr = 887 OR pokedex_nbr = 916 OR pokedex_nbr = 932;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 76) WHERE
pokedex_nbr = 457 OR pokedex_nbr = 678 OR pokedex_nbr = 709;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 77) WHERE
pokedex_nbr = 34 OR pokedex_nbr = 345 OR pokedex_nbr = 479 OR pokedex_nbr = 648 
OR pokedex_nbr = 660 OR pokedex_nbr = 696 OR pokedex_nbr = 740 OR pokedex_nbr = 959;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 78) WHERE
pokedex_nbr = 6 OR pokedex_nbr = 55 OR pokedex_nbr = 157 OR pokedex_nbr = 449
OR pokedex_nbr = 675 OR pokedex_nbr = 910 OR pokedex_nbr = 920;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 79) WHERE
pokedex_nbr = 107 OR pokedex_nbr = 130 OR pokedex_nbr = 350 OR pokedex_nbr = 405
OR pokedex_nbr = 988;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 80) WHERE
pokedex_nbr = 8 OR pokedex_nbr = 47 OR pokedex_nbr = 59 OR pokedex_nbr = 68
OR pokedex_nbr = 87 OR pokedex_nbr = 102 OR pokedex_nbr = 115 OR pokedex_nbr = 123
OR pokedex_nbr = 131 OR pokedex_nbr = 153 OR pokedex_nbr = 159 OR pokedex_nbr = 169
OR pokedex_nbr = 184 OR pokedex_nbr = 199 OR pokedex_nbr = 221 OR pokedex_nbr = 286
OR pokedex_nbr = 288 OR pokedex_nbr = 330 OR pokedex_nbr = 358 OR pokedex_nbr = 362
OR pokedex_nbr = 373 OR pokedex_nbr = 374 OR pokedex_nbr = 381 OR pokedex_nbr = 473
OR pokedex_nbr = 489 OR pokedex_nbr = 521 OR pokedex_nbr = 542 OR pokedex_nbr = 553
OR pokedex_nbr = 561 OR pokedex_nbr = 594 OR pokedex_nbr = 604 OR pokedex_nbr = 614
OR pokedex_nbr = 623 OR pokedex_nbr = 715 OR pokedex_nbr = 756 OR pokedex_nbr = 760
OR pokedex_nbr = 765 OR pokedex_nbr = 769 OR pokedex_nbr = 778 OR pokedex_nbr = 802
OR pokedex_nbr = 825 OR pokedex_nbr = 840 OR pokedex_nbr = 841 OR pokedex_nbr = 842
OR pokedex_nbr = 898 OR pokedex_nbr = 914 OR pokedex_nbr = 937 OR pokedex_nbr = 979
OR pokedex_nbr = 982 OR pokedex_nbr = 1002 OR pokedex_nbr = 1004 OR pokedex_nbr = 1022;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 82) WHERE
pokedex_nbr = 569 OR pokedex_nbr = 1016;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 83) WHERE
pokedex_nbr = 3 OR pokedex_nbr = 317 OR pokedex_nbr = 357;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 84) WHERE
pokedex_nbr = 428 OR pokedex_nbr = 618 OR pokedex_nbr = 1017;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 85) WHERE
pokedex_nbr = 27 OR pokedex_nbr = 45 OR pokedex_nbr = 103 OR pokedex_nbr = 121
OR pokedex_nbr = 145 OR pokedex_nbr = 176 OR pokedex_nbr = 181 OR pokedex_nbr = 195
OR pokedex_nbr = 211 OR pokedex_nbr = 244 OR pokedex_nbr = 303 OR pokedex_nbr = 338
OR pokedex_nbr = 342 OR pokedex_nbr = 366 OR pokedex_nbr = 388 OR pokedex_nbr = 413
OR pokedex_nbr = 503 OR pokedex_nbr = 518 OR pokedex_nbr = 524 OR pokedex_nbr = 533
OR pokedex_nbr = 538 OR pokedex_nbr = 547 OR pokedex_nbr = 557 OR pokedex_nbr = 562
OR pokedex_nbr = 584 OR pokedex_nbr = 616 OR pokedex_nbr = 712 OR pokedex_nbr = 780
OR pokedex_nbr = 785 OR pokedex_nbr = 954 OR pokedex_nbr = 962 OR pokedex_nbr = 1024;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 86) WHERE
pokedex_nbr = 436 OR pokedex_nbr = 469 OR pokedex_nbr = 531 OR pokedex_nbr = 685
OR pokedex_nbr = 993;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 87) WHERE
pokedex_nbr = 31;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 88) WHERE
pokedex_nbr = 395 OR pokedex_nbr = 687 OR pokedex_nbr = 693 OR pokedex_nbr = 1010;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 89) WHERE
pokedex_nbr = 545 OR pokedex_nbr = 792;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 90) WHERE
pokedex_nbr = 98 OR pokedex_nbr = 140 OR pokedex_nbr = 146 OR pokedex_nbr = 150
OR pokedex_nbr = 204 OR pokedex_nbr = 233 OR pokedex_nbr = 250 OR pokedex_nbr = 260
OR pokedex_nbr = 290 OR pokedex_nbr = 334 OR pokedex_nbr = 355 OR pokedex_nbr = 365
OR pokedex_nbr = 380 OR pokedex_nbr = 382 OR pokedex_nbr = 384 OR pokedex_nbr = 451
OR pokedex_nbr = 491 OR pokedex_nbr = 508 OR pokedex_nbr = 541 OR pokedex_nbr = 609
OR pokedex_nbr = 612 OR pokedex_nbr = 621 OR pokedex_nbr = 635 OR pokedex_nbr = 639
OR pokedex_nbr = 645 OR pokedex_nbr = 646 OR pokedex_nbr = 647 OR pokedex_nbr = 691
OR pokedex_nbr = 727 OR pokedex_nbr = 738 OR pokedex_nbr = 754 OR pokedex_nbr = 764
OR pokedex_nbr = 766 OR pokedex_nbr = 783 OR pokedex_nbr = 812 OR pokedex_nbr = 830
OR pokedex_nbr = 834 OR pokedex_nbr = 838 OR pokedex_nbr = 853 OR pokedex_nbr = 880
OR pokedex_nbr = 881 OR pokedex_nbr = 930 OR pokedex_nbr = 943 OR pokedex_nbr = 966
OR pokedex_nbr = 970 OR pokedex_nbr = 1006;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 91) WHERE
pokedex_nbr = 597 OR pokedex_nbr = 707 OR pokedex_nbr = 939 OR pokedex_nbr = 1009
OR pokedex_nbr = 1021;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 92) WHERE
pokedex_nbr = 752 OR pokedex_nbr = 918 OR pokedex_nbr = 998;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 95) WHERE
pokedex_nbr = 62 OR pokedex_nbr = 82 OR pokedex_nbr = 104 OR pokedex_nbr = 109
OR pokedex_nbr = 111 OR pokedex_nbr = 117 OR pokedex_nbr = 128 OR pokedex_nbr = 149
OR pokedex_nbr = 182 OR pokedex_nbr = 222 OR pokedex_nbr = 230 OR pokedex_nbr = 237
OR pokedex_nbr = 438 OR pokedex_nbr = 445 OR pokedex_nbr = 463 OR pokedex_nbr = 468
OR pokedex_nbr = 497 OR pokedex_nbr = 534 OR pokedex_nbr = 576 OR pokedex_nbr = 600
OR pokedex_nbr = 626 OR pokedex_nbr = 649 OR pokedex_nbr = 651 OR pokedex_nbr = 716
OR pokedex_nbr = 717 OR pokedex_nbr = 737 OR pokedex_nbr = 772 OR pokedex_nbr = 773
OR pokedex_nbr = 820 OR pokedex_nbr = 858 OR pokedex_nbr = 865 OR pokedex_nbr = 871
OR pokedex_nbr = 890 OR pokedex_nbr = 900 OR pokedex_nbr = 904 OR pokedex_nbr = 1000;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 97) WHERE
pokedex_nbr = 346 OR pokedex_nbr = 989;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 98) WHERE
pokedex_nbr = 763;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 99) WHERE
pokedex_nbr = 544 OR pokedex_nbr = 985 OR pokedex_nbr = 986;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 100) WHERE
pokedex_nbr = 9 OR pokedex_nbr = 74 OR pokedex_nbr = 90 OR pokedex_nbr = 127
OR pokedex_nbr = 138 OR pokedex_nbr = 144 OR pokedex_nbr = 151 OR pokedex_nbr = 154
OR pokedex_nbr = 160 OR pokedex_nbr = 212 OR pokedex_nbr = 251 OR pokedex_nbr = 279
OR pokedex_nbr = 289 OR pokedex_nbr = 304 OR pokedex_nbr = 348 OR pokedex_nbr = 372
OR pokedex_nbr = 375 OR pokedex_nbr = 378 OR pokedex_nbr = 385 OR pokedex_nbr = 484
OR pokedex_nbr = 490 OR pokedex_nbr = 492 OR pokedex_nbr = 494 OR pokedex_nbr = 625
OR pokedex_nbr = 643 OR pokedex_nbr = 679 OR pokedex_nbr = 750 OR pokedex_nbr = 774
OR pokedex_nbr = 781 OR pokedex_nbr = 832 OR pokedex_nbr = 863 OR pokedex_nbr = 870
OR pokedex_nbr = 882 OR pokedex_nbr = 883 OR pokedex_nbr = 892 OR pokedex_nbr = 911
OR pokedex_nbr = 933 OR pokedex_nbr = 936 OR pokedex_nbr = 972 OR pokedex_nbr = 1001
OR pokedex_nbr = 1008 OR pokedex_nbr = 1023;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 101) WHERE
pokedex_nbr = 800 OR pokedex_nbr = 862;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 102) WHERE
pokedex_nbr = 416;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 103) WHERE
pokedex_nbr = 564 OR pokedex_nbr = 797;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 105) WHERE
pokedex_nbr = 128 OR pokedex_nbr = 141 OR pokedex_nbr = 207 OR pokedex_nbr = 241
OR pokedex_nbr = 344 OR pokedex_nbr = 367 OR pokedex_nbr = 368 OR pokedex_nbr = 389
OR pokedex_nbr = 481 OR pokedex_nbr = 525 OR pokedex_nbr = 589 OR pokedex_nbr = 630 
OR pokedex_nbr = 823 OR pokedex_nbr = 893 OR pokedex_nbr = 901;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 106) WHERE
pokedex_nbr = 485 OR pokedex_nbr = 1013;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 107) WHERE
pokedex_nbr = 479 OR pokedex_nbr = 791;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 108) WHERE
pokedex_nbr = 442 OR pokedex_nbr = 992;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 110) WHERE
pokedex_nbr = 28 OR pokedex_nbr = 80 OR pokedex_nbr = 105 OR pokedex_nbr = 197
OR pokedex_nbr = 248 OR pokedex_nbr = 452 OR pokedex_nbr = 471 OR pokedex_nbr = 486
OR pokedex_nbr = 488 OR pokedex_nbr = 770 OR pokedex_nbr = 826 OR pokedex_nbr = 875 
OR pokedex_nbr = 995 OR pokedex_nbr = 1011 OR pokedex_nbr = 1019;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 112) WHERE
pokedex_nbr = 632;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 114) WHERE
pokedex_nbr = 991;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 115) WHERE
pokedex_nbr = 75 OR pokedex_nbr = 99 OR pokedex_nbr = 114 OR pokedex_nbr = 185
OR pokedex_nbr = 245 OR pokedex_nbr = 462 OR pokedex_nbr = 560 OR pokedex_nbr = 601
OR pokedex_nbr = 689 OR pokedex_nbr = 787 OR pokedex_nbr = 788 OR pokedex_nbr = 801
OR pokedex_nbr = 884 OR pokedex_nbr = 888 OR pokedex_nbr = 889 OR pokedex_nbr = 927
OR pokedex_nbr = 950 OR pokedex_nbr = 977 OR pokedex_nbr = 1007 OR pokedex_nbr = 1014;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 116) WHERE
pokedex_nbr = 437;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 118) WHERE
pokedex_nbr = 410 OR pokedex_nbr = 450;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 119) WHERE
pokedex_nbr = 697;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 120) WHERE
pokedex_nbr = 110 OR pokedex_nbr = 112 OR pokedex_nbr = 219 OR pokedex_nbr = 232
OR pokedex_nbr = 483 OR pokedex_nbr = 487 OR pokedex_nbr = 493 OR pokedex_nbr = 644
OR pokedex_nbr = 721 OR pokedex_nbr = 839 OR pokedex_nbr = 983 OR pokedex_nbr = 990;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 121) WHERE
pokedex_nbr = 718 OR pokedex_nbr = 1020;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 122) WHERE
pokedex_nbr = 652 OR pokedex_nbr = 711;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 125) WHERE
pokedex_nbr = 139 OR pokedex_nbr = 465 OR pokedex_nbr = 472 OR pokedex_nbr = 558
OR pokedex_nbr = 784 OR pokedex_nbr = 844 OR pokedex_nbr = 1003;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 129) WHERE
pokedex_nbr = 638;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 130) WHERE
pokedex_nbr = 76 OR pokedex_nbr = 249 OR pokedex_nbr = 356 OR pokedex_nbr = 369
OR pokedex_nbr = 376 OR pokedex_nbr = 464 OR pokedex_nbr = 470 OR pokedex_nbr = 480
OR pokedex_nbr = 526 OR pokedex_nbr = 771 OR pokedex_nbr = 896 OR pokedex_nbr = 934
OR pokedex_nbr = 1018;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 131) WHERE
pokedex_nbr = 598 OR pokedex_nbr = 790 OR pokedex_nbr = 798 OR pokedex_nbr = 984;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 133) WHERE
pokedex_nbr = 565;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 135) WHERE
pokedex_nbr = 299 OR pokedex_nbr = 477 OR pokedex_nbr = 776 OR pokedex_nbr = 874;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 139) WHERE 
pokedex_nbr = 794;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 140) WHERE
pokedex_nbr = 205 OR pokedex_nbr = 227 OR pokedex_nbr = 305 OR pokedex_nbr = 324
OR pokedex_nbr = 383 OR pokedex_nbr = 681 OR pokedex_nbr = 768;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 143) WHERE
pokedex_nbr = 809;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 145) WHERE
pokedex_nbr = 476 OR pokedex_nbr = 563 OR pokedex_nbr = 867 OR pokedex_nbr = 968;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 150) WHERE
pokedex_nbr = 379 OR pokedex_nbr = 680 OR pokedex_nbr = 703 OR pokedex_nbr = 719;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 152) WHERE
pokedex_nbr = 748;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 160) WHERE
pokedex_nbr = 95 OR pokedex_nbr = 1025;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 168) WHERE
pokedex_nbr = 411;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 180) WHERE
pokedex_nbr = 91 OR pokedex_nbr = 306;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 184) WHERE
pokedex_nbr = 713;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 200) WHERE
pokedex_nbr = 208 OR pokedex_nbr = 377;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 211) WHERE
pokedex_nbr = 805;

UPDATE pokedex SET stats = json_set(stats, '$[2].value', 230) WHERE
pokedex_nbr = 213;
COMMIT;