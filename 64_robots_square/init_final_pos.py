
from numpy import *
import scipy
from scipy.io import loadmat

def init_final_pos():

    x_init_1 = 4.0
    y_init_1 = 0.0
    z_init_1 = 1.0


    x_fin_1 = -4.0
    y_fin_1 = 0.0
    z_fin_1 = 1.0

    x_init_2 = 4.0
    y_init_2 = 0.5
    z_init_2 = 1.0

    x_fin_2 = -4.0
    y_fin_2 = -0.5
    z_fin_2 = 1.0

    x_init_3 = 4.0
    y_init_3 = 1.0
    z_init_3 = 1.0

    x_fin_3 = -4.0
    y_fin_3 = -1.0
    z_fin_3 = 1.0

    x_init_4 = 4.0
    y_init_4 = 1.5
    z_init_4 = 1.0

    x_fin_4 = -4.0
    y_fin_4 = -1.5
    z_fin_4 = 1.0

    x_init_5 = 4.0
    y_init_5 = 2.0
    z_init_5 = 1.0

    x_fin_5 = -4.0
    y_fin_5 = -2.0
    z_fin_5 = 1.0

    x_init_6 = 4.0
    y_init_6 = 2.5
    z_init_6 = 1.0

    x_fin_6 = -4.0
    y_fin_6 = -2.5
    z_fin_6 = 1.0

    x_init_7 = 4.0
    y_init_7 = 3.0
    z_init_7 = 1.0

    x_fin_7 = -4.0
    y_fin_7 = -3.0
    z_fin_7 = 1.0

    x_init_8 = 4.0
    y_init_8 = 3.5
    z_init_8 = 1.0

    x_fin_8 = -4.0
    y_fin_8 = -3.5
    z_fin_8 = 1.0

    x_init_9 = 4.0
    y_init_9 = 4.0
    z_init_9 = 1.0

    x_fin_9 = -4.0
    y_fin_9 = -4.0
    z_fin_9 = 1.0

    x_init_10 = 3.5
    y_init_10 = 4.0
    z_init_10 = 1.0

    x_fin_10 = -3.5
    y_fin_10 = -4.0
    z_fin_10 = 1.0

    x_init_11 = 3.0
    y_init_11 = 4.0
    z_init_11 = 1.0

    x_fin_11 = -3.0
    y_fin_11 = -4.0
    z_fin_11 = 1.0

    x_init_12 = 2.5
    y_init_12 = 4.0
    z_init_12 = 1.0

    x_fin_12 = -2.5
    y_fin_12 = -4.0
    z_fin_12 = 1.0

    x_init_13 = 2.0
    y_init_13 = 4.0
    z_init_13 = 1.0

    x_fin_13 = -2.0
    y_fin_13 = -4.0
    z_fin_13 = 1.0

    x_init_14 = 1.5
    y_init_14 = 4.0
    z_init_14 = 1.0

    x_fin_14 = -1.5
    y_fin_14 = -4.0
    z_fin_14 = 1.0

    x_init_15 = 1.0
    y_init_15 = 4.0
    z_init_15 = 1.0

    x_fin_15 = -1.0
    y_fin_15 = -4.0
    z_fin_15 = 1.0

    x_init_16 = 0.5
    y_init_16 = 4.0
    z_init_16 = 1.0

    x_fin_16 = -0.5
    y_fin_16 = -4.0
    z_fin_16 = 1.0

    x_init_17 = 0.0
    y_init_17 = 4.0
    z_init_17 = 1.0

    x_fin_17 = 0.0
    y_fin_17 = -4.0
    z_fin_17 = 1.0

    x_init_18 = -0.5
    y_init_18 = 4.0
    z_init_18 = 1.0

    x_fin_18 = 0.5
    y_fin_18 = -4.0
    z_fin_18 = 1.0

    x_init_19 = -1.0
    y_init_19 = 4.0
    z_init_19 = 1.0

    x_fin_19 = 1.0
    y_fin_19 = -4.0
    z_fin_19 = 1.0

    x_init_20 = -1.5
    y_init_20 = 4.0
    z_init_20 = 1.0

    x_fin_20 = 1.5
    y_fin_20 = -4.0
    z_fin_20 = 1.0

    x_init_21 = -2.0
    y_init_21 = 4.0
    z_init_21 = 1.0

    x_fin_21 = 2.0
    y_fin_21 = -4.0
    z_fin_21 = 1.0

    x_init_22 = -2.5
    y_init_22 = 4.0
    z_init_22 = 1.0

    x_fin_22 = 2.5
    y_fin_22 = -4.0
    z_fin_22 = 1.0

    x_init_23 = -3.0
    y_init_23 = 4.0
    z_init_23 = 1.0

    x_fin_23 = 3.0
    y_fin_23 = -4.0
    z_fin_23 = 1.0

    x_init_24 = -3.5
    y_init_24 = 4.0
    z_init_24 = 1.0

    x_fin_24 = 3.5
    y_fin_24 = -4.0
    z_fin_24 = 1.0


    x_init_25 = -4.0
    y_init_25 = 4.0
    z_init_25 = 1.0

    x_fin_25 = 4.0
    y_fin_25 = -4.0
    z_fin_25 = 1.0

    x_init_26 = -4.0
    y_init_26 = 3.5
    z_init_26 = 1.0

    x_fin_26 = 4.0
    y_fin_26 = -3.5
    z_fin_26 = 1.0

    x_init_27 = -4.0
    y_init_27 = 3.0
    z_init_27 = 1.0

    x_fin_27 = 4.0
    y_fin_27 = -3.0
    z_fin_27 = 1.0

    x_init_28 = -4.0
    y_init_28 = 2.5
    z_init_28 = 1.0

    x_fin_28 = 4.0
    y_fin_28 = -2.5
    z_fin_28 = 1.0

    x_init_29 = -4.0
    y_init_29 = 2.0
    z_init_29 = 1.0

    x_fin_29 = 4.0
    y_fin_29 = -2.0
    z_fin_29 = 1.0

    x_init_30 = -4.0
    y_init_30 = 1.5
    z_init_30 = 1.0

    x_fin_30 = 4.0
    y_fin_30 = -1.5
    z_fin_30 = 1.0

    x_init_31 = -4.0
    y_init_31 = 1.0
    z_init_31 = 1.0

    x_fin_31 = 4.0
    y_fin_31 = -1.0
    z_fin_31 = 1.0

    x_init_32 = -4.0
    y_init_32 = 0.5
    z_init_32 = 1.0

    x_fin_32 = 4.0
    y_fin_32 = -0.5
    z_fin_32 = 1.0


    x_init_33 = -4.0
    y_init_33 = 0.0
    z_init_33 = 1.0

    x_fin_33 = 4.0
    y_fin_33 = 0.0
    z_fin_33 = 1.0

    x_init_34 = -4.0
    y_init_34 = -0.5
    z_init_34 = 1.0

    x_fin_34 = 4.0
    y_fin_34 = 0.5
    z_fin_34 = 1.0

    x_init_35 = -4.0
    y_init_35 = -1.0
    z_init_35 = 1.0

    x_fin_35 = 4.0
    y_fin_35 = 1.0
    z_fin_35 = 1.0

    x_init_36 = -4.0
    y_init_36 = -1.5
    z_init_36 = 1.0

    x_fin_36 = 4.0
    y_fin_36 = 1.5
    z_fin_36 = 1.0

    x_init_37 = -4.0
    y_init_37 = -2.0
    z_init_37 = 1.0

    x_fin_37 = 4.0
    y_fin_37 = 2.0
    z_fin_37 = 1.0

    x_init_38 = -4.0
    y_init_38 = -2.5
    z_init_38 = 1.0

    x_fin_38 = 4.0
    y_fin_38 = 2.5
    z_fin_38 = 1.0

    x_init_39 = -4.0
    y_init_39 = -3.0
    z_init_39 = 1.0

    x_fin_39 = 4.0
    y_fin_39 = 3.0
    z_fin_39 = 1.0

    x_init_40 = -4.0
    y_init_40 = -3.5
    z_init_40 = 1.0

    x_fin_40 = 4.0
    y_fin_40 = 3.5
    z_fin_40 = 1.0

    x_init_41 = -4.0
    y_init_41 = -4.0
    z_init_41 = 1.0

    x_fin_41 = 4.0
    y_fin_41 = 4.0
    z_fin_41 = 1.0

    x_init_42 = -3.5
    y_init_42 = -4.0
    z_init_42 = 1.0

    x_fin_42 = 3.5
    y_fin_42 = 4.0
    z_fin_42 = 1.0

    x_init_43 = -3.0
    y_init_43 = -4.0
    z_init_43 = 1.0

    x_fin_43 = 3.0
    y_fin_43 = 4.0
    z_fin_43 = 1.0

    x_init_44 = -2.5
    y_init_44 = -4.0
    z_init_44 = 1.0

    x_fin_44 = 2.5
    y_fin_44 = 4.0
    z_fin_44 = 1.0

    x_init_45 = -2.0
    y_init_45 = -4.0
    z_init_45 = 1.0

    x_fin_45 = 2.0
    y_fin_45 = 4.0
    z_fin_45 = 1.0

    x_init_46 = -1.5
    y_init_46 = -4.0
    z_init_46 = 1.0

    x_fin_46 = 1.5
    y_fin_46 = 4.0
    z_fin_46 = 1.0

    x_init_47 = -1.0
    y_init_47 = -4.0
    z_init_47 = 1.0

    x_fin_47 = 1.0
    y_fin_47 = 4.0
    z_fin_47 = 1.0

    x_init_48 = -0.5
    y_init_48 = -4.0
    z_init_48 = 1.0

    x_fin_48 = 0.5
    y_fin_48 = 4.0
    z_fin_48 = 1.0

    x_init_49 = 0.0
    y_init_49 = -4.0
    z_init_49 = 1.0

    x_fin_49 = 0.0
    y_fin_49 = 4.0
    z_fin_49 = 1.0

    x_init_50 = 0.5
    y_init_50 = -4.0
    z_init_50 = 1.0

    x_fin_50 = -0.5
    y_fin_50 = 4.0
    z_fin_50 = 1.0

    x_init_51 = 1.0
    y_init_51 = -4.0
    z_init_51 = 1.0

    x_fin_51 = -1.0
    y_fin_51 = 4.0
    z_fin_51 = 1.0

    x_init_52 = 1.5
    y_init_52 = -4.0
    z_init_52 = 1.0

    x_fin_52 = -1.5
    y_fin_52 = 4.0
    z_fin_52 = 1.0

    x_init_53 = 2.0
    y_init_53 = -4.0
    z_init_53 = 1.0

    x_fin_53 = -2.0
    y_fin_53 = 4.0
    z_fin_53 = 1.0

    x_init_54 = 2.5
    y_init_54 = -4.0
    z_init_54 = 1.0

    x_fin_54 = -2.5
    y_fin_54 = 4.0
    z_fin_54 = 1.0

    x_init_55 = 3.0
    y_init_55 = -4.0
    z_init_55 = 1.0

    x_fin_55 = -3.0
    y_fin_55 = 4.0
    z_fin_55 = 1.0

    x_init_56 = 3.5
    y_init_56 = -4.0
    z_init_56 = 1.0

    x_fin_56 = -3.5
    y_fin_56 = 4.0
    z_fin_56 = 1.0

    x_init_57 = 4.0
    y_init_57 = -4.0
    z_init_57 = 1.0

    x_fin_57 = -4.0
    y_fin_57 = 4.0
    z_fin_57 = 1.0

    x_init_58 = 4.0
    y_init_58 = -3.5
    z_init_58 = 1.0

    x_fin_58 = -4.0
    y_fin_58 = 3.5
    z_fin_58 = 1.0

    x_init_59 = 4.0
    y_init_59 = -3.0
    z_init_59 = 1.0

    x_fin_59 = -4.0
    y_fin_59 = 3.0
    z_fin_59 = 1.0

    x_init_60 = 4.0
    y_init_60 = -2.5
    z_init_60 = 1.0

    x_fin_60 = -4.0
    y_fin_60 = 2.5
    z_fin_60 = 1.0

    x_init_61 = 4.0
    y_init_61 = -2.0
    z_init_61 = 1.0

    x_fin_61 = -4.0
    y_fin_61 = 2.0
    z_fin_61 = 1.0

    x_init_62 = 4.0
    y_init_62 = -1.5
    z_init_62 = 1.0

    x_fin_62 = -4.0
    y_fin_62 = 1.5
    z_fin_62 = 1.0

    x_init_63 = 4.0
    y_init_63 = -1.0
    z_init_63 = 1.0

    x_fin_63 = -4.0
    y_fin_63 = 1.0
    z_fin_63 = 1.0

    x_init_64 = 4.0
    y_init_64 = -0.5
    z_init_64 = 1.0

    x_fin_64 = -4.0
    y_fin_64 = 0.5
    z_fin_64 = 1.0


    x_init = hstack(( x_init_1, x_init_2, x_init_3, x_init_4, x_init_5, x_init_6, x_init_7, x_init_8, x_init_9, x_init_10, x_init_11, x_init_12, x_init_13, x_init_14, x_init_15, x_init_16, x_init_17, x_init_18, x_init_19, x_init_20, x_init_21, x_init_22, x_init_23, x_init_24, x_init_25, x_init_26, x_init_27, x_init_28, x_init_29, x_init_30, x_init_31, x_init_32, x_init_33, x_init_34, x_init_35, x_init_36, x_init_37, x_init_38, x_init_39, x_init_40, x_init_41, x_init_42, x_init_43, x_init_44, x_init_45, x_init_46, x_init_47, x_init_48, x_init_49, x_init_50, x_init_51, x_init_52, x_init_53, x_init_54, x_init_55, x_init_56, x_init_57, x_init_58, x_init_59, x_init_60, x_init_61, x_init_62, x_init_63, x_init_64))
    y_init = hstack(( y_init_1, y_init_2, y_init_3, y_init_4, y_init_5, y_init_6, y_init_7, y_init_8, y_init_9, y_init_10, y_init_11, y_init_12, y_init_13, y_init_14, y_init_15, y_init_16, y_init_17, y_init_18, y_init_19, y_init_20, y_init_21, y_init_22, y_init_23, y_init_24, y_init_25, y_init_26, y_init_27, y_init_28, y_init_29, y_init_30, y_init_31, y_init_32, y_init_33, y_init_34, y_init_35, y_init_36, y_init_37, y_init_38, y_init_39, y_init_40, y_init_41, y_init_42, y_init_43, y_init_44, y_init_45, y_init_46, y_init_47, y_init_48, y_init_49, y_init_50, y_init_51, y_init_52, y_init_53, y_init_54, y_init_55, y_init_56, y_init_57, y_init_58, y_init_59, y_init_60, y_init_61, y_init_62, y_init_63, y_init_64))
    z_init = hstack(( z_init_1, z_init_2, z_init_3, z_init_4, z_init_5, z_init_6, z_init_7, z_init_8, z_init_9, z_init_10, z_init_11, z_init_12, z_init_13, z_init_14, z_init_15, z_init_16, z_init_17, z_init_18, z_init_19, z_init_20, z_init_21, z_init_22, z_init_23, z_init_24, z_init_25, z_init_26, z_init_27, z_init_28, z_init_29, z_init_30, z_init_31, z_init_32, z_init_33, z_init_34, z_init_35, z_init_36, z_init_37, z_init_38, z_init_39, z_init_40, z_init_41, z_init_42, z_init_43, z_init_44, z_init_45, z_init_46, z_init_47, z_init_48, z_init_49, z_init_50, z_init_51, z_init_52, z_init_53, z_init_54, z_init_55, z_init_56, z_init_57, z_init_58, z_init_59, z_init_60, z_init_61, z_init_62, z_init_63, z_init_64 ))

    x_fin = hstack(( x_fin_1, x_fin_2, x_fin_3, x_fin_4, x_fin_5, x_fin_6, x_fin_7, x_fin_8, x_fin_9, x_fin_10, x_fin_11, x_fin_12, x_fin_13, x_fin_14, x_fin_15, x_fin_16, x_fin_17, x_fin_18, x_fin_19, x_fin_20, x_fin_21, x_fin_22, x_fin_23, x_fin_24, x_fin_25, x_fin_26, x_fin_27, x_fin_28, x_fin_29, x_fin_30, x_fin_31, x_fin_32, x_fin_33, x_fin_34, x_fin_35, x_fin_36, x_fin_37, x_fin_38, x_fin_39, x_fin_40, x_fin_41, x_fin_42, x_fin_43, x_fin_44, x_fin_45, x_fin_46, x_fin_47, x_fin_48, x_fin_49, x_fin_50, x_fin_51, x_fin_52, x_fin_53, x_fin_54, x_fin_55, x_fin_56, x_fin_57, x_fin_58, x_fin_59, x_fin_60, x_fin_61, x_fin_62, x_fin_63, x_fin_64))
    y_fin = hstack(( y_fin_1, y_fin_2, y_fin_3, y_fin_4, y_fin_5, y_fin_6, y_fin_7, y_fin_8, y_fin_9, y_fin_10, y_fin_11, y_fin_12, y_fin_13, y_fin_14, y_fin_15, y_fin_16, y_fin_17, y_fin_18, y_fin_19, y_fin_20, y_fin_21, y_fin_22, y_fin_23, y_fin_24, y_fin_25, y_fin_26, y_fin_27, y_fin_28, y_fin_29, y_fin_30, y_fin_31, y_fin_32, y_fin_33, y_fin_34, y_fin_35, y_fin_36, y_fin_37, y_fin_38, y_fin_39, y_fin_40, y_fin_41, y_fin_42, y_fin_43, y_fin_44, y_fin_45, y_fin_46, y_fin_47, y_fin_48, y_fin_49, y_fin_50, y_fin_51, y_fin_52, y_fin_53, y_fin_54, y_fin_55, y_fin_56, y_fin_57, y_fin_58, y_fin_59, y_fin_60, y_fin_61, y_fin_62, y_fin_63, y_fin_64))
    z_fin = hstack(( z_fin_1, z_fin_2, z_fin_3, z_fin_4, z_fin_5, z_fin_6, z_fin_7, z_fin_8, z_fin_9, z_fin_10, z_fin_11, z_fin_12, z_fin_13, z_fin_14, z_fin_15, z_fin_16, z_fin_17, z_fin_18, z_fin_19, z_fin_20, z_fin_21, z_fin_22, z_fin_23, z_fin_24, z_fin_25, z_fin_26, z_fin_27, z_fin_28, z_fin_29, z_fin_30, z_fin_31, z_fin_32, z_fin_33, z_fin_34, z_fin_35, z_fin_36, z_fin_37, z_fin_38, z_fin_39, z_fin_40, z_fin_41, z_fin_42, z_fin_43, z_fin_44, z_fin_45, z_fin_46, z_fin_47, z_fin_48, z_fin_49, z_fin_50, z_fin_51, z_fin_52, z_fin_53, z_fin_54, z_fin_55, z_fin_56, z_fin_57, z_fin_58, z_fin_59, z_fin_60, z_fin_61, z_fin_62, z_fin_63, z_fin_64))

    return x_init, y_init, z_init, x_fin, y_fin, z_fin 

