import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PartAllocRuleClassSvc
# Description: PartAllocRuleClassSvc
# Version: v1



#########################################################################
# OData methods:
#########################################################################
async def getServiceDocument(epicorHeaders = None):
   """  
   Summary: Get service document
   Description: Get service document for the service
   OperationID: GetServiceDocument
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => application/json
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/",headers=creds) as resp:
           return await resp.json()

async def get_metadata(epicorHeaders = None):
   """  
   Summary: Get metadata document
   Description: Get service ODATA metadata in XML format
   OperationID: GetMetadata
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: Returns metadata document => content
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PartAllocRuleClasses(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartAllocRuleClasses items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAllocRuleClasses
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleClassRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses",headers=creds) as resp:
           return await resp.json()

async def post_PartAllocRuleClasses(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartAllocRuleClasses
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartAllocRuleClasses_Company_RuleClassID(Company, RuleClassID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartAllocRuleClass item
   Description: Calls GetByID to retrieve the PartAllocRuleClass item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAllocRuleClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RuleClassID: Desc: RuleClassID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses(" + Company + "," + RuleClassID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartAllocRuleClasses_Company_RuleClassID(Company, RuleClassID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartAllocRuleClass for the service
   Description: Calls UpdateExt to update PartAllocRuleClass. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartAllocRuleClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RuleClassID: Desc: RuleClassID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses(" + Company + "," + RuleClassID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartAllocRuleClasses_Company_RuleClassID(Company, RuleClassID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartAllocRuleClass item
   Description: Call UpdateExt to delete PartAllocRuleClass item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartAllocRuleClass
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RuleClassID: Desc: RuleClassID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses(" + Company + "," + RuleClassID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartAllocRuleClasses_Company_RuleClassID_PartAllocRuleClassDtls(Company, RuleClassID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PartAllocRuleClassDtls items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PartAllocRuleClassDtls1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RuleClassID: Desc: RuleClassID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleClassDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses(" + Company + "," + RuleClassID + ")/PartAllocRuleClassDtls",headers=creds) as resp:
           return await resp.json()

async def get_PartAllocRuleClasses_Company_RuleClassID_PartAllocRuleClassDtls_Company_RuleClassID_RuleID(Company, RuleClassID, RuleID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartAllocRuleClassDtl item
   Description: Calls GetByID to retrieve the PartAllocRuleClassDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAllocRuleClassDtl1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RuleClassID: Desc: RuleClassID   Required: True   Allow empty value : True
      :param RuleID: Desc: RuleID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClasses(" + Company + "," + RuleClassID + ")/PartAllocRuleClassDtls(" + Company + "," + RuleClassID + "," + RuleID + ")",headers=creds) as resp:
           return await resp.json()

async def get_PartAllocRuleClassDtls(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PartAllocRuleClassDtls items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PartAllocRuleClassDtls
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleClassDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClassDtls",headers=creds) as resp:
           return await resp.json()

async def post_PartAllocRuleClassDtls(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PartAllocRuleClassDtls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClassDtls", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PartAllocRuleClassDtls_Company_RuleClassID_RuleID(Company, RuleClassID, RuleID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PartAllocRuleClassDtl item
   Description: Calls GetByID to retrieve the PartAllocRuleClassDtl item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PartAllocRuleClassDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RuleClassID: Desc: RuleClassID   Required: True   Allow empty value : True
      :param RuleID: Desc: RuleID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClassDtls(" + Company + "," + RuleClassID + "," + RuleID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PartAllocRuleClassDtls_Company_RuleClassID_RuleID(Company, RuleClassID, RuleID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PartAllocRuleClassDtl for the service
   Description: Calls UpdateExt to update PartAllocRuleClassDtl. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PartAllocRuleClassDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RuleClassID: Desc: RuleClassID   Required: True   Allow empty value : True
      :param RuleID: Desc: RuleID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartAllocRuleClassDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClassDtls(" + Company + "," + RuleClassID + "," + RuleID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PartAllocRuleClassDtls_Company_RuleClassID_RuleID(Company, RuleClassID, RuleID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PartAllocRuleClassDtl item
   Description: Call UpdateExt to delete PartAllocRuleClassDtl item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PartAllocRuleClassDtl
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RuleClassID: Desc: RuleClassID   Required: True   Allow empty value : True
      :param RuleID: Desc: RuleID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      204 Desc: No Content. Operation is successful.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/PartAllocRuleClassDtls(" + Company + "," + RuleClassID + "," + RuleID + ")",headers=creds) as resp:
           return await resp.json()

async def get_List(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetList for the service
   Description: Get list of items<div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetList
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartAllocRuleClassListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePartAllocRuleClass, whereClausePartAllocRuleClassDtl, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRows_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartAllocRuleClass=" + whereClausePartAllocRuleClass
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartAllocRuleClassDtl=" + whereClausePartAllocRuleClassDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(ruleClassID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ruleClassID=" + ruleClassID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetList(whereClause, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetList
   Description: Returns a list of rows that satisfy the where clause.
   OperationID: Get_GetList
      :param whereClause: Desc: An expression used to filter the rows. Can be left blank for all rows.   Required: True   Allow empty value : True
      :param pageSize: Desc: The maximum number of rows to return. Leave as zero for no maximum.   Required: True
      :param absolutePage: Desc: Page of rows to return.   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClause=" + whereClause
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "pageSize=" + pageSize
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "absolutePage=" + absolutePage

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_CopyPartAllocRuleClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CopyPartAllocRuleClass
   Description: Copies the current rule class and all rules to a new rule class of the specified name.
   OperationID: CopyPartAllocRuleClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CopyPartAllocRuleClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CopyPartAllocRuleClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartAllocRuleClassActive(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartAllocRuleClassActive
   Description: Invoked when the PartAllocRuleClass Active flag is changed.  Returns a warning message string if there are potential issues with the rules
   OperationID: OnChangePartAllocRuleClassActive
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassActive_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassActive_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartAllocRuleClassDtlAction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartAllocRuleClassDtlAction
   Description: Invoked when PartAllocRuleClassDtl Action is changed.
   OperationID: OnChangePartAllocRuleClassDtlAction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassDtlAction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassDtlAction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartAllocRuleClassDtlAllocTemplateID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartAllocRuleClassDtlAllocTemplateID
   Description: Invoked when PartAllocRuleClassDtl AllocTemplateID is changed.
   OperationID: OnChangePartAllocRuleClassDtlAllocTemplateID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassDtlAllocTemplateID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassDtlAllocTemplateID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartAllocRuleClassDtlMasterRuleID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartAllocRuleClassDtlMasterRuleID
   Description: Invoked when MasterRuleID is changed.  Updates fields from PartAllocRuleMasterDtl
   OperationID: OnChangePartAllocRuleClassDtlMasterRuleID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassDtlMasterRuleID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassDtlMasterRuleID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartAllocRuleClassDtlMasterDtlSync(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartAllocRuleClassDtlMasterDtlSync
   Description: Invoked when MasterDtlSync is set true. Updates fields from PartAllocRuleMasterDtl
   OperationID: OnChangePartAllocRuleClassDtlMasterDtlSync
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassDtlMasterDtlSync_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassDtlMasterDtlSync_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangePartAllocRuleClassDtlQueryID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangePartAllocRuleClassDtlQueryID
   Description: Invoked when PartAllocRuleClassDtl QueryID is changed.  Query must have PartAllocQueueInfo as its first table.
   OperationID: OnChangePartAllocRuleClassDtlQueryID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangePartAllocRuleClassDtlQueryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangePartAllocRuleClassDtlQueryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_BuildTree(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method BuildTree
   Description: Returns a DataSet with information required to build the Data and Functions trees in Expression Editor
   OperationID: BuildTree
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/BuildTree_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/BuildTree_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckSyntax(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckSyntax
   Description: Invoked from Expression Editor. Checks the syntax of the formula. If a query is defined the joins are extracted from the BAQ.
   OperationID: CheckSyntax
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckSyntax_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckSyntax_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TestFulfillmentRuleClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TestFulfillmentRuleClass
   Description: Called from Automated Fulfillment Rule Entry to test the execution of a Rule Class.
1) After each rule is executed, a snapshot of PartAllocQueueInfo is taken stamped with the RuleClassID and RuleID
2) Log entries that would be written to the Automated Fulfillment Process log during the execution of the Rule are written to a file called AutomatedFulfillmentRuleTester.log.
   OperationID: TestFulfillmentRuleClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TestFulfillmentRuleClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TestFulfillmentRuleClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetFulfillmentRuleTesterTableset(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetFulfillmentRuleTesterTableset
   Description: Called from Automated Fulfillment Rule Entry to display a snapshot of PartAllocQueueInfo taken after the execution of the Rule
   OperationID: GetFulfillmentRuleTesterTableset
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetFulfillmentRuleTesterTableset_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetFulfillmentRuleTesterTableset_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartAllocRuleClass(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartAllocRuleClass
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartAllocRuleClass
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartAllocRuleClass_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartAllocRuleClass_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartAllocRuleClassDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartAllocRuleClassDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartAllocRuleClassDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartAllocRuleClassDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartAllocRuleClassDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteByID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteByID
   Description: Deletes a row given its ID.
   OperationID: DeleteByID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteByID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteByID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowID(id, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowID
   OperationID: Get_GetBySysRowID
   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "id=" + id

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetBySysRowIDs(ids, epicorHeaders = None):
   """  
   Summary: Invoke method GetBySysRowIDs
   OperationID: Get_GetBySysRowIDs
   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetBySysRowIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  

   firstParam = True
   params = ""
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "ids=" + ids

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_Update(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method Update
   Description: Commits the DataSet changes to the data store.
   OperationID: Update
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Update_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/Update_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateExt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateExt
   Description: Apply input data to service by calling GetByID/GetNew/Update methods.
   OperationID: UpdateExt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateExt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateExt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PartAllocRuleClassSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartAllocRuleClassDtlRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartAllocRuleClassListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartAllocRuleClassRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartAllocRuleClassRow] = obj["value"]
      pass

class Erp_Tablesets_PartAllocRuleClassDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.RuleClassID:str = obj["RuleClassID"]
      """  Rule Class ID  """  
      self.RuleID:str = obj["RuleID"]
      """  Unique ID of Rule  """  
      self.Description:str = obj["Description"]
      """  Description of the rule  """  
      self.Sequence:int = obj["Sequence"]
      """  The sequence that the rules are processed in  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo  """  
      self.Action:str = obj["Action"]
      """  The action that is executed for this rule  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rule is Active  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Indicates the PartAllocTemplate to use when allocating  """  
      self.Formula:str = obj["Formula"]
      """  The formula defined for this rule  """  
      self.MasterDtlSync:bool = obj["MasterDtlSync"]
      """  Indicates if changes made to Reusable Rule are synchronized to this class rule  """  
      self.MasterRuleID:str = obj["MasterRuleID"]
      """  Reusable master rule linked to this class rule.  """  
      self.RuleCalcFulfillOnSearch:bool = obj["RuleCalcFulfillOnSearch"]
      """  Used to determine whether or not we (re)calculate fulfillment values following the return of the results of a search.  """  
      self.RuleUseDemandWhseOnly:bool = obj["RuleUseDemandWhseOnly"]
      """  When TRUE the fulfillment calculations and actions will consider the Demand Warehouse only.  When false, all warehouses will be considered in fulfillment calculations, and the user will be able to choose on Reserve actions whether to consider only the Primary Warehouse or all warehouses.  """  
      self.RuleLimitedRefresh:bool = obj["RuleLimitedRefresh"]
      """  Following the execution of an action (Reserve, Allocate, Release for Picking, Unreserve, Unallocate), when true we will only refresh the rows that were actioned on, when false we will refresh all records.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  DevCharacter01  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  DevDecimal01  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  DevBoolean01  """  
      self.DevDate01:str = obj["DevDate01"]
      """  DevDate01  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllocDemandType:str = obj["AllocDemandType"]
      """  The type of allocation based on the Action.  Valid Values:  Order, Job, Transfer, or blank.  """  
      self.EnableAllocTemplateID:bool = obj["EnableAllocTemplateID"]
      """  Indicates if the AllocationTemplate field should be enabled  """  
      self.EnableFormula:bool = obj["EnableFormula"]
      """  Indicates if the user is able to enter a formula  """  
      self.EnableQueryID:bool = obj["EnableQueryID"]
      """  Indicates if the QueryID field should be enabled  """  
      self.ActiveSysTaskExists:bool = obj["ActiveSysTaskExists"]
      """  Indicates if an Active SysTask exists for this rule class.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartAllocRuleMasterDtlFormula:str = obj["PartAllocRuleMasterDtlFormula"]
      self.PartAllocRuleMasterDtlAction:str = obj["PartAllocRuleMasterDtlAction"]
      self.PartAllocRuleMasterDtlAllocTemplateID:str = obj["PartAllocRuleMasterDtlAllocTemplateID"]
      self.PartAllocRuleMasterDtlQueryID:str = obj["PartAllocRuleMasterDtlQueryID"]
      self.PartAllocRuleMasterDtlDescription:str = obj["PartAllocRuleMasterDtlDescription"]
      self.PartAllocTemplateAllocTemplateDesc:str = obj["PartAllocTemplateAllocTemplateDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocRuleClassListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.RuleClassID:str = obj["RuleClassID"]
      """  Rule Class ID  """  
      self.Description:str = obj["Description"]
      """  Description of the rule class  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rule Class is Active  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocRuleClassRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.RuleClassID:str = obj["RuleClassID"]
      """  Rule Class ID  """  
      self.Description:str = obj["Description"]
      """  Description of the rule class  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rule Class is Active  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class BuildTree_input:
   """ Required : 
   action
   queryID
   """  
   def __init__(self, obj):
      self.action:str = obj["action"]
      self.queryID:str = obj["queryID"]
      pass

class BuildTree_output:
   def __init__(self, obj):
      self.returnObj      #schema had no properties on an object.
      pass

class CheckSyntax_input:
   """ Required : 
   action
   queryID
   formula
   ruleClassID
   """  
   def __init__(self, obj):
      self.action:str = obj["action"]
      self.queryID:str = obj["queryID"]
      self.formula:str = obj["formula"]
      self.ruleClassID:str = obj["ruleClassID"]
      pass

class CheckSyntax_output:
   def __init__(self, obj):
      pass

class CopyPartAllocRuleClass_input:
   """ Required : 
   ruleClassID
   newRuleClassID
   newRuleClassDescription
   """  
   def __init__(self, obj):
      self.ruleClassID:str = obj["ruleClassID"]
      self.newRuleClassID:str = obj["newRuleClassID"]
      self.newRuleClassDescription:str = obj["newRuleClassDescription"]
      pass

class CopyPartAllocRuleClass_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["returnObj"]
      pass

class DeleteByID_input:
   """ Required : 
   ruleClassID
   """  
   def __init__(self, obj):
      self.ruleClassID:str = obj["ruleClassID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_FulfillmentRuleTesterTableset:
   def __init__(self, obj):
      self.PartAllocQueueInfo:list[Erp_Tablesets_PartAllocQueueInfoRow] = obj["PartAllocQueueInfo"]
      self.PartAllocQueueInfoLog:list[Erp_Tablesets_PartAllocQueueInfoLogRow] = obj["PartAllocQueueInfoLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartAllocQueueInfoLogRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.UserPlant:str = obj["UserPlant"]
      """  UserPlant  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  SysTaskNum  """  
      self.TestMode:bool = obj["TestMode"]
      """  TestMode  """  
      self.RuleClassID:str = obj["RuleClassID"]
      """  RuleClassID  """  
      self.RuleID:str = obj["RuleID"]
      """  RuleID  """  
      self.Sequence:int = obj["Sequence"]
      """  Sequence  """  
      self.LogText:str = obj["LogText"]
      """  LogText  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  CreatedOn  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocQueueInfoRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.UserID:str = obj["UserID"]
      """  UserID  """  
      self.UserPlant:str = obj["UserPlant"]
      """  UserPlant  """  
      self.SysTaskNum:int = obj["SysTaskNum"]
      """  SysTaskNum  """  
      self.TestMode:bool = obj["TestMode"]
      """  TestMode  """  
      self.RelatedToSchemaName:str = obj["RelatedToSchemaName"]
      """  RelatedToSchemaName  """  
      self.RelatedToTableName:str = obj["RelatedToTableName"]
      """  RelatedToTableName  """  
      self.RelatedToSysRowID:str = obj["RelatedToSysRowID"]
      """  RelatedToSysRowID  """  
      self.RuleClassID:str = obj["RuleClassID"]
      """  RuleClassID  """  
      self.RuleID:str = obj["RuleID"]
      """  RuleID  """  
      self.Action:str = obj["Action"]
      """  The action that is to be executed on this demand.  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.OrderLine:int = obj["OrderLine"]
      """  OrderLine  """  
      self.LineType:str = obj["LineType"]
      """  LineType  """  
      self.ReqDate:str = obj["ReqDate"]
      """  ReqDate  """  
      self.OurReqQty:int = obj["OurReqQty"]
      """  OurReqQty  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipViaCode  """  
      self.OpenRelease:bool = obj["OpenRelease"]
      """  OpenRelease  """  
      self.FirmRelease:bool = obj["FirmRelease"]
      """  FirmRelease  """  
      self.Make:bool = obj["Make"]
      """  Make  """  
      self.OurJobQty:int = obj["OurJobQty"]
      """  OurJobQty  """  
      self.OurJobShippedQty:int = obj["OurJobShippedQty"]
      """  OurJobShippedQty  """  
      self.VoidRelease:bool = obj["VoidRelease"]
      """  VoidRelease  """  
      self.OurStockQty:int = obj["OurStockQty"]
      """  OurStockQty  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode  """  
      self.OurStockShippedQty:int = obj["OurStockShippedQty"]
      """  OurStockShippedQty  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.TaxExempt:str = obj["TaxExempt"]
      """  TaxExempt  """  
      self.ShpConNum:int = obj["ShpConNum"]
      """  ShpConNum  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.SelectForPicking:bool = obj["SelectForPicking"]
      """  SelectForPicking  """  
      self.PickError:str = obj["PickError"]
      """  PickError  """  
      self.BuyToOrder:bool = obj["BuyToOrder"]
      """  BuyToOrder  """  
      self.PONum:int = obj["PONum"]
      """  PONum  """  
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.SalesUM:str = obj["SalesUM"]
      """  SalesUM  """  
      self.AttributeSetID:int = obj["AttributeSetID"]
      """  AttributeSetID  """  
      self.DispOrderShippedQty:int = obj["DispOrderShippedQty"]
      """  DispOrderShippedQty  """  
      self.DispOrderRemainingQty:int = obj["DispOrderRemainingQty"]
      """  DispOrderRemainingQty  """  
      self.DispOurStockShippedQty:int = obj["DispOurStockShippedQty"]
      """  DispOurStockShippedQty  """  
      self.DispOurJobShippedQty:int = obj["DispOurJobShippedQty"]
      """  DispOurJobShippedQty  """  
      self.DispOrderReserved:int = obj["DispOrderReserved"]
      """  DispOrderReserved  """  
      self.DispOrderMfgReserved:int = obj["DispOrderMfgReserved"]
      """  DispOrderMfgReserved  """  
      self.DispOrderStockReserved:int = obj["DispOrderStockReserved"]
      """  DispOrderStockReserved  """  
      self.CustID:str = obj["CustID"]
      """  CustID  """  
      self.CustName:str = obj["CustName"]
      """  CustName  """  
      self.ShipToCity:str = obj["ShipToCity"]
      """  ShipToCity  """  
      self.ShipToState:str = obj["ShipToState"]
      """  ShipToState  """  
      self.ShipToZip:str = obj["ShipToZip"]
      """  ShipToZip  """  
      self.ShipToCountryNum:int = obj["ShipToCountryNum"]
      """  ShipToCountryNum  """  
      self.StagingWhseDescription:str = obj["StagingWhseDescription"]
      """  StagingWhseDescription  """  
      self.ErrorStatusDisplay:str = obj["ErrorStatusDisplay"]
      """  ErrorStatusDisplay  """  
      self.StageWhseCode:str = obj["StageWhseCode"]
      """  StageWhseCode  """  
      self.StageBin:str = obj["StageBin"]
      """  StageBin  """  
      self.EnableSelectForPicking:bool = obj["EnableSelectForPicking"]
      """  EnableSelectForPicking  """  
      self.OrderNumLineRel:str = obj["OrderNumLineRel"]
      """  OrderNumLineRel  """  
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      """  ShipViaCodeDescription  """  
      self.WarehouseCodeDescription:str = obj["WarehouseCodeDescription"]
      """  WarehouseCodeDescription  """  
      self.ShipToName:str = obj["ShipToName"]
      """  ShipToName  """  
      self.ShipToAddress1:str = obj["ShipToAddress1"]
      """  ShipToAddress1  """  
      self.ShipToAddress2:str = obj["ShipToAddress2"]
      """  ShipToAddress2  """  
      self.ShipToAddress3:str = obj["ShipToAddress3"]
      """  ShipToAddress3  """  
      self.SupplyPartNum:str = obj["SupplyPartNum"]
      """  SupplyPartNum  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  ReservePriorityCode  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  DoNotShipBeforeDate  """  
      self.CustGroupCode:str = obj["CustGroupCode"]
      """  CustGroupCode  """  
      self.KitParentPartNum:str = obj["KitParentPartNum"]
      """  KitParentPartNum  """  
      self.KitParentLine:int = obj["KitParentLine"]
      """  KitParentLine  """  
      self.SelectedForAction:bool = obj["SelectedForAction"]
      """  SelectedForAction  """  
      self.ReservedQty:int = obj["ReservedQty"]
      """  ReservedQty  """  
      self.PickingQty:int = obj["PickingQty"]
      """  PickingQty  """  
      self.PickedQty:int = obj["PickedQty"]
      """  PickedQty  """  
      self.RemainingToReserve:int = obj["RemainingToReserve"]
      """  RemainingToReserve  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  UnitPrice  """  
      self.ExtPrice:int = obj["ExtPrice"]
      """  ExtPrice  """  
      self.UnreservedInventory:int = obj["UnreservedInventory"]
      """  UnreservedInventory  """  
      self.AvailablePercent:int = obj["AvailablePercent"]
      """  AvailablePercent  """  
      self.OrderedLessShipped:int = obj["OrderedLessShipped"]
      """  OrderedLessShipped  """  
      self.PartWhseOnHandQty:int = obj["PartWhseOnHandQty"]
      """  PartWhseOnHandQty  """  
      self.KitFulfillmentValuePct:int = obj["KitFulfillmentValuePct"]
      """  KitFulfillmentValuePct  """  
      self.KitFulfilledValuePct:int = obj["KitFulfilledValuePct"]
      """  KitFulfilledValuePct  """  
      self.PotentialReserveQty:int = obj["PotentialReserveQty"]
      """  PotentialReserveQty  """  
      self.FulfilledQtyPct:int = obj["FulfilledQtyPct"]
      """  FulfilledQtyPct  """  
      self.FulfillmentQtyPct:int = obj["FulfillmentQtyPct"]
      """  FulfillmentQtyPct  """  
      self.PartVolume:int = obj["PartVolume"]
      """  PartVolume  """  
      self.PartWeight:int = obj["PartWeight"]
      """  PartWeight  """  
      self.KitFlag:str = obj["KitFlag"]
      """  KitFlag  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  DoNotShipAfterDate  """  
      self.NeedsUpdate:bool = obj["NeedsUpdate"]
      """  NeedsUpdate  """  
      self.KitShipComplete:bool = obj["KitShipComplete"]
      """  KitShipComplete  """  
      self.KitQtyPer:int = obj["KitQtyPer"]
      """  KitQtyPer  """  
      self.AllocatedQty:int = obj["AllocatedQty"]
      """  AllocatedQty  """  
      self.ReservedQtyPct:int = obj["ReservedQtyPct"]
      """  ReservedQtyPct  """  
      self.AllocatedQtyPct:int = obj["AllocatedQtyPct"]
      """  AllocatedQtyPct  """  
      self.FulfilledQty:int = obj["FulfilledQty"]
      """  FulfilledQty  """  
      self.WaveNum:int = obj["WaveNum"]
      """  WaveNum  """  
      self.WaveDestBinNum:str = obj["WaveDestBinNum"]
      """  WaveDestBinNum  """  
      self.WavePickTicketPrinted:bool = obj["WavePickTicketPrinted"]
      """  WavePickTicketPrinted  """  
      self.PartTrackLots:bool = obj["PartTrackLots"]
      """  PartTrackLots  """  
      self.PartTrackSerialNum:bool = obj["PartTrackSerialNum"]
      """  PartTrackSerialNum  """  
      self.PartTrackMultipleUOM:bool = obj["PartTrackMultipleUOM"]
      """  PartTrackMultipleUOM  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  BTCustNum  """  
      self.BTCustID:str = obj["BTCustID"]
      """  BTCustID  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  ShipOrderComplete  """  
      self.CreditHold:bool = obj["CreditHold"]
      """  CreditHold  """  
      self.BTCustName:str = obj["BTCustName"]
      """  BTCustName  """  
      self.AllocatedUM:str = obj["AllocatedUM"]
      """  AllocatedUM  """  
      self.ReservedUM:str = obj["ReservedUM"]
      """  ReservedUM  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  AssemblySeq  """  
      self.MtlSeq:int = obj["MtlSeq"]
      """  MtlSeq  """  
      self.TFOrdNum:str = obj["TFOrdNum"]
      """  TFOrdNum  """  
      self.TFOrdLine:int = obj["TFOrdLine"]
      """  TFOrdLine  """  
      self.TFOrdNumTFOrdLine:str = obj["TFOrdNumTFOrdLine"]
      """  TFOrdNumTFOrdLine  """  
      self.DemandType:str = obj["DemandType"]
      """  DemandType  """  
      self.DemandKey1:str = obj["DemandKey1"]
      """  DemandKey1  """  
      self.DemandKey2:str = obj["DemandKey2"]
      """  DemandKey2  """  
      self.DemandKey3:str = obj["DemandKey3"]
      """  DemandKey3  """  
      self.JobAssemblyMtl:str = obj["JobAssemblyMtl"]
      """  JobAssemblyMtl  """  
      self.DemandTypeDesc:str = obj["DemandTypeDesc"]
      """  DemandTypeDesc  """  
      self.FulfillmentSeq:int = obj["FulfillmentSeq"]
      """  FulfillmentSeq  """  
      self.CrossDockedQty:int = obj["CrossDockedQty"]
      """  CrossDockedQty  """  
      self.OrderFulfillmentPct:int = obj["OrderFulfillmentPct"]
      """  OrderFulfillmentPct  """  
      self.ReservePriorityOverride:int = obj["ReservePriorityOverride"]
      """  ReservePriorityOverride  """  
      self.CustCategory:str = obj["CustCategory"]
      """  CustCategory  """  
      self.CustTerritoryID:str = obj["CustTerritoryID"]
      """  CustTerritoryID  """  
      self.PartWeightUOM:str = obj["PartWeightUOM"]
      """  PartWeightUOM  """  
      self.NormalizedPartWeight:int = obj["NormalizedPartWeight"]
      """  NormalizedPartWeight  """  
      self.NormalizedPartWeightUOM:str = obj["NormalizedPartWeightUOM"]
      """  NormalizedPartWeightUOM  """  
      self.NormalizedPartVolume:int = obj["NormalizedPartVolume"]
      """  NormalizedPartVolume  """  
      self.NormalizedPartVolumeUOM:str = obj["NormalizedPartVolumeUOM"]
      """  NormalizedPartVolumeUOM  """  
      self.PartVolumeUOM:str = obj["PartVolumeUOM"]
      """  PartVolumeUOM  """  
      self.UnitPriceCurrencyCode:str = obj["UnitPriceCurrencyCode"]
      """  UnitPriceCurrencyCode  """  
      self.TotalValue:int = obj["TotalValue"]
      """  TotalValue  """  
      self.TotalVolume:int = obj["TotalVolume"]
      """  TotalVolume  """  
      self.TotalWeight:int = obj["TotalWeight"]
      """  TotalWeight  """  
      self.FulfillmentValue:int = obj["FulfillmentValue"]
      """  FulfillmentValue  """  
      self.FulfillmentValuePct:int = obj["FulfillmentValuePct"]
      """  FulfillmentValuePct  """  
      self.FulfilledValue:int = obj["FulfilledValue"]
      """  FulfilledValue  """  
      self.FulfilledValuePct:int = obj["FulfilledValuePct"]
      """  FulfilledValuePct  """  
      self.OrderProjectID:str = obj["OrderProjectID"]
      """  OrderProjectID  """  
      self.UDShortChar01:str = obj["UDShortChar01"]
      """  UDShortChar01  """  
      self.UDShortChar02:str = obj["UDShortChar02"]
      """  UDShortChar02  """  
      self.UDNumber01:int = obj["UDNumber01"]
      """  UDNumber01  """  
      self.UDNumber02:int = obj["UDNumber02"]
      """  UDNumber02  """  
      self.UDCheckbox01:bool = obj["UDCheckbox01"]
      """  UDCheckbox01  """  
      self.UDCheckbox02:bool = obj["UDCheckbox02"]
      """  UDCheckbox02  """  
      self.UDDate01:str = obj["UDDate01"]
      """  UDDate01  """  
      self.UDDate02:str = obj["UDDate02"]
      """  UDDate02  """  
      self.OrderCounterSale:bool = obj["OrderCounterSale"]
      """  OrderCounterSale  """  
      self.DistributionType:str = obj["DistributionType"]
      """  DistributionType  """  
      self.WaveDesc:str = obj["WaveDesc"]
      """  WaveDesc  """  
      self.TFOrdToPlant:str = obj["TFOrdToPlant"]
      """  TFOrdToPlant  """  
      self.TFOrdToPlantName:str = obj["TFOrdToPlantName"]
      """  TFOrdToPlantName  """  
      self.TFOrdToPlantCity:str = obj["TFOrdToPlantCity"]
      """  TFOrdToPlantCity  """  
      self.TFOrdToPlantState:str = obj["TFOrdToPlantState"]
      """  TFOrdToPlantState  """  
      self.TFOrdToPlantZip:str = obj["TFOrdToPlantZip"]
      """  TFOrdToPlantZip  """  
      self.TFOrdToPlantCountry:str = obj["TFOrdToPlantCountry"]
      """  TFOrdToPlantCountry  """  
      self.TFOrdFromPlant:str = obj["TFOrdFromPlant"]
      """  TFOrdFromPlant  """  
      self.TFOrdFromWarehouseCode:str = obj["TFOrdFromWarehouseCode"]
      """  TFOrdFromWarehouseCode  """  
      self.PartProdCode:str = obj["PartProdCode"]
      """  PartProdCode  """  
      self.LineCount:int = obj["LineCount"]
      """  LineCount  """  
      self.OrderStatus:str = obj["OrderStatus"]
      """  OrderStatus  """  
      self.JobStatus:str = obj["JobStatus"]
      """  JobStatus  """  
      self.TFOrdStatus:str = obj["TFOrdStatus"]
      """  TFOrdStatus  """  
      self.CustRegionCode:str = obj["CustRegionCode"]
      """  CustRegionCode  """  
      self.JobStartDate:str = obj["JobStartDate"]
      """  JobStartDate  """  
      self.JobSchedCode:str = obj["JobSchedCode"]
      """  JobSchedCode  """  
      self.JobPartNum:str = obj["JobPartNum"]
      """  JobPartNum  """  
      self.ReleaseCount:int = obj["ReleaseCount"]
      """  ReleaseCount  """  
      self.ReleaseForPickingSeq:int = obj["ReleaseForPickingSeq"]
      """  ReleaseForPickingSeq  """  
      self.OrderHeld:bool = obj["OrderHeld"]
      """  OrderHeld  """  
      self.BackFlush:bool = obj["BackFlush"]
      """  BackFlush  """  
      self.DisplaySeq:int = obj["DisplaySeq"]
      """  DisplaySeq  """  
      self.MtlQueueSeq:int = obj["MtlQueueSeq"]
      """  MtlQueueSeq  """  
      self.OrderPONum:str = obj["OrderPONum"]
      """  OrderPONum  """  
      self.OrderAllocSupplyCounter:int = obj["OrderAllocSupplyCounter"]
      """  OrderAllocSupplyCounter  """  
      self.KitOurReqQty:int = obj["KitOurReqQty"]
      """  KitOurReqQty  """  
      self.KitUnitPrice:int = obj["KitUnitPrice"]
      """  KitUnitPrice  """  
      self.KitExtPrice:int = obj["KitExtPrice"]
      """  KitExtPrice  """  
      self.KitPricing:str = obj["KitPricing"]
      """  KitPricing  """  
      self.PartDescription:str = obj["PartDescription"]
      """  PartDescription  """  
      self.AttributeSetShortDescription:str = obj["AttributeSetShortDescription"]
      """  AttributeSetShortDescription  """  
      self.AttributeSetDescription:str = obj["AttributeSetDescription"]
      """  AttributeSetDescription  """  
      self.PartAttrClassID:str = obj["PartAttrClassID"]
      """  PartAttrClassID  """  
      self.FilterAttributeSetID:int = obj["FilterAttributeSetID"]
      """  FilterAttributeSetID  """  
      self.FilterAttributeSetShortDescription:str = obj["FilterAttributeSetShortDescription"]
      """  FilterAttributeSetShortDescription  """  
      self.TrackInventoryAttributes:bool = obj["TrackInventoryAttributes"]
      """  TrackInventoryAttributes  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      """  TrackInventoryByRevision  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  OrderRelNum  """  
      self.OrderRelShippedTotal:int = obj["OrderRelShippedTotal"]
      """  OrderRelShippedTotal  """  
      self.MtoAvailQty:int = obj["MtoAvailQty"]
      """  MtoAvailQty  """  
      self.PartAllocQueueSysRowID:str = obj["PartAllocQueueSysRowID"]
      """  PartAllocQueueSysRowID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocRuleClassDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.RuleClassID:str = obj["RuleClassID"]
      """  Rule Class ID  """  
      self.RuleID:str = obj["RuleID"]
      """  Unique ID of Rule  """  
      self.Description:str = obj["Description"]
      """  Description of the rule  """  
      self.Sequence:int = obj["Sequence"]
      """  The sequence that the rules are processed in  """  
      self.QueryID:str = obj["QueryID"]
      """  QueryID of a BAQ used to join other tables to the PartAllocQueueInfo  """  
      self.Action:str = obj["Action"]
      """  The action that is executed for this rule  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rule is Active  """  
      self.AllocTemplateID:str = obj["AllocTemplateID"]
      """  Indicates the PartAllocTemplate to use when allocating  """  
      self.Formula:str = obj["Formula"]
      """  The formula defined for this rule  """  
      self.MasterDtlSync:bool = obj["MasterDtlSync"]
      """  Indicates if changes made to Reusable Rule are synchronized to this class rule  """  
      self.MasterRuleID:str = obj["MasterRuleID"]
      """  Reusable master rule linked to this class rule.  """  
      self.RuleCalcFulfillOnSearch:bool = obj["RuleCalcFulfillOnSearch"]
      """  Used to determine whether or not we (re)calculate fulfillment values following the return of the results of a search.  """  
      self.RuleUseDemandWhseOnly:bool = obj["RuleUseDemandWhseOnly"]
      """  When TRUE the fulfillment calculations and actions will consider the Demand Warehouse only.  When false, all warehouses will be considered in fulfillment calculations, and the user will be able to choose on Reserve actions whether to consider only the Primary Warehouse or all warehouses.  """  
      self.RuleLimitedRefresh:bool = obj["RuleLimitedRefresh"]
      """  Following the execution of an action (Reserve, Allocate, Release for Picking, Unreserve, Unallocate), when true we will only refresh the rows that were actioned on, when false we will refresh all records.  """  
      self.DevCharacter01:str = obj["DevCharacter01"]
      """  DevCharacter01  """  
      self.DevDecimal01:int = obj["DevDecimal01"]
      """  DevDecimal01  """  
      self.DevBoolean01:bool = obj["DevBoolean01"]
      """  DevBoolean01  """  
      self.DevDate01:str = obj["DevDate01"]
      """  DevDate01  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.AllocDemandType:str = obj["AllocDemandType"]
      """  The type of allocation based on the Action.  Valid Values:  Order, Job, Transfer, or blank.  """  
      self.EnableAllocTemplateID:bool = obj["EnableAllocTemplateID"]
      """  Indicates if the AllocationTemplate field should be enabled  """  
      self.EnableFormula:bool = obj["EnableFormula"]
      """  Indicates if the user is able to enter a formula  """  
      self.EnableQueryID:bool = obj["EnableQueryID"]
      """  Indicates if the QueryID field should be enabled  """  
      self.ActiveSysTaskExists:bool = obj["ActiveSysTaskExists"]
      """  Indicates if an Active SysTask exists for this rule class.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PartAllocRuleMasterDtlFormula:str = obj["PartAllocRuleMasterDtlFormula"]
      self.PartAllocRuleMasterDtlAction:str = obj["PartAllocRuleMasterDtlAction"]
      self.PartAllocRuleMasterDtlAllocTemplateID:str = obj["PartAllocRuleMasterDtlAllocTemplateID"]
      self.PartAllocRuleMasterDtlQueryID:str = obj["PartAllocRuleMasterDtlQueryID"]
      self.PartAllocRuleMasterDtlDescription:str = obj["PartAllocRuleMasterDtlDescription"]
      self.PartAllocTemplateAllocTemplateDesc:str = obj["PartAllocTemplateAllocTemplateDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocRuleClassListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.RuleClassID:str = obj["RuleClassID"]
      """  Rule Class ID  """  
      self.Description:str = obj["Description"]
      """  Description of the rule class  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rule Class is Active  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocRuleClassListTableset:
   def __init__(self, obj):
      self.PartAllocRuleClassList:list[Erp_Tablesets_PartAllocRuleClassListRow] = obj["PartAllocRuleClassList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PartAllocRuleClassRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.RuleClassID:str = obj["RuleClassID"]
      """  Rule Class ID  """  
      self.Description:str = obj["Description"]
      """  Description of the rule class  """  
      self.Active:bool = obj["Active"]
      """  Indicates if the Rule Class is Active  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartAllocRuleClassTableset:
   def __init__(self, obj):
      self.PartAllocRuleClass:list[Erp_Tablesets_PartAllocRuleClassRow] = obj["PartAllocRuleClass"]
      self.PartAllocRuleClassDtl:list[Erp_Tablesets_PartAllocRuleClassDtlRow] = obj["PartAllocRuleClassDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtPartAllocRuleClassTableset:
   def __init__(self, obj):
      self.PartAllocRuleClass:list[Erp_Tablesets_PartAllocRuleClassRow] = obj["PartAllocRuleClass"]
      self.PartAllocRuleClassDtl:list[Erp_Tablesets_PartAllocRuleClassDtlRow] = obj["PartAllocRuleClassDtl"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   ruleClassID
   """  
   def __init__(self, obj):
      self.ruleClassID:str = obj["ruleClassID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["returnObj"]
      pass

class GetBySysRowID_input:
   """ Required : 
   id
   """  
   def __init__(self, obj):
      self.id:str = obj["id"]
      pass

class GetBySysRowID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["returnObj"]
      pass

class GetBySysRowIDs_input:
   """ Required : 
   ids
   """  
   def __init__(self, obj):
      self.ids:str = obj["ids"]
      pass

class GetBySysRowIDs_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["returnObj"]
      pass

class GetFulfillmentRuleTesterTableset_input:
   """ Required : 
   ruleClassID
   ruleID
   """  
   def __init__(self, obj):
      self.ruleClassID:str = obj["ruleClassID"]
      self.ruleID:str = obj["ruleID"]
      pass

class GetFulfillmentRuleTesterTableset_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_FulfillmentRuleTesterTableset] = obj["returnObj"]
      pass

class GetList_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  An expression used to filter the rows. Can be left blank for all rows.  """  
      self.pageSize:int = obj["pageSize"]
      """  The maximum number of rows to return. Leave as zero for no maximum.  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return.  """  
      pass

class GetList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAllocRuleClassListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewPartAllocRuleClassDtl_input:
   """ Required : 
   ds
   ruleClassID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      self.ruleClassID:str = obj["ruleClassID"]
      pass

class GetNewPartAllocRuleClassDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartAllocRuleClass_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

class GetNewPartAllocRuleClass_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePartAllocRuleClass
   whereClausePartAllocRuleClassDtl
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePartAllocRuleClass:str = obj["whereClausePartAllocRuleClass"]
      self.whereClausePartAllocRuleClassDtl:str = obj["whereClausePartAllocRuleClassDtl"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class Ice_BOUpdErrorRow:
   def __init__(self, obj):
      self.TableName:str = obj["TableName"]
      self.ErrorLevel:str = obj["ErrorLevel"]
      self.ErrorType:str = obj["ErrorType"]
      self.ErrorText:str = obj["ErrorText"]
      self.ErrorSysRowID:str = obj["ErrorSysRowID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      pass

class Ice_BOUpdErrorTableset:
   def __init__(self, obj):
      self.BOUpdError:list[Ice_BOUpdErrorRow] = obj["BOUpdError"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Ice_Extensions_ExtensionRow:
   def __init__(self, obj):
      self.ColumnValues:object
      self.RowMod:str = obj["RowMod"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class Ice_Extensions_ExtensionTableColumn:
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ColumnType:str = obj["ColumnType"]
      pass

class Ice_Extensions_ExtensionTableData:
   def __init__(self, obj):
      self.Table:list[Ice_Extensions_ExtensionRow] = obj["Table"]
      self.SystemCode:str = obj["SystemCode"]
      self.TableName:str = obj["TableName"]
      self.Columns:list[Ice_Extensions_ExtensionTableColumn] = obj["Columns"]
      self.PrimaryKeyColumns:str = obj["PrimaryKeyColumns"]
      self.PeerTableSystemCode:str = obj["PeerTableSystemCode"]
      self.PeerTableName:str = obj["PeerTableName"]
      pass

class OnChangePartAllocRuleClassActive_input:
   """ Required : 
   newActive
   ds
   """  
   def __init__(self, obj):
      self.newActive:bool = obj["newActive"]
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

class OnChangePartAllocRuleClassActive_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class OnChangePartAllocRuleClassDtlAction_input:
   """ Required : 
   newAction
   checkForWarnings
   ds
   """  
   def __init__(self, obj):
      self.newAction:str = obj["newAction"]
      self.checkForWarnings:bool = obj["checkForWarnings"]
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

class OnChangePartAllocRuleClassDtlAction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartAllocRuleClassDtlAllocTemplateID_input:
   """ Required : 
   newAllocTemplateID
   ds
   """  
   def __init__(self, obj):
      self.newAllocTemplateID:str = obj["newAllocTemplateID"]
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

class OnChangePartAllocRuleClassDtlAllocTemplateID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartAllocRuleClassDtlMasterDtlSync_input:
   """ Required : 
   newMasterDtlSync
   ds
   """  
   def __init__(self, obj):
      self.newMasterDtlSync:bool = obj["newMasterDtlSync"]
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

class OnChangePartAllocRuleClassDtlMasterDtlSync_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartAllocRuleClassDtlMasterRuleID_input:
   """ Required : 
   newMasterRuleID
   checkOverride
   ds
   """  
   def __init__(self, obj):
      self.newMasterRuleID:str = obj["newMasterRuleID"]
      self.checkOverride:bool = obj["checkOverride"]
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

class OnChangePartAllocRuleClassDtlMasterRuleID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.overrideWarning:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangePartAllocRuleClassDtlQueryID_input:
   """ Required : 
   newQueryID
   checkForWarnings
   ds
   """  
   def __init__(self, obj):
      self.newQueryID:str = obj["newQueryID"]
      self.checkForWarnings:bool = obj["checkForWarnings"]
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

class OnChangePartAllocRuleClassDtlQueryID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.warningMsg:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

class TestFulfillmentRuleClass_input:
   """ Required : 
   ruleClassID
   """  
   def __init__(self, obj):
      self.ruleClassID:str = obj["ruleClassID"]
      pass

class TestFulfillmentRuleClass_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartAllocRuleClassTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPartAllocRuleClassTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PartAllocRuleClassTableset] = obj["ds"]
      pass

      """  output parameters  """  

