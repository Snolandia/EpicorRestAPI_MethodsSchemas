import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.RenewalCodeSvc
# Description: Add your summary for this object here
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_RenewalCodes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RenewalCodes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RenewalCodes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RenewalCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodes",headers=creds) as resp:
           return await resp.json()

async def post_RenewalCodes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RenewalCodes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RenewalCodeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RenewalCodeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RenewalCodes_Company_RenewalCode1(Company, RenewalCode1, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RenewalCode item
   Description: Calls GetByID to retrieve the RenewalCode item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RenewalCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RenewalCode1: Desc: RenewalCode1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RenewalCodeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodes(" + Company + "," + RenewalCode1 + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RenewalCodes_Company_RenewalCode1(Company, RenewalCode1, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RenewalCode for the service
   Description: Calls UpdateExt to update RenewalCode. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RenewalCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RenewalCode1: Desc: RenewalCode1   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RenewalCodeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodes(" + Company + "," + RenewalCode1 + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RenewalCodes_Company_RenewalCode1(Company, RenewalCode1, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RenewalCode item
   Description: Call UpdateExt to delete RenewalCode item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RenewalCode
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RenewalCode1: Desc: RenewalCode1   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodes(" + Company + "," + RenewalCode1 + ")",headers=creds) as resp:
           return await resp.json()

async def get_RenewalCodes_Company_RenewalCode1_RenewalCodeAttches(Company, RenewalCode1, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get RenewalCodeAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_RenewalCodeAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RenewalCode1: Desc: RenewalCode1   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RenewalCodeAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodes(" + Company + "," + RenewalCode1 + ")/RenewalCodeAttches",headers=creds) as resp:
           return await resp.json()

async def get_RenewalCodes_Company_RenewalCode1_RenewalCodeAttches_Company_RenewalCode_DrawingSeq(Company, RenewalCode1, RenewalCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RenewalCodeAttch item
   Description: Calls GetByID to retrieve the RenewalCodeAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RenewalCodeAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RenewalCode1: Desc: RenewalCode1   Required: True   Allow empty value : True
      :param RenewalCode: Desc: RenewalCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RenewalCodeAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodes(" + Company + "," + RenewalCode1 + ")/RenewalCodeAttches(" + Company + "," + RenewalCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_RenewalCodeAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get RenewalCodeAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_RenewalCodeAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RenewalCodeAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodeAttches",headers=creds) as resp:
           return await resp.json()

async def post_RenewalCodeAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_RenewalCodeAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.RenewalCodeAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.RenewalCodeAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodeAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_RenewalCodeAttches_Company_RenewalCode_DrawingSeq(Company, RenewalCode, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the RenewalCodeAttch item
   Description: Calls GetByID to retrieve the RenewalCodeAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_RenewalCodeAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RenewalCode: Desc: RenewalCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.RenewalCodeAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodeAttches(" + Company + "," + RenewalCode + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_RenewalCodeAttches_Company_RenewalCode_DrawingSeq(Company, RenewalCode, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update RenewalCodeAttch for the service
   Description: Calls UpdateExt to update RenewalCodeAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_RenewalCodeAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RenewalCode: Desc: RenewalCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.RenewalCodeAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodeAttches(" + Company + "," + RenewalCode + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_RenewalCodeAttches_Company_RenewalCode_DrawingSeq(Company, RenewalCode, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete RenewalCodeAttch item
   Description: Call UpdateExt to delete RenewalCodeAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_RenewalCodeAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RenewalCode: Desc: RenewalCode   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/RenewalCodeAttches(" + Company + "," + RenewalCode + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.RenewalCodeListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseRenewalCode, whereClauseRenewalCodeAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseRenewalCode=" + whereClauseRenewalCode
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseRenewalCodeAttch=" + whereClauseRenewalCodeAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(renewalCode, epicorHeaders = None):
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
   params += "renewalCode=" + renewalCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfIncreaseMeth(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfIncreaseMeth
   Description: This method should be called to set Increase Method.
   OperationID: OnChangeOfIncreaseMeth
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfIncreaseMeth_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfIncreaseMeth_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfQuoted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfQuoted
   Description: This method should be called to set Quoted.
   OperationID: OnChangeOfQuoted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfQuoted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfQuoted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePriceList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePriceList
   Description: Performs required logic when RenewalCode.PriceListCode is modified.
   OperationID: ValidatePriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePriceList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateTaskSet(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateTaskSet
   Description: Performs required logic when RenewalCode.TaskSetID is modified.
   OperationID: ValidateTaskSet
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTaskSet_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTaskSet_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRenewalCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRenewalCode
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRenewalCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRenewalCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRenewalCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewRenewalCodeAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewRenewalCodeAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewRenewalCodeAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewRenewalCodeAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewRenewalCodeAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.RenewalCodeSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RenewalCodeAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RenewalCodeAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RenewalCodeListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RenewalCodeListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_RenewalCodeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_RenewalCodeRow] = obj["value"]
      pass

class Erp_Tablesets_RenewalCodeAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RenewalCode:str = obj["RenewalCode"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RenewalCodeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RenewalCode:str = obj["RenewalCode"]
      """  Unique identifier of the renewal.  """  
      self.RenewalDesc:str = obj["RenewalDesc"]
      """  Free form text describing the renewal code.  """  
      self.RenewalType:int = obj["RenewalType"]
      """  Reserved for future development.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if a quote needs to be created before a contract can be invoiced.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.IncreaseMethod:int = obj["IncreaseMethod"]
      """   Identifies how price increases will be calculated.
1 = Amount.  A flat amount will be added to the amount that existed in the contract.
2 = Percentage. A percentage of each line will be added to the amount.
3 = Price Lists.  The amount is calculated based upon a price list.  """  
      self.IncreaseAmt:int = obj["IncreaseAmt"]
      """  The amount to increase when the increase method equals Amount.  """  
      self.IncreasePct:int = obj["IncreasePct"]
      """  The percentage to increase when the increase method is percentage.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MethodDesc:str = obj["MethodDesc"]
      """  Increase Method Description used in search grid (should correspond to codedesc of Increase Method)  """  
      self.PriceListCodeListDescription:str = obj["PriceListCodeListDescription"]
      """  Description of the price list.  """  
      self.PriceListCodeListCode:str = obj["PriceListCodeListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      """  Description of the task set.  """  
      self.TaskSetIDTaskSetID:str = obj["TaskSetIDTaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RenewalCodeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RenewalCode1:str = obj["RenewalCode1"]
      self.RenewalDesc:str = obj["RenewalDesc"]
      """  Free form text describing the renewal code.  """  
      self.RenewalType:int = obj["RenewalType"]
      """  Reserved for future development.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if a quote needs to be created before a contract can be invoiced.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.IncreaseMethod:int = obj["IncreaseMethod"]
      """   Identifies how price increases will be calculated.
1 = Amount.  A flat amount will be added to the amount that existed in the contract.
2 = Percentage. A percentage of each line will be added to the amount.
3 = Price Lists.  The amount is calculated based upon a price list.  """  
      self.IncreaseAmt:int = obj["IncreaseAmt"]
      """  The amount to increase when the increase method equals Amount.  """  
      self.IncreasePct:int = obj["IncreasePct"]
      """  The percentage to increase when the increase method is percentage.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Renewable:bool = obj["Renewable"]
      """  To indicate the contract renewal generated using the renewal code is valid for further renewal.  """  
      self.MethodDesc:str = obj["MethodDesc"]
      """  Increase Method Description used in search grid (should correspond to codedesc of Increase Method)  """  
      self.HasBeenUsed:bool = obj["HasBeenUsed"]
      """  Internal field used by the UI for row rules.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PriceListCodeListDescription:str = obj["PriceListCodeListDescription"]
      self.PriceListCodeListCode:str = obj["PriceListCodeListCode"]
      self.TaskSetIDTaskSetID:str = obj["TaskSetIDTaskSetID"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   renewalCode
   """  
   def __init__(self, obj):
      self.renewalCode:str = obj["renewalCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_RenewalCodeAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.RenewalCode:str = obj["RenewalCode"]
      self.DrawingSeq:int = obj["DrawingSeq"]
      self.XFileRefNum:int = obj["XFileRefNum"]
      self.SysRevID:int = obj["SysRevID"]
      self.SysRowID:str = obj["SysRowID"]
      self.ForeignSysRowID:str = obj["ForeignSysRowID"]
      self.DrawDesc:str = obj["DrawDesc"]
      self.FileName:str = obj["FileName"]
      self.PDMDocID:str = obj["PDMDocID"]
      self.DocTypeID:str = obj["DocTypeID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RenewalCodeListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RenewalCode:str = obj["RenewalCode"]
      """  Unique identifier of the renewal.  """  
      self.RenewalDesc:str = obj["RenewalDesc"]
      """  Free form text describing the renewal code.  """  
      self.RenewalType:int = obj["RenewalType"]
      """  Reserved for future development.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if a quote needs to be created before a contract can be invoiced.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.IncreaseMethod:int = obj["IncreaseMethod"]
      """   Identifies how price increases will be calculated.
1 = Amount.  A flat amount will be added to the amount that existed in the contract.
2 = Percentage. A percentage of each line will be added to the amount.
3 = Price Lists.  The amount is calculated based upon a price list.  """  
      self.IncreaseAmt:int = obj["IncreaseAmt"]
      """  The amount to increase when the increase method equals Amount.  """  
      self.IncreasePct:int = obj["IncreasePct"]
      """  The percentage to increase when the increase method is percentage.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.MethodDesc:str = obj["MethodDesc"]
      """  Increase Method Description used in search grid (should correspond to codedesc of Increase Method)  """  
      self.PriceListCodeListDescription:str = obj["PriceListCodeListDescription"]
      """  Description of the price list.  """  
      self.PriceListCodeListCode:str = obj["PriceListCodeListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      """  Description of the task set.  """  
      self.TaskSetIDTaskSetID:str = obj["TaskSetIDTaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RenewalCodeListTableset:
   def __init__(self, obj):
      self.RenewalCodeList:list[Erp_Tablesets_RenewalCodeListRow] = obj["RenewalCodeList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_RenewalCodeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RenewalCode:str = obj["RenewalCode"]
      """  Unique identifier of the renewal.  """  
      self.RenewalDesc:str = obj["RenewalDesc"]
      """  Free form text describing the renewal code.  """  
      self.RenewalType:int = obj["RenewalType"]
      """  Reserved for future development.  """  
      self.Quoted:bool = obj["Quoted"]
      """  Indicates if a quote needs to be created before a contract can be invoiced.  """  
      self.TaskSetID:str = obj["TaskSetID"]
      """  Unique identifier of the task set assigned by the user.  """  
      self.IncreaseMethod:int = obj["IncreaseMethod"]
      """   Identifies how price increases will be calculated.
1 = Amount.  A flat amount will be added to the amount that existed in the contract.
2 = Percentage. A percentage of each line will be added to the amount.
3 = Price Lists.  The amount is calculated based upon a price list.  """  
      self.IncreaseAmt:int = obj["IncreaseAmt"]
      """  The amount to increase when the increase method equals Amount.  """  
      self.IncreasePct:int = obj["IncreasePct"]
      """  The percentage to increase when the increase method is percentage.  """  
      self.PriceListCode:str = obj["PriceListCode"]
      """  Unique identifier of the price list assigned by the user.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Renewable:bool = obj["Renewable"]
      """  To indicate the contract renewal generated using the renewal code is valid for further renewal.  """  
      self.MethodDesc:str = obj["MethodDesc"]
      """  Increase Method Description used in search grid (should correspond to codedesc of Increase Method)  """  
      self.HasBeenUsed:bool = obj["HasBeenUsed"]
      """  Internal field used by the UI for row rules.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PriceListCodeListDescription:str = obj["PriceListCodeListDescription"]
      self.PriceListCodeListCode:str = obj["PriceListCodeListCode"]
      self.TaskSetIDTaskSetID:str = obj["TaskSetIDTaskSetID"]
      self.TaskSetIDTaskSetDescription:str = obj["TaskSetIDTaskSetDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_RenewalCodeTableset:
   def __init__(self, obj):
      self.RenewalCode:list[Erp_Tablesets_RenewalCodeRow] = obj["RenewalCode"]
      self.RenewalCodeAttch:list[Erp_Tablesets_RenewalCodeAttchRow] = obj["RenewalCodeAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtRenewalCodeTableset:
   def __init__(self, obj):
      self.RenewalCode:list[Erp_Tablesets_RenewalCodeRow] = obj["RenewalCode"]
      self.RenewalCodeAttch:list[Erp_Tablesets_RenewalCodeAttchRow] = obj["RenewalCodeAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   renewalCode
   """  
   def __init__(self, obj):
      self.renewalCode:str = obj["renewalCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RenewalCodeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RenewalCodeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RenewalCodeTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_RenewalCodeListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewRenewalCodeAttch_input:
   """ Required : 
   ds
   renewalCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      self.renewalCode:str = obj["renewalCode"]
      pass

class GetNewRenewalCodeAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewRenewalCode_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

class GetNewRenewalCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseRenewalCode
   whereClauseRenewalCodeAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseRenewalCode:str = obj["whereClauseRenewalCode"]
      self.whereClauseRenewalCodeAttch:str = obj["whereClauseRenewalCodeAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_RenewalCodeTableset] = obj["returnObj"]
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

class OnChangeOfIncreaseMeth_input:
   """ Required : 
   ipRenewalCode
   ipIncreaseMethNew
   ds
   """  
   def __init__(self, obj):
      self.ipRenewalCode:str = obj["ipRenewalCode"]
      """  Renewal Code.  """  
      self.ipIncreaseMethNew:int = obj["ipIncreaseMethNew"]
      """  New Increase Method.  """  
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

class OnChangeOfIncreaseMeth_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfQuoted_input:
   """ Required : 
   ipQuoted
   ds
   """  
   def __init__(self, obj):
      self.ipQuoted:bool = obj["ipQuoted"]
      """  Quoted.  """  
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

class OnChangeOfQuoted_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRenewalCodeTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtRenewalCodeTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePriceList_input:
   """ Required : 
   ipPriceListCode
   ds
   """  
   def __init__(self, obj):
      self.ipPriceListCode:str = obj["ipPriceListCode"]
      """  Proposed input value of PriceListCode  """  
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

class ValidatePriceList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateTaskSet_input:
   """ Required : 
   ipTaskSet
   ds
   """  
   def __init__(self, obj):
      self.ipTaskSet:str = obj["ipTaskSet"]
      """  Proposed input value of TaskSetID  """  
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

class ValidateTaskSet_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_RenewalCodeTableset] = obj["ds"]
      pass

      """  output parameters  """  

