\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{QIBook}[2023/03/29 The QI Book Class revised on 2023/06/14]

%\LoadClassWithOptions{scrbook}

%=======================================================================================================
% Parameterization
% 0. book title, author
% 1. geometry
% 2. colors
% 3. fonts
% 4. theme (titlepage, headers, etc.)
%=======================================================================================================
\RequirePackage{pgfkeys}
\RequirePackage{pgffor}
\RequirePackage{pgfopts}

\pgfkeys{/qi/book/.is family}
\pgfkeys{/qi/book,
        geometry/.code={\RequirePackage[#1]{QIGeometry}},
        palette/.code={\RequirePackage[palette=#1]{QIColor}},
        language/.code={\RequirePackage[#1]{QIFont}},
        doctype/.code={\RequirePackage[doctype=#1]{QICommon}},
        color theme/.code={\RequirePackage[#1]{QIElements}},
        math font/.code={\useMathFont{#1}},
        light/.style={
                        geometry=a4paper,
                        palette=#1,
                        language=en,
                        doctype=book,
                        color theme=light,
                        math font=palatino},
        dark/.style={
                        geometry=a4paper,
                        palette=#1,
                        language=en,
                        doctype=book,
                        color theme=dark,
                        math font=palatino},
}
%=======================================================================================================
% Processing options for srcbook
%=======================================================================================================
% \DeclareOption{options}{\pgfkeys{/qi/book,#1}}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}} % Pass through any options to the base class
\ProcessOptions\relax
\LoadClass[usegeometry]{scrbook} % Load the base class

%-------------------------------------------------------------------------------------------------------
% Processing options for QI components
%-------------------------------------------------------------------------------------------------------
\ProcessPgfOptions{/qi/book}

\endinput