class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique_emails = set() # Create a hash set

        for e in emails:
            # splitting local and domain name and save it
            local, domain = e.split('@')
            # extract what's before the + sign in the local name
            local = local.split('+')[0]
            # remove . in local name cuz it's basically the same
            local = local.replace('.','')
            # make it like an email address
            email_address = local + '@' + domain
            # add it to the hash set
            # if there's duplicate values, it won't be added to the hashset.
            unique_emails.add(email_address)
        # return the len of the hash set
        return len(unique_emails)
