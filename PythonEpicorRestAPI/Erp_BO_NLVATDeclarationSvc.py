import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.NLVATDeclarationSvc
# Description: Netherlands Electronic VAT Declaration BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_NLVATDeclarations(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get NLVATDeclarations items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NLVATDeclarations
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NLTaxReportDeclarationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations",headers=creds) as resp:
           return await resp.json()

async def post_NLVATDeclarations(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NLVATDeclarations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_NLVATDeclarations_Company_DeclarationUID(Company, DeclarationUID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NLVATDeclaration item
   Description: Calls GetByID to retrieve the NLVATDeclaration item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NLVATDeclaration
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationUID: Desc: DeclarationUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations(" + Company + "," + DeclarationUID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_NLVATDeclarations_Company_DeclarationUID(Company, DeclarationUID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update NLVATDeclaration for the service
   Description: Calls UpdateExt to update NLVATDeclaration. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NLVATDeclaration
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationUID: Desc: DeclarationUID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations(" + Company + "," + DeclarationUID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_NLVATDeclarations_Company_DeclarationUID(Company, DeclarationUID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete NLVATDeclaration item
   Description: Call UpdateExt to delete NLVATDeclaration item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NLVATDeclaration
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationUID: Desc: DeclarationUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations(" + Company + "," + DeclarationUID + ")",headers=creds) as resp:
           return await resp.json()

async def get_NLVATDeclarations_Company_DeclarationUID_NLTaxReportDeclarationAttches(Company, DeclarationUID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get NLTaxReportDeclarationAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_NLTaxReportDeclarationAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationUID: Desc: DeclarationUID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NLTaxReportDeclarationAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations(" + Company + "," + DeclarationUID + ")/NLTaxReportDeclarationAttches",headers=creds) as resp:
           return await resp.json()

async def get_NLVATDeclarations_Company_DeclarationUID_NLTaxReportDeclarationAttches_Company_DeclarationUID_DrawingSeq(Company, DeclarationUID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NLTaxReportDeclarationAttch item
   Description: Calls GetByID to retrieve the NLTaxReportDeclarationAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NLTaxReportDeclarationAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationUID: Desc: DeclarationUID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLVATDeclarations(" + Company + "," + DeclarationUID + ")/NLTaxReportDeclarationAttches(" + Company + "," + DeclarationUID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_NLTaxReportDeclarationAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get NLTaxReportDeclarationAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_NLTaxReportDeclarationAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NLTaxReportDeclarationAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLTaxReportDeclarationAttches",headers=creds) as resp:
           return await resp.json()

async def post_NLTaxReportDeclarationAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_NLTaxReportDeclarationAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLTaxReportDeclarationAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_NLTaxReportDeclarationAttches_Company_DeclarationUID_DrawingSeq(Company, DeclarationUID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the NLTaxReportDeclarationAttch item
   Description: Calls GetByID to retrieve the NLTaxReportDeclarationAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_NLTaxReportDeclarationAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationUID: Desc: DeclarationUID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLTaxReportDeclarationAttches(" + Company + "," + DeclarationUID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_NLTaxReportDeclarationAttches_Company_DeclarationUID_DrawingSeq(Company, DeclarationUID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update NLTaxReportDeclarationAttch for the service
   Description: Calls UpdateExt to update NLTaxReportDeclarationAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_NLTaxReportDeclarationAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationUID: Desc: DeclarationUID   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.NLTaxReportDeclarationAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLTaxReportDeclarationAttches(" + Company + "," + DeclarationUID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_NLTaxReportDeclarationAttches_Company_DeclarationUID_DrawingSeq(Company, DeclarationUID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete NLTaxReportDeclarationAttch item
   Description: Call UpdateExt to delete NLTaxReportDeclarationAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_NLTaxReportDeclarationAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param DeclarationUID: Desc: DeclarationUID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/NLTaxReportDeclarationAttches(" + Company + "," + DeclarationUID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.NLTaxReportDeclarationListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseNLTaxReportDeclaration, whereClauseNLTaxReportDeclarationAttch, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseNLTaxReportDeclaration=" + whereClauseNLTaxReportDeclaration
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseNLTaxReportDeclarationAttch=" + whereClauseNLTaxReportDeclarationAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(declarationUID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
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
   params += "declarationUID=" + declarationUID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNextNewNLTaxReportDeclaration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNextNewNLTaxReportDeclaration
   Description: This method add new NLTaxReportDeclaration row to data set for specific VAT Report
   OperationID: GetNextNewNLTaxReportDeclaration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNextNewNLTaxReportDeclaration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNextNewNLTaxReportDeclaration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTaxBoxData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTaxBoxData
   Description: This method retrieve Tax Box Amounts
   OperationID: GetTaxBoxData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTaxBoxData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTaxBoxData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenExportFile(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenExportFile
   Description: Export VAT Declaration to XBRL *.xml file.
   OperationID: GenExportFile
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenExportFile_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenExportFile_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetDeclarationStatus(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetDeclarationStatus
   Description: This method Reset VAT Declaration status to NOT GENERATED.
   OperationID: ResetDeclarationStatus
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetDeclarationStatus_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetDeclarationStatus_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetStatusToSubmitted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetStatusToSubmitted
   Description: This method Manually Submitted VAT Declaration.
   OperationID: SetStatusToSubmitted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetStatusToSubmitted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetStatusToSubmitted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewNLTaxReportDeclaration(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewNLTaxReportDeclaration
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNLTaxReportDeclaration
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNLTaxReportDeclaration_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNLTaxReportDeclaration_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewNLTaxReportDeclarationAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewNLTaxReportDeclarationAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewNLTaxReportDeclarationAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewNLTaxReportDeclarationAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewNLTaxReportDeclarationAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.NLVATDeclarationSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NLTaxReportDeclarationAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NLTaxReportDeclarationListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_NLTaxReportDeclarationRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_NLTaxReportDeclarationRow] = obj["value"]
      pass

class Erp_Tablesets_NLTaxReportDeclarationAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DeclarationUID:int = obj["DeclarationUID"]
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

class Erp_Tablesets_NLTaxReportDeclarationListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DeclarationUID:int = obj["DeclarationUID"]
      """  Declaration Unique Identifier.  """  
      self.DeclarationDate:str = obj["DeclarationDate"]
      """  Declaration Date.  """  
      self.Correction:bool = obj["Correction"]
      """  Document Flag (0 - Declaration, 1 - Correction).  """  
      self.ReportID:str = obj["ReportID"]
      """  Tax Report ID.  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Electronic Interface Unique Identifier.  """  
      self.LastExportedDate:str = obj["LastExportedDate"]
      """  Last Exported Date.  """  
      self.LastSentDate:str = obj["LastSentDate"]
      """  Last Sent Date.  """  
      self.SentStatus:int = obj["SentStatus"]
      """  Sent Status (0 – Not Generated; 1 – Ready; 2 – Error; 3 – Sent; 4 – Accepted; 5 – Manually Submitted)  """  
      self.DeclarationCode:str = obj["DeclarationCode"]
      """  Declaration/Correction Code  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NLTaxReportDeclarationRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DeclarationUID:int = obj["DeclarationUID"]
      """  Declaration Unique Identifier.  """  
      self.DeclarationDate:str = obj["DeclarationDate"]
      """  Declaration Date.  """  
      self.Correction:bool = obj["Correction"]
      """  Document Flag (0 - Declaration, 1 - Correction).  """  
      self.ReportID:str = obj["ReportID"]
      """  Tax Report ID.  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Electronic Interface Unique Identifier.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Output File.  """  
      self.LastExportedDate:str = obj["LastExportedDate"]
      """  Last Exported Date.  """  
      self.LastExportedBy:str = obj["LastExportedBy"]
      """  Last Exported By User.  """  
      self.LastSentDate:str = obj["LastSentDate"]
      """  Last Sent Date.  """  
      self.LastSentBy:str = obj["LastSentBy"]
      """  Last Sent By User.  """  
      self.SentStatus:int = obj["SentStatus"]
      """  Sent Status (0 – Not Generated; 1 – Ready; 2 – Error; 3 – Sent; 4 – Accepted; 5 – Manually Submitted)  """  
      self.SentErrorMessage:str = obj["SentErrorMessage"]
      """  Sent Error Message.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code.  """  
      self.RptComment:str = obj["RptComment"]
      """  Comment text.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DeclarationCode:str = obj["DeclarationCode"]
      """  Declaration/Correction Code  """  
      self.ReportDescription:str = obj["ReportDescription"]
      """  Tax Report Description  """  
      self.Box1aDocTaxableAmt:int = obj["Box1aDocTaxableAmt"]
      """  Box 1a Taxable Amount in Doc Currency  """  
      self.Box1aDocTaxAmt:int = obj["Box1aDocTaxAmt"]
      """  Box 1a Tax Amount in Doc Currency  """  
      self.Box1aTaxableAmt:int = obj["Box1aTaxableAmt"]
      """  Box 1a Taxable Amount  """  
      self.Box1aTaxAmt:int = obj["Box1aTaxAmt"]
      """  Box 1a Tax Amount  """  
      self.Box1bDocTaxableAmt:int = obj["Box1bDocTaxableAmt"]
      """  Box 1b Taxable Amount in Doc Currency  """  
      self.Box1bDocTaxAmt:int = obj["Box1bDocTaxAmt"]
      """  Box 1b Tax Amount in Doc Currency  """  
      self.Box1bTaxableAmt:int = obj["Box1bTaxableAmt"]
      """  Box 1b Taxable Amount  """  
      self.Box1bTaxAmt:int = obj["Box1bTaxAmt"]
      """  Box 1b Tax Amount  """  
      self.Box1cDocTaxableAmt:int = obj["Box1cDocTaxableAmt"]
      """  Box 1c Taxable Amount in Doc Currency  """  
      self.Box1cDocTaxAmt:int = obj["Box1cDocTaxAmt"]
      """  Box 1c Tax Amount in Doc Currency  """  
      self.Box1cTaxableAmt:int = obj["Box1cTaxableAmt"]
      """  Box 1c Taxable Amount  """  
      self.Box1cTaxAmt:int = obj["Box1cTaxAmt"]
      """  Box 1c Tax Amount  """  
      self.Box1dDocTaxableAmt:int = obj["Box1dDocTaxableAmt"]
      """  Box 1d Taxable Amount in Doc Currency  """  
      self.Box1dDocTaxAmt:int = obj["Box1dDocTaxAmt"]
      """  Box 1d Tax Amount in Doc Currency  """  
      self.Box1dTaxableAmt:int = obj["Box1dTaxableAmt"]
      """  Box 1d Taxable Amount  """  
      self.Box1dTaxAmt:int = obj["Box1dTaxAmt"]
      """  Box 1d Tax Amount  """  
      self.Box1eDocTaxableAmt:int = obj["Box1eDocTaxableAmt"]
      """  Box 1e Taxable Amount in Doc Currency  """  
      self.Box1eTaxableAmt:int = obj["Box1eTaxableAmt"]
      """  Box 1e Taxable Amount  """  
      self.Box2aDocTaxableAmt:int = obj["Box2aDocTaxableAmt"]
      """  Box 2a Taxable Amount in Doc Currency  """  
      self.Box2aDocTaxAmt:int = obj["Box2aDocTaxAmt"]
      """  Box 2a Tax Amount in Doc Currency  """  
      self.Box2aTaxableAmt:int = obj["Box2aTaxableAmt"]
      """  Box 2a Taxable Amount  """  
      self.Box2aTaxAmt:int = obj["Box2aTaxAmt"]
      """  Box 2a Tax Amount  """  
      self.Box3aDocTaxableAmt:int = obj["Box3aDocTaxableAmt"]
      """  Box 3a Taxable Amount in Doc Currency  """  
      self.Box3aTaxableAmt:int = obj["Box3aTaxableAmt"]
      """  Box 3a Taxable Amount  """  
      self.Box3bDocTaxableAmt:int = obj["Box3bDocTaxableAmt"]
      """  Box 3b Taxable Amount in Doc Currency  """  
      self.Box3bTaxableAmt:int = obj["Box3bTaxableAmt"]
      """  Box 3b Taxable Amount  """  
      self.Box3cDocTaxableAmt:int = obj["Box3cDocTaxableAmt"]
      """  Box 3c Taxable Amount in Doc Currency  """  
      self.Box3cTaxableAmt:int = obj["Box3cTaxableAmt"]
      """  Box 3c Taxable Amount  """  
      self.Box4aDocTaxableAmt:int = obj["Box4aDocTaxableAmt"]
      """  Box 4a Taxable Amount in Doc Currency  """  
      self.Box4aDocTaxAmt:int = obj["Box4aDocTaxAmt"]
      """  Box 4a Tax Amount in Doc Currency  """  
      self.Box4aTaxableAmt:int = obj["Box4aTaxableAmt"]
      """  Box 4a Taxable Amount  """  
      self.Box4aTaxAmt:int = obj["Box4aTaxAmt"]
      """  Box 4a Tax Amount  """  
      self.Box4bDocTaxableAmt:int = obj["Box4bDocTaxableAmt"]
      """  Box 4b Taxable Amount in Doc Currency  """  
      self.Box4bDocTaxAmt:int = obj["Box4bDocTaxAmt"]
      """  Box 4b Tax Amount in Doc Currency  """  
      self.Box4bTaxableAmt:int = obj["Box4bTaxableAmt"]
      """  Box 4b Taxable Amount  """  
      self.Box4bTaxAmt:int = obj["Box4bTaxAmt"]
      """  Box 4b Tax Amount  """  
      self.Box5aDocTaxAmt:int = obj["Box5aDocTaxAmt"]
      """  Box 5a Tax Amount in Doc Currency  """  
      self.Box5aTaxAmt:int = obj["Box5aTaxAmt"]
      """  Box 5a Tax Amount  """  
      self.Box5bDocTaxAmt:int = obj["Box5bDocTaxAmt"]
      """  Box 5b Tax Amount in Doc Currency  """  
      self.Box5bTaxAmt:int = obj["Box5bTaxAmt"]
      """  Box 5b Tax Amount  """  
      self.Box5cDocTaxAmt:int = obj["Box5cDocTaxAmt"]
      """  Box 5c Tax Amount in Doc Currency  """  
      self.Box5cTaxAmt:int = obj["Box5cTaxAmt"]
      """  Box 5c Tax Amount  """  
      self.Box5dDocTaxAmt:int = obj["Box5dDocTaxAmt"]
      """  Box 5d Tax Amount in Doc Currency  """  
      self.Box5dTaxAmt:int = obj["Box5dTaxAmt"]
      """  Box 5d Tax Amount  """  
      self.Box5eDocTaxAmt:int = obj["Box5eDocTaxAmt"]
      """  Box 5e Tax Amount in Doc Currency  """  
      self.Box5eTaxAmt:int = obj["Box5eTaxAmt"]
      """  Box 5e Tax Amount  """  
      self.Box5fDocTaxAmt:int = obj["Box5fDocTaxAmt"]
      """  Box 5f Tax Amount in Doc Currency  """  
      self.Box5fTaxAmt:int = obj["Box5fTaxAmt"]
      """  Box 5f Tax Amount  """  
      self.Box5gToPayDocTaxAmt:int = obj["Box5gToPayDocTaxAmt"]
      """  Box 5g To Pay Tax Amount in Doc Currency  """  
      self.Box5gToPayTaxAmt:int = obj["Box5gToPayTaxAmt"]
      """  Box 5g To Pay Tax Amount  """  
      self.Box5gToReclaimDocTaxAmt:int = obj["Box5gToReclaimDocTaxAmt"]
      """  Box 5g To Reclaim Tax Amount in Doc Currency  """  
      self.Box5gToReclaimTaxAmt:int = obj["Box5gToReclaimTaxAmt"]
      """  Box 5g To Reclaim Tax Amount  """  
      self.Box5gIsToPay:bool = obj["Box5gIsToPay"]
      """  Is To Pay  """  
      self.Box5gIsToReclaim:bool = obj["Box5gIsToReclaim"]
      """  Is To Reclaim  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   declarationUID
   """  
   def __init__(self, obj):
      self.declarationUID:int = obj["declarationUID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_NLTaxReportDeclarationAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.DeclarationUID:int = obj["DeclarationUID"]
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

class Erp_Tablesets_NLTaxReportDeclarationListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DeclarationUID:int = obj["DeclarationUID"]
      """  Declaration Unique Identifier.  """  
      self.DeclarationDate:str = obj["DeclarationDate"]
      """  Declaration Date.  """  
      self.Correction:bool = obj["Correction"]
      """  Document Flag (0 - Declaration, 1 - Correction).  """  
      self.ReportID:str = obj["ReportID"]
      """  Tax Report ID.  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Electronic Interface Unique Identifier.  """  
      self.LastExportedDate:str = obj["LastExportedDate"]
      """  Last Exported Date.  """  
      self.LastSentDate:str = obj["LastSentDate"]
      """  Last Sent Date.  """  
      self.SentStatus:int = obj["SentStatus"]
      """  Sent Status (0 – Not Generated; 1 – Ready; 2 – Error; 3 – Sent; 4 – Accepted; 5 – Manually Submitted)  """  
      self.DeclarationCode:str = obj["DeclarationCode"]
      """  Declaration/Correction Code  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NLTaxReportDeclarationRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.DeclarationUID:int = obj["DeclarationUID"]
      """  Declaration Unique Identifier.  """  
      self.DeclarationDate:str = obj["DeclarationDate"]
      """  Declaration Date.  """  
      self.Correction:bool = obj["Correction"]
      """  Document Flag (0 - Declaration, 1 - Correction).  """  
      self.ReportID:str = obj["ReportID"]
      """  Tax Report ID.  """  
      self.EFTHeadUID:int = obj["EFTHeadUID"]
      """  Electronic Interface Unique Identifier.  """  
      self.OutputFile:str = obj["OutputFile"]
      """  Output File.  """  
      self.LastExportedDate:str = obj["LastExportedDate"]
      """  Last Exported Date.  """  
      self.LastExportedBy:str = obj["LastExportedBy"]
      """  Last Exported By User.  """  
      self.LastSentDate:str = obj["LastSentDate"]
      """  Last Sent Date.  """  
      self.LastSentBy:str = obj["LastSentBy"]
      """  Last Sent By User.  """  
      self.SentStatus:int = obj["SentStatus"]
      """  Sent Status (0 – Not Generated; 1 – Ready; 2 – Error; 3 – Sent; 4 – Accepted; 5 – Manually Submitted)  """  
      self.SentErrorMessage:str = obj["SentErrorMessage"]
      """  Sent Error Message.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  Currency Code.  """  
      self.RptComment:str = obj["RptComment"]
      """  Comment text.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DeclarationCode:str = obj["DeclarationCode"]
      """  Declaration/Correction Code  """  
      self.ReportDescription:str = obj["ReportDescription"]
      """  Tax Report Description  """  
      self.Box1aDocTaxableAmt:int = obj["Box1aDocTaxableAmt"]
      """  Box 1a Taxable Amount in Doc Currency  """  
      self.Box1aDocTaxAmt:int = obj["Box1aDocTaxAmt"]
      """  Box 1a Tax Amount in Doc Currency  """  
      self.Box1aTaxableAmt:int = obj["Box1aTaxableAmt"]
      """  Box 1a Taxable Amount  """  
      self.Box1aTaxAmt:int = obj["Box1aTaxAmt"]
      """  Box 1a Tax Amount  """  
      self.Box1bDocTaxableAmt:int = obj["Box1bDocTaxableAmt"]
      """  Box 1b Taxable Amount in Doc Currency  """  
      self.Box1bDocTaxAmt:int = obj["Box1bDocTaxAmt"]
      """  Box 1b Tax Amount in Doc Currency  """  
      self.Box1bTaxableAmt:int = obj["Box1bTaxableAmt"]
      """  Box 1b Taxable Amount  """  
      self.Box1bTaxAmt:int = obj["Box1bTaxAmt"]
      """  Box 1b Tax Amount  """  
      self.Box1cDocTaxableAmt:int = obj["Box1cDocTaxableAmt"]
      """  Box 1c Taxable Amount in Doc Currency  """  
      self.Box1cDocTaxAmt:int = obj["Box1cDocTaxAmt"]
      """  Box 1c Tax Amount in Doc Currency  """  
      self.Box1cTaxableAmt:int = obj["Box1cTaxableAmt"]
      """  Box 1c Taxable Amount  """  
      self.Box1cTaxAmt:int = obj["Box1cTaxAmt"]
      """  Box 1c Tax Amount  """  
      self.Box1dDocTaxableAmt:int = obj["Box1dDocTaxableAmt"]
      """  Box 1d Taxable Amount in Doc Currency  """  
      self.Box1dDocTaxAmt:int = obj["Box1dDocTaxAmt"]
      """  Box 1d Tax Amount in Doc Currency  """  
      self.Box1dTaxableAmt:int = obj["Box1dTaxableAmt"]
      """  Box 1d Taxable Amount  """  
      self.Box1dTaxAmt:int = obj["Box1dTaxAmt"]
      """  Box 1d Tax Amount  """  
      self.Box1eDocTaxableAmt:int = obj["Box1eDocTaxableAmt"]
      """  Box 1e Taxable Amount in Doc Currency  """  
      self.Box1eTaxableAmt:int = obj["Box1eTaxableAmt"]
      """  Box 1e Taxable Amount  """  
      self.Box2aDocTaxableAmt:int = obj["Box2aDocTaxableAmt"]
      """  Box 2a Taxable Amount in Doc Currency  """  
      self.Box2aDocTaxAmt:int = obj["Box2aDocTaxAmt"]
      """  Box 2a Tax Amount in Doc Currency  """  
      self.Box2aTaxableAmt:int = obj["Box2aTaxableAmt"]
      """  Box 2a Taxable Amount  """  
      self.Box2aTaxAmt:int = obj["Box2aTaxAmt"]
      """  Box 2a Tax Amount  """  
      self.Box3aDocTaxableAmt:int = obj["Box3aDocTaxableAmt"]
      """  Box 3a Taxable Amount in Doc Currency  """  
      self.Box3aTaxableAmt:int = obj["Box3aTaxableAmt"]
      """  Box 3a Taxable Amount  """  
      self.Box3bDocTaxableAmt:int = obj["Box3bDocTaxableAmt"]
      """  Box 3b Taxable Amount in Doc Currency  """  
      self.Box3bTaxableAmt:int = obj["Box3bTaxableAmt"]
      """  Box 3b Taxable Amount  """  
      self.Box3cDocTaxableAmt:int = obj["Box3cDocTaxableAmt"]
      """  Box 3c Taxable Amount in Doc Currency  """  
      self.Box3cTaxableAmt:int = obj["Box3cTaxableAmt"]
      """  Box 3c Taxable Amount  """  
      self.Box4aDocTaxableAmt:int = obj["Box4aDocTaxableAmt"]
      """  Box 4a Taxable Amount in Doc Currency  """  
      self.Box4aDocTaxAmt:int = obj["Box4aDocTaxAmt"]
      """  Box 4a Tax Amount in Doc Currency  """  
      self.Box4aTaxableAmt:int = obj["Box4aTaxableAmt"]
      """  Box 4a Taxable Amount  """  
      self.Box4aTaxAmt:int = obj["Box4aTaxAmt"]
      """  Box 4a Tax Amount  """  
      self.Box4bDocTaxableAmt:int = obj["Box4bDocTaxableAmt"]
      """  Box 4b Taxable Amount in Doc Currency  """  
      self.Box4bDocTaxAmt:int = obj["Box4bDocTaxAmt"]
      """  Box 4b Tax Amount in Doc Currency  """  
      self.Box4bTaxableAmt:int = obj["Box4bTaxableAmt"]
      """  Box 4b Taxable Amount  """  
      self.Box4bTaxAmt:int = obj["Box4bTaxAmt"]
      """  Box 4b Tax Amount  """  
      self.Box5aDocTaxAmt:int = obj["Box5aDocTaxAmt"]
      """  Box 5a Tax Amount in Doc Currency  """  
      self.Box5aTaxAmt:int = obj["Box5aTaxAmt"]
      """  Box 5a Tax Amount  """  
      self.Box5bDocTaxAmt:int = obj["Box5bDocTaxAmt"]
      """  Box 5b Tax Amount in Doc Currency  """  
      self.Box5bTaxAmt:int = obj["Box5bTaxAmt"]
      """  Box 5b Tax Amount  """  
      self.Box5cDocTaxAmt:int = obj["Box5cDocTaxAmt"]
      """  Box 5c Tax Amount in Doc Currency  """  
      self.Box5cTaxAmt:int = obj["Box5cTaxAmt"]
      """  Box 5c Tax Amount  """  
      self.Box5dDocTaxAmt:int = obj["Box5dDocTaxAmt"]
      """  Box 5d Tax Amount in Doc Currency  """  
      self.Box5dTaxAmt:int = obj["Box5dTaxAmt"]
      """  Box 5d Tax Amount  """  
      self.Box5eDocTaxAmt:int = obj["Box5eDocTaxAmt"]
      """  Box 5e Tax Amount in Doc Currency  """  
      self.Box5eTaxAmt:int = obj["Box5eTaxAmt"]
      """  Box 5e Tax Amount  """  
      self.Box5fDocTaxAmt:int = obj["Box5fDocTaxAmt"]
      """  Box 5f Tax Amount in Doc Currency  """  
      self.Box5fTaxAmt:int = obj["Box5fTaxAmt"]
      """  Box 5f Tax Amount  """  
      self.Box5gToPayDocTaxAmt:int = obj["Box5gToPayDocTaxAmt"]
      """  Box 5g To Pay Tax Amount in Doc Currency  """  
      self.Box5gToPayTaxAmt:int = obj["Box5gToPayTaxAmt"]
      """  Box 5g To Pay Tax Amount  """  
      self.Box5gToReclaimDocTaxAmt:int = obj["Box5gToReclaimDocTaxAmt"]
      """  Box 5g To Reclaim Tax Amount in Doc Currency  """  
      self.Box5gToReclaimTaxAmt:int = obj["Box5gToReclaimTaxAmt"]
      """  Box 5g To Reclaim Tax Amount  """  
      self.Box5gIsToPay:bool = obj["Box5gIsToPay"]
      """  Is To Pay  """  
      self.Box5gIsToReclaim:bool = obj["Box5gIsToReclaim"]
      """  Is To Reclaim  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_NLVATDeclarationListTableset:
   def __init__(self, obj):
      self.NLTaxReportDeclarationList:list[Erp_Tablesets_NLTaxReportDeclarationListRow] = obj["NLTaxReportDeclarationList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_NLVATDeclarationTableset:
   def __init__(self, obj):
      self.NLTaxReportDeclaration:list[Erp_Tablesets_NLTaxReportDeclarationRow] = obj["NLTaxReportDeclaration"]
      self.NLTaxReportDeclarationAttch:list[Erp_Tablesets_NLTaxReportDeclarationAttchRow] = obj["NLTaxReportDeclarationAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_UpdExtNLVATDeclarationTableset:
   def __init__(self, obj):
      self.NLTaxReportDeclaration:list[Erp_Tablesets_NLTaxReportDeclarationRow] = obj["NLTaxReportDeclaration"]
      self.NLTaxReportDeclarationAttch:list[Erp_Tablesets_NLTaxReportDeclarationAttchRow] = obj["NLTaxReportDeclarationAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenExportFile_input:
   """ Required : 
   declarationUID
   eftHeadUID
   exportFileName
   """  
   def __init__(self, obj):
      self.declarationUID:int = obj["declarationUID"]
      """  VAT Declaration ID  """  
      self.eftHeadUID:int = obj["eftHeadUID"]
      """  Electronic Interface ID  """  
      self.exportFileName:str = obj["exportFileName"]
      """  Export File Name  """  
      pass

class GenExportFile_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      """  Generated File Name  """  
      pass

   def parameters(self, obj):
      self.attachErrMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   declarationUID
   """  
   def __init__(self, obj):
      self.declarationUID:int = obj["declarationUID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_NLVATDeclarationListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewNLTaxReportDeclarationAttch_input:
   """ Required : 
   ds
   declarationUID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["ds"]
      self.declarationUID:int = obj["declarationUID"]
      pass

class GetNewNLTaxReportDeclarationAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewNLTaxReportDeclaration_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["ds"]
      pass

class GetNewNLTaxReportDeclaration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNextNewNLTaxReportDeclaration_input:
   """ Required : 
   vatReportID
   ds
   """  
   def __init__(self, obj):
      self.vatReportID:str = obj["vatReportID"]
      """  VAT Report ID  """  
      self.ds:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["ds"]
      pass

class GetNextNewNLTaxReportDeclaration_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseNLTaxReportDeclaration
   whereClauseNLTaxReportDeclarationAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseNLTaxReportDeclaration:str = obj["whereClauseNLTaxReportDeclaration"]
      self.whereClauseNLTaxReportDeclarationAttch:str = obj["whereClauseNLTaxReportDeclarationAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTaxBoxData_input:
   """ Required : 
   vatReportID
   ds
   """  
   def __init__(self, obj):
      self.vatReportID:str = obj["vatReportID"]
      """  VAT Report ID  """  
      self.ds:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["ds"]
      pass

class GetTaxBoxData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["ds"]
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

class ResetDeclarationStatus_input:
   """ Required : 
   declarationUID
   """  
   def __init__(self, obj):
      self.declarationUID:int = obj["declarationUID"]
      """  VAT Declaration ID  """  
      pass

class ResetDeclarationStatus_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.attachErrMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class SetStatusToSubmitted_input:
   """ Required : 
   declarationUID
   """  
   def __init__(self, obj):
      self.declarationUID:int = obj["declarationUID"]
      """  VAT Declaration ID  """  
      pass

class SetStatusToSubmitted_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtNLVATDeclarationTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtNLVATDeclarationTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_NLVATDeclarationTableset] = obj["ds"]
      pass

      """  output parameters  """  

