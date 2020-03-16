import unittest

# import your module, make sure you have a function segment_phrase that takes the string to be processed
import task1


class TestSegmentation(unittest.TestCase):

    def test_segment_phrases(self):
        data = "Understand customer needs and develop high-quality presentations, proposals and software demonstrations that speak to these needs - building a consensus for change on a multi-stakeholder basis"  # spacy has a problem to parse this properly
        result = task1.segment_phrase(data)
        result_expected = [
            'Understand customer needs',
            'develop high-quality presentations',
            'develop proposals',
            # 'develop software demonstrations',  # this is a problem with Spacy's dependency parser
            'develop software',  # problem in spacy
            'develop demonstrations',  # problem in spacy
            'building a consensus for change on a multi-stakeholder basis',
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")

        data = "Work with the Enterprise sales team to build, manage and maintain customer relationships"
        result = task1.segment_phrase(data)
        result_expected = [
            'Work with the Enterprise sales team to build customer relationships',
            'Work with the Enterprise sales team to manage customer relationships',
            'Work with the Enterprise sales team to maintain customer relationships',
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")

        data = "Need to understand and demonstrate the solution and how to integrate to other business systems"
        result = task1.segment_phrase(data)
        result_expected = [
            'Need to understand the solution',
            'Need to demonstrate the solution',
            'Need to understand how to integrate to other business systems',
            'Need to demonstrate how to integrate to other business systems',
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")

        data = "Understanding and experience within KPIs, identifying data sources, building a visualization map and dashboarding."  # this is rather bad english!
        result = task1.segment_phrase(data)
        result_expected = [
            'Understanding within KPIs identifying data sources, building a visualization map',
            'experience within KPIs identifying data sources, building a visualization map',
            'Understanding within KPIs identifying data sources, building dashboarding',
            'experience within KPIs identifying data sources, building dashboarding',
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")

        data = "Define, guide and implement innovation programs' governance, portfolio mix and business fit"
        result = task1.segment_phrase(data)
        result_expected = [
            "Define innovation programs' governance",
            "Define portfolio mix",
            "Define business fit",
            "guide innovation programs' governance",
            "guide portfolio mix",
            "guide business fit",
            "implement innovation programs' governance",
            "implement portfolio mix",
            "implement business fit",
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")

        data = "Establish the use of cloud services as a means to drive innovation"
        result = task1.segment_phrase(data)
        result_expected = [
            "Establish the use of cloud services as a means to drive innovation",
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")

        data = "Collaborate with other AWS specialist teams to drive and shape solutions to accelerate our customer's business outcomes"
        result = task1.segment_phrase(data)
        result_expected = [
            "Collaborate with other AWS specialist teams to drive solutions to accelerate our customer's business outcomes",
            "Collaborate with other AWS specialist teams to shape solutions to accelerate our customer's business outcomes",
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")

        data = "Experience with a major consulting firm or experience in a corporate role delivering strategy and operations projects with an emphasis in business transformation at the intersection of new operating models and new digital technologies."
        result = task1.segment_phrase(data)
        result_expected = [
            "Experience with a major consulting firm in a corporate role delivering strategy and operations projects with an emphasis in business transformation at the intersection of new operating models",
            "Experience with a major consulting firm in a corporate role delivering strategy and operations projects with an emphasis in business transformation at the intersection of new digital technologies",
            "Experience with a experience in a corporate role delivering strategy and operations projects with an emphasis in business transformation at the intersection of new operating models",
            "Experience with a experience in a corporate role delivering strategy and operations projects with an emphasis in business transformation at the intersection of new digital technologies",
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")

        data = "Understanding of modern cloud delivery models (Public, Private and Hybrid)."  # remove parenthesis
        result = task1.segment_phrase(data)
        result_expected = [
            "Understanding of modern cloud delivery models Public",
            "Understanding of modern cloud delivery models Private",
            "Understanding of modern cloud delivery models Hybrid",
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")

        data = "Excellent program management skills including developing project plans, resourcing and budgeting projects, and managing a disciplined execution methodology with both internal (direct) and external (indirect) team members."  # remove parenthesis
        result = task1.segment_phrase(data)
        result_expected = [
            "Excellent program management skills including developing project plans",
            "Excellent program management skills including resourcing and budgeting projects",
            "Excellent program management skills including managing a disciplined execution methodology with internal direct team members",
            # remove 'both' in the conjunction
            "Excellent program management skills including managing a disciplined execution methodology with external indirect team members",
            # remove 'both' in the conjunction
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")

        data = "Experience in two or more of the following transformation practice areas: ERP (business process architecture and solution implementation), business case and use case development, financial modelling, BI and Analytics strategy and implementation, complex program management, enterprise business / process / IT architectures, executive agenda items and metrics."  # very complex sentence; split at ':' but still process together; remove parenthesis
        result = task1.segment_phrase(data)
        result_expected = [
            "Experience in two or more of the following transformation practice areas",
            # split off before the ":" ; avoid splitting NUM-CONJ-ADJ - two or more
            "ERP business process architecture and solution implementation",
            "business case",
            "use case development",
            "financial modelling",
            "BI strategy",
            "Analytics strategy",
            "BI implementation",
            "Analytics implementation",
            "complex program management",
            "enterprise business / process",
            "IT architectures"
            "executive agenda items",
            "executive agenda metrics",
        ]
        self.assertCountEqual(result, result_expected, "Segmentation incorrect")


if __name__ == '__main__':
    unittest.main()
