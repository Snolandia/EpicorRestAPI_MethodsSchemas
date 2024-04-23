import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.MXAPPaymentFolioImportSvc
# Description: 
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_MXAPPaymentFolioImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get MXAPPaymentFolioImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_MXAPPaymentFolioImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXAPPaymentFolioImportParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/MXAPPaymentFolioImports",headers=creds) as resp:
           return await resp.json()

async def post_MXAPPaymentFolioImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_MXAPPaymentFolioImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.MXAPPaymentFolioImportParamRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.MXAPPaymentFolioImportParamRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/MXAPPaymentFolioImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_MXAPPaymentFolioImports_Company_UserID(Company, UserID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the MXAPPaymentFolioImport item
   Description: Calls GetByID to retrieve the MXAPPaymentFolioImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_MXAPPaymentFolioImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.MXAPPaymentFolioImportParamRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/MXAPPaymentFolioImports(" + Company + "," + UserID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_MXAPPaymentFolioImports_Company_UserID(Company, UserID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update MXAPPaymentFolioImport for the service
   Description: Calls UpdateExt to update MXAPPaymentFolioImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_MXAPPaymentFolioImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.MXAPPaymentFolioImportParamRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/MXAPPaymentFolioImports(" + Company + "," + UserID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_MXAPPaymentFolioImports_Company_UserID(Company, UserID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete MXAPPaymentFolioImport item
   Description: Call UpdateExt to delete MXAPPaymentFolioImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_MXAPPaymentFolioImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param UserID: Desc: UserID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/MXAPPaymentFolioImports(" + Company + "," + UserID + ")",headers=creds) as resp:
           return await resp.json()

async def get_APPaymentFolioImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get APPaymentFolioImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_APPaymentFolioImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.APPaymentFolioImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/APPaymentFolioImports",headers=creds) as resp:
           return await resp.json()

async def post_APPaymentFolioImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_APPaymentFolioImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.APPaymentFolioImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.APPaymentFolioImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/APPaymentFolioImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_APPaymentFolioImports_FileName_HeadNum(FileName, HeadNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the APPaymentFolioImport item
   Description: Calls GetByID to retrieve the APPaymentFolioImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_APPaymentFolioImport
      :param FileName: Desc: FileName   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.APPaymentFolioImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/APPaymentFolioImports(" + FileName + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_APPaymentFolioImports_FileName_HeadNum(FileName, HeadNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update APPaymentFolioImport for the service
   Description: Calls UpdateExt to update APPaymentFolioImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_APPaymentFolioImport
      :param FileName: Desc: FileName   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.APPaymentFolioImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/APPaymentFolioImports(" + FileName + "," + HeadNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_APPaymentFolioImports_FileName_HeadNum(FileName, HeadNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete APPaymentFolioImport item
   Description: Call UpdateExt to delete APPaymentFolioImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_APPaymentFolioImport
      :param FileName: Desc: FileName   Required: True   Allow empty value : True
      :param HeadNum: Desc: HeadNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/APPaymentFolioImports(" + FileName + "," + HeadNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PaymentXmlFiles(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PaymentXmlFiles items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PaymentXmlFiles
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PaymentXmlFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/PaymentXmlFiles",headers=creds) as resp:
           return await resp.json()

async def post_PaymentXmlFiles(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PaymentXmlFiles
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PaymentXmlFileRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PaymentXmlFileRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/PaymentXmlFiles", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PaymentXmlFiles_FileName(FileName, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PaymentXmlFile item
   Description: Calls GetByID to retrieve the PaymentXmlFile item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PaymentXmlFile
      :param FileName: Desc: FileName   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PaymentXmlFileRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/PaymentXmlFiles(" + FileName + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PaymentXmlFiles_FileName(FileName, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PaymentXmlFile for the service
   Description: Calls UpdateExt to update PaymentXmlFile. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PaymentXmlFile
      :param FileName: Desc: FileName   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PaymentXmlFileRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/PaymentXmlFiles(" + FileName + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PaymentXmlFiles_FileName(FileName, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PaymentXmlFile item
   Description: Call UpdateExt to delete PaymentXmlFile item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PaymentXmlFile
      :param FileName: Desc: FileName   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/PaymentXmlFiles(" + FileName + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.MXAPPaymentFolioImportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseMXAPPaymentFolioImportParam, whereClauseAPPaymentFolioImport, whereClausePaymentXmlFile, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseMXAPPaymentFolioImportParam=" + whereClauseMXAPPaymentFolioImportParam
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAPPaymentFolioImport=" + whereClauseAPPaymentFolioImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePaymentXmlFile=" + whereClausePaymentXmlFile
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, userID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "company=" + company
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "userID=" + userID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNewParameters(epicorHeaders = None):
   """  
   Summary: Invoke method GetNewParameters
   Description: Get default parameters for current user.
   OperationID: GetNewParameters
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewParameters_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaults
   Description: Get default parameters for current user.
   OperationID: GetDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SaveDefaults(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SaveDefaults
   Description: Save default parameters for current user.
   OperationID: SaveDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SaveDefaults_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SaveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveDefaults(epicorHeaders = None):
   """  
   Summary: Invoke method RemoveDefaults
   Description: Remove default parameters for current user.
   OperationID: RemoveDefaults
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveDefaults_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ParseXmls(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ParseXmls
   Description: Parses XMLs in order to retrieve Fiscal Folio and auto map them to AP Payments
   OperationID: ParseXmls
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseXmls_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseXmls_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ParseXmlsInStr(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ParseXmlsInStr
   Description: Parses XMLs in order to retrieve Fiscal Folio and auto map them to AP Payments
   OperationID: ParseXmlsInStr
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ParseXmlsInStr_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ParseXmlsInStr_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnMatchedChanged(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnMatchedChanged
   Description: Match or unmatch xml and payment
   OperationID: OnMatchedChanged
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnMatchedChanged_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnMatchedChanged_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnMatchedChanged_Ref(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnMatchedChanged_Ref
   Description: Match or unmatch xml and payment
   OperationID: OnMatchedChanged_Ref
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnMatchedChanged_Ref_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnMatchedChanged_Ref_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateFiscalFolio(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UpdateFiscalFolio
   Description: Finally updates Fiscal Folio on all matched payments
   OperationID: UpdateFiscalFolio
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UpdateFiscalFolio_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateFiscalFolio_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.MXAPPaymentFolioImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_APPaymentFolioImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_APPaymentFolioImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXAPPaymentFolioImportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MXAPPaymentFolioImportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_MXAPPaymentFolioImportParamRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_MXAPPaymentFolioImportParamRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PaymentXmlFileRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PaymentXmlFileRow] = obj["value"]
      pass

class Erp_Tablesets_APPaymentFolioImportRow:
   def __init__(self, obj):
      self.CheckAmt:int = obj["CheckAmt"]
      self.CheckDate:str = obj["CheckDate"]
      self.CheckNum:int = obj["CheckNum"]
      self.FileName:str = obj["FileName"]
      """  Xml File Name  """  
      self.FiscalFolio:str = obj["FiscalFolio"]
      """  Fiscal Folio  """  
      self.HeadNum:int = obj["HeadNum"]
      self.PayMethod:str = obj["PayMethod"]
      self.SupplierTaxId:str = obj["SupplierTaxId"]
      """  Supplier Tax ID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXAPPaymentFolioImportListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXAPPaymentFolioImportParamRow:
   def __init__(self, obj):
      self.CheckAmtXPath:str = obj["CheckAmtXPath"]
      """  XPath to Check Amount field  """  
      self.CheckNumXPath:str = obj["CheckNumXPath"]
      """  XPath to Check Number field  """  
      self.FiscalFolioXPath:str = obj["FiscalFolioXPath"]
      """  XPath to Fiscal Folio field  """  
      self.PayDateXPath:str = obj["PayDateXPath"]
      """  XPath to Payment Date field  """  
      self.PayMethodXPath:str = obj["PayMethodXPath"]
      """  XPath to Payment Method field  """  
      self.SupTaxIdXPath:str = obj["SupTaxIdXPath"]
      """  XPath to Supplier Tax ID field  """  
      self.PayMethodIsUsed:bool = obj["PayMethodIsUsed"]
      """  Enable/disable Payment Method field value for additional search with manual matching  """  
      self.PayDateIsUsed:bool = obj["PayDateIsUsed"]
      """  Enable/disable Payment Date field value for additional search with manual matching  """  
      self.CheckAmtIsUsed:bool = obj["CheckAmtIsUsed"]
      """  Enable/disable Check Amount field value for additional search with manual matching  """  
      self.CheckNumIsUsed:bool = obj["CheckNumIsUsed"]
      """  Enable/disable Check Number field value for additional search with manual matching  """  
      self.Company:str = obj["Company"]
      self.UserID:str = obj["UserID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PaymentXmlFileRow:
   def __init__(self, obj):
      self.CheckAmt:int = obj["CheckAmt"]
      self.CheckDate:str = obj["CheckDate"]
      self.CheckNum:int = obj["CheckNum"]
      self.ErrorMessage:str = obj["ErrorMessage"]
      """  Error Message  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.FiscalFolio:str = obj["FiscalFolio"]
      """  Fiscal Folio  """  
      self.HeadNum:int = obj["HeadNum"]
      self.IsMatched:bool = obj["IsMatched"]
      """  Is file matched with invoice  """  
      self.PayMethod:str = obj["PayMethod"]
      self.SupplierTaxId:str = obj["SupplierTaxId"]
      """  Supplier Tax ID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class Erp_Tablesets_APPaymentFolioImportRow:
   def __init__(self, obj):
      self.CheckAmt:int = obj["CheckAmt"]
      self.CheckDate:str = obj["CheckDate"]
      self.CheckNum:int = obj["CheckNum"]
      self.FileName:str = obj["FileName"]
      """  Xml File Name  """  
      self.FiscalFolio:str = obj["FiscalFolio"]
      """  Fiscal Folio  """  
      self.HeadNum:int = obj["HeadNum"]
      self.PayMethod:str = obj["PayMethod"]
      self.SupplierTaxId:str = obj["SupplierTaxId"]
      """  Supplier Tax ID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXAPPaymentFolioImportListRow:
   def __init__(self, obj):
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXAPPaymentFolioImportListTableset:
   def __init__(self, obj):
      self.MXAPPaymentFolioImportList:list[Erp_Tablesets_MXAPPaymentFolioImportListRow] = obj["MXAPPaymentFolioImportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_MXAPPaymentFolioImportParamRow:
   def __init__(self, obj):
      self.CheckAmtXPath:str = obj["CheckAmtXPath"]
      """  XPath to Check Amount field  """  
      self.CheckNumXPath:str = obj["CheckNumXPath"]
      """  XPath to Check Number field  """  
      self.FiscalFolioXPath:str = obj["FiscalFolioXPath"]
      """  XPath to Fiscal Folio field  """  
      self.PayDateXPath:str = obj["PayDateXPath"]
      """  XPath to Payment Date field  """  
      self.PayMethodXPath:str = obj["PayMethodXPath"]
      """  XPath to Payment Method field  """  
      self.SupTaxIdXPath:str = obj["SupTaxIdXPath"]
      """  XPath to Supplier Tax ID field  """  
      self.PayMethodIsUsed:bool = obj["PayMethodIsUsed"]
      """  Enable/disable Payment Method field value for additional search with manual matching  """  
      self.PayDateIsUsed:bool = obj["PayDateIsUsed"]
      """  Enable/disable Payment Date field value for additional search with manual matching  """  
      self.CheckAmtIsUsed:bool = obj["CheckAmtIsUsed"]
      """  Enable/disable Check Amount field value for additional search with manual matching  """  
      self.CheckNumIsUsed:bool = obj["CheckNumIsUsed"]
      """  Enable/disable Check Number field value for additional search with manual matching  """  
      self.Company:str = obj["Company"]
      self.UserID:str = obj["UserID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_MXAPPaymentFolioImportTableset:
   def __init__(self, obj):
      self.MXAPPaymentFolioImportParam:list[Erp_Tablesets_MXAPPaymentFolioImportParamRow] = obj["MXAPPaymentFolioImportParam"]
      self.APPaymentFolioImport:list[Erp_Tablesets_APPaymentFolioImportRow] = obj["APPaymentFolioImport"]
      self.PaymentXmlFile:list[Erp_Tablesets_PaymentXmlFileRow] = obj["PaymentXmlFile"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PaymentXmlFileRow:
   def __init__(self, obj):
      self.CheckAmt:int = obj["CheckAmt"]
      self.CheckDate:str = obj["CheckDate"]
      self.CheckNum:int = obj["CheckNum"]
      self.ErrorMessage:str = obj["ErrorMessage"]
      """  Error Message  """  
      self.FileName:str = obj["FileName"]
      """  File Name  """  
      self.FiscalFolio:str = obj["FiscalFolio"]
      """  Fiscal Folio  """  
      self.HeadNum:int = obj["HeadNum"]
      self.IsMatched:bool = obj["IsMatched"]
      """  Is file matched with invoice  """  
      self.PayMethod:str = obj["PayMethod"]
      self.SupplierTaxId:str = obj["SupplierTaxId"]
      """  Supplier Tax ID  """  
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtMXAPPaymentFolioImportTableset:
   def __init__(self, obj):
      self.MXAPPaymentFolioImportParam:list[Erp_Tablesets_MXAPPaymentFolioImportParamRow] = obj["MXAPPaymentFolioImportParam"]
      self.APPaymentFolioImport:list[Erp_Tablesets_APPaymentFolioImportRow] = obj["APPaymentFolioImport"]
      self.PaymentXmlFile:list[Erp_Tablesets_PaymentXmlFileRow] = obj["PaymentXmlFile"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   company
   userID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.userID:str = obj["userID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["returnObj"]
      pass

class GetDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      pass

class GetDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

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
      self.returnObj:list[Erp_Tablesets_MXAPPaymentFolioImportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewParameters_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["returnObj"]
      pass

class GetRows_input:
   """ Required : 
   whereClauseMXAPPaymentFolioImportParam
   whereClauseAPPaymentFolioImport
   whereClausePaymentXmlFile
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseMXAPPaymentFolioImportParam:str = obj["whereClauseMXAPPaymentFolioImportParam"]
      self.whereClauseAPPaymentFolioImport:str = obj["whereClauseAPPaymentFolioImport"]
      self.whereClausePaymentXmlFile:str = obj["whereClausePaymentXmlFile"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["returnObj"]
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

class OnMatchedChanged_Ref_input:
   """ Required : 
   ds
   newIsMatched
   filename
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      self.newIsMatched:bool = obj["newIsMatched"]
      self.filename:str = obj["filename"]
      pass

class OnMatchedChanged_Ref_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnMatchedChanged_input:
   """ Required : 
   ds
   newIsMatched
   filename
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      self.newIsMatched:bool = obj["newIsMatched"]
      self.filename:str = obj["filename"]
      pass

class OnMatchedChanged_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["returnObj"]
      pass

class ParseXmlsInStr_input:
   """ Required : 
   ds
   filenames
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      self.filenames:str = obj["filenames"]
      """  list of filename, delimited by '|'  """  
      pass

class ParseXmlsInStr_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ParseXmls_input:
   """ Required : 
   ds
   filenames
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      self.filenames:str = obj["filenames"]
      """  array of filenames  """  
      pass

class ParseXmls_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["returnObj"]
      pass

class RemoveDefaults_output:
   def __init__(self, obj):
      pass

class SaveDefaults_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      pass

class SaveDefaults_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMXAPPaymentFolioImportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtMXAPPaymentFolioImportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class UpdateFiscalFolio_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      pass

class UpdateFiscalFolio_output:
   def __init__(self, obj):
      self.returnObj:int = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_MXAPPaymentFolioImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

