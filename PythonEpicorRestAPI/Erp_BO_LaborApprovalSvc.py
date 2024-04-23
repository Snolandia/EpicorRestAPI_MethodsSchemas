import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LaborApprovalSvc
# Description: BL logic for Time approval used by TimeExpApprovalEntry
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LaborApprovals(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborApprovals items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborApprovals
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborApprovals",headers=creds) as resp:
           return await resp.json()

async def post_LaborApprovals(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborApprovals
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborApprovals", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborApprovals_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborApproval item
   Description: Calls GetByID to retrieve the LaborApproval item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborApproval
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborApprovals(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborApprovals_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborApproval for the service
   Description: Calls UpdateExt to update LaborApproval. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborApproval
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborApprovals(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborApprovals_Company_LaborHedSeq_LaborDtlSeq(Company, LaborHedSeq, LaborDtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborApproval item
   Description: Call UpdateExt to delete LaborApproval item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborApproval
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborApprovals(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborApprovals_Company_LaborHedSeq_LaborDtlSeq_LaborDtlComments(Company, LaborHedSeq, LaborDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LaborDtlComments items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LaborDtlComments1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborApprovals(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlComments",headers=creds) as resp:
           return await resp.json()

async def get_LaborApprovals_Company_LaborHedSeq_LaborDtlSeq_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlComment item
   Description: Calls GetByID to retrieve the LaborDtlComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlComment1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborApprovals(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + ")/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlComments(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LaborDtlComments items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LaborDtlComments
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborDtlComments",headers=creds) as resp:
           return await resp.json()

async def post_LaborDtlComments(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LaborDtlComments
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborDtlComments", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LaborDtlComment item
   Description: Calls GetByID to retrieve the LaborDtlComment item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LaborDtlComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LaborDtlComment for the service
   Description: Calls UpdateExt to update LaborDtlComment. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LaborDtlComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LaborDtlCommentRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LaborDtlComments_Company_LaborHedSeq_LaborDtlSeq_CommentNum(Company, LaborHedSeq, LaborDtlSeq, CommentNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LaborDtlComment item
   Description: Call UpdateExt to delete LaborDtlComment item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LaborDtlComment
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LaborHedSeq: Desc: LaborHedSeq   Required: True
      :param LaborDtlSeq: Desc: LaborDtlSeq   Required: True
      :param CommentNum: Desc: CommentNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/LaborDtlComments(" + Company + "," + LaborHedSeq + "," + LaborDtlSeq + "," + CommentNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LaborDtlListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLaborDtl, whereClauseLaborDtlComment, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseLaborDtl=" + whereClauseLaborDtl
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLaborDtlComment=" + whereClauseLaborDtlComment
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(laborHedSeq, laborDtlSeq, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True
   Required: True
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
   params += "laborHedSeq=" + laborHedSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "laborDtlSeq=" + laborDtlSeq

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ApproveReject(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ApproveReject
   Description: The procedure is called when the user selects LaborDtl records for reject or approve
   OperationID: ApproveReject
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ApproveReject_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ApproveReject_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRecall(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRecall
   Description: The procedure is called prior to performing a recall.  It will check
if subsequent approvals have occurred.  If they have the user
will have the opportunity to cancel the recall.
   OperationID: CheckRecall
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRecall_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRecall_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetRowsTran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetRowsTran
   Description: Called from Aprrovals screen to get related task transactions
   OperationID: GetRowsTran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetRowsTran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetRowsTran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RecallTrans(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RecallTrans
   Description: The procedure is called when the user selects LaborDtl records to recall
   OperationID: RecallTrans
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RecallTrans_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RecallTrans_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetChargeRate(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetChargeRate
   Description: This method should call when EquipID is changed
   OperationID: SetChargeRate
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetChargeRate_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetChargeRate_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateChargeRateForTimeType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateChargeRateForTimeType
   Description: Validates if there is no valid Charge Rate according to selected Time Type.
This validation can also be found on BO/Labor.
   OperationID: ValidateChargeRateForTimeType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateChargeRateForTimeType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateChargeRateForTimeType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteLabor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DeleteLabor
   Description: Method to delete multiple labor rows by LaborHedSeq and LaborDtlSeq
   OperationID: DeleteLabor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DeleteLabor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteLabor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtl
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLaborDtlComment(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLaborDtlComment
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLaborDtlComment
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLaborDtlComment_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLaborDtlComment_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LaborApprovalSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlCommentRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborDtlCommentRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborDtlListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LaborDtlRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LaborDtlRow] = obj["value"]
      pass

class Erp_Tablesets_LaborDtlCommentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  The unique identifier of the Labor Header the comment relates to.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.CommentNum:int = obj["CommentNum"]
      """  Internal identifier of the comment record.  Used in conjunction with EmpTimeNum to make the record unique.  """  
      self.CommentType:str = obj["CommentType"]
      """   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.TimeEntryCommentTypeList:str = obj["TimeEntryCommentTypeList"]
      """  List of valid comment types for Time Entry  """  
      self.CommentTypeDesc:str = obj["CommentTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborType:str = obj["LaborType"]
      """   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.ReWork:bool = obj["ReWork"]
      """  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.JCDept:str = obj["JCDept"]
      """  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.OpCode:str = obj["OpCode"]
      """  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  """  
      self.LaborQty:int = obj["LaborQty"]
      """  The Total production quantity reported.  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this transaction "completes" either the setup or production for this operation.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.LaborNote:str = obj["LaborNote"]
      """  A short note that the user can make about the labor transaction.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the labordtl record inspection has completed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this service record belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The line number of the service call this labor detail is for.  """  
      self.ServNum:int = obj["ServNum"]
      """  the service that is being performed on this line.  """  
      self.ServCode:str = obj["ServCode"]
      """  A unique code that identifies the Service  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID,used in PostingEngine  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  The Project Billing Invoice Number where these charges were processed.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the time.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the time received final approval.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The User ID of the submitter.  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  Project Billing calculation in COSandWIP: Currency code is got from Project  """  
      self.PBHours:int = obj["PBHours"]
      """  Project Billing calculation in COSandWIP: Hours used for charge  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ActID:int = obj["ActID"]
      """  Links to PActDtl.ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail. Links to PActDtl.DetailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used By Project Analysis Process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JobType:str = obj["JobType"]
      self.CompleteFlag:bool = obj["CompleteFlag"]
      self.ProdDesc:str = obj["ProdDesc"]
      self.DisplayJob:str = obj["DisplayJob"]
      self.FSComplete:bool = obj["FSComplete"]
      self.DspTotHours:str = obj["DspTotHours"]
      self.OkToChangeResourceGrpID:bool = obj["OkToChangeResourceGrpID"]
      """  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  """  
      self.EndActivity:bool = obj["EndActivity"]
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      self.NextOprSeq:int = obj["NextOprSeq"]
      self.RequestMove:bool = obj["RequestMove"]
      self.NextResourceDesc:str = obj["NextResourceDesc"]
      self.NextOperDesc:str = obj["NextOperDesc"]
      self.EnableResourceGrpID:bool = obj["EnableResourceGrpID"]
      self.JCSystScrapReasons:bool = obj["JCSystScrapReasons"]
      self.JobOperComplete:bool = obj["JobOperComplete"]
      self.EnableRequestMove:bool = obj["EnableRequestMove"]
      self.UnapprovedFirstArt:bool = obj["UnapprovedFirstArt"]
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableComplete:bool = obj["EnableComplete"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.PrintNCTag:bool = obj["PrintNCTag"]
      self.LaborCost:int = obj["LaborCost"]
      """  calculated field: LaborHrs * LaborRate  """  
      self.BurdenCost:int = obj["BurdenCost"]
      """  calculated field: BurdenHrs * BurdenRate  """  
      self.DtClockIn:str = obj["DtClockIn"]
      self.DtClockOut:str = obj["DtClockOut"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.CapabilityDescription:str = obj["CapabilityDescription"]
      self.MultipleEmployeesText:str = obj["MultipleEmployeesText"]
      self.StartActivity:bool = obj["StartActivity"]
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  Labor Detail Employee Name  """  
      self.EfficiencyPercentage:int = obj["EfficiencyPercentage"]
      """  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  """  
      self.JCSystReworkReasons:bool = obj["JCSystReworkReasons"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.DiscrepUOM:str = obj["DiscrepUOM"]
      """  Unit of Measure used for DiscrepQty  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for LaborQty  """  
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Unit of Measure used for ScrapQty.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Enable the SN Button?  """  
      self.PhaseOprSeq:int = obj["PhaseOprSeq"]
      """  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  """  
      self.PhaseJobNum:str = obj["PhaseJobNum"]
      """  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  """  
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      """  Field that indicates if field PrjRoleCd should be disabled.  """  
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      """  Field that indicates if field TimeTypCd should be disabled.  """  
      self.DisLaborType:bool = obj["DisLaborType"]
      """  Field that indicates if field DisLaborTypeshould be disabled.  """  
      self.NewPrjRoleCd:str = obj["NewPrjRoleCd"]
      """  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  """  
      self.NewRoleCdDesc:str = obj["NewRoleCdDesc"]
      """  Holds the description for NewPrjRoleCd  """  
      self.JobTypeCode:str = obj["JobTypeCode"]
      """  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  """  
      self.PrjUsedTran:str = obj["PrjUsedTran"]
      self.PBAllowModify:bool = obj["PBAllowModify"]
      self.ApprovedBy:str = obj["ApprovedBy"]
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.EnableInspection:bool = obj["EnableInspection"]
      self.LbrDay:str = obj["LbrDay"]
      """  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrMonth:str = obj["LbrMonth"]
      """  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrWeek:str = obj["LbrWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  """  
      self.BaseCurrCodeDesc:str = obj["BaseCurrCodeDesc"]
      """  Company Base currency code description for display in LaborDtl grid.  """  
      self.ChgRateCurrDesc:str = obj["ChgRateCurrDesc"]
      """  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  """  
      self.ChargeRate:int = obj["ChargeRate"]
      """  Charge rate calculated for Time and Expense approval  """  
      self.ChargeRateSRC:str = obj["ChargeRateSRC"]
      """  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  """  
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.NotSubmitted:bool = obj["NotSubmitted"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.RoleCdDisplayAll:bool = obj["RoleCdDisplayAll"]
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user has access to the row  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.MES:bool = obj["MES"]
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available for an approver  """  
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open task or not.  """  
      self.EnteredOnCurPlant:bool = obj["EnteredOnCurPlant"]
      """  To know if the LaborDtl was created on the current plant  """  
      self.DiscrpRsnDescription:str = obj["DiscrpRsnDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      """  First name of employee.  """  
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      """  Last name of employee  """  
      self.EmpBasicName:str = obj["EmpBasicName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      """  Full description of the Labor Expense Code master.  """  
      self.IndirectDescription:str = obj["IndirectDescription"]
      """  Full description of the Indirect Labor.  """  
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      """  Job Costing department description.  """  
      self.MachineDescription:str = obj["MachineDescription"]
      """  Full description of Resource.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.PayMethodType:int = obj["PayMethodType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.PayMethodName:str = obj["PayMethodName"]
      """  Name of the payment method  """  
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      """  Description  """  
      self.ProjectDescription:str = obj["ProjectDescription"]
      """  Full description of Project Management Code.  """  
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      """  Long description of the Resource Group.  """  
      self.ResReasonDescription:str = obj["ResReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.ReWorkReasonDescription:str = obj["ReWorkReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      """  A description of the role.  """  
      self.ScrapReasonDescription:str = obj["ScrapReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.ShiftDescription:str = obj["ShiftDescription"]
      """  A concatenation of Start + End time.  """  
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      """  The description of the Time Type Code  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborType:str = obj["LaborType"]
      """   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.ReWork:bool = obj["ReWork"]
      """  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.JCDept:str = obj["JCDept"]
      """  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.OpCode:str = obj["OpCode"]
      """  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  """  
      self.LaborQty:int = obj["LaborQty"]
      """  The Total production quantity reported.  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this transaction "completes" either the setup or production for this operation.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.LaborNote:str = obj["LaborNote"]
      """  A short note that the user can make about the labor transaction.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the labordtl record inspection has completed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this service record belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The line number of the service call this labor detail is for.  """  
      self.ServNum:int = obj["ServNum"]
      """  the service that is being performed on this line.  """  
      self.ServCode:str = obj["ServCode"]
      """  A unique code that identifies the Service  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID,used in PostingEngine  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  The Project Billing Invoice Number where these charges were processed.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the time.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the time received final approval.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The User ID of the submitter.  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  Project Billing calculation in COSandWIP: Currency code is got from Project  """  
      self.PBHours:int = obj["PBHours"]
      """  Project Billing calculation in COSandWIP: Hours used for charge  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ActID:int = obj["ActID"]
      """  Links to PActDtl.ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail. Links to PActDtl.DetailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used By Project Analysis Process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process.  """  
      self.JDFInputFiles:str = obj["JDFInputFiles"]
      """  JDFInputFiles  """  
      self.JDFNumberOfPages:str = obj["JDFNumberOfPages"]
      """  JDFNumberOfPages  """  
      self.BatchWasSaved:str = obj["BatchWasSaved"]
      """  BatchWasSaved  """  
      self.AssignToBatch:bool = obj["AssignToBatch"]
      """  AssignToBatch  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchRequestMove:bool = obj["BatchRequestMove"]
      """  BatchRequestMove  """  
      self.BatchPrint:bool = obj["BatchPrint"]
      """  BatchPrint  """  
      self.BatchLaborHrs:int = obj["BatchLaborHrs"]
      """  BatchLaborHrs  """  
      self.BatchPctOfTotHrs:int = obj["BatchPctOfTotHrs"]
      """  BatchPctOfTotHrs  """  
      self.BatchQty:int = obj["BatchQty"]
      """  BatchQty  """  
      self.BatchTotalExpectedHrs:int = obj["BatchTotalExpectedHrs"]
      """  BatchTotalExpectedHrs  """  
      self.JDFOpCompleted:str = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Downtime:bool = obj["Downtime"]
      """  Downtime  """  
      self.RefJobNum:str = obj["RefJobNum"]
      """  RefJobNum  """  
      self.RefAssemblySeq:int = obj["RefAssemblySeq"]
      """  RefAssemblySeq  """  
      self.RefOprSeq:int = obj["RefOprSeq"]
      """  RefOprSeq  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.BillServiceRate:int = obj["BillServiceRate"]
      """  BillServiceRate  """  
      self.HCMPayHours:int = obj["HCMPayHours"]
      """  Pay Hours used for HCM  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.DiscrepAttributeSetID:int = obj["DiscrepAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  """  
      self.LaborAttributeSetID:int = obj["LaborAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  """  
      self.ScrapAttributeSetID:int = obj["ScrapAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.NonConfPCID:str = obj["NonConfPCID"]
      """  NonConfPCID  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open task or not.  """  
      self.BaseCurrCodeDesc:str = obj["BaseCurrCodeDesc"]
      """  Company Base currency code description for display in LaborDtl grid.  """  
      self.BurdenCost:int = obj["BurdenCost"]
      """  calculated field: BurdenHrs * BurdenRate  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.CapabilityDescription:str = obj["CapabilityDescription"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.ChargeRate:int = obj["ChargeRate"]
      """  Charge rate calculated for Time and Expense approval  """  
      self.ChargeRateSRC:str = obj["ChargeRateSRC"]
      """  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  """  
      self.ChgRateCurrDesc:str = obj["ChgRateCurrDesc"]
      """  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  """  
      self.CompleteFlag:bool = obj["CompleteFlag"]
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.DiscrepUOM:str = obj["DiscrepUOM"]
      """  Unit of Measure used for DiscrepQty  """  
      self.DisLaborType:bool = obj["DisLaborType"]
      """  Field that indicates if field DisLaborTypeshould be disabled.  """  
      self.DisplayJob:str = obj["DisplayJob"]
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      """  Field that indicates if field PrjRoleCd should be disabled.  """  
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      """  Field that indicates if field TimeTypCd should be disabled.  """  
      self.DowntimeTotal:int = obj["DowntimeTotal"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.DspTotHours:str = obj["DspTotHours"]
      self.DtClockIn:str = obj["DtClockIn"]
      self.DtClockOut:str = obj["DtClockOut"]
      self.EfficiencyPercentage:int = obj["EfficiencyPercentage"]
      """  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  Labor Detail Employee Name  """  
      self.EnableComplete:bool = obj["EnableComplete"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.EnableInspection:bool = obj["EnableInspection"]
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableNextOprSeq:bool = obj["EnableNextOprSeq"]
      self.EnablePrintTagsList:bool = obj["EnablePrintTagsList"]
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available for an approver  """  
      self.EnableRequestMove:bool = obj["EnableRequestMove"]
      self.EnableResourceGrpID:bool = obj["EnableResourceGrpID"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Enable the SN Button?  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EndActivity:bool = obj["EndActivity"]
      self.EnteredOnCurPlant:bool = obj["EnteredOnCurPlant"]
      """  To know if the LaborDtl was created on the current plant  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FSComplete:bool = obj["FSComplete"]
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user has access to the row  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the labor detail has comments  """  
      self.HH:bool = obj["HH"]
      """  To tell the bo that this transaction was being modified from HH.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.ISFixHourAndQtyOnly:bool = obj["ISFixHourAndQtyOnly"]
      """  Indicates if the job operation is marked as fixed hours and quantity only.  """  
      self.JCSystReworkReasons:bool = obj["JCSystReworkReasons"]
      self.JCSystScrapReasons:bool = obj["JCSystScrapReasons"]
      self.JobOperComplete:bool = obj["JobOperComplete"]
      self.JobType:str = obj["JobType"]
      self.JobTypeCode:str = obj["JobTypeCode"]
      """  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  """  
      self.LaborCost:int = obj["LaborCost"]
      """  calculated field: LaborHrs * LaborRate  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for LaborQty  """  
      self.LbrDay:str = obj["LbrDay"]
      """  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrMonth:str = obj["LbrMonth"]
      """  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrWeek:str = obj["LbrWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  """  
      self.MES:bool = obj["MES"]
      self.MultipleEmployeesText:str = obj["MultipleEmployeesText"]
      self.NewDifDateFlag:int = obj["NewDifDateFlag"]
      self.NewPrjRoleCd:str = obj["NewPrjRoleCd"]
      """  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  """  
      self.NewRoleCdDesc:str = obj["NewRoleCdDesc"]
      """  Holds the description for NewPrjRoleCd  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      self.NextOperDesc:str = obj["NextOperDesc"]
      self.NextOprSeq:int = obj["NextOprSeq"]
      self.NextResourceDesc:str = obj["NextResourceDesc"]
      self.NonConfProcessed:bool = obj["NonConfProcessed"]
      """  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  """  
      self.NotSubmitted:bool = obj["NotSubmitted"]
      self.OkToChangeResourceGrpID:bool = obj["OkToChangeResourceGrpID"]
      """  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.PBAllowModify:bool = obj["PBAllowModify"]
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      self.PhaseJobNum:str = obj["PhaseJobNum"]
      """  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  """  
      self.PhaseOprSeq:int = obj["PhaseOprSeq"]
      """  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  """  
      self.PrintNCTag:bool = obj["PrintNCTag"]
      self.PrjUsedTran:str = obj["PrjUsedTran"]
      self.ProdDesc:str = obj["ProdDesc"]
      self.ProjPhaseID:str = obj["ProjPhaseID"]
      self.RequestMove:bool = obj["RequestMove"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.RoleCdDisplayAll:bool = obj["RoleCdDisplayAll"]
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Unit of Measure used for ScrapQty.  """  
      self.SentFromMES:bool = obj["SentFromMES"]
      """  Flag field to identify if the row is being sent from MES  """  
      self.StartActivity:bool = obj["StartActivity"]
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.UnapprovedFirstArt:bool = obj["UnapprovedFirstArt"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.EnablePCID:bool = obj["EnablePCID"]
      """  EnablePCID  """  
      self.OutputBin:str = obj["OutputBin"]
      """  The output bin from the resource  """  
      self.OutputWarehouse:str = obj["OutputWarehouse"]
      """  The output warehouse from the resource  """  
      self.EnableLot:bool = obj["EnableLot"]
      """  Internal flag used for the row rules to control whether the Lot columns should be enabled.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number that is to be added to the PCID  """  
      self.PrintPCIDContents:bool = obj["PrintPCIDContents"]
      """  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  """  
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the labor detail has attachments  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.DiscrepAttributeSetDescription:str = obj["DiscrepAttributeSetDescription"]
      """  The Full Description of the Attribute Set for DiscrepQty  """  
      self.DiscrepAttributeSetShortDescription:str = obj["DiscrepAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for DiscrepQty  """  
      self.ScrapAttributeSetDescription:str = obj["ScrapAttributeSetDescription"]
      """  The Full Description of the Attribute Set for ScrapQty  """  
      self.ScrapAttributeSetShortDescription:str = obj["ScrapAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for ScrapQty  """  
      self.LaborAttributeSetDescription:str = obj["LaborAttributeSetDescription"]
      """  The Full Description of the Attribute Set for LaborQty  """  
      self.LaborAttributeSetShortDescription:str = obj["LaborAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for LaborQty  """  
      self.DisableRecallAndDelete:bool = obj["DisableRecallAndDelete"]
      """  Indicates if recall and delete should be disabled  """  
      self.RoleCdList:str = obj["RoleCdList"]
      """  List of available role codes  """  
      self.RowSelected:bool = obj["RowSelected"]
      """  Indicates if the row is selected for submit, recall, or copy  """  
      self.AppointmentStart:str = obj["AppointmentStart"]
      """  Start date/time for calendar appoinment  """  
      self.AppointmentEnd:str = obj["AppointmentEnd"]
      """  End date/time for calendar appoinment  """  
      self.AppointmentTitle:str = obj["AppointmentTitle"]
      """  Title to display for the calendar appointment  """  
      self.TemplateID:str = obj["TemplateID"]
      """  PDF Form Template linked to the Job Operation  """  
      self.WIPTransaction:bool = obj["WIPTransaction"]
      """  Flag to validate if the transaction includes WIP  """  
      self.DiscrepRevision:str = obj["DiscrepRevision"]
      """  Revision for DiscrepQty  """  
      self.LaborRevision:str = obj["LaborRevision"]
      """  Revision for LaborQty  """  
      self.ScrapRevision:str = obj["ScrapRevision"]
      """  Revision for ScrapQty  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.ReportPartQtyAllowed:bool = obj["ReportPartQtyAllowed"]
      """  Indicates whether co-parts can be entered  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DiscrpRsnDescription:str = obj["DiscrpRsnDescription"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HCMIntregationHCMEnabled:bool = obj["HCMIntregationHCMEnabled"]
      self.HCMStatusStatus:str = obj["HCMStatusStatus"]
      self.IndirectDescription:str = obj["IndirectDescription"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.JobAsmblPartNum:str = obj["JobAsmblPartNum"]
      self.JobAsmblDescription:str = obj["JobAsmblDescription"]
      self.MachineDescription:str = obj["MachineDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpDescOpDesc:str = obj["OpDescOpDesc"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.ResReasonDescription:str = obj["ResReasonDescription"]
      self.ReWorkReasonDescription:str = obj["ReWorkReasonDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.ScrapReasonDescription:str = obj["ScrapReasonDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ApproveReject_input:
   """ Required : 
   ipSalesRepCode
   ipAction
   ipComment
   ds
   """  
   def __init__(self, obj):
      self.ipSalesRepCode:str = obj["ipSalesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.ipAction:str = obj["ipAction"]
      """  Action to take A = approver, R = reject.  """  
      self.ipComment:str = obj["ipComment"]
      """  Comment text if comments are to be created.  """  
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

class ApproveReject_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class CheckRecall_input:
   """ Required : 
   ipSalesRepCode
   ds
   """  
   def __init__(self, obj):
      self.ipSalesRepCode:str = obj["ipSalesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

class CheckRecall_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      self.outRecallMsg:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class DeleteLabor_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

class DeleteLabor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Erp_Tablesets_LaborApprovalTableset:
   def __init__(self, obj):
      self.LaborDtl:list[Erp_Tablesets_LaborDtlRow] = obj["LaborDtl"]
      self.LaborDtlComment:list[Erp_Tablesets_LaborDtlCommentRow] = obj["LaborDtlComment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LaborDtlCommentRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  The unique identifier of the Labor Header the comment relates to.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.CommentNum:int = obj["CommentNum"]
      """  Internal identifier of the comment record.  Used in conjunction with EmpTimeNum to make the record unique.  """  
      self.CommentType:str = obj["CommentType"]
      """   The comment type of this record.  Values are:
"SUB" Submit
"APP" Approve
"REJ" Reject  """  
      self.CommentText:str = obj["CommentText"]
      """  The comment text.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  The identifier of the Task record the comment is related to.  Can be zero, which indicates the comment is not related to a specific task.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.TimeEntryCommentTypeList:str = obj["TimeEntryCommentTypeList"]
      """  List of valid comment types for Time Entry  """  
      self.CommentTypeDesc:str = obj["CommentTypeDesc"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborType:str = obj["LaborType"]
      """   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.ReWork:bool = obj["ReWork"]
      """  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.JCDept:str = obj["JCDept"]
      """  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.OpCode:str = obj["OpCode"]
      """  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  """  
      self.LaborQty:int = obj["LaborQty"]
      """  The Total production quantity reported.  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this transaction "completes" either the setup or production for this operation.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.LaborNote:str = obj["LaborNote"]
      """  A short note that the user can make about the labor transaction.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the labordtl record inspection has completed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this service record belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The line number of the service call this labor detail is for.  """  
      self.ServNum:int = obj["ServNum"]
      """  the service that is being performed on this line.  """  
      self.ServCode:str = obj["ServCode"]
      """  A unique code that identifies the Service  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID,used in PostingEngine  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  The Project Billing Invoice Number where these charges were processed.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the time.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the time received final approval.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The User ID of the submitter.  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  Project Billing calculation in COSandWIP: Currency code is got from Project  """  
      self.PBHours:int = obj["PBHours"]
      """  Project Billing calculation in COSandWIP: Hours used for charge  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ActID:int = obj["ActID"]
      """  Links to PActDtl.ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail. Links to PActDtl.DetailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used By Project Analysis Process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JobType:str = obj["JobType"]
      self.CompleteFlag:bool = obj["CompleteFlag"]
      self.ProdDesc:str = obj["ProdDesc"]
      self.DisplayJob:str = obj["DisplayJob"]
      self.FSComplete:bool = obj["FSComplete"]
      self.DspTotHours:str = obj["DspTotHours"]
      self.OkToChangeResourceGrpID:bool = obj["OkToChangeResourceGrpID"]
      """  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  """  
      self.EndActivity:bool = obj["EndActivity"]
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      self.NextOprSeq:int = obj["NextOprSeq"]
      self.RequestMove:bool = obj["RequestMove"]
      self.NextResourceDesc:str = obj["NextResourceDesc"]
      self.NextOperDesc:str = obj["NextOperDesc"]
      self.EnableResourceGrpID:bool = obj["EnableResourceGrpID"]
      self.JCSystScrapReasons:bool = obj["JCSystScrapReasons"]
      self.JobOperComplete:bool = obj["JobOperComplete"]
      self.EnableRequestMove:bool = obj["EnableRequestMove"]
      self.UnapprovedFirstArt:bool = obj["UnapprovedFirstArt"]
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableComplete:bool = obj["EnableComplete"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.PrintNCTag:bool = obj["PrintNCTag"]
      self.LaborCost:int = obj["LaborCost"]
      """  calculated field: LaborHrs * LaborRate  """  
      self.BurdenCost:int = obj["BurdenCost"]
      """  calculated field: BurdenHrs * BurdenRate  """  
      self.DtClockIn:str = obj["DtClockIn"]
      self.DtClockOut:str = obj["DtClockOut"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.CapabilityDescription:str = obj["CapabilityDescription"]
      self.MultipleEmployeesText:str = obj["MultipleEmployeesText"]
      self.StartActivity:bool = obj["StartActivity"]
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  Labor Detail Employee Name  """  
      self.EfficiencyPercentage:int = obj["EfficiencyPercentage"]
      """  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  """  
      self.JCSystReworkReasons:bool = obj["JCSystReworkReasons"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.DiscrepUOM:str = obj["DiscrepUOM"]
      """  Unit of Measure used for DiscrepQty  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for LaborQty  """  
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Unit of Measure used for ScrapQty.  """  
      self.EnableSN:bool = obj["EnableSN"]
      """  Enable the SN Button?  """  
      self.PhaseOprSeq:int = obj["PhaseOprSeq"]
      """  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  """  
      self.PhaseJobNum:str = obj["PhaseJobNum"]
      """  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  """  
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      """  Field that indicates if field PrjRoleCd should be disabled.  """  
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      """  Field that indicates if field TimeTypCd should be disabled.  """  
      self.DisLaborType:bool = obj["DisLaborType"]
      """  Field that indicates if field DisLaborTypeshould be disabled.  """  
      self.NewPrjRoleCd:str = obj["NewPrjRoleCd"]
      """  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  """  
      self.NewRoleCdDesc:str = obj["NewRoleCdDesc"]
      """  Holds the description for NewPrjRoleCd  """  
      self.JobTypeCode:str = obj["JobTypeCode"]
      """  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  """  
      self.PrjUsedTran:str = obj["PrjUsedTran"]
      self.PBAllowModify:bool = obj["PBAllowModify"]
      self.ApprovedBy:str = obj["ApprovedBy"]
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.EnableInspection:bool = obj["EnableInspection"]
      self.LbrDay:str = obj["LbrDay"]
      """  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrMonth:str = obj["LbrMonth"]
      """  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrWeek:str = obj["LbrWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  """  
      self.BaseCurrCodeDesc:str = obj["BaseCurrCodeDesc"]
      """  Company Base currency code description for display in LaborDtl grid.  """  
      self.ChgRateCurrDesc:str = obj["ChgRateCurrDesc"]
      """  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  """  
      self.ChargeRate:int = obj["ChargeRate"]
      """  Charge rate calculated for Time and Expense approval  """  
      self.ChargeRateSRC:str = obj["ChargeRateSRC"]
      """  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  """  
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.NotSubmitted:bool = obj["NotSubmitted"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.RoleCdDisplayAll:bool = obj["RoleCdDisplayAll"]
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user has access to the row  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.MES:bool = obj["MES"]
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available for an approver  """  
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open task or not.  """  
      self.EnteredOnCurPlant:bool = obj["EnteredOnCurPlant"]
      """  To know if the LaborDtl was created on the current plant  """  
      self.DiscrpRsnDescription:str = obj["DiscrpRsnDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      """  First name of employee.  """  
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      """  Last name of employee  """  
      self.EmpBasicName:str = obj["EmpBasicName"]
      """  This is the employee's full name. This is not directly maintainable. It is a concatenation of the FirstName + MiddleInitial + LastName fields. It exists so that it can be used in browses or where ever the complete name in a first, middle, last fashion is required.  """  
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      """  Full description of the Labor Expense Code master.  """  
      self.IndirectDescription:str = obj["IndirectDescription"]
      """  Full description of the Indirect Labor.  """  
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      """  Job Costing department description.  """  
      self.MachineDescription:str = obj["MachineDescription"]
      """  Full description of Resource.  """  
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      """  Description of the operation.  Job, BOM, and Quote entry use this as a default description when entering operation details.  """  
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      """   Indicates that invoices for the customer is summarized and sent as a sum to the bank without specifying the individual invoices.
A single bank transaction is created for the payment but what?s actually sent to the bank will be determined by the electronic interface plug-in program.
Only enabled if type is set to ?Electronic Interface?  """  
      self.PayMethodType:int = obj["PayMethodType"]
      """  Indicated the type of payment with the following options:
 0 = Manual (default)
 1 = Electronic Interface
 2 = Check Printing
 3 = Payment Instrument Type 1
 4 = Payment Instrument Type 2  """  
      self.PayMethodName:str = obj["PayMethodName"]
      """  Name of the payment method  """  
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      """  Description  """  
      self.ProjectDescription:str = obj["ProjectDescription"]
      """  Full description of Project Management Code.  """  
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      """  Long description of the Resource Group.  """  
      self.ResReasonDescription:str = obj["ResReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.ReWorkReasonDescription:str = obj["ReWorkReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      """  A description of the role.  """  
      self.ScrapReasonDescription:str = obj["ScrapReasonDescription"]
      """  Full description of Reason... used on displays/reports.  """  
      self.ShiftDescription:str = obj["ShiftDescription"]
      """  A concatenation of Start + End time.  """  
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      """  The description of the Time Type Code  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LaborDtlListTableset:
   def __init__(self, obj):
      self.LaborDtlList:list[Erp_Tablesets_LaborDtlListRow] = obj["LaborDtlList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LaborDtlRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.EmployeeNum:str = obj["EmployeeNum"]
      """   The number of the employee that performed the work. This field is duplicated from the LaborHed.EmployeeNum. It is here so that an index can be built and used when finding how many jobs are
concurrently active for an employee in order to distribute the labor hours.  """  
      self.LaborHedSeq:int = obj["LaborHedSeq"]
      """  Used as the foreign key to the LaborHed record.  """  
      self.LaborDtlSeq:int = obj["LaborDtlSeq"]
      """  An integer assigned by the system to uniquely identify the LaborDtl record. This integer is created by using the database sequence "LaborDtlSeq".  """  
      self.LaborType:str = obj["LaborType"]
      """   Indicates the type of labor transaction. It can be "I" = Indirect, "P" - Production, "S" - Setup.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.LaborTypePseudo:str = obj["LaborTypePseudo"]
      """   Correlates to LaborType.  Indicates the type of labor transaction, however "Production" LaborType can be broken out into "Project", "Production" or "Service".  Valid Values are "I" = Indirect, "P" - Production, "S" - Setup, "J" - Project, or "V" - Service.
This value controls what fields are displayed/prompted for. 
"I" Indirect does not use JobNum, LotNum, SetupPctCmp, OprComplete, OpCode, LaborQty, ScrapQty, ScrapReasonCode, Rework, ReworkReasonCode.
"S" Setup does not use IndirectCode.
"P" Production does not use IndirectCode or SetupPctCmp,  """  
      self.ReWork:bool = obj["ReWork"]
      """  Logical flag that indicates if this is a Rework labor transaction. This MUST be NO for Indirect labor (LaborDtl.LaborType = I)  """  
      self.ReworkReasonCode:str = obj["ReworkReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this rework is occurring on this operation  and allows the system the ability to recap rework by a code for analysis purposes.
This should only exist  when LaborDtl.Rework = Yes.  """  
      self.JobNum:str = obj["JobNum"]
      """  Job number to which this labor transaction applies. For Setup & Production labor this is a mandatory entry.  The program will use the JobNum/LotNum to validate that a record exists in Jhead and that Jhead.JobClosed is false.  """  
      self.AssemblySeq:int = obj["AssemblySeq"]
      """  The Assembly Sequence of the Job that the labor transaction applies to. This can be blank or must be valid in the JobAsmbl file.  """  
      self.OprSeq:int = obj["OprSeq"]
      """   The sequence of the operation record within the specific Job/Assembly to which this labor transaction applies.
For setup & production entries this must be valid and must not be a subcontract operation (JobOper.SubContract = NO).  """  
      self.JCDept:str = obj["JCDept"]
      """  The Department in which the work was done. Default is from WrkCenter.JCDEpt. This code is DIRECTLY ENTERED.  """  
      self.ResourceGrpID:str = obj["ResourceGrpID"]
      """   The Resource Group in which the labor was performed.  This code IS DIRECTLY entered in labor entry, instead of the finding it based on the description.  This is mandatory and must be valid in the Resource Group table.
For production labor (LaborType = "S" or "P") the default is from the JobOper.PrimaryProdDtl JobOpDtl.ResourceGrpID.
For indirect labor (LaborType = I) there is no default.  """  
      self.OpCode:str = obj["OpCode"]
      """  The operation Code for this labor transaction. Default from JobOper.OpCode. This field IS DIRECTLY ENTERED. This is a mandatory field for direct labor transactions.  """  
      self.LaborHrs:int = obj["LaborHrs"]
      """  Labor hours are used in calculating labor cost for a job. It is stored as hours-hundredths. It is calculated whenever the start/stop time is changed. It can then be overridden.  """  
      self.BurdenHrs:int = obj["BurdenHrs"]
      """  Job Cost Burden hours. Calculated whenever the start/stop times are changed. Can then be overridden.  This is zero for indirect labor.  """  
      self.LaborQty:int = obj["LaborQty"]
      """  The Total production quantity reported.  """  
      self.ScrapQty:int = obj["ScrapQty"]
      """  The reported scrap quantity.  """  
      self.ScrapReasonCode:str = obj["ScrapReasonCode"]
      """   The reason code that is used to link this transaction to a Reason master record, which indicates why this scrap occurred and allows the system the ability to recap scrap by a code for analysis purposes.
This should only exist  when ScrapQty Ne 0.00.  """  
      self.SetupPctComplete:int = obj["SetupPctComplete"]
      """  Indicates what percent of the setup is considered complete as of this labor transaction.  If LaborDtl.SetupPctCmp is > JobOper.SetupPctCmp then let JobOper.SetupPctCmp = LaborDtl.SetupPctCmp.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates if this transaction "completes" either the setup or production for this operation.  """  
      self.IndirectCode:str = obj["IndirectCode"]
      """  A code that links to the Indirect master record that describes the type of indirect labor for this transaction. This field IS DIRECTLY ENTERED, not via a description/selection list method.   This is only valid when LaborType = "I" and must then be valid.  """  
      self.LaborNote:str = obj["LaborNote"]
      """  A short note that the user can make about the labor transaction.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  The expense code for this labor transaction. An expense code is a abbreviated method of indirectly assigning a G/L account for the labor expense. DEFAULTS: for direct labor;  use the JobHead.ExpenseCode if its non-blank,  else use the Employee.ExpenseCode.                                                                   For Indirect Labor use the Indirect.ExpenseCode if not blank, else use the employee.ExpenseCode.  """  
      self.LaborCollection:bool = obj["LaborCollection"]
      """  An internal flag that indicates if this record was created by the Labor Collection system.  It does not have any specific purpose, but it would be nice to know in debugging situations.  """  
      self.AppliedToSchedule:bool = obj["AppliedToSchedule"]
      """  an internal flag which indicates if this labor transaction has updated the job schedule. This will be updated via a Schedule refresh process.  """  
      self.ClockInMInute:int = obj["ClockInMInute"]
      """  Contains both the clock in date and time represented as the # of minutes from a base date. The date/time is stored in this format to allow an easier method for comparing time ranges. This will be utilized in labor collection logic when determining the # of jobs or # of employees to split labor and burden hours. This field is Not directly maintainable. It is just another representation of the ClockInDate and ClockInTime fields.  """  
      self.ClockOutMinute:int = obj["ClockOutMinute"]
      """  Contains both the clock out date and time. See "ClockinMinute" for further explanation of clock in/out. When Labor Collection first creates this record it sets ClockOutMinute = ClockInMinute + 1440. Then later during the clockout process it gets updated to represent the clockout time.  """  
      self.ClockInDate:str = obj["ClockInDate"]
      """  The clock in date that corresponds to the clock in time field. Labor entry uses the LaborHed.ClockInDate as a default for the first LaborDtl record of the LaborHed and then will use the date from the Last LaborDtl record. Labor Collection creates this field based on an adjusted system date.  See LaborHed.ClockInDate field description on adjusting the date.  """  
      self.ClockinTime:int = obj["ClockinTime"]
      """   The adjusted ClockIn time for job costing. Labor Collection updates this with the adjusted time. (see LaborHed.ClockIn for explanation of adjusted time). Labor entry uses LaborHed.Clockin as a default for the first LaborDtl record of a LaborHed. Then use the ClockOut of the last LaborDtl record for this LaborHed. Do not allow the ClockIn Time to be < the LaborHed.ClockIn time.  Stored as hours.hundreths. The clockin/clockout are used to calculate the LaborHours, BurdenHours.
This field is Not directly maintainable. Instead the user enters the clockin time through a program defined fill-in widget which is formatted to conform to either Hours:Minutes or Hours.Hundreths based on the setting in JCSyst.TimeFormat. 
The programs will handle the logic to convert "to" and "from" the fill-in widget.  """  
      self.ClockOutTime:int = obj["ClockOutTime"]
      """   The adjusted Clock Out time for job costing.  Labor entry uses  the LaborHed.ClockOut as a default on the first LaborDtl transaction of a LaborHed record. Do not allow the ClockOut to go past the LaborHed.ClockOut.  See "Clockin" for further explanation of clock in/out.

Labor Entry updates this field at the time of clocking out of a job with the adjusted time. (see LaborHed.ClockOut for description of adjusted time)  """  
      self.ActiveTrans:bool = obj["ActiveTrans"]
      """   Used by Labor collection to indicate that this LaborDtl record is currently active. When the employee clocks out of the operation it is set to "No".

If record is created by Labor Entry this value is "NO".

This field is controlled by the programs and not directly updated by the user. It will be used to prevent clocking in twice to same operation, displaying which operations are currently active.....  """  
      self.OverRidePayRate:int = obj["OverRidePayRate"]
      """  User-defined rate.   The Manufacturing System provides entry/maintenance to this field in labor entry.  It is not referenced in any other part of the Manufacturing System.  Solely intended for use by programs the users may wish to develop.  """  
      self.LaborRate:int = obj["LaborRate"]
      """  Labor rate used for this transaction. This is not maintainable or viewable from labor entry. It is captured from the EmpBasic.LaborRate at time of entry.  """  
      self.BurdenRate:int = obj["BurdenRate"]
      """  The burden rate for this transaction at the time the transaction was created. Capture the appropriate rate from the WrkCenter.ProdBurRate or WrkCenter.SetupBurRate. Note that these rates can be either a "flat" rate or a "percent' of labor rate.  This is not user maintainable or viewable by Labor Entry.  Always Zero for indirect labor transactions.  """  
      self.DspClockInTime:str = obj["DspClockInTime"]
      """  A "pre-formatted" ClockinTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.DspClockOutTime:str = obj["DspClockOutTime"]
      """  A "pre-formatted" ClockOutTime field  used for displays purposes only.  If JCSyst.ClockFormat = "M" then output the clockin time as Hours:Minutes else output it as Hours.Hundreths. Note that the colon or  period  are physically part of the field.  """  
      self.ResourceID:str = obj["ResourceID"]
      """  The ID of the Resource that was used to do the work. This field will be used to run reports using LaborDtl records to show how much work has been done on a specific Resource. This ID is directly entered in labor entry and Labor collection. It is only prompted for if the JcSyst.MachinePrompt = Yes/  """  
      self.OpComplete:bool = obj["OpComplete"]
      """  When displayed in Labor entry this field represents the current status of JobOper.OpComplete. It is used to directly toggle the operation from open to closed. The LaborDtl write trigger uses this to set JobOper.OpComplete.  """  
      self.EarnedHrs:int = obj["EarnedHrs"]
      """  The amount of hours that it should have taken (based on standard) to produce the reported LaborQty. For Setup labor the Earned hours is the lessor of (Est.Setup - ActSetUp) or LaborDtl.BurdenHrs. Rework labor always has zero Earned hrs. Earned hours for production labor is calculated as (JobOper.EstProdHours / JobOper.RunQty) * LaborDtl.LaborQty  """  
      self.AddedOper:bool = obj["AddedOper"]
      """  This indicates if this labor transaction was against an "added operation" at the time it was created/updated. This field is a copy of the JobOPer.AddedOper. It is for internal use only. Used in the logic concerned with updating the ShopPerf summary file. This field prevents the summary from being corrupted if the user changes the JobOPer.AddedOper field after labor activity has occurred.  """  
      self.PayrollDate:str = obj["PayrollDate"]
      """  Not directly user maintainable. Duplicated from LaborHed.PayrollDate. Is used as one of the selection criteria of the labor edit report. See LaborHed.PayrollDate for further info.  """  
      self.PostedToGL:bool = obj["PostedToGL"]
      """   Indicates if this labor/burden cost was posted to G/L WIP accounts.  Transactions are posted in summary form.
Note: All GL related fields (Fiscalyear,FiscalPeriod,Account,etc.) are established during the Caputure WIP/COS process (JCP80-GN.W)  """  
      self.FiscalYear:int = obj["FiscalYear"]
      """   Fiscal year that entry was posted to in G/L.
Note: applicable only when posted to G/L.  """  
      self.FiscalPeriod:int = obj["FiscalPeriod"]
      """   Fiscal period that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.JournalNum:int = obj["JournalNum"]
      """   Journal # that entry was posted to.
Note: applicable only when posted to G/L.  """  
      self.GLTrans:bool = obj["GLTrans"]
      """  Internal flag to indicates if this is the type of transaction that would affect GL.  It is used to prevent certain transactions from posting to G/L.  Currently details created from Job Split do not affect GL and set this to NO.  """  
      self.JournalCode:str = obj["JournalCode"]
      """  Journal Code of the related GLJrnDtl.  """  
      self.InspectionPending:bool = obj["InspectionPending"]
      """  Indicates if the labordtl record inspection has completed.  """  
      self.CallNum:int = obj["CallNum"]
      """  The service call that this service record belongs to.  """  
      self.CallLine:int = obj["CallLine"]
      """  The line number of the service call this labor detail is for.  """  
      self.ServNum:int = obj["ServNum"]
      """  the service that is being performed on this line.  """  
      self.ServCode:str = obj["ServCode"]
      """  A unique code that identifies the Service  """  
      self.ResReasonCode:str = obj["ResReasonCode"]
      """  Problem reason code from the reason master table. type Service call.  """  
      self.WipPosted:bool = obj["WipPosted"]
      """  Indicates that record was processed by the Capture Wip/Cos program (JCP80-GN.W).  WipPosted records cannot be maintained through labor entry.  """  
      self.DiscrepQty:int = obj["DiscrepQty"]
      """  The Non-conformance (scrap) quantity reported in this field would go into Q/A for inspection.  """  
      self.DiscrpRsnCode:str = obj["DiscrpRsnCode"]
      """   The reason code that is used to link the transaction to the reason master record, which indicates why the Non-Conformance (discrepant) occurred and allows the system the ability to recap Non-Conformance (scrap) by a code for analysis purposes.

This should only exist  when DiscrepQty Ne 0.00.  """  
      self.ParentLaborDtlSeq:int = obj["ParentLaborDtlSeq"]
      """  If this record was created through Back Flushing, then this field contains the LaborDtlSeq of the LaborDtl record which caused this record to be created.  The LaborDtl record wich caused the Back Flushing process to start and create other LaborDtl recods is the Parent and the LaborDtl records created by the Back Flushing process are the Children.  """  
      self.LaborEntryMethod:str = obj["LaborEntryMethod"]
      """  Indicates the Method for Labor Entry.  Can be "T" - Time and Quantity, "Q" - Quantity Only (Time is estimated) or "B" - Backflush.  If "B" then the LaborNote will be "Backflushed".  """  
      self.FiscalYearSuffix:str = obj["FiscalYearSuffix"]
      """  Fiscal year suffix.  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  The fiscal calendar year/suffix/period were derived from.  """  
      self.BFLaborReq:bool = obj["BFLaborReq"]
      """  It indicates that the laborDtl record is pending labor for Backflush operations. It is cleared by Backflush Labor Server Process after processing the pending labor  """  
      self.ABTUID:str = obj["ABTUID"]
      """  Reference to the ABT, it is GUID,used in PostingEngine  """  
      self.ProjectID:str = obj["ProjectID"]
      """  Descriptive code assigned by the user to uniquely identify the Jobs, Orders, POs, and Tasks in a Project.  Cannot be blank.  """  
      self.PhaseID:str = obj["PhaseID"]
      """  Project Phase ID  """  
      self.RoleCd:str = obj["RoleCd"]
      """  Project Role Code  """  
      self.TimeTypCd:str = obj["TimeTypCd"]
      """  Time Type Code  """  
      self.PBInvNum:int = obj["PBInvNum"]
      """  The Project Billing Invoice Number where these charges were processed.  """  
      self.PMUID:int = obj["PMUID"]
      """  The payment method of the time.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to Task set  """  
      self.ApprovedDate:str = obj["ApprovedDate"]
      """  The date the time received final approval.  """  
      self.ClaimRef:str = obj["ClaimRef"]
      """  Brief description of the time.  Can be used to group time entries together, for example, all time entries incurred on the same trip can be assigned the same reference.  """  
      self.QuickEntryCode:str = obj["QuickEntryCode"]
      """  Quick entry code.  Reference to the QuickEntry table.  Can be used to default information into the time record.  """  
      self.TimeStatus:str = obj["TimeStatus"]
      """   The status of the time.  Values are:
Blank
E - Entered
S - Submitted
P - Partially Approved
A - Approved
R - Rejected  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Userid of the user who created the record.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the record was created.  """  
      self.CreateTime:int = obj["CreateTime"]
      """  The time the record was created (in seconds since midnight)  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Userid of the user who made the last change to this record.  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the record was last changed.  """  
      self.ChangeTime:int = obj["ChangeTime"]
      """  The time the record was last changed (in seconds since midnight)  """  
      self.ActiveTaskID:str = obj["ActiveTaskID"]
      """  The Currently active Stage changing task  """  
      self.LastTaskID:str = obj["LastTaskID"]
      """  The Last Complete Milestone task  """  
      self.CreatedViaTEWeekView:bool = obj["CreatedViaTEWeekView"]
      """  For development use only.  This field indicates that this LaborDtl record was generated via the Weekly View tab of Time and Expense Entry, which is a way for the user to enter bulk data for hours within a week for the same task.  """  
      self.CurrentWFStageID:str = obj["CurrentWFStageID"]
      """  The identifier of the workflow stage.  """  
      self.WFGroupID:str = obj["WFGroupID"]
      """  The identifier of the workflow group  """  
      self.WFComplete:bool = obj["WFComplete"]
      """  This indicates if the workflow for this group is complete.  """  
      self.ApprovalRequired:bool = obj["ApprovalRequired"]
      """  Indicates if approval is required for this transaction.  """  
      self.SubmittedBy:str = obj["SubmittedBy"]
      """  The User ID of the submitter.  """  
      self.PBRateFrom:str = obj["PBRateFrom"]
      """  Project Billing calculation in COSandWIP: where Rate is got from (EMPL=Employee, ROLE=Role, PROJ = Project)  """  
      self.PBCurrencyCode:str = obj["PBCurrencyCode"]
      """  Project Billing calculation in COSandWIP: Currency code is got from Project  """  
      self.PBHours:int = obj["PBHours"]
      """  Project Billing calculation in COSandWIP: Hours used for charge  """  
      self.PBChargeRate:int = obj["PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup  """  
      self.PBChargeAmt:int = obj["PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours)  """  
      self.DocPBChargeRate:int = obj["DocPBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Project currency  """  
      self.Rpt1PBChargeRate:int = obj["Rpt1PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt2PBChargeRate:int = obj["Rpt2PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.Rpt3PBChargeRate:int = obj["Rpt3PBChargeRate"]
      """  Project Billing calculation in COSandWIP: Rate is got according to the Project setup in the Reporting currency  """  
      self.DocPBChargeAmt:int = obj["DocPBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Project currency  """  
      self.Rpt1PBChargeAmt:int = obj["Rpt1PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt2PBChargeAmt:int = obj["Rpt2PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Rpt3PBChargeAmt:int = obj["Rpt3PBChargeAmt"]
      """  Project Billing calculation in COSandWIP: Charge amount (Rate * hours) in the Reporting currency  """  
      self.Shift:int = obj["Shift"]
      """  Indicates the shift in which the employee clocked in.  Default from the Employee master. Must be valid in the master table JCShift.  """  
      self.ActID:int = obj["ActID"]
      """  Links to PActDtl.ActID  """  
      self.DtailID:int = obj["DtailID"]
      """  System assigned unique id number for the detail. Links to PActDtl.DetailID  """  
      self.ProjProcessed:bool = obj["ProjProcessed"]
      """  Logical field to indicate if this record has been read by project analysis process.  """  
      self.AsOfDate:str = obj["AsOfDate"]
      """  Used By Project Analysis Process.  """  
      self.AsOfSeq:int = obj["AsOfSeq"]
      """  Used By Project Analysis Process.  """  
      self.JDFInputFiles:str = obj["JDFInputFiles"]
      """  JDFInputFiles  """  
      self.JDFNumberOfPages:str = obj["JDFNumberOfPages"]
      """  JDFNumberOfPages  """  
      self.BatchWasSaved:str = obj["BatchWasSaved"]
      """  BatchWasSaved  """  
      self.AssignToBatch:bool = obj["AssignToBatch"]
      """  AssignToBatch  """  
      self.BatchComplete:bool = obj["BatchComplete"]
      """  BatchComplete  """  
      self.BatchRequestMove:bool = obj["BatchRequestMove"]
      """  BatchRequestMove  """  
      self.BatchPrint:bool = obj["BatchPrint"]
      """  BatchPrint  """  
      self.BatchLaborHrs:int = obj["BatchLaborHrs"]
      """  BatchLaborHrs  """  
      self.BatchPctOfTotHrs:int = obj["BatchPctOfTotHrs"]
      """  BatchPctOfTotHrs  """  
      self.BatchQty:int = obj["BatchQty"]
      """  BatchQty  """  
      self.BatchTotalExpectedHrs:int = obj["BatchTotalExpectedHrs"]
      """  BatchTotalExpectedHrs  """  
      self.JDFOpCompleted:str = obj["JDFOpCompleted"]
      """  JDFOpCompleted  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Downtime:bool = obj["Downtime"]
      """  Downtime  """  
      self.RefJobNum:str = obj["RefJobNum"]
      """  RefJobNum  """  
      self.RefAssemblySeq:int = obj["RefAssemblySeq"]
      """  RefAssemblySeq  """  
      self.RefOprSeq:int = obj["RefOprSeq"]
      """  RefOprSeq  """  
      self.Imported:bool = obj["Imported"]
      """  Imported  """  
      self.ImportDate:str = obj["ImportDate"]
      """  ImportDate  """  
      self.TimeAutoSubmit:bool = obj["TimeAutoSubmit"]
      """   If the Time Detail is submited when record is saved, defaulted from Plant Configuration Control;
Enable for new records only  """  
      self.BatchMode:bool = obj["BatchMode"]
      """  BatchMode  """  
      self.BillServiceRate:int = obj["BillServiceRate"]
      """  BillServiceRate  """  
      self.HCMPayHours:int = obj["HCMPayHours"]
      """  Pay Hours used for HCM  """  
      self.EpicorFSA:bool = obj["EpicorFSA"]
      """  True if transaction is related to Epicor FSA  """  
      self.DiscrepAttributeSetID:int = obj["DiscrepAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Non-comformance quantity  """  
      self.LaborAttributeSetID:int = obj["LaborAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the Labor Qty  """  
      self.ScrapAttributeSetID:int = obj["ScrapAttributeSetID"]
      """  The unique identifier of the related Dynamic Attribute Set for the reported Scrap Quantity  """  
      self.PCID:str = obj["PCID"]
      """  PCID  """  
      self.NonConfPCID:str = obj["NonConfPCID"]
      """  NonConfPCID  """  
      self.AllowDirLbr:bool = obj["AllowDirLbr"]
      """  Field that indicates how the EmpBasic.AllowDirLbr flag is set.  Used in UI for row rule.  """  
      self.ApprovalPhaseDesc:str = obj["ApprovalPhaseDesc"]
      """  Used by Time and Expense approval only, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalPhaseID:str = obj["ApprovalPhaseID"]
      """  Used by Time and Expense approval only, populated with the JobHead.PhaseID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectDesc:str = obj["ApprovalProjectDesc"]
      """  Used by Time and Expense approval only, populated with the Project.Description for ApprovalProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovalProjectID:str = obj["ApprovalProjectID"]
      """  Used by Time and Expense approval only, populated with the JobHead.ProjectID, not done as a linked field so it won't impact performance in processes other than Approval.  """  
      self.ApprovedBy:str = obj["ApprovedBy"]
      self.ApprvrHasOpenTask:bool = obj["ApprvrHasOpenTask"]
      """  Used in approval entry.  Indicates if the approver has an open task or not.  """  
      self.BaseCurrCodeDesc:str = obj["BaseCurrCodeDesc"]
      """  Company Base currency code description for display in LaborDtl grid.  """  
      self.BurdenCost:int = obj["BurdenCost"]
      """  calculated field: BurdenHrs * BurdenRate  """  
      self.CallCode:str = obj["CallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.CapabilityDescription:str = obj["CapabilityDescription"]
      self.CapabilityID:str = obj["CapabilityID"]
      self.ChargeRate:int = obj["ChargeRate"]
      """  Charge rate calculated for Time and Expense approval  """  
      self.ChargeRateSRC:str = obj["ChargeRateSRC"]
      """  Transalated text that indicates where the Charge Rate was derived from: Project, Employee, Role, Labor Rate  """  
      self.ChgRateCurrDesc:str = obj["ChgRateCurrDesc"]
      """  The currency code description for the laborDtl charge rate - displayed in labor approval labordtl grid  """  
      self.CompleteFlag:bool = obj["CompleteFlag"]
      self.ContractCode:str = obj["ContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.ContractNum:int = obj["ContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.DiscrepUOM:str = obj["DiscrepUOM"]
      """  Unit of Measure used for DiscrepQty  """  
      self.DisLaborType:bool = obj["DisLaborType"]
      """  Field that indicates if field DisLaborTypeshould be disabled.  """  
      self.DisplayJob:str = obj["DisplayJob"]
      self.DisPrjRoleCd:bool = obj["DisPrjRoleCd"]
      """  Field that indicates if field PrjRoleCd should be disabled.  """  
      self.DisTimeTypCd:bool = obj["DisTimeTypCd"]
      """  Field that indicates if field TimeTypCd should be disabled.  """  
      self.DowntimeTotal:int = obj["DowntimeTotal"]
      self.DspChangeTime:str = obj["DspChangeTime"]
      self.DspCreateTime:str = obj["DspCreateTime"]
      self.DspTotHours:str = obj["DspTotHours"]
      self.DtClockIn:str = obj["DtClockIn"]
      self.DtClockOut:str = obj["DtClockOut"]
      self.EfficiencyPercentage:int = obj["EfficiencyPercentage"]
      """  Shows the efficiency of the hours calculated by dividing the Earned Hours by the Burden Hours when the latter are greater than zero.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  Labor Detail Employee Name  """  
      self.EnableComplete:bool = obj["EnableComplete"]
      self.EnableCopy:bool = obj["EnableCopy"]
      """  Indicates if the copy button is enabled  """  
      self.EnableDiscrepQty:bool = obj["EnableDiscrepQty"]
      self.EnableInspection:bool = obj["EnableInspection"]
      self.EnableLaborQty:bool = obj["EnableLaborQty"]
      self.EnableNextOprSeq:bool = obj["EnableNextOprSeq"]
      self.EnablePrintTagsList:bool = obj["EnablePrintTagsList"]
      self.EnableRecall:bool = obj["EnableRecall"]
      """  Indicates if the recall button is enabled  """  
      self.EnableRecallAprv:bool = obj["EnableRecallAprv"]
      """  Indicates if recall is available for an approver  """  
      self.EnableRequestMove:bool = obj["EnableRequestMove"]
      self.EnableResourceGrpID:bool = obj["EnableResourceGrpID"]
      self.EnableScrapQty:bool = obj["EnableScrapQty"]
      self.EnableSN:bool = obj["EnableSN"]
      """  Enable the SN Button?  """  
      self.EnableSubmit:bool = obj["EnableSubmit"]
      """  Indicates if the submit button is enabled  """  
      self.EndActivity:bool = obj["EndActivity"]
      self.EnteredOnCurPlant:bool = obj["EnteredOnCurPlant"]
      """  To know if the LaborDtl was created on the current plant  """  
      self.FSAAction:str = obj["FSAAction"]
      """  Has the Transaction Type field set in FSA and is stored on FSAExtData db table.  """  
      self.FSACallCode:str = obj["FSACallCode"]
      """  Is the Call Type created on ERP and mapped through System External Key table with Service Type in FSA, stored on FSAExtData db table.  """  
      self.FSAContractCode:str = obj["FSAContractCode"]
      """  Contract Code created on ERP and processed by FSA, stored on FSAExtData db table.  """  
      self.FSAContractNum:int = obj["FSAContractNum"]
      """  Contract created in ERP generated on FSA as Service Agreement, stored on FSAExtData db table.  """  
      self.FSAEmpID:str = obj["FSAEmpID"]
      """  Employee created in ERP and processed on FSA as Service Technician, stored on FSAExtData db table.  """  
      self.FSAEquipmentInstallID:int = obj["FSAEquipmentInstallID"]
      """  Resource ID for Equipment in FSAOffice ( this can be found in the Equipment information/Administrative tab in the Resource ID). Stored on FSAExtData db table.  """  
      self.FSAEquipmentPartNum:str = obj["FSAEquipmentPartNum"]
      """  Part created as equipment in ERP and Installed through FSA process, stored in FSAExtData.  """  
      self.FSAServiceOrderNum:int = obj["FSAServiceOrderNum"]
      """  Service Order number generated on FSA, stored on FSAExtData db table.  """  
      self.FSAServiceOrderResourceNum:int = obj["FSAServiceOrderResourceNum"]
      """  Service Order Resource generated on FSA, stored on FSAExtData db table.  """  
      self.FSAWarrantyCode:str = obj["FSAWarrantyCode"]
      """  Warranty created in ERP and processed on FSA, stored on FSAExtData db table.  """  
      self.FSComplete:bool = obj["FSComplete"]
      self.GLTranAmt:int = obj["GLTranAmt"]
      """  GL Journal Source Transaction Amount  """  
      self.GLTranDate:str = obj["GLTranDate"]
      """  GL Journal Source Transaction Date  """  
      self.HasAccessToRow:bool = obj["HasAccessToRow"]
      """  Indicates if the user has access to the row  """  
      self.HasComments:bool = obj["HasComments"]
      """  Indicates if the labor detail has comments  """  
      self.HH:bool = obj["HH"]
      """  To tell the bo that this transaction was being modified from HH.  """  
      self.IntExternalKey:str = obj["IntExternalKey"]
      """  Unique identifier of related integration record.  """  
      self.ISFixHourAndQtyOnly:bool = obj["ISFixHourAndQtyOnly"]
      """  Indicates if the job operation is marked as fixed hours and quantity only.  """  
      self.JCSystReworkReasons:bool = obj["JCSystReworkReasons"]
      self.JCSystScrapReasons:bool = obj["JCSystScrapReasons"]
      self.JobOperComplete:bool = obj["JobOperComplete"]
      self.JobType:str = obj["JobType"]
      self.JobTypeCode:str = obj["JobTypeCode"]
      """  JobHead.Jobtype. Needed a different name since LaborDtl.JobType was used as a transalated value of JobHead.JobType  """  
      self.LaborCost:int = obj["LaborCost"]
      """  calculated field: LaborHrs * LaborRate  """  
      self.LaborUOM:str = obj["LaborUOM"]
      """  Unit of Measure used for LaborQty  """  
      self.LbrDay:str = obj["LbrDay"]
      """  Text for the day of the week that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrMonth:str = obj["LbrMonth"]
      """  Text for the calendar month name that corresponds to the LaborDtl.ClockInDate  """  
      self.LbrWeek:str = obj["LbrWeek"]
      """  Text to show the week date range (Sunday-Saturday) that corresponds to the LaborDtl.ClockInDate such as "5/2/2009 - 5/9/2009"  """  
      self.MES:bool = obj["MES"]
      self.MultipleEmployeesText:str = obj["MultipleEmployeesText"]
      self.NewDifDateFlag:int = obj["NewDifDateFlag"]
      self.NewPrjRoleCd:str = obj["NewPrjRoleCd"]
      """  field to designate a new Project Role Code ? used by Labor Transaction Project Role Code Maint  """  
      self.NewRoleCdDesc:str = obj["NewRoleCdDesc"]
      """  Holds the description for NewPrjRoleCd  """  
      self.NextAssemblySeq:int = obj["NextAssemblySeq"]
      self.NextOperDesc:str = obj["NextOperDesc"]
      self.NextOprSeq:int = obj["NextOprSeq"]
      self.NextResourceDesc:str = obj["NextResourceDesc"]
      self.NonConfProcessed:bool = obj["NonConfProcessed"]
      """  To evaluate if the NonComformance has been already processed in inspection and no changes can be applied on LaborDtl then.  """  
      self.NotSubmitted:bool = obj["NotSubmitted"]
      self.OkToChangeResourceGrpID:bool = obj["OkToChangeResourceGrpID"]
      """  Holds user's answer to question: "Resource belongs to a different ResourceGroup.  ResourceGroup will be changed.  Do you wish to continue?"  """  
      self.PartDescription:str = obj["PartDescription"]
      self.PartNum:str = obj["PartNum"]
      self.PBAllowModify:bool = obj["PBAllowModify"]
      self.PendingApprovalBy:str = obj["PendingApprovalBy"]
      self.PhaseJobNum:str = obj["PhaseJobNum"]
      """  External field for the Job associated with the WBS Phase ID. The JobNum defaulted into this field will also be defaulted into LaborDtl.JobNum  """  
      self.PhaseOprSeq:int = obj["PhaseOprSeq"]
      """  External field for the Operation associated with the WBS Phase ID. The operation entered in this field will be defaulted into  LaborDtl.OprSeq  """  
      self.PrintNCTag:bool = obj["PrintNCTag"]
      self.PrjUsedTran:str = obj["PrjUsedTran"]
      self.ProdDesc:str = obj["ProdDesc"]
      self.ProjPhaseID:str = obj["ProjPhaseID"]
      self.RequestMove:bool = obj["RequestMove"]
      self.ResourceDesc:str = obj["ResourceDesc"]
      self.RoleCdDisplayAll:bool = obj["RoleCdDisplayAll"]
      self.ScrapUOM:str = obj["ScrapUOM"]
      """  Unit of Measure used for ScrapQty.  """  
      self.SentFromMES:bool = obj["SentFromMES"]
      """  Flag field to identify if the row is being sent from MES  """  
      self.StartActivity:bool = obj["StartActivity"]
      self.TimeDisableDelete:bool = obj["TimeDisableDelete"]
      self.TimeDisableUpdate:bool = obj["TimeDisableUpdate"]
      self.TreeNodeImageName:str = obj["TreeNodeImageName"]
      self.UnapprovedFirstArt:bool = obj["UnapprovedFirstArt"]
      self.WarrantyCode:str = obj["WarrantyCode"]
      """  Warranty linked to part and processed by FSA, stored on FSAExtData db table.  """  
      self.WeekDisplayText:str = obj["WeekDisplayText"]
      self.EnablePCID:bool = obj["EnablePCID"]
      """  EnablePCID  """  
      self.OutputBin:str = obj["OutputBin"]
      """  The output bin from the resource  """  
      self.OutputWarehouse:str = obj["OutputWarehouse"]
      """  The output warehouse from the resource  """  
      self.EnableLot:bool = obj["EnableLot"]
      """  Internal flag used for the row rules to control whether the Lot columns should be enabled.  """  
      self.LotNum:str = obj["LotNum"]
      """  Lot number that is to be added to the PCID  """  
      self.PrintPCIDContents:bool = obj["PrintPCIDContents"]
      """  Flag to indicate that whether to print a PCID contents label for the entered PCID after the processing the reported quantity,  """  
      self.HasAttachments:bool = obj["HasAttachments"]
      """  Indicates if the labor detail has attachments  """  
      self.AttrClassID:str = obj["AttrClassID"]
      self.DiscrepAttributeSetDescription:str = obj["DiscrepAttributeSetDescription"]
      """  The Full Description of the Attribute Set for DiscrepQty  """  
      self.DiscrepAttributeSetShortDescription:str = obj["DiscrepAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for DiscrepQty  """  
      self.ScrapAttributeSetDescription:str = obj["ScrapAttributeSetDescription"]
      """  The Full Description of the Attribute Set for ScrapQty  """  
      self.ScrapAttributeSetShortDescription:str = obj["ScrapAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for ScrapQty  """  
      self.LaborAttributeSetDescription:str = obj["LaborAttributeSetDescription"]
      """  The Full Description of the Attribute Set for LaborQty  """  
      self.LaborAttributeSetShortDescription:str = obj["LaborAttributeSetShortDescription"]
      """  The Short Description of the Attribute Set for LaborQty  """  
      self.DisableRecallAndDelete:bool = obj["DisableRecallAndDelete"]
      """  Indicates if recall and delete should be disabled  """  
      self.RoleCdList:str = obj["RoleCdList"]
      """  List of available role codes  """  
      self.RowSelected:bool = obj["RowSelected"]
      """  Indicates if the row is selected for submit, recall, or copy  """  
      self.AppointmentStart:str = obj["AppointmentStart"]
      """  Start date/time for calendar appoinment  """  
      self.AppointmentEnd:str = obj["AppointmentEnd"]
      """  End date/time for calendar appoinment  """  
      self.AppointmentTitle:str = obj["AppointmentTitle"]
      """  Title to display for the calendar appointment  """  
      self.TemplateID:str = obj["TemplateID"]
      """  PDF Form Template linked to the Job Operation  """  
      self.WIPTransaction:bool = obj["WIPTransaction"]
      """  Flag to validate if the transaction includes WIP  """  
      self.DiscrepRevision:str = obj["DiscrepRevision"]
      """  Revision for DiscrepQty  """  
      self.LaborRevision:str = obj["LaborRevision"]
      """  Revision for LaborQty  """  
      self.ScrapRevision:str = obj["ScrapRevision"]
      """  Revision for ScrapQty  """  
      self.TrackInventoryByRevision:bool = obj["TrackInventoryByRevision"]
      self.ReportPartQtyAllowed:bool = obj["ReportPartQtyAllowed"]
      """  Indicates whether co-parts can be entered  """  
      self.BitFlag:int = obj["BitFlag"]
      self.DiscrpRsnDescription:str = obj["DiscrpRsnDescription"]
      self.EmpBasicLastName:str = obj["EmpBasicLastName"]
      self.EmpBasicFirstName:str = obj["EmpBasicFirstName"]
      self.EmpBasicName:str = obj["EmpBasicName"]
      self.ExpenseCodeDescription:str = obj["ExpenseCodeDescription"]
      self.HCMIntregationHCMEnabled:bool = obj["HCMIntregationHCMEnabled"]
      self.HCMStatusStatus:str = obj["HCMStatusStatus"]
      self.IndirectDescription:str = obj["IndirectDescription"]
      self.JCDeptDescription:str = obj["JCDeptDescription"]
      self.JobAsmblPartNum:str = obj["JobAsmblPartNum"]
      self.JobAsmblDescription:str = obj["JobAsmblDescription"]
      self.MachineDescription:str = obj["MachineDescription"]
      self.OpCodeOpDesc:str = obj["OpCodeOpDesc"]
      self.OpDescOpDesc:str = obj["OpDescOpDesc"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PhaseIDDescription:str = obj["PhaseIDDescription"]
      self.ProjectDescription:str = obj["ProjectDescription"]
      self.ResourceGrpDescription:str = obj["ResourceGrpDescription"]
      self.ResReasonDescription:str = obj["ResReasonDescription"]
      self.ReWorkReasonDescription:str = obj["ReWorkReasonDescription"]
      self.RoleCdRoleDescription:str = obj["RoleCdRoleDescription"]
      self.ScrapReasonDescription:str = obj["ScrapReasonDescription"]
      self.ShiftDescription:str = obj["ShiftDescription"]
      self.TimeTypCdDescription:str = obj["TimeTypCdDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """  The master file to which the task is related.  Opportunity/Quote, Customer, ECO Group etc...  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a task related to a quote (Customer) this field would contain the related Customer.CustNum value.  """  
      self.Key2:str = obj["Key2"]
      """  2nd component of the foreign key to the related master record.  """  
      self.Key3:str = obj["Key3"]
      """  3rd component of the foreign key to the related master record.  """  
      self.TaskID:str = obj["TaskID"]
      """  Link to the TaskMast table. Contains the TaskMast.TaskID value related to this task.  """  
      self.TaskSeqNum:int = obj["TaskSeqNum"]
      """  Used to uniquely identify the record.  Used so more than 1 Task can exist for a given record.  The next sequence is found by finding the last PCE with the same key fields then adding 1 to its seqnum.  """  
      self.TaskDescription:str = obj["TaskDescription"]
      """  Default description from the TaskMaster. TaskMast.TaskDescription. The user can override the default description for this specific task.  """  
      self.SalesRepCode:str = obj["SalesRepCode"]
      """  The SalesRep that this task is assigned to. Will default from Role on TaskMaster  """  
      self.StartDate:str = obj["StartDate"]
      """  Defaults is TODAY.  """  
      self.DueDate:str = obj["DueDate"]
      """  The Task should be completed by this date.  """  
      self.StatusCode:str = obj["StatusCode"]
      """  Status Code. From TaskStat table  """  
      self.PercentComplete:int = obj["PercentComplete"]
      """  Percent of task that is complete.  Valid values are 0-100. User maintained.  """  
      self.Complete:bool = obj["Complete"]
      """  Indicates that this task is complete.  When checked this will trigger creation of the next task and the global alert process.  """  
      self.CompleteDate:str = obj["CompleteDate"]
      """  User entered completion date.  Default to TODAY when the complete flag is checked.  """  
      self.CurrentStage:str = obj["CurrentStage"]
      """   The LOQ must be in this stage to be selected or it will be put in this stage if the LOQ is already past this stage.
Valid Choices are
Lead, Oppo = Opportunity, Quot = Quote.
Not maintainable  """  
      self.Mandatory:bool = obj["Mandatory"]
      """  This task must be completed before the LOQ can move to the next milestone.  Not maintainable as actual task  """  
      self.Milestone:bool = obj["Milestone"]
      """  This task must be completed before the LOQ can move to the next Milestone.  Only one Milestone task can be active on a quote at one time.  Not maintainable as actual task.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.SendAlertComplete:bool = obj["SendAlertComplete"]
      """  Completion of the task will send a Global Alert  """  
      self.PriorityCode:int = obj["PriorityCode"]
      """  Valid values are 1 - 99 1 = HIGH,  99 = LOW  """  
      self.TaskComment:str = obj["TaskComment"]
      """  Contains comments about the Task.  """  
      self.Conclusion:str = obj["Conclusion"]
      """  Valid values are "win" "lose" "next" "next" is the default .  This will display as a radio set.  If "win" is selected then completing this task will require a reason code from CRM Win type. A sales order will be created if all mandatory tasks at this milestone are complete.  If  "lose" is selected all tasks and the quote will close  and a CRM Lose reason code is required. If "next" is selected then the "next task" drop down is enabled and the list of possible next tasks from the task set(TaskSNxt) will be displayed, reason code will be optional  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  Select from list of Win or loss reason codes depending on the setting if the conclusion field  """  
      self.NextTaskID:str = obj["NextTaskID"]
      """  When this task is completed and the conclusion is "next" this field will hold the next Milestone task to be created.  """  
      self.NextTaskSeq:int = obj["NextTaskSeq"]
      """  Indentifies the nest milestone task sequence.  """  
      self.TaskQuoteNum:int = obj["TaskQuoteNum"]
      """  The Quote that this Task is related to.  """  
      self.TaskCustNum:int = obj["TaskCustNum"]
      """  The Customer that this task is related to  """  
      self.TaskShipToNum:str = obj["TaskShipToNum"]
      """  The Customer Ship To that this task is related to  """  
      self.TaskConNum:int = obj["TaskConNum"]
      """  The Customer contact that this Task is related to.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Link to the task set.  """  
      self.TaskSetSeq:int = obj["TaskSetSeq"]
      """  Link to the Task Set Detail  """  
      self.CreateOrder:bool = obj["CreateOrder"]
      """  Setting this when the opportunity is a "win" will trigger the logic that creates a sales order.  """  
      self.SendAlertCreate:bool = obj["SendAlertCreate"]
      """  Creation of the task will send a Global Alert  """  
      self.TypeCode:str = obj["TypeCode"]
      """  Defines the type of task this is.  From the TaskType table.  """  
      self.TaskVendorNum:int = obj["TaskVendorNum"]
      """  The Vendor number associated with this task.  """  
      self.TaskPurPoint:str = obj["TaskPurPoint"]
      """  The Vendor purchase point related to this task.  """  
      self.TaskPrcConNum:int = obj["TaskPrcConNum"]
      """  The purchasing contact person associated with this task.  """  
      self.TaskMktgCampaignID:str = obj["TaskMktgCampaignID"]
      """  Link to the Marketing Campaign related to this Task.  """  
      self.OtherSalesRepCode:str = obj["OtherSalesRepCode"]
      """  A salesperson that the assigned salesperson needs to contact to complete this task  """  
      self.CustomerCategory:bool = obj["CustomerCategory"]
      """  Defines if this task is included in the Customer category.  Categories are used for selecting tasks for assignment to TaskSets.  """  
      self.EngineeringCategory:bool = obj["EngineeringCategory"]
      """  Defines if this task is included in the Engineering category.  """  
      self.VendorCategory:bool = obj["VendorCategory"]
      """  Defines if this task is included in the Vendor category.  """  
      self.PersonalCategory:bool = obj["PersonalCategory"]
      """  Defines if this task is included in the Personal category.  """  
      self.ManagementCategory:bool = obj["ManagementCategory"]
      """  Defines if this task is included in the Management category.  """  
      self.OtherCategory:bool = obj["OtherCategory"]
      """  Defines if this task is included in the Other category.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Role of person who would default as the owner of this task when the task is created. From the RoleCD table.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EmployeeName:str = obj["EmployeeName"]
      """  EmployeeName  """  
      self.TimeOrExp:str = obj["TimeOrExp"]
      """   Text to indicate if this task is for "Time" or "Expense" (translated text). Used only by Labor Approval
TaskList search for search results column.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID, used only by Task Time and Expense search as a search results grid.  """  
      self.TransDate:str = obj["TransDate"]
      """  Holds the date of the transaction that created the task, used by TimeExpense approval search form.  """  
      self.JobNum:str = obj["JobNum"]
      """  JobNum, used only by task time and expense approbal search as search results grid  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaskListTableset:
   def __init__(self, obj):
      self.TaskList:list[Erp_Tablesets_TaskListRow] = obj["TaskList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtLaborApprovalTableset:
   def __init__(self, obj):
      self.LaborDtl:list[Erp_Tablesets_LaborDtlRow] = obj["LaborDtl"]
      self.LaborDtlComment:list[Erp_Tablesets_LaborDtlCommentRow] = obj["LaborDtlComment"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborApprovalTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LaborApprovalTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LaborApprovalTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LaborDtlListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewLaborDtlComment_input:
   """ Required : 
   ds
   laborHedSeq
   laborDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      self.laborDtlSeq:int = obj["laborDtlSeq"]
      pass

class GetNewLaborDtlComment_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLaborDtl_input:
   """ Required : 
   ds
   laborHedSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      self.laborHedSeq:int = obj["laborHedSeq"]
      pass

class GetNewLaborDtl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRowsTran_input:
   """ Required : 
   calcLbrChrg
   ds
   """  
   def __init__(self, obj):
      self.calcLbrChrg:bool = obj["calcLbrChrg"]
      """  To inlcude charge rate  """  
      self.ds:list[Erp_Tablesets_TaskListTableset] = obj["ds"]
      pass

class GetRowsTran_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborApprovalTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_TaskListTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseLaborDtl
   whereClauseLaborDtlComment
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLaborDtl:str = obj["whereClauseLaborDtl"]
      self.whereClauseLaborDtlComment:str = obj["whereClauseLaborDtlComment"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LaborApprovalTableset] = obj["returnObj"]
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

class RecallTrans_input:
   """ Required : 
   ipSalesRepCode
   ds
   """  
   def __init__(self, obj):
      self.ipSalesRepCode:str = obj["ipSalesRepCode"]
      """  The sales Rep Code of the approver.  """  
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

class RecallTrans_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      self.outMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetChargeRate_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

class SetChargeRate_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLaborApprovalTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLaborApprovalTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateChargeRateForTimeType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      pass

class ValidateChargeRateForTimeType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LaborApprovalTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

