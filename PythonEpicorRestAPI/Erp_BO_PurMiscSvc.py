import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.PurMiscSvc
# Description: Purchase Management System Miscellaneous charge/credit master.
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_PurMiscs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PurMiscs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurMiscs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs",headers=creds) as resp:
           return await resp.json()

async def post_PurMiscs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurMiscs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurMiscRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PurMiscRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PurMiscs_Company_MiscCode(Company, MiscCode, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurMisc item
   Description: Calls GetByID to retrieve the PurMisc item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurMiscRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs(" + Company + "," + MiscCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PurMiscs_Company_MiscCode(Company, MiscCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PurMisc for the service
   Description: Calls UpdateExt to update PurMisc. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurMiscRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs(" + Company + "," + MiscCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PurMiscs_Company_MiscCode(Company, MiscCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PurMisc item
   Description: Call UpdateExt to delete PurMisc item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurMisc
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs(" + Company + "," + MiscCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurMiscs_Company_MiscCode_EntityGLCs(Company, MiscCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs(" + Company + "," + MiscCode + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_PurMiscs_Company_MiscCode_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, MiscCode, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs(" + Company + "," + MiscCode + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurMiscs_Company_MiscCode_PurMiscExpUBs(Company, MiscCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PurMiscExpUBs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PurMiscExpUBs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurMiscExpUBRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs(" + Company + "," + MiscCode + ")/PurMiscExpUBs",headers=creds) as resp:
           return await resp.json()

async def get_PurMiscs_Company_MiscCode_PurMiscExpUBs_Company_MiscCode_FromEffectiveDate_ClaimCurrencyCode(Company, MiscCode, FromEffectiveDate, ClaimCurrencyCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurMiscExpUB item
   Description: Calls GetByID to retrieve the PurMiscExpUB item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurMiscExpUB1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param FromEffectiveDate: Desc: FromEffectiveDate   Required: True   Allow empty value : True
      :param ClaimCurrencyCode: Desc: ClaimCurrencyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurMiscExpUBRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs(" + Company + "," + MiscCode + ")/PurMiscExpUBs(" + Company + "," + MiscCode + "," + FromEffectiveDate + "," + ClaimCurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurMiscs_Company_MiscCode_PurMiscVends(Company, MiscCode, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PurMiscVends items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PurMiscVends1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurMiscVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs(" + Company + "," + MiscCode + ")/PurMiscVends",headers=creds) as resp:
           return await resp.json()

async def get_PurMiscs_Company_MiscCode_PurMiscVends_Company_MiscCode_VendorNum(Company, MiscCode, VendorNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurMiscVend item
   Description: Calls GetByID to retrieve the PurMiscVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurMiscVend1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurMiscVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscs(" + Company + "," + MiscCode + ")/PurMiscVends(" + Company + "," + MiscCode + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get EntityGLCs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_EntityGLCs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def post_EntityGLCs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_EntityGLCs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def patch_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update EntityGLC for the service
   Description: Calls UpdateExt to update EntityGLC. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.EntityGLCRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete EntityGLC item
   Description: Call UpdateExt to delete EntityGLC item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_EntityGLC
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param Key3: Desc: Key3   Required: True   Allow empty value : True
      :param Key4: Desc: Key4   Required: True   Allow empty value : True
      :param Key5: Desc: Key5   Required: True   Allow empty value : True
      :param Key6: Desc: Key6   Required: True   Allow empty value : True
      :param GLControlType: Desc: GLControlType   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurMiscExpUBs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PurMiscExpUBs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurMiscExpUBs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurMiscExpUBRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscExpUBs",headers=creds) as resp:
           return await resp.json()

async def post_PurMiscExpUBs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurMiscExpUBs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurMiscExpUBRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PurMiscExpUBRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscExpUBs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PurMiscExpUBs_Company_MiscCode_FromEffectiveDate_ClaimCurrencyCode(Company, MiscCode, FromEffectiveDate, ClaimCurrencyCode, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurMiscExpUB item
   Description: Calls GetByID to retrieve the PurMiscExpUB item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurMiscExpUB
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param FromEffectiveDate: Desc: FromEffectiveDate   Required: True   Allow empty value : True
      :param ClaimCurrencyCode: Desc: ClaimCurrencyCode   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurMiscExpUBRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscExpUBs(" + Company + "," + MiscCode + "," + FromEffectiveDate + "," + ClaimCurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PurMiscExpUBs_Company_MiscCode_FromEffectiveDate_ClaimCurrencyCode(Company, MiscCode, FromEffectiveDate, ClaimCurrencyCode, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PurMiscExpUB for the service
   Description: Calls UpdateExt to update PurMiscExpUB. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurMiscExpUB
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param FromEffectiveDate: Desc: FromEffectiveDate   Required: True   Allow empty value : True
      :param ClaimCurrencyCode: Desc: ClaimCurrencyCode   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurMiscExpUBRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscExpUBs(" + Company + "," + MiscCode + "," + FromEffectiveDate + "," + ClaimCurrencyCode + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PurMiscExpUBs_Company_MiscCode_FromEffectiveDate_ClaimCurrencyCode(Company, MiscCode, FromEffectiveDate, ClaimCurrencyCode, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PurMiscExpUB item
   Description: Call UpdateExt to delete PurMiscExpUB item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurMiscExpUB
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param FromEffectiveDate: Desc: FromEffectiveDate   Required: True   Allow empty value : True
      :param ClaimCurrencyCode: Desc: ClaimCurrencyCode   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscExpUBs(" + Company + "," + MiscCode + "," + FromEffectiveDate + "," + ClaimCurrencyCode + ")",headers=creds) as resp:
           return await resp.json()

async def get_PurMiscVends(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PurMiscVends items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PurMiscVends
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurMiscVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscVends",headers=creds) as resp:
           return await resp.json()

async def post_PurMiscVends(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PurMiscVends
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PurMiscVendRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PurMiscVendRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscVends", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PurMiscVends_Company_MiscCode_VendorNum(Company, MiscCode, VendorNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PurMiscVend item
   Description: Calls GetByID to retrieve the PurMiscVend item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PurMiscVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PurMiscVendRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscVends(" + Company + "," + MiscCode + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PurMiscVends_Company_MiscCode_VendorNum(Company, MiscCode, VendorNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PurMiscVend for the service
   Description: Calls UpdateExt to update PurMiscVend. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PurMiscVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PurMiscVendRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscVends(" + Company + "," + MiscCode + "," + VendorNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PurMiscVends_Company_MiscCode_VendorNum(Company, MiscCode, VendorNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PurMiscVend item
   Description: Call UpdateExt to delete PurMiscVend item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PurMiscVend
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param MiscCode: Desc: MiscCode   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/PurMiscVends(" + Company + "," + MiscCode + "," + VendorNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PurMiscListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClausePurMisc, whereClauseEntityGLC, whereClausePurMiscExpUB, whereClausePurMiscVend, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClausePurMisc=" + whereClausePurMisc
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseEntityGLC=" + whereClauseEntityGLC
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePurMiscExpUB=" + whereClausePurMiscExpUB
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePurMiscVend=" + whereClausePurMiscVend
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(miscCode, epicorHeaders = None):
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
   params += "miscCode=" + miscCode

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: To return the CodeDescriptionList values of a given table.field.
   OperationID: GetCodeDescList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetCodeDescList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetCodeDescList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnEmpExpenseFlagChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnEmpExpenseFlagChange
   Description: Sets or clears the fields related to the EmpExpanseFlag
   OperationID: OnEmpExpenseFlagChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnEmpExpenseFlagChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnEmpExpenseFlagChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnSupplierChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnSupplierChange
   Description: Verifies if is valid supplier.
   OperationID: OnSupplierChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnSupplierChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnSupplierChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPurMisc(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPurMisc
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurMisc
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPurMisc_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurMisc_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewEntityGLC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewEntityGLC
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewEntityGLC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewEntityGLC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewEntityGLC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPurMiscExpUB(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPurMiscExpUB
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurMiscExpUB
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPurMiscExpUB_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurMiscExpUB_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPurMiscVend(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPurMiscVend
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPurMiscVend
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPurMiscVend_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPurMiscVend_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.PurMiscSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurMiscExpUBRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurMiscExpUBRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurMiscListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurMiscListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurMiscRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurMiscRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PurMiscVendRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PurMiscVendRow] = obj["value"]
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurMiscExpUBRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.FromEffectiveDate:str = obj["FromEffectiveDate"]
      """  From Effective Date of this Unit Based record.  The value must be unique per PurMisc Code.  This value cannot be changed after the initial save.  """  
      self.ToEffectiveDate:str = obj["ToEffectiveDate"]
      """  To Effective Date of this Unit Based record.  Value is not required.  This value cannot be changed after the initial save.  """  
      self.ExpenseUnitDesc:str = obj["ExpenseUnitDesc"]
      """  Description of a Unit to be used as the label for Expense Units during expense entry.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if this Unit Based record is inactive.  """  
      self.ClaimUnitMaximum:int = obj["ClaimUnitMaximum"]
      """  Indicates the maximum number of units a user can enter in a single expense transaction.  If the number entered exceeds this value then the system will set the claim units value to the specified maximum value.  A value of zero indicates no maximum.  """  
      self.ClaimUnitAmount:int = obj["ClaimUnitAmount"]
      """  The amount per unit in base currency that will be used to calculate the total expense transaction amount.  """  
      self.Override:bool = obj["Override"]
      """  Indicates if the user can override the claim unit amount during expense entry.  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.GlobalPurMiscExpUB:bool = obj["GlobalPurMiscExpUB"]
      """  Marks this PurMiscExpUB as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      """  Claim Currency  """  
      self.BaseCurrencyCodeCurrDesc:str = obj["BaseCurrencyCodeCurrDesc"]
      self.MultiCurrency:bool = obj["MultiCurrency"]
      """  Indicates if multi-currency is licensed  """  
      self.FromEffectiveDateAux:str = obj["FromEffectiveDateAux"]
      """  From Effective Date (auxiliar field)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClaimCCCurrencyID:str = obj["ClaimCCCurrencyID"]
      self.ClaimCCCurrSymbol:str = obj["ClaimCCCurrSymbol"]
      self.ClaimCCCurrDesc:str = obj["ClaimCCCurrDesc"]
      self.ClaimCCCurrName:str = obj["ClaimCCCurrName"]
      self.ClaimCCDocumentDesc:str = obj["ClaimCCDocumentDesc"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscLCAmount:int = obj["PurMiscLCAmount"]
      self.PurMiscLCCurrencyCode:str = obj["PurMiscLCCurrencyCode"]
      self.PurMiscLCDisburseMethod:str = obj["PurMiscLCDisburseMethod"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurMiscListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Misc. charge. Can be blank or must be valid in the TaxCat master file.  """  
      self.ISCharge:str = obj["ISCharge"]
      """   Indicates whether this charge should be included in the calculation of Intrastat Statistical Value.  The valid values are:
"I" - Include this charge in the Intrastat Statistical Value
"E" - Do not include this charge in the Intrastat calculation
"P" - Apply a percentage of this charge in the Intrastat Statistical Value.  The actual percentage is stored in the BorderPct table.  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the Miscellaneous Charge is for Landed Cost.  """  
      self.LCAmount:int = obj["LCAmount"]
      """  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.LCCurrencyCode:str = obj["LCCurrencyCode"]
      """  The Landed Cost Currency Code for this miscellaneous charge.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.EmpExpenseFlag:bool = obj["EmpExpenseFlag"]
      """  Indicates if the Miscellaneous Charge is for Employee Expenses.  """  
      self.ExpCommentRequired:bool = obj["ExpCommentRequired"]
      """  Indicates whether to require a value in PurMisc.ExpCommentText.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Comment  """  
      self.ExpUnitBased:bool = obj["ExpUnitBased"]
      """  When an expense charge, indicates if the code is unit based.  """  
      self.ExpChargeable:bool = obj["ExpChargeable"]
      """  When an expense charge, indicates if the code is chargeable.  """  
      self.ExpPMUID:int = obj["ExpPMUID"]
      """  When an expense charge, indicates the payment method of the code.  """  
      self.ExpIndirect:bool = obj["ExpIndirect"]
      """  When an expense charge, indicates if the code is to be selected for entry of indirect (non-project) expenses.  """  
      self.ExpTaxRegionCode:str = obj["ExpTaxRegionCode"]
      """  When an expense charge, indicates the tax liability of the code.  """  
      self.ExpProject:bool = obj["ExpProject"]
      """  When an expense charge, indicates if the code is be selected for entry of project expenses.  """  
      self.ExpDescription:str = obj["ExpDescription"]
      """  When used for expenses, a description of the expense.  """  
      self.GlobalPurMisc:bool = obj["GlobalPurMisc"]
      """  Marks this PurMisc as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ExpAdvanceRequest:bool = obj["ExpAdvanceRequest"]
      """  When an expense charge, indicates if the code is be selected for entry of advance request expenses.  """  
      self.ExpJob:bool = obj["ExpJob"]
      """  When an expense charge, indicates if the code is be selected for entry of job expenses.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Inactive:bool = obj["Inactive"]
      """  When an Expense Type is marked as Inactive it should NOT appear in the Expense Type drop down on Expense Entry  """  
      self.MiscGLAcct:str = obj["MiscGLAcct"]
      """  Purchase Miscellaneous GL Account Number  """  
      self.MiscGLAcctDesc:str = obj["MiscGLAcctDesc"]
      """  Purchase Miscellaneous GL Account Description  """  
      self.TaxCatIDDesc:str = obj["TaxCatIDDesc"]
      """  Tax Category Description  """  
      self.EnableUnitBased:bool = obj["EnableUnitBased"]
      """  Indicates whether the unit based field should be enabled in the ui form  """  
      self.EnableEmpExpense:bool = obj["EnableEmpExpense"]
      """  Flag to indicate whether the EmpExpenseFlag should be enabled.  """  
      self.LCCurrencyCodeCurrSymbol:str = obj["LCCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.LCCurrencyCodeCurrencyID:str = obj["LCCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.LCCurrencyCodeDocumentDesc:str = obj["LCCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.LCCurrencyCodeCurrName:str = obj["LCCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.LCCurrencyCodeCurrDesc:str = obj["LCCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
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
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      """  Full description for the Tax Region.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Misc. charge. Can be blank or must be valid in the TaxCat master file.  """  
      self.ISCharge:str = obj["ISCharge"]
      """   Indicates whether this charge should be included in the calculation of Intrastat Statistical Value.  The valid values are:
"I" - Include this charge in the Intrastat Statistical Value
"E" - Do not include this charge in the Intrastat calculation
"P" - Apply a percentage of this charge in the Intrastat Statistical Value.  The actual percentage is stored in the BorderPct table.  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the Miscellaneous Charge is for Landed Cost.  """  
      self.LCAmount:int = obj["LCAmount"]
      """  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.LCCurrencyCode:str = obj["LCCurrencyCode"]
      """  The Landed Cost Currency Code for this miscellaneous charge.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.EmpExpenseFlag:bool = obj["EmpExpenseFlag"]
      """  Indicates if the Miscellaneous Charge is for Employee Expenses.  """  
      self.ExpCommentRequired:bool = obj["ExpCommentRequired"]
      """  Indicates whether to require a value in PurMisc.ExpCommentText.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Comment  """  
      self.ExpUnitBased:bool = obj["ExpUnitBased"]
      """  When an expense charge, indicates if the code is unit based.  """  
      self.ExpChargeable:bool = obj["ExpChargeable"]
      """  When an expense charge, indicates if the code is chargeable.  """  
      self.ExpPMUID:int = obj["ExpPMUID"]
      """  When an expense charge, indicates the payment method of the code.  """  
      self.ExpIndirect:bool = obj["ExpIndirect"]
      """  When an expense charge, indicates if the code is to be selected for entry of indirect (non-project) expenses.  """  
      self.ExpTaxRegionCode:str = obj["ExpTaxRegionCode"]
      """  When an expense charge, indicates the tax liability of the code.  """  
      self.ExpProject:bool = obj["ExpProject"]
      """  When an expense charge, indicates if the code is be selected for entry of project expenses.  """  
      self.ExpDescription:str = obj["ExpDescription"]
      """  When used for expenses, a description of the expense.  """  
      self.GlobalPurMisc:bool = obj["GlobalPurMisc"]
      """  Marks this PurMisc as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ExpAdvanceRequest:bool = obj["ExpAdvanceRequest"]
      """  When an expense charge, indicates if the code is be selected for entry of advance request expenses.  """  
      self.ExpJob:bool = obj["ExpJob"]
      """  When an expense charge, indicates if the code is be selected for entry of job expenses.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Inactive:bool = obj["Inactive"]
      """  When an Expense Type is marked as Inactive it should NOT appear in the Expense Type drop down on Expense Entry  """  
      self.TakeDiscount:bool = obj["TakeDiscount"]
      """  Indicates if terms discount applies to the charge.  """  
      self.isAdValorem:bool = obj["isAdValorem"]
      """  Identifies if the amount added to a DUA invoice is Ad Valorem (CSF - Peru)  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  True if the record should be synced to FSA, otherwise false.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      """  UNCL5189 and UNCL7161  """  
      self.EnableEmpExpense:bool = obj["EnableEmpExpense"]
      """  Flag to indicate whether the EmpExpenseFlag should be enabled.  """  
      self.EnableUnitBased:bool = obj["EnableUnitBased"]
      """  Indicates whether the unit based field should be enabled in the ui form  """  
      self.MiscGLAcct:str = obj["MiscGLAcct"]
      """  Purchase Miscellaneous GL Account Number  """  
      self.MiscGLAcctDesc:str = obj["MiscGLAcctDesc"]
      """  Purchase Miscellaneous GL Account Description  """  
      self.TaxCatIDDesc:str = obj["TaxCatIDDesc"]
      """  Tax Category Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.LCCurrencyCodeCurrencyID:str = obj["LCCurrencyCodeCurrencyID"]
      self.LCCurrencyCodeCurrSymbol:str = obj["LCCurrencyCodeCurrSymbol"]
      self.LCCurrencyCodeDocumentDesc:str = obj["LCCurrencyCodeDocumentDesc"]
      self.LCCurrencyCodeCurrDesc:str = obj["LCCurrencyCodeCurrDesc"]
      self.LCCurrencyCodeCurrName:str = obj["LCCurrencyCodeCurrName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurMiscVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.LCAmount:int = obj["LCAmount"]
      """  Supplier specific Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipt for this supplier.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume , Weight, Value, Quantity and Manual.  """  
      self.LCCurrencyCode:str = obj["LCCurrencyCode"]
      """  The Landed Cost Currency Code.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount (A) or if is calculated as a percentage of the extended price (P).  """  
      self.GlobalPurMiscVend:bool = obj["GlobalPurMiscVend"]
      """  Marks this PurMiscVend as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.LCCurrencyCodeCurrName:str = obj["LCCurrencyCodeCurrName"]
      self.LCCurrencyCodeCurrSymbol:str = obj["LCCurrencyCodeCurrSymbol"]
      self.LCCurrencyCodeCurrDesc:str = obj["LCCurrencyCodeCurrDesc"]
      self.LCCurrencyCodeCurrencyID:str = obj["LCCurrencyCodeCurrencyID"]
      self.LCCurrencyCodeDocumentDesc:str = obj["LCCurrencyCodeDocumentDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class DeleteByID_input:
   """ Required : 
   miscCode
   """  
   def __init__(self, obj):
      self.miscCode:str = obj["miscCode"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.RelatedToFile:str = obj["RelatedToFile"]
      """   Identifies the master file to which the GL Control is related to.  This field is used to properly isolate controls to the masters they are related to.
For example; Customer, PartClass identifies controls that are related to Customers and Part Classes  """  
      self.Key1:str = obj["Key1"]
      """  Major component of the foreign key of the related master record. For example: For a "Part"  control this field would contain the related Part Number,  for a "Customer"  it contains the Customer.CustNum.  """  
      self.Key2:str = obj["Key2"]
      """   2nd component of the foreign key to the related master record.
The usage of this field is dependent on the type of record.  """  
      self.Key3:str = obj["Key3"]
      """   3rd component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key4:str = obj["Key4"]
      """   4th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key5:str = obj["Key5"]
      """   5th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.Key6:str = obj["Key6"]
      """   6th component of the foreign key to the related master record.
The usage of this field is dependent record type.  """  
      self.GLControlType:str = obj["GLControlType"]
      """  Identifier of the GL Control Type.  """  
      self.GLControlCode:str = obj["GLControlCode"]
      """  GL Control Identifier.  """  
      self.BusinessEntity:str = obj["BusinessEntity"]
      """  Identifies the entity.  Reference only.  Used for integrity validation when deleting a GLCTEntity record.  """  
      self.ExtCompanyID:str = obj["ExtCompanyID"]
      """  Global Company identifier.  Used in Multi-Company Journal.  """  
      self.IsExternalCompany:bool = obj["IsExternalCompany"]
      """  Flag to indicate the account in this record is for an external company.  """  
      self.GlobalEntityGLC:bool = obj["GlobalEntityGLC"]
      """  Marks this EntityGLC as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BankAcctID:str = obj["BankAcctID"]
      """  BankAcctID of the related BankAcct record.  """  
      self.BankFeeID:str = obj["BankFeeID"]
      self.CallCode:str = obj["CallCode"]
      """  CallCode of the related FSCallCd record.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      self.ClassCode:str = obj["ClassCode"]
      """  ClassCode of the related FAClass record.  """  
      self.ClassID:str = obj["ClassID"]
      """  ClassID.  This can be ClassID of PartClass, PRClsDed, or PRClsTax  """  
      self.ContractCode:str = obj["ContractCode"]
      """  ContractCode of the related FSContCd record.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode of the related Currency record.  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum of the related Customer record  """  
      self.DeductionID:str = obj["DeductionID"]
      """  DeductionID of PRClsDed or PRDeduct.  """  
      self.EmpID:str = obj["EmpID"]
      """  EmpID of the related PREmpMas record.  """  
      self.ExpenseCode:str = obj["ExpenseCode"]
      """  ExpenseCode of PayTLbr, LabExpCd  """  
      self.ExtSystemID:str = obj["ExtSystemID"]
      """  ExtSystemID of ExtCompany table  """  
      self.FromPlant:str = obj["FromPlant"]
      """  FromPlant value of the related PlntTranDef record.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  GroupCode of the related FAGroup record.  """  
      self.GroupID:str = obj["GroupID"]
      self.HeadNum:int = obj["HeadNum"]
      self.InvoiceNum:str = obj["InvoiceNum"]
      self.JCDept:str = obj["JCDept"]
      """  JCDept of the related JCDept record.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode of the related MiscChrg or PurMisc record.  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum of the related Part record.  """  
      self.PayTypeID:str = obj["PayTypeID"]
      """  PayTypeID of PayType  """  
      self.PerConName:str = obj["PerConName"]
      self.PIStatus:str = obj["PIStatus"]
      """  PI Status  """  
      self.Plant:str = obj["Plant"]
      """  Plant of the related PlantConfCtrl record.  """  
      self.ProdCode:str = obj["ProdCode"]
      """  ProdCode of the related ProdGrup record.  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID of the related Project record.  """  
      self.PurchCode:str = obj["PurchCode"]
      """  PurchCode of the related GLPurch record.  """  
      self.RateCode:str = obj["RateCode"]
      """  RateCode of the related GLRate record.  """  
      self.ReasonCode:str = obj["ReasonCode"]
      """  ReasonCode of the related Reason record.  """  
      self.ReasonType:str = obj["ReasonType"]
      """  ReasonType of the related Reason record.  """  
      self.SalesCatID:str = obj["SalesCatID"]
      """  SalesCatID of the related SalesCat record.  """  
      self.Shift:int = obj["Shift"]
      """  Shift value of the related JCShift record.  """  
      self.TaxCode:str = obj["TaxCode"]
      """  TaxCode of the related SalesTax record.  """  
      self.TaxTblID:str = obj["TaxTblID"]
      """  TaxTblID of PRTaxMas or PRClsTax.  """  
      self.ToPlant:str = obj["ToPlant"]
      """  ToPlant value of the related PlntTranDef record.  """  
      self.TransferMethod:str = obj["TransferMethod"]
      """  TransferMethod of ExtCompany table  """  
      self.TypeID:str = obj["TypeID"]
      """  Type ID  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum of the related Vendor record.  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  WarehouseCode of the related Warehse record.  """  
      self.ExpenseTypeCode:str = obj["ExpenseTypeCode"]
      self.IsFiltered:bool = obj["IsFiltered"]
      self.OprTypeCode:str = obj["OprTypeCode"]
      self.CashDeskID:str = obj["CashDeskID"]
      self.TIN:str = obj["TIN"]
      self.ReclassCodeID:str = obj["ReclassCodeID"]
      self.BitFlag:int = obj["BitFlag"]
      self.GLCntrlDescription:str = obj["GLCntrlDescription"]
      self.GLCntrlTypeDescription:str = obj["GLCntrlTypeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurMiscExpUBRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.FromEffectiveDate:str = obj["FromEffectiveDate"]
      """  From Effective Date of this Unit Based record.  The value must be unique per PurMisc Code.  This value cannot be changed after the initial save.  """  
      self.ToEffectiveDate:str = obj["ToEffectiveDate"]
      """  To Effective Date of this Unit Based record.  Value is not required.  This value cannot be changed after the initial save.  """  
      self.ExpenseUnitDesc:str = obj["ExpenseUnitDesc"]
      """  Description of a Unit to be used as the label for Expense Units during expense entry.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if this Unit Based record is inactive.  """  
      self.ClaimUnitMaximum:int = obj["ClaimUnitMaximum"]
      """  Indicates the maximum number of units a user can enter in a single expense transaction.  If the number entered exceeds this value then the system will set the claim units value to the specified maximum value.  A value of zero indicates no maximum.  """  
      self.ClaimUnitAmount:int = obj["ClaimUnitAmount"]
      """  The amount per unit in base currency that will be used to calculate the total expense transaction amount.  """  
      self.Override:bool = obj["Override"]
      """  Indicates if the user can override the claim unit amount during expense entry.  """  
      self.ClaimCurrencyCode:str = obj["ClaimCurrencyCode"]
      """  The currency the claim amounts are in.  """  
      self.GlobalPurMiscExpUB:bool = obj["GlobalPurMiscExpUB"]
      """  Marks this PurMiscExpUB as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BaseCurrencyCode:str = obj["BaseCurrencyCode"]
      """  Claim Currency  """  
      self.BaseCurrencyCodeCurrDesc:str = obj["BaseCurrencyCodeCurrDesc"]
      self.MultiCurrency:bool = obj["MultiCurrency"]
      """  Indicates if multi-currency is licensed  """  
      self.FromEffectiveDateAux:str = obj["FromEffectiveDateAux"]
      """  From Effective Date (auxiliar field)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.ClaimCCCurrencyID:str = obj["ClaimCCCurrencyID"]
      self.ClaimCCCurrSymbol:str = obj["ClaimCCCurrSymbol"]
      self.ClaimCCCurrDesc:str = obj["ClaimCCCurrDesc"]
      self.ClaimCCCurrName:str = obj["ClaimCCCurrName"]
      self.ClaimCCDocumentDesc:str = obj["ClaimCCDocumentDesc"]
      self.PurMiscDescription:str = obj["PurMiscDescription"]
      self.PurMiscLCAmount:int = obj["PurMiscLCAmount"]
      self.PurMiscLCCurrencyCode:str = obj["PurMiscLCCurrencyCode"]
      self.PurMiscLCDisburseMethod:str = obj["PurMiscLCDisburseMethod"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurMiscListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Misc. charge. Can be blank or must be valid in the TaxCat master file.  """  
      self.ISCharge:str = obj["ISCharge"]
      """   Indicates whether this charge should be included in the calculation of Intrastat Statistical Value.  The valid values are:
"I" - Include this charge in the Intrastat Statistical Value
"E" - Do not include this charge in the Intrastat calculation
"P" - Apply a percentage of this charge in the Intrastat Statistical Value.  The actual percentage is stored in the BorderPct table.  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the Miscellaneous Charge is for Landed Cost.  """  
      self.LCAmount:int = obj["LCAmount"]
      """  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.LCCurrencyCode:str = obj["LCCurrencyCode"]
      """  The Landed Cost Currency Code for this miscellaneous charge.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.EmpExpenseFlag:bool = obj["EmpExpenseFlag"]
      """  Indicates if the Miscellaneous Charge is for Employee Expenses.  """  
      self.ExpCommentRequired:bool = obj["ExpCommentRequired"]
      """  Indicates whether to require a value in PurMisc.ExpCommentText.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Comment  """  
      self.ExpUnitBased:bool = obj["ExpUnitBased"]
      """  When an expense charge, indicates if the code is unit based.  """  
      self.ExpChargeable:bool = obj["ExpChargeable"]
      """  When an expense charge, indicates if the code is chargeable.  """  
      self.ExpPMUID:int = obj["ExpPMUID"]
      """  When an expense charge, indicates the payment method of the code.  """  
      self.ExpIndirect:bool = obj["ExpIndirect"]
      """  When an expense charge, indicates if the code is to be selected for entry of indirect (non-project) expenses.  """  
      self.ExpTaxRegionCode:str = obj["ExpTaxRegionCode"]
      """  When an expense charge, indicates the tax liability of the code.  """  
      self.ExpProject:bool = obj["ExpProject"]
      """  When an expense charge, indicates if the code is be selected for entry of project expenses.  """  
      self.ExpDescription:str = obj["ExpDescription"]
      """  When used for expenses, a description of the expense.  """  
      self.GlobalPurMisc:bool = obj["GlobalPurMisc"]
      """  Marks this PurMisc as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ExpAdvanceRequest:bool = obj["ExpAdvanceRequest"]
      """  When an expense charge, indicates if the code is be selected for entry of advance request expenses.  """  
      self.ExpJob:bool = obj["ExpJob"]
      """  When an expense charge, indicates if the code is be selected for entry of job expenses.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Inactive:bool = obj["Inactive"]
      """  When an Expense Type is marked as Inactive it should NOT appear in the Expense Type drop down on Expense Entry  """  
      self.MiscGLAcct:str = obj["MiscGLAcct"]
      """  Purchase Miscellaneous GL Account Number  """  
      self.MiscGLAcctDesc:str = obj["MiscGLAcctDesc"]
      """  Purchase Miscellaneous GL Account Description  """  
      self.TaxCatIDDesc:str = obj["TaxCatIDDesc"]
      """  Tax Category Description  """  
      self.EnableUnitBased:bool = obj["EnableUnitBased"]
      """  Indicates whether the unit based field should be enabled in the ui form  """  
      self.EnableEmpExpense:bool = obj["EnableEmpExpense"]
      """  Flag to indicate whether the EmpExpenseFlag should be enabled.  """  
      self.LCCurrencyCodeCurrSymbol:str = obj["LCCurrencyCodeCurrSymbol"]
      """  A symbol that identifies the currency. Used on Forms and displays  """  
      self.LCCurrencyCodeCurrencyID:str = obj["LCCurrencyCodeCurrencyID"]
      """  This is the updatable version of CurrencyCode.  This currency cannot be a record already in the currency table.  """  
      self.LCCurrencyCodeDocumentDesc:str = obj["LCCurrencyCodeDocumentDesc"]
      """   An extended description that can be used on documents such as
POs and invoices.  """  
      self.LCCurrencyCodeCurrName:str = obj["LCCurrencyCodeCurrName"]
      """   Used to print as the suffix to the word amount line printed on checks.  For example:
One Hundred and 00/100 Dollars. In this case  "Dollars" is the CurrName  """  
      self.LCCurrencyCodeCurrDesc:str = obj["LCCurrencyCodeCurrDesc"]
      """  Description of the currency  """  
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
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      """  Full description for the Sales Tax category.  """  
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      """  Full description for the Tax Region.  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurMiscListTableset:
   def __init__(self, obj):
      self.PurMiscList:list[Erp_Tablesets_PurMiscListRow] = obj["PurMiscList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PurMiscRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.Description:str = obj["Description"]
      """  Description of the Miscellaneous Charge. Used as a default to Orders and Invoices.  """  
      self.TaxCatID:str = obj["TaxCatID"]
      """  Indicates the Tax Category for this Misc. charge. Can be blank or must be valid in the TaxCat master file.  """  
      self.ISCharge:str = obj["ISCharge"]
      """   Indicates whether this charge should be included in the calculation of Intrastat Statistical Value.  The valid values are:
"I" - Include this charge in the Intrastat Statistical Value
"E" - Do not include this charge in the Intrastat calculation
"P" - Apply a percentage of this charge in the Intrastat Statistical Value.  The actual percentage is stored in the BorderPct table.  """  
      self.LCFlag:bool = obj["LCFlag"]
      """  Indicates if the Miscellaneous Charge is for Landed Cost.  """  
      self.LCAmount:int = obj["LCAmount"]
      """  Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipts.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume (only for po releases tied to a container), Weight, Value, Quantity and Manual.  """  
      self.LCCurrencyCode:str = obj["LCCurrencyCode"]
      """  The Landed Cost Currency Code for this miscellaneous charge.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount or if is calculated as a percentage of the extended price.  """  
      self.EmpExpenseFlag:bool = obj["EmpExpenseFlag"]
      """  Indicates if the Miscellaneous Charge is for Employee Expenses.  """  
      self.ExpCommentRequired:bool = obj["ExpCommentRequired"]
      """  Indicates whether to require a value in PurMisc.ExpCommentText.  """  
      self.ExpCommentText:str = obj["ExpCommentText"]
      """  Comment  """  
      self.ExpUnitBased:bool = obj["ExpUnitBased"]
      """  When an expense charge, indicates if the code is unit based.  """  
      self.ExpChargeable:bool = obj["ExpChargeable"]
      """  When an expense charge, indicates if the code is chargeable.  """  
      self.ExpPMUID:int = obj["ExpPMUID"]
      """  When an expense charge, indicates the payment method of the code.  """  
      self.ExpIndirect:bool = obj["ExpIndirect"]
      """  When an expense charge, indicates if the code is to be selected for entry of indirect (non-project) expenses.  """  
      self.ExpTaxRegionCode:str = obj["ExpTaxRegionCode"]
      """  When an expense charge, indicates the tax liability of the code.  """  
      self.ExpProject:bool = obj["ExpProject"]
      """  When an expense charge, indicates if the code is be selected for entry of project expenses.  """  
      self.ExpDescription:str = obj["ExpDescription"]
      """  When used for expenses, a description of the expense.  """  
      self.GlobalPurMisc:bool = obj["GlobalPurMisc"]
      """  Marks this PurMisc as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.ExpAdvanceRequest:bool = obj["ExpAdvanceRequest"]
      """  When an expense charge, indicates if the code is be selected for entry of advance request expenses.  """  
      self.ExpJob:bool = obj["ExpJob"]
      """  When an expense charge, indicates if the code is be selected for entry of job expenses.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.Inactive:bool = obj["Inactive"]
      """  When an Expense Type is marked as Inactive it should NOT appear in the Expense Type drop down on Expense Entry  """  
      self.TakeDiscount:bool = obj["TakeDiscount"]
      """  Indicates if terms discount applies to the charge.  """  
      self.isAdValorem:bool = obj["isAdValorem"]
      """  Identifies if the amount added to a DUA invoice is Ad Valorem (CSF - Peru)  """  
      self.SendToFSA:bool = obj["SendToFSA"]
      """  True if the record should be synced to FSA, otherwise false.  """  
      self.ChargeCode:str = obj["ChargeCode"]
      """  UNCL5189 and UNCL7161  """  
      self.EnableEmpExpense:bool = obj["EnableEmpExpense"]
      """  Flag to indicate whether the EmpExpenseFlag should be enabled.  """  
      self.EnableUnitBased:bool = obj["EnableUnitBased"]
      """  Indicates whether the unit based field should be enabled in the ui form  """  
      self.MiscGLAcct:str = obj["MiscGLAcct"]
      """  Purchase Miscellaneous GL Account Number  """  
      self.MiscGLAcctDesc:str = obj["MiscGLAcctDesc"]
      """  Purchase Miscellaneous GL Account Description  """  
      self.TaxCatIDDesc:str = obj["TaxCatIDDesc"]
      """  Tax Category Description  """  
      self.BitFlag:int = obj["BitFlag"]
      self.LCCurrencyCodeCurrencyID:str = obj["LCCurrencyCodeCurrencyID"]
      self.LCCurrencyCodeCurrSymbol:str = obj["LCCurrencyCodeCurrSymbol"]
      self.LCCurrencyCodeDocumentDesc:str = obj["LCCurrencyCodeDocumentDesc"]
      self.LCCurrencyCodeCurrDesc:str = obj["LCCurrencyCodeCurrDesc"]
      self.LCCurrencyCodeCurrName:str = obj["LCCurrencyCodeCurrName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.TaxCatIDDescription:str = obj["TaxCatIDDescription"]
      self.TaxRgnDescription:str = obj["TaxRgnDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PurMiscTableset:
   def __init__(self, obj):
      self.PurMisc:list[Erp_Tablesets_PurMiscRow] = obj["PurMisc"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.PurMiscExpUB:list[Erp_Tablesets_PurMiscExpUBRow] = obj["PurMiscExpUB"]
      self.PurMiscVend:list[Erp_Tablesets_PurMiscVendRow] = obj["PurMiscVend"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PurMiscVendRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.MiscCode:str = obj["MiscCode"]
      """  Descriptive code assigned by user which uniquely identifies a Purchasing Misc charge/credit master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.LCAmount:int = obj["LCAmount"]
      """  Supplier specific Landed Cost amount in the specified document currency.  This will be the default when this miscellaneous charge is used as Indirect Cost during receipt for this supplier.  """  
      self.LCDisburseMethod:str = obj["LCDisburseMethod"]
      """  Identifies how the landed cost will be disbursed among the receipt details.  Valid options are Volume , Weight, Value, Quantity and Manual.  """  
      self.LCCurrencyCode:str = obj["LCCurrencyCode"]
      """  The Landed Cost Currency Code.  """  
      self.Percentage:int = obj["Percentage"]
      """  This field will be used to define the percentage of the extended amount that will be applied as the 'Miscellaneous charge'.  """  
      self.Type:str = obj["Type"]
      """  This field will define if the miscellaneous charge is calculated as a flat amount (A) or if is calculated as a percentage of the extended price (P).  """  
      self.GlobalPurMiscVend:bool = obj["GlobalPurMiscVend"]
      """  Marks this PurMiscVend as global, available to be sent out to other companies.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disables this record from receiving global updates.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.LCCurrencyCodeCurrName:str = obj["LCCurrencyCodeCurrName"]
      self.LCCurrencyCodeCurrSymbol:str = obj["LCCurrencyCodeCurrSymbol"]
      self.LCCurrencyCodeCurrDesc:str = obj["LCCurrencyCodeCurrDesc"]
      self.LCCurrencyCodeCurrencyID:str = obj["LCCurrencyCodeCurrencyID"]
      self.LCCurrencyCodeDocumentDesc:str = obj["LCCurrencyCodeDocumentDesc"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtPurMiscTableset:
   def __init__(self, obj):
      self.PurMisc:list[Erp_Tablesets_PurMiscRow] = obj["PurMisc"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.PurMiscExpUB:list[Erp_Tablesets_PurMiscExpUBRow] = obj["PurMiscExpUB"]
      self.PurMiscVend:list[Erp_Tablesets_PurMiscVendRow] = obj["PurMiscVend"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   miscCode
   """  
   def __init__(self, obj):
      self.miscCode:str = obj["miscCode"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PurMiscTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PurMiscTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PurMiscTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Name of the Table  """  
      self.fieldName:str = obj["fieldName"]
      """  Name of the Field  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_PurMiscListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewEntityGLC_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   key3
   key4
   key5
   key6
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.key3:str = obj["key3"]
      self.key4:str = obj["key4"]
      self.key5:str = obj["key5"]
      self.key6:str = obj["key6"]
      pass

class GetNewEntityGLC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPurMiscExpUB_input:
   """ Required : 
   ds
   miscCode
   fromEffectiveDate
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      self.miscCode:str = obj["miscCode"]
      self.fromEffectiveDate:str = obj["fromEffectiveDate"]
      pass

class GetNewPurMiscExpUB_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPurMiscVend_input:
   """ Required : 
   ds
   miscCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      self.miscCode:str = obj["miscCode"]
      pass

class GetNewPurMiscVend_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPurMisc_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

class GetNewPurMisc_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClausePurMisc
   whereClauseEntityGLC
   whereClausePurMiscExpUB
   whereClausePurMiscVend
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClausePurMisc:str = obj["whereClausePurMisc"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClausePurMiscExpUB:str = obj["whereClausePurMiscExpUB"]
      self.whereClausePurMiscVend:str = obj["whereClausePurMiscVend"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_PurMiscTableset] = obj["returnObj"]
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

class OnEmpExpenseFlagChange_input:
   """ Required : 
   ipEmpExpenseFlag
   ds
   """  
   def __init__(self, obj):
      self.ipEmpExpenseFlag:bool = obj["ipEmpExpenseFlag"]
      """  The proposed value for EmpExpenseFlag  """  
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

class OnEmpExpenseFlagChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnSupplierChange_input:
   """ Required : 
   ipSupplierID
   ds
   """  
   def __init__(self, obj):
      self.ipSupplierID:str = obj["ipSupplierID"]
      """  The Supplier ID  """  
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

class OnSupplierChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPurMiscTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtPurMiscTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_PurMiscTableset] = obj["ds"]
      pass

      """  output parameters  """  

