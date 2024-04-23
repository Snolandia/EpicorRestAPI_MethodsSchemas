import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.CustContImportSvc
# Description: Purpose:
Parameters:  none
Notes:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_CustContImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustContImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustContImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustomerImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustContImports",headers=creds) as resp:
           return await resp.json()

async def post_CustContImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustContImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustomerImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustomerImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustContImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustContImports_Company_ImportID(Company, ImportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustContImport item
   Description: Calls GetByID to retrieve the CustContImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustContImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustomerImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustContImports(" + Company + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustContImports_Company_ImportID(Company, ImportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustContImport for the service
   Description: Calls UpdateExt to update CustContImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustContImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustomerImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustContImports(" + Company + "," + ImportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustContImports_Company_ImportID(Company, ImportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustContImport item
   Description: Call UpdateExt to delete CustContImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustContImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustContImports(" + Company + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustContImports_Company_ImportID_CustCntImports(Company, ImportID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CustCntImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CustCntImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustContImports(" + Company + "," + ImportID + ")/CustCntImports",headers=creds) as resp:
           return await resp.json()

async def get_CustContImports_Company_ImportID_CustCntImports_Company_ParentImportID_ImportID(Company, ImportID, ParentImportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustCntImport item
   Description: Calls GetByID to retrieve the CustCntImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCntImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param ParentImportID: Desc: ParentImportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustCntImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustContImports(" + Company + "," + ImportID + ")/CustCntImports(" + Company + "," + ParentImportID + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustContImports_Company_ImportID_CustomerImportAttches(Company, ImportID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CustomerImportAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CustomerImportAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustomerImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustContImports(" + Company + "," + ImportID + ")/CustomerImportAttches",headers=creds) as resp:
           return await resp.json()

async def get_CustContImports_Company_ImportID_CustomerImportAttches_Company_ImportID_DrawingSeq(Company, ImportID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustomerImportAttch item
   Description: Calls GetByID to retrieve the CustomerImportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustomerImportAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustomerImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustContImports(" + Company + "," + ImportID + ")/CustomerImportAttches(" + Company + "," + ImportID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustCntImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustCntImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustCntImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImports",headers=creds) as resp:
           return await resp.json()

async def post_CustCntImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustCntImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustCntImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustCntImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustCntImports_Company_ParentImportID_ImportID(Company, ParentImportID, ImportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustCntImport item
   Description: Calls GetByID to retrieve the CustCntImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCntImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ParentImportID: Desc: ParentImportID   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustCntImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImports(" + Company + "," + ParentImportID + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustCntImports_Company_ParentImportID_ImportID(Company, ParentImportID, ImportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustCntImport for the service
   Description: Calls UpdateExt to update CustCntImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustCntImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ParentImportID: Desc: ParentImportID   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustCntImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImports(" + Company + "," + ParentImportID + "," + ImportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustCntImports_Company_ParentImportID_ImportID(Company, ParentImportID, ImportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustCntImport item
   Description: Call UpdateExt to delete CustCntImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustCntImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ParentImportID: Desc: ParentImportID   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImports(" + Company + "," + ParentImportID + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustCntImports_Company_ParentImportID_ImportID_CustCntImportAttches(Company, ParentImportID, ImportID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get CustCntImportAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_CustCntImportAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ParentImportID: Desc: ParentImportID   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImports(" + Company + "," + ParentImportID + "," + ImportID + ")/CustCntImportAttches",headers=creds) as resp:
           return await resp.json()

async def get_CustCntImports_Company_ParentImportID_ImportID_CustCntImportAttches_Company_ParentImportID_ImportID_DrawingSeq(Company, ParentImportID, ImportID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustCntImportAttch item
   Description: Calls GetByID to retrieve the CustCntImportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCntImportAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ParentImportID: Desc: ParentImportID   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustCntImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImports(" + Company + "," + ParentImportID + "," + ImportID + ")/CustCntImportAttches(" + Company + "," + ParentImportID + "," + ImportID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustCntImportAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustCntImportAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustCntImportAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustCntImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImportAttches",headers=creds) as resp:
           return await resp.json()

async def post_CustCntImportAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustCntImportAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustCntImportAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustCntImportAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImportAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustCntImportAttches_Company_ParentImportID_ImportID_DrawingSeq(Company, ParentImportID, ImportID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustCntImportAttch item
   Description: Calls GetByID to retrieve the CustCntImportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustCntImportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ParentImportID: Desc: ParentImportID   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustCntImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImportAttches(" + Company + "," + ParentImportID + "," + ImportID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustCntImportAttches_Company_ParentImportID_ImportID_DrawingSeq(Company, ParentImportID, ImportID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustCntImportAttch for the service
   Description: Calls UpdateExt to update CustCntImportAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustCntImportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ParentImportID: Desc: ParentImportID   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustCntImportAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImportAttches(" + Company + "," + ParentImportID + "," + ImportID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustCntImportAttches_Company_ParentImportID_ImportID_DrawingSeq(Company, ParentImportID, ImportID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustCntImportAttch item
   Description: Call UpdateExt to delete CustCntImportAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustCntImportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ParentImportID: Desc: ParentImportID   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustCntImportAttches(" + Company + "," + ParentImportID + "," + ImportID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_CustomerImportAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get CustomerImportAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_CustomerImportAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustomerImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustomerImportAttches",headers=creds) as resp:
           return await resp.json()

async def post_CustomerImportAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_CustomerImportAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.CustomerImportAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.CustomerImportAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustomerImportAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_CustomerImportAttches_Company_ImportID_DrawingSeq(Company, ImportID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the CustomerImportAttch item
   Description: Calls GetByID to retrieve the CustomerImportAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_CustomerImportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.CustomerImportAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustomerImportAttches(" + Company + "," + ImportID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_CustomerImportAttches_Company_ImportID_DrawingSeq(Company, ImportID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update CustomerImportAttch for the service
   Description: Calls UpdateExt to update CustomerImportAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_CustomerImportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.CustomerImportAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustomerImportAttches(" + Company + "," + ImportID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_CustomerImportAttches_Company_ImportID_DrawingSeq(Company, ImportID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete CustomerImportAttch item
   Description: Call UpdateExt to delete CustomerImportAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_CustomerImportAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/CustomerImportAttches(" + Company + "," + ImportID + "," + DrawingSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.CustomerImportListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseCustomerImport, whereClauseCustomerImportAttch, whereClauseCustCntImport, whereClauseCustCntImportAttch, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
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
   params += "whereClauseCustomerImport=" + whereClauseCustomerImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCustomerImportAttch=" + whereClauseCustomerImportAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCustCntImport=" + whereClauseCustCntImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseCustCntImportAttch=" + whereClauseCustCntImportAttch
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(importID, epicorHeaders = None):
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
   params += "importID=" + importID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_AutoMatch(epicorHeaders = None):
   """  
   Summary: Invoke method AutoMatch
   Description: Method to call to auto match import customers to existing customers.
   OperationID: AutoMatch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/AutoMatch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ChangeRoleCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRoleCode
   Description: Method to call when changing the role code on an imported customer contact record.  Validates the
role code and updates the role code description with the new value.
   OperationID: ChangeRoleCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRoleCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRoleCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeSalesRepCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeSalesRepCode
   Description: Method to call when changing the sales rep code on an imported customer record.  Validates the
sales rep code and updates the Sales Rep Name with the new value.
   OperationID: ChangeSalesRepCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeSalesRepCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeSalesRepCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTerritoryID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTerritoryID
   Description: Method to call when changing the territory id on an imported customer record.  Validates the
territory id and updates the territory description with the new value.
   OperationID: ChangeTerritoryID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTerritoryID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTerritoryID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DeleteAll(epicorHeaders = None):
   """  
   Summary: Invoke method DeleteAll
   Description: Method to call delete all CustomerImport and CustCntImport records.  The CustContImport
dataset should be cleared by the app that called this method after this method is run
because the records in the dataset will be obsolete.
   OperationID: DeleteAll
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/DeleteAll_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetExistingCustomers(epicorHeaders = None):
   """  
   Summary: Invoke method GetExistingCustomers
   Description: Method to call to retrieve the existing Customers and Customer contacts.
   OperationID: GetExistingCustomers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetExistingCustomers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ImportCustomersAndContacts(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportCustomersAndContacts
   Description: Method to call to import customers and contacts from a datatable.
   OperationID: ImportCustomersAndContacts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportCustomersAndContacts_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportCustomersAndContacts_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchImpCustCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchImpCustCnt
   Description: Method to call to match an import customer contact to an existing customer contact.
   OperationID: MatchImpCustCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchImpCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchImpCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_MatchImpCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method MatchImpCustomer
   Description: Method to call to match an import customer to an existing customer.
   OperationID: MatchImpCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/MatchImpCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/MatchImpCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnmatchImpCustCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnmatchImpCustCnt
   Description: Method to call to unmatch an import customer contact from an existing customer contact.
   OperationID: UnmatchImpCustCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnmatchImpCustCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchImpCustCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnmatchImpCustomer(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnmatchImpCustomer
   Description: Method to call to unmatch an import customer from an existing customer.
   OperationID: UnmatchImpCustomer
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnmatchImpCustomer_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnmatchImpCustomer_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UpdateCustomers(epicorHeaders = None):
   """  
   Summary: Invoke method UpdateCustomers
   Description: Method to call update existing Customers with data from the imported Customers.
   OperationID: UpdateCustomers
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/UpdateCustomers_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_ImportFileFromWeb(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportFileFromWeb
   Description: Imports Customers\Contacts with the .CSV file uploaded through the web into a special folder.
   OperationID: ImportFileFromWeb
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportFileFromWeb_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportFileFromWeb_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustomerImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustomerImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustomerImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustomerImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustomerImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustomerImportAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustomerImportAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustomerImportAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustomerImportAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustomerImportAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustCntImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustCntImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustCntImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustCntImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustCntImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewCustCntImportAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewCustCntImportAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewCustCntImportAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewCustCntImportAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewCustCntImportAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.CustContImportSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntImportAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustCntImportAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustCntImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustCntImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustomerImportAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustomerImportAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustomerImportListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustomerImportListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_CustomerImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_CustomerImportRow] = obj["value"]
      pass

class Erp_Tablesets_CustCntImportAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ParentImportID:int = obj["ParentImportID"]
      self.ImportID:int = obj["ImportID"]
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

class Erp_Tablesets_CustCntImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ParentImportID:int = obj["ParentImportID"]
      self.ImportID:int = obj["ImportID"]
      self.CustNum:int = obj["CustNum"]
      self.ConNum:int = obj["ConNum"]
      self.Name:str = obj["Name"]
      self.Func:str = obj["Func"]
      self.FaxNum:str = obj["FaxNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.SpecialAddress:bool = obj["SpecialAddress"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      self.CorpName:str = obj["CorpName"]
      self.EMailAddress:str = obj["EMailAddress"]
      self.CountryNum:int = obj["CountryNum"]
      self.RoleCode:str = obj["RoleCode"]
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      self.PagerNum:str = obj["PagerNum"]
      self.HomeNum:str = obj["HomeNum"]
      self.AltNum:str = obj["AltNum"]
      self.ContactTitle:str = obj["ContactTitle"]
      self.NoContact:bool = obj["NoContact"]
      self.MatchedCustNum:int = obj["MatchedCustNum"]
      self.MatchedConNum:int = obj["MatchedConNum"]
      self.MatchedFlag:str = obj["MatchedFlag"]
      self.FirstName:str = obj["FirstName"]
      self.MiddleName:str = obj["MiddleName"]
      self.LastName:str = obj["LastName"]
      self.Prefix:str = obj["Prefix"]
      self.Suffix:str = obj["Suffix"]
      self.Initials:str = obj["Initials"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispMatchedFlag:str = obj["DispMatchedFlag"]
      self.BitFlag:int = obj["BitFlag"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustomerImportAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ImportID:int = obj["ImportID"]
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

class Erp_Tablesets_CustomerImportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ImportID:int = obj["ImportID"]
      self.CustID:str = obj["CustID"]
      self.CustNum:int = obj["CustNum"]
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.TerritoryID:str = obj["TerritoryID"]
      self.FaxNum:str = obj["FaxNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.EMailAddress:str = obj["EMailAddress"]
      self.CustomerType:str = obj["CustomerType"]
      self.NoContact:bool = obj["NoContact"]
      self.CustURL:str = obj["CustURL"]
      self.ExtID:str = obj["ExtID"]
      self.MatchedCustNum:int = obj["MatchedCustNum"]
      self.MatchedFlag:str = obj["MatchedFlag"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      self.DispMatchedFlag:str = obj["DispMatchedFlag"]
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name  """  
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      """  Description of the territory.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustomerImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ImportID:int = obj["ImportID"]
      self.CustID:str = obj["CustID"]
      self.CustNum:int = obj["CustNum"]
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.TerritoryID:str = obj["TerritoryID"]
      self.FaxNum:str = obj["FaxNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.EMailAddress:str = obj["EMailAddress"]
      self.CustomerType:str = obj["CustomerType"]
      self.NoContact:bool = obj["NoContact"]
      self.CustURL:str = obj["CustURL"]
      self.ExtID:str = obj["ExtID"]
      self.MatchedCustNum:int = obj["MatchedCustNum"]
      self.MatchedFlag:str = obj["MatchedFlag"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      self.DispMatchedFlag:str = obj["DispMatchedFlag"]
      self.BitFlag:int = obj["BitFlag"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AutoMatch_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustContImportTableset] = obj["returnObj"]
      pass

class ChangeRoleCode_input:
   """ Required : 
   ProposedRoleCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedRoleCode:str = obj["ProposedRoleCode"]
      """  The proposed role code  """  
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

class ChangeRoleCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeSalesRepCode_input:
   """ Required : 
   ProposedSalesRepCode
   ds
   """  
   def __init__(self, obj):
      self.ProposedSalesRepCode:str = obj["ProposedSalesRepCode"]
      """  The proposed sales rep code  """  
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

class ChangeSalesRepCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTerritoryID_input:
   """ Required : 
   ProposedTerritoryID
   ds
   """  
   def __init__(self, obj):
      self.ProposedTerritoryID:str = obj["ProposedTerritoryID"]
      """  The proposed sales rep code  """  
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

class ChangeTerritoryID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteAll_output:
   def __init__(self, obj):
      pass

class DeleteByID_input:
   """ Required : 
   importID
   """  
   def __init__(self, obj):
      self.importID:int = obj["importID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_CustCntImportAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ParentImportID:int = obj["ParentImportID"]
      self.ImportID:int = obj["ImportID"]
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

class Erp_Tablesets_CustCntImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ParentImportID:int = obj["ParentImportID"]
      self.ImportID:int = obj["ImportID"]
      self.CustNum:int = obj["CustNum"]
      self.ConNum:int = obj["ConNum"]
      self.Name:str = obj["Name"]
      self.Func:str = obj["Func"]
      self.FaxNum:str = obj["FaxNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.SpecialAddress:bool = obj["SpecialAddress"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      self.CorpName:str = obj["CorpName"]
      self.EMailAddress:str = obj["EMailAddress"]
      self.CountryNum:int = obj["CountryNum"]
      self.RoleCode:str = obj["RoleCode"]
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      self.PagerNum:str = obj["PagerNum"]
      self.HomeNum:str = obj["HomeNum"]
      self.AltNum:str = obj["AltNum"]
      self.ContactTitle:str = obj["ContactTitle"]
      self.NoContact:bool = obj["NoContact"]
      self.MatchedCustNum:int = obj["MatchedCustNum"]
      self.MatchedConNum:int = obj["MatchedConNum"]
      self.MatchedFlag:str = obj["MatchedFlag"]
      self.FirstName:str = obj["FirstName"]
      self.MiddleName:str = obj["MiddleName"]
      self.LastName:str = obj["LastName"]
      self.Prefix:str = obj["Prefix"]
      self.Suffix:str = obj["Suffix"]
      self.Initials:str = obj["Initials"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.DispMatchedFlag:str = obj["DispMatchedFlag"]
      self.BitFlag:int = obj["BitFlag"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustContExistingTableset:
   def __init__(self, obj):
      self.ImpCustomerExisting:list[Erp_Tablesets_ImpCustomerExistingRow] = obj["ImpCustomerExisting"]
      self.ImpCustCntExisting:list[Erp_Tablesets_ImpCustCntExistingRow] = obj["ImpCustCntExisting"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustContImportExportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.CustCustID:str = obj["CustCustID"]
      self.CustName:str = obj["CustName"]
      self.CustAddress1:str = obj["CustAddress1"]
      self.CustAddress2:str = obj["CustAddress2"]
      self.CustAddress3:str = obj["CustAddress3"]
      self.CustCity:str = obj["CustCity"]
      self.CustState:str = obj["CustState"]
      self.CustZip:str = obj["CustZip"]
      self.CustCountry:str = obj["CustCountry"]
      self.CustSalesRepCode:str = obj["CustSalesRepCode"]
      self.CustTerritoryID:str = obj["CustTerritoryID"]
      self.CustFaxNum:str = obj["CustFaxNum"]
      self.CustPhoneNum:str = obj["CustPhoneNum"]
      self.CustNoContact:int = obj["CustNoContact"]
      self.CustEMailAddress:str = obj["CustEMailAddress"]
      self.CustCustomerType:str = obj["CustCustomerType"]
      self.CustCustURL:str = obj["CustCustURL"]
      self.CustExtID:str = obj["CustExtID"]
      self.CustCharacter01:str = obj["CustCharacter01"]
      self.CustCharacter02:str = obj["CustCharacter02"]
      self.CustCharacter03:str = obj["CustCharacter03"]
      self.CustCharacter04:str = obj["CustCharacter04"]
      self.CustCharacter05:str = obj["CustCharacter05"]
      self.CustCharacter06:str = obj["CustCharacter06"]
      self.CustCharacter07:str = obj["CustCharacter07"]
      self.CustCharacter08:str = obj["CustCharacter08"]
      self.CustCharacter09:str = obj["CustCharacter09"]
      self.CustCharacter10:str = obj["CustCharacter10"]
      self.CustNumber01:int = obj["CustNumber01"]
      self.CustNumber02:int = obj["CustNumber02"]
      self.CustNumber03:int = obj["CustNumber03"]
      self.CustNumber04:int = obj["CustNumber04"]
      self.CustNumber05:int = obj["CustNumber05"]
      self.CustNumber06:int = obj["CustNumber06"]
      self.CustNumber07:int = obj["CustNumber07"]
      self.CustNumber08:int = obj["CustNumber08"]
      self.CustNumber09:int = obj["CustNumber09"]
      self.CustNumber10:int = obj["CustNumber10"]
      self.CustDate01:str = obj["CustDate01"]
      self.CustDate02:str = obj["CustDate02"]
      self.CustDate03:str = obj["CustDate03"]
      self.CustDate04:str = obj["CustDate04"]
      self.CustDate05:str = obj["CustDate05"]
      self.CustCheckBox01:int = obj["CustCheckBox01"]
      self.CustCheckBox02:int = obj["CustCheckBox02"]
      self.CustCheckBox03:int = obj["CustCheckBox03"]
      self.CustCheckBox04:int = obj["CustCheckBox04"]
      self.CustCheckBox05:int = obj["CustCheckBox05"]
      self.ContName:str = obj["ContName"]
      self.ContPrefix:str = obj["ContPrefix"]
      self.ContInitials:str = obj["ContInitials"]
      self.ContFirstName:str = obj["ContFirstName"]
      self.ContMiddleName:str = obj["ContMiddleName"]
      self.ContLastName:str = obj["ContLastName"]
      self.ContSuffix:str = obj["ContSuffix"]
      self.ContFunc:str = obj["ContFunc"]
      self.ContSpecialAddress:int = obj["ContSpecialAddress"]
      self.ContAddress1:str = obj["ContAddress1"]
      self.ContAddress2:str = obj["ContAddress2"]
      self.ContAddress3:str = obj["ContAddress3"]
      self.ContCity:str = obj["ContCity"]
      self.ContState:str = obj["ContState"]
      self.ContZip:str = obj["ContZip"]
      self.ContCountry:str = obj["ContCountry"]
      self.ContFaxNum:str = obj["ContFaxNum"]
      self.ContPhoneNum:str = obj["ContPhoneNum"]
      self.ContCorpName:str = obj["ContCorpName"]
      self.ContEMailAddress:str = obj["ContEMailAddress"]
      self.ContRoleCode:str = obj["ContRoleCode"]
      self.ContCellPhoneNum:str = obj["ContCellPhoneNum"]
      self.ContPagerNum:str = obj["ContPagerNum"]
      self.ContHomeNum:str = obj["ContHomeNum"]
      self.ContAltNum:str = obj["ContAltNum"]
      self.ContContactTitle:str = obj["ContContactTitle"]
      self.ContNoContact:int = obj["ContNoContact"]
      self.ContCharacter01:str = obj["ContCharacter01"]
      self.ContCharacter02:str = obj["ContCharacter02"]
      self.ContCharacter03:str = obj["ContCharacter03"]
      self.ContCharacter04:str = obj["ContCharacter04"]
      self.ContCharacter05:str = obj["ContCharacter05"]
      self.ContCharacter06:str = obj["ContCharacter06"]
      self.ContCharacter07:str = obj["ContCharacter07"]
      self.ContCharacter08:str = obj["ContCharacter08"]
      self.ContCharacter09:str = obj["ContCharacter09"]
      self.ContCharacter10:str = obj["ContCharacter10"]
      self.ContNumber01:int = obj["ContNumber01"]
      self.ContNumber02:int = obj["ContNumber02"]
      self.ContNumber03:int = obj["ContNumber03"]
      self.ContNumber04:int = obj["ContNumber04"]
      self.ContNumber05:int = obj["ContNumber05"]
      self.ContNumber06:int = obj["ContNumber06"]
      self.ContNumber07:int = obj["ContNumber07"]
      self.ContNumber08:int = obj["ContNumber08"]
      self.ContNumber09:int = obj["ContNumber09"]
      self.ContNumber10:int = obj["ContNumber10"]
      self.ContDate01:str = obj["ContDate01"]
      self.ContDate02:str = obj["ContDate02"]
      self.ContDate03:str = obj["ContDate03"]
      self.ContDate04:str = obj["ContDate04"]
      self.ContDate05:str = obj["ContDate05"]
      self.ContCheckBox01:int = obj["ContCheckBox01"]
      self.ContCheckBox02:int = obj["ContCheckBox02"]
      self.ContCheckBox03:int = obj["ContCheckBox03"]
      self.ContCheckBox04:int = obj["ContCheckBox04"]
      self.ContCheckBox05:int = obj["ContCheckBox05"]
      self.ImportErrorMsg:str = obj["ImportErrorMsg"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustContImportExportTableset:
   def __init__(self, obj):
      self.CustContImportExport:list[Erp_Tablesets_CustContImportExportRow] = obj["CustContImportExport"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustContImportTableset:
   def __init__(self, obj):
      self.CustomerImport:list[Erp_Tablesets_CustomerImportRow] = obj["CustomerImport"]
      self.CustomerImportAttch:list[Erp_Tablesets_CustomerImportAttchRow] = obj["CustomerImportAttch"]
      self.CustCntImport:list[Erp_Tablesets_CustCntImportRow] = obj["CustCntImport"]
      self.CustCntImportAttch:list[Erp_Tablesets_CustCntImportAttchRow] = obj["CustCntImportAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustomerImportAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ImportID:int = obj["ImportID"]
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

class Erp_Tablesets_CustomerImportListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ImportID:int = obj["ImportID"]
      self.CustID:str = obj["CustID"]
      self.CustNum:int = obj["CustNum"]
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.TerritoryID:str = obj["TerritoryID"]
      self.FaxNum:str = obj["FaxNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.EMailAddress:str = obj["EMailAddress"]
      self.CustomerType:str = obj["CustomerType"]
      self.NoContact:bool = obj["NoContact"]
      self.CustURL:str = obj["CustURL"]
      self.ExtID:str = obj["ExtID"]
      self.MatchedCustNum:int = obj["MatchedCustNum"]
      self.MatchedFlag:str = obj["MatchedFlag"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      self.DispMatchedFlag:str = obj["DispMatchedFlag"]
      self.SalesRepName:str = obj["SalesRepName"]
      """  Name  """  
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      """  Description of the territory.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_CustomerImportListTableset:
   def __init__(self, obj):
      self.CustomerImportList:list[Erp_Tablesets_CustomerImportListRow] = obj["CustomerImportList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_CustomerImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.ImportID:int = obj["ImportID"]
      self.CustID:str = obj["CustID"]
      self.CustNum:int = obj["CustNum"]
      self.Name:str = obj["Name"]
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      self.SalesRepCode:str = obj["SalesRepCode"]
      self.TerritoryID:str = obj["TerritoryID"]
      self.FaxNum:str = obj["FaxNum"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.EMailAddress:str = obj["EMailAddress"]
      self.CustomerType:str = obj["CustomerType"]
      self.NoContact:bool = obj["NoContact"]
      self.CustURL:str = obj["CustURL"]
      self.ExtID:str = obj["ExtID"]
      self.MatchedCustNum:int = obj["MatchedCustNum"]
      self.MatchedFlag:str = obj["MatchedFlag"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      self.DispMatchedFlag:str = obj["DispMatchedFlag"]
      self.BitFlag:int = obj["BitFlag"]
      self.SalesRepName:str = obj["SalesRepName"]
      self.TerritoryIDTerritoryDesc:str = obj["TerritoryIDTerritoryDesc"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImpCustCntExistingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustNum:int = obj["CustNum"]
      """  The Customer.CustNum value of the customer that the contact is related to.  """  
      self.ConNum:int = obj["ConNum"]
      """  A system generated number used to uniquely identify the contact record for the related customer or ship to. When creating new contacts the system reads the last existing contact record for the customer or ship to being processed and then uses its number plus one as the number for the new contact.  """  
      self.Name:str = obj["Name"]
      """  Full name of the contact.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  The contact's fax number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contact's number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The contact's business telephone number. When displaying phone numbers of contacts the system will use the phone number found in the Customer or Shipto file if the contacts number is blank.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  The contact's email address.  """  
      self.RoleCode:str = obj["RoleCode"]
      """  RoleCD.RoleCode value of the role assigned to the contact.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.RoleCodeDescription:str = obj["RoleCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImpCustomerExistingRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.CustID:str = obj["CustID"]
      """  A user defined external customer ID.  This must be unique within the file.  This ID may be used in certain screen displays or reports where a full customer name is inappropriate. Therefore users should use meaningful characters as they would in any other master file. This master file key is a little different in that the user can change. This change is allowed because the system is not using the CustID as a foreign key in any other file.  Rather it uses the CustNum field which is assigned to the customer by the system.  """  
      self.CustNum:int = obj["CustNum"]
      """  A  unique integer assigned by the system to new customers by the customer maintenance program.  This field is used as the foreign key to identify the customer in other files such as OrderHed or InvcHead.  The end user should never see this field in the application but can use it for reporting purposes.  """  
      self.Name:str = obj["Name"]
      """  The full name of the customer.  """  
      self.Address1:str = obj["Address1"]
      """  The first line of the customer's main address.  """  
      self.Address2:str = obj["Address2"]
      """  The second line of the customer's main address.  """  
      self.Address3:str = obj["Address3"]
      """  The third line of the customer's main address.  """  
      self.City:str = obj["City"]
      """  The city portion of the customer's main address.  """  
      self.State:str = obj["State"]
      """  The state or province portion of the customer's main address.  """  
      self.Zip:str = obj["Zip"]
      """  The zip or postal code portion of the customer's main address.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the customer. Displayed in Order entry when no contact is given or when contact has a blank phone number.  """  
      self.CustomerType:str = obj["CustomerType"]
      """  Used to define the type of the customer record.  """  
      self.ExternalID:str = obj["ExternalID"]
      """  Customer ID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AddrList:str = obj["AddrList"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtCustContImportTableset:
   def __init__(self, obj):
      self.CustomerImport:list[Erp_Tablesets_CustomerImportRow] = obj["CustomerImport"]
      self.CustomerImportAttch:list[Erp_Tablesets_CustomerImportAttchRow] = obj["CustomerImportAttch"]
      self.CustCntImport:list[Erp_Tablesets_CustCntImportRow] = obj["CustCntImport"]
      self.CustCntImportAttch:list[Erp_Tablesets_CustCntImportAttchRow] = obj["CustCntImportAttch"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   importID
   """  
   def __init__(self, obj):
      self.importID:int = obj["importID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustContImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustContImportTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustContImportTableset] = obj["returnObj"]
      pass

class GetExistingCustomers_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustContExistingTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_CustomerImportListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewCustCntImportAttch_input:
   """ Required : 
   ds
   parentImportID
   importID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      self.parentImportID:int = obj["parentImportID"]
      self.importID:int = obj["importID"]
      pass

class GetNewCustCntImportAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCustCntImport_input:
   """ Required : 
   ds
   parentImportID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      self.parentImportID:int = obj["parentImportID"]
      pass

class GetNewCustCntImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCustomerImportAttch_input:
   """ Required : 
   ds
   importID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      self.importID:int = obj["importID"]
      pass

class GetNewCustomerImportAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewCustomerImport_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

class GetNewCustomerImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseCustomerImport
   whereClauseCustomerImportAttch
   whereClauseCustCntImport
   whereClauseCustCntImportAttch
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseCustomerImport:str = obj["whereClauseCustomerImport"]
      self.whereClauseCustomerImportAttch:str = obj["whereClauseCustomerImportAttch"]
      self.whereClauseCustCntImport:str = obj["whereClauseCustCntImport"]
      self.whereClauseCustCntImportAttch:str = obj["whereClauseCustCntImportAttch"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustContImportTableset] = obj["returnObj"]
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

class ImportCustomersAndContacts_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportExportTableset] = obj["ds"]
      pass

class ImportCustomersAndContacts_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportExportTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ImportFileFromWeb_input:
   """ Required : 
   sFileSubPath
   """  
   def __init__(self, obj):
      self.sFileSubPath:str = obj["sFileSubPath"]
      """  Imported file subpath of SpecialFolder.UserData.  """  
      pass

class ImportFileFromWeb_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustContImportExportTableset] = obj["returnObj"]
      pass

class MatchImpCustCnt_input:
   """ Required : 
   iParentImportID
   iImportID
   ExistingCustNum
   ExistingConNum
   """  
   def __init__(self, obj):
      self.iParentImportID:int = obj["iParentImportID"]
      """  The ParentImportID of the imported customer contact record  """  
      self.iImportID:int = obj["iImportID"]
      """  The ImportID of the imported customer contact record  """  
      self.ExistingCustNum:int = obj["ExistingCustNum"]
      """  The Customer Number of the existing customer contact to match to  """  
      self.ExistingConNum:int = obj["ExistingConNum"]
      """  The Contact Number of the existing customer contact to match to  """  
      pass

class MatchImpCustCnt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustContImportTableset] = obj["returnObj"]
      pass

class MatchImpCustomer_input:
   """ Required : 
   ImpCustomerImportID
   ExistingCustNum
   """  
   def __init__(self, obj):
      self.ImpCustomerImportID:int = obj["ImpCustomerImportID"]
      """  The ImportID of the imported customer record  """  
      self.ExistingCustNum:int = obj["ExistingCustNum"]
      """  The Customer Number of the existing customer to match to  """  
      pass

class MatchImpCustomer_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustContImportTableset] = obj["returnObj"]
      pass

class UnmatchImpCustCnt_input:
   """ Required : 
   iParentImportID
   iImportID
   """  
   def __init__(self, obj):
      self.iParentImportID:int = obj["iParentImportID"]
      """  The ParentImportID of the imported customer contact record  """  
      self.iImportID:int = obj["iImportID"]
      """  The ImportID of the imported customer contact record  """  
      pass

class UnmatchImpCustCnt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustContImportTableset] = obj["returnObj"]
      pass

class UnmatchImpCustomer_input:
   """ Required : 
   iImportID
   """  
   def __init__(self, obj):
      self.iImportID:int = obj["iImportID"]
      """  The ImportID of the imported customer record  """  
      pass

class UnmatchImpCustomer_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_CustContImportTableset] = obj["returnObj"]
      pass

class UpdateCustomers_output:
   def __init__(self, obj):
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustContImportTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtCustContImportTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_CustContImportTableset] = obj["ds"]
      pass

      """  output parameters  """  

