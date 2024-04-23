import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.LegalNumCnfgSvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumCnfgs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumCnfgs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumCnfgs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumCnfgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumCnfgs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumCnfgs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumCnfgRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumCnfgRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumCnfgs_Company_LegalNumberID(Company, LegalNumberID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumCnfg item
   Description: Calls GetByID to retrieve the LegalNumCnfg item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumCnfg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumCnfgRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumCnfgs_Company_LegalNumberID(Company, LegalNumberID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumCnfg for the service
   Description: Calls UpdateExt to update LegalNumCnfg. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumCnfg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumCnfgRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumCnfgs_Company_LegalNumberID(Company, LegalNumberID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumCnfg item
   Description: Call UpdateExt to delete LegalNumCnfg item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumCnfg
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumCnfgs_Company_LegalNumberID_LegalNumDocTypes(Company, LegalNumberID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LegalNumDocTypes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LegalNumDocTypes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumDocTypes",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumCnfgs_Company_LegalNumberID_LegalNumDocTypes_Company_LegalNumberID_TranDocTypeID(Company, LegalNumberID, TranDocTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumDocType item
   Description: Calls GetByID to retrieve the LegalNumDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumDocType1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumDocTypes(" + Company + "," + LegalNumberID + "," + TranDocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumCnfgs_Company_LegalNumberID_LegalNumPrefixes(Company, LegalNumberID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LegalNumPrefixes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LegalNumPrefixes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumPrefixRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumPrefixes",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumCnfgs_Company_LegalNumberID_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant(Company, LegalNumberID, Prefix, Plant, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumPrefix item
   Description: Calls GetByID to retrieve the LegalNumPrefix item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumPrefix1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param Prefix: Desc: Prefix   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumPrefixRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumCnfgs_Company_LegalNumberID_LegalNumSeqs(Company, LegalNumberID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LegalNumSeqs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LegalNumSeqs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumSeqs",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumCnfgs_Company_LegalNumberID_LegalNumSeqs_Company_LegalNumberID_DefaultPrefix_TransYear_TransYearSuffix_TransPeriod_SysRowID(Company, LegalNumberID, DefaultPrefix, TransYear, TransYearSuffix, TransPeriod, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumSeq item
   Description: Calls GetByID to retrieve the LegalNumSeq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumSeq1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param DefaultPrefix: Desc: DefaultPrefix   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param TransYearSuffix: Desc: TransYearSuffix   Required: True   Allow empty value : True
      :param TransPeriod: Desc: TransPeriod   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumCnfgs(" + Company + "," + LegalNumberID + ")/LegalNumSeqs(" + Company + "," + LegalNumberID + "," + DefaultPrefix + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumDocTypes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumDocTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumDocTypes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumDocTypes",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumDocTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumDocTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumDocTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumDocTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumDocTypes_Company_LegalNumberID_TranDocTypeID(Company, LegalNumberID, TranDocTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumDocType item
   Description: Calls GetByID to retrieve the LegalNumDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumDocTypes(" + Company + "," + LegalNumberID + "," + TranDocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumDocTypes_Company_LegalNumberID_TranDocTypeID(Company, LegalNumberID, TranDocTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumDocType for the service
   Description: Calls UpdateExt to update LegalNumDocType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumDocTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumDocTypes(" + Company + "," + LegalNumberID + "," + TranDocTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumDocTypes_Company_LegalNumberID_TranDocTypeID(Company, LegalNumberID, TranDocTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumDocType item
   Description: Call UpdateExt to delete LegalNumDocType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumDocTypes(" + Company + "," + LegalNumberID + "," + TranDocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumPrefixes(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumPrefixes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumPrefixes
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumPrefixRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumPrefixes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumPrefixes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumPrefixRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumPrefixRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant(Company, LegalNumberID, Prefix, Plant, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumPrefix item
   Description: Calls GetByID to retrieve the LegalNumPrefix item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumPrefix
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param Prefix: Desc: Prefix   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumPrefixRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant(Company, LegalNumberID, Prefix, Plant, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumPrefix for the service
   Description: Calls UpdateExt to update LegalNumPrefix. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumPrefix
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param Prefix: Desc: Prefix   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumPrefixRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant(Company, LegalNumberID, Prefix, Plant, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumPrefix item
   Description: Call UpdateExt to delete LegalNumPrefix item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumPrefix
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param Prefix: Desc: Prefix   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant_LegalNumSeqPrefixes(Company, LegalNumberID, Prefix, Plant, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get LegalNumSeqPrefixes items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_LegalNumSeqPrefixes1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param Prefix: Desc: Prefix   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumSeqPrefixRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")/LegalNumSeqPrefixes",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumPrefixes_Company_LegalNumberID_Prefix_Plant_LegalNumSeqPrefixes_Company_LegalNumberID_Prefix_Plant_TransYear_TransYearSuffix_TransPeriod_StartSequence(Company, LegalNumberID, Prefix, Plant, TransYear, TransYearSuffix, TransPeriod, StartSequence, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumSeqPrefix item
   Description: Calls GetByID to retrieve the LegalNumSeqPrefix item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumSeqPrefix1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param Prefix: Desc: Prefix   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param TransYearSuffix: Desc: TransYearSuffix   Required: True   Allow empty value : True
      :param TransPeriod: Desc: TransPeriod   Required: True
      :param StartSequence: Desc: StartSequence   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumSeqPrefixRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + ")/LegalNumSeqPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + StartSequence + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumSeqPrefixes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumSeqPrefixes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumSeqPrefixes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumSeqPrefixRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqPrefixes",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumSeqPrefixes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumSeqPrefixes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqPrefixRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqPrefixRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqPrefixes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumSeqPrefixes_Company_LegalNumberID_Prefix_Plant_TransYear_TransYearSuffix_TransPeriod_StartSequence(Company, LegalNumberID, Prefix, Plant, TransYear, TransYearSuffix, TransPeriod, StartSequence, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumSeqPrefix item
   Description: Calls GetByID to retrieve the LegalNumSeqPrefix item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumSeqPrefix
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param Prefix: Desc: Prefix   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param TransYearSuffix: Desc: TransYearSuffix   Required: True   Allow empty value : True
      :param TransPeriod: Desc: TransPeriod   Required: True
      :param StartSequence: Desc: StartSequence   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumSeqPrefixRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + StartSequence + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumSeqPrefixes_Company_LegalNumberID_Prefix_Plant_TransYear_TransYearSuffix_TransPeriod_StartSequence(Company, LegalNumberID, Prefix, Plant, TransYear, TransYearSuffix, TransPeriod, StartSequence, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumSeqPrefix for the service
   Description: Calls UpdateExt to update LegalNumSeqPrefix. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumSeqPrefix
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param Prefix: Desc: Prefix   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param TransYearSuffix: Desc: TransYearSuffix   Required: True   Allow empty value : True
      :param TransPeriod: Desc: TransPeriod   Required: True
      :param StartSequence: Desc: StartSequence   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqPrefixRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + StartSequence + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumSeqPrefixes_Company_LegalNumberID_Prefix_Plant_TransYear_TransYearSuffix_TransPeriod_StartSequence(Company, LegalNumberID, Prefix, Plant, TransYear, TransYearSuffix, TransPeriod, StartSequence, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumSeqPrefix item
   Description: Call UpdateExt to delete LegalNumSeqPrefix item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumSeqPrefix
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param Prefix: Desc: Prefix   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param TransYearSuffix: Desc: TransYearSuffix   Required: True   Allow empty value : True
      :param TransPeriod: Desc: TransPeriod   Required: True
      :param StartSequence: Desc: StartSequence   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqPrefixes(" + Company + "," + LegalNumberID + "," + Prefix + "," + Plant + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + StartSequence + ")",headers=creds) as resp:
           return await resp.json()

async def get_LegalNumSeqs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get LegalNumSeqs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_LegalNumSeqs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqs",headers=creds) as resp:
           return await resp.json()

async def post_LegalNumSeqs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_LegalNumSeqs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_LegalNumSeqs_Company_LegalNumberID_DefaultPrefix_TransYear_TransYearSuffix_TransPeriod_SysRowID(Company, LegalNumberID, DefaultPrefix, TransYear, TransYearSuffix, TransPeriod, SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the LegalNumSeq item
   Description: Calls GetByID to retrieve the LegalNumSeq item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_LegalNumSeq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param DefaultPrefix: Desc: DefaultPrefix   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param TransYearSuffix: Desc: TransYearSuffix   Required: True   Allow empty value : True
      :param TransPeriod: Desc: TransPeriod   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.LegalNumSeqRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqs(" + Company + "," + LegalNumberID + "," + DefaultPrefix + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_LegalNumSeqs_Company_LegalNumberID_DefaultPrefix_TransYear_TransYearSuffix_TransPeriod_SysRowID(Company, LegalNumberID, DefaultPrefix, TransYear, TransYearSuffix, TransPeriod, SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update LegalNumSeq for the service
   Description: Calls UpdateExt to update LegalNumSeq. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_LegalNumSeq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param DefaultPrefix: Desc: DefaultPrefix   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param TransYearSuffix: Desc: TransYearSuffix   Required: True   Allow empty value : True
      :param TransPeriod: Desc: TransPeriod   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.LegalNumSeqRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqs(" + Company + "," + LegalNumberID + "," + DefaultPrefix + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_LegalNumSeqs_Company_LegalNumberID_DefaultPrefix_TransYear_TransYearSuffix_TransPeriod_SysRowID(Company, LegalNumberID, DefaultPrefix, TransYear, TransYearSuffix, TransPeriod, SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete LegalNumSeq item
   Description: Call UpdateExt to delete LegalNumSeq item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_LegalNumSeq
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param LegalNumberID: Desc: LegalNumberID   Required: True   Allow empty value : True
      :param DefaultPrefix: Desc: DefaultPrefix   Required: True   Allow empty value : True
      :param TransYear: Desc: TransYear   Required: True
      :param TransYearSuffix: Desc: TransYearSuffix   Required: True   Allow empty value : True
      :param TransPeriod: Desc: TransPeriod   Required: True
      :param SysRowID: Desc: SysRowID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/LegalNumSeqs(" + Company + "," + LegalNumberID + "," + DefaultPrefix + "," + TransYear + "," + TransYearSuffix + "," + TransPeriod + "," + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AvailableDocTypes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AvailableDocTypes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AvailableDocTypes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AvailableDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableDocTypes",headers=creds) as resp:
           return await resp.json()

async def post_AvailableDocTypes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AvailableDocTypes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AvailableDocTypeRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AvailableDocTypeRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableDocTypes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AvailableDocTypes_Company_TranDocTypeID(Company, TranDocTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AvailableDocType item
   Description: Calls GetByID to retrieve the AvailableDocType item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AvailableDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AvailableDocTypeRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableDocTypes(" + Company + "," + TranDocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AvailableDocTypes_Company_TranDocTypeID(Company, TranDocTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AvailableDocType for the service
   Description: Calls UpdateExt to update AvailableDocType. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AvailableDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AvailableDocTypeRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableDocTypes(" + Company + "," + TranDocTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AvailableDocTypes_Company_TranDocTypeID(Company, TranDocTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AvailableDocType item
   Description: Call UpdateExt to delete AvailableDocType item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AvailableDocType
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param TranDocTypeID: Desc: TranDocTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableDocTypes(" + Company + "," + TranDocTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_AvailableLegalNumFormats(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get AvailableLegalNumFormats items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_AvailableLegalNumFormats
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.AvailableLegalNumFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableLegalNumFormats",headers=creds) as resp:
           return await resp.json()

async def post_AvailableLegalNumFormats(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_AvailableLegalNumFormats
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.AvailableLegalNumFormatRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.AvailableLegalNumFormatRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableLegalNumFormats", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_AvailableLegalNumFormats_SysRowID(SysRowID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the AvailableLegalNumFormat item
   Description: Calls GetByID to retrieve the AvailableLegalNumFormat item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_AvailableLegalNumFormat
      :param SysRowID: Desc: SysRowID   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.AvailableLegalNumFormatRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableLegalNumFormats(" + SysRowID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_AvailableLegalNumFormats_SysRowID(SysRowID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update AvailableLegalNumFormat for the service
   Description: Calls UpdateExt to update AvailableLegalNumFormat. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_AvailableLegalNumFormat
      :param SysRowID: Desc: SysRowID   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.AvailableLegalNumFormatRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableLegalNumFormats(" + SysRowID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_AvailableLegalNumFormats_SysRowID(SysRowID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete AvailableLegalNumFormat item
   Description: Call UpdateExt to delete AvailableLegalNumFormat item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_AvailableLegalNumFormat
      :param SysRowID: Desc: SysRowID   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/AvailableLegalNumFormats(" + SysRowID + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.LegalNumCnfgListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseLegalNumCnfg, whereClauseLegalNumDocType, whereClauseLegalNumPrefix, whereClauseLegalNumSeqPrefix, whereClauseLegalNumSeq, whereClauseAvailableDocType, whereClauseAvailableLegalNumFormat, pageSize, absolutePage, epicorHeaders = None):
   """  
   Summary: Invoke method GetRows
   Description: Returns a dataset containing all rows that satisfy the where clauses.
   OperationID: Get_GetRows
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseLegalNumCnfg=" + whereClauseLegalNumCnfg
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumDocType=" + whereClauseLegalNumDocType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumPrefix=" + whereClauseLegalNumPrefix
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumSeqPrefix=" + whereClauseLegalNumSeqPrefix
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseLegalNumSeq=" + whereClauseLegalNumSeq
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAvailableDocType=" + whereClauseAvailableDocType
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseAvailableLegalNumFormat=" + whereClauseAvailableLegalNumFormat
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(legalNumberID, epicorHeaders = None):
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
   params += "legalNumberID=" + legalNumberID

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: CODE TO PROVIDE PUBLIC METHOD TO RETRIEVE THE CORRESPONDING LIST OF DESCRIPTIONS FOR A CODE FIELD
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetTranDocType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetTranDocType
   Description: This method return the TranDoctType that has not already assinged to legalNumber
   OperationID: GetTranDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetTranDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetTranDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetMXTaxRcptType(epicorHeaders = None):
   """  
   Summary: Invoke method GetMXTaxRcptType
   Description: Getting Mexican Tax Receipt Type from Conpany configuration without parameters (by default)
   OperationID: GetMXTaxRcptType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetMXTaxRcptType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFormat
   Description: This method should be called if the Format changes.
   OperationID: OnChangeFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeGenSSCC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeGenSSCC
   Description: This method should be called if the Generate SSCC changes.
   OperationID: OnChangeGenSSCC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeGenSSCC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeGenSSCC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfGenerationOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfGenerationOption
   Description: This method is called when 'Generate On' (GenerationOption) is changed
   OperationID: OnChangeOfGenerationOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfGenerationOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfGenerationOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfGenerationType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfGenerationType
   Description: This method should be called if the Generation Type changes.
   OperationID: OnChangeOfGenerationType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfGenerationType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfGenerationType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfLegalNumberType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfLegalNumberType
   Description: This method should be called after the LegalNumberType comboBox changes.
   OperationID: OnChangeOfLegalNumberType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumberType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumberType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfNumberOption(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfNumberOption
   Description: This method should be called after the NumberOption comboBox changes.
   OperationID: OnChangeOfNumberOption
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfNumberOption_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfNumberOption_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfPrefixType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfPrefixType
   Description: This method should be called if the Prefix Type changes.
   OperationID: OnChangeOfPrefixType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfPrefixType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfPrefixType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfLegalNumCnfgAutomaticVoiding(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfLegalNumCnfgAutomaticVoiding
   Description: This method should be called after the Legal Number Configuration Automatic Voiding option changes.
   OperationID: OnChangeOfLegalNumCnfgAutomaticVoiding
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumCnfgAutomaticVoiding_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumCnfgAutomaticVoiding_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfLegalNumPrefix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfLegalNumPrefix
   Description: This method should be called if the LegalNumPrefix changes.
   OperationID: OnChangeOfLegalNumPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfLegalNumSeqEndSequence(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfLegalNumSeqEndSequence
   Description: This method should be called if the End Sequence changes.
   OperationID: OnChangeOfLegalNumSeqEndSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumSeqEndSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumSeqEndSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfLegalNumSeqPrefixEndSequence(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfLegalNumSeqPrefixEndSequence
   Description: This method should be called if the End Sequence changes.
   OperationID: OnChangeOfLegalNumSeqPrefixEndSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumSeqPrefixEndSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumSeqPrefixEndSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfLegalNumSeqStartSequence(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfLegalNumSeqStartSequence
   Description: This method should be called if the End Sequence changes.
   OperationID: OnChangeOfLegalNumSeqStartSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumSeqStartSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumSeqStartSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeOfLegalNumSeqPrefixStartSequence(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeOfLegalNumSeqPrefixStartSequence
   Description: This method should be called if the End Sequence changes.
   OperationID: OnChangeOfLegalNumSeqPrefixStartSequence
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeOfLegalNumSeqPrefixStartSequence_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeOfLegalNumSeqPrefixStartSequence_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ProcessPrefix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ProcessPrefix
   Description: This method should be called after changing the default prefix.  This method
checks for a modified ttLegalNumCnfg record so an update shouldn't be done
before calling this method (it needs the modified record to see what the old
default prefix was).
It will check to see if sequences have been created using the old default
sequence.  If opMsgText is not returned as null, it should be displayed to the
user as a Yes/No question.  If the user answers "Yes" then the method RemoveSequences
should be called.
   OperationID: ProcessPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ProcessPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ProcessPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_AltPrefixValidations(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method AltPrefixValidations
   Description: AltPrefixValidations
   OperationID: AltPrefixValidations
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/AltPrefixValidations_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/AltPrefixValidations_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveAltPrefix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveAltPrefix
   Description: RemoveAltPrefix
   OperationID: RemoveAltPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveAltPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveAltPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RemoveSequences(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RemoveSequences
   Description: This method should be called after calling the ProcessPrefix method and the user
answer "Yes" to the message returned from ProcessPrefix.  This method will remove
sequences that are using the old Default Prefix.
   OperationID: RemoveSequences
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RemoveSequences_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RemoveSequences_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetTaxLegalNumber(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetTaxLegalNumber
   Description: This method will remove Legal Number and Tax Print Date from TaxTran and void Legal Number on LegalNumHistory Table.
   OperationID: ResetTaxLegalNumber
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetTaxLegalNumber_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetTaxLegalNumber_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RetrievePaymentInfo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RetrievePaymentInfo
   Description: This method will build the Payment information using the parameters
passed into the method.
   OperationID: RetrievePaymentInfo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RetrievePaymentInfo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RetrievePaymentInfo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VoidLegalNumCnfg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VoidLegalNumCnfg
   Description: Purpose: Void Spoiled Legal Numbers.
Parameters:  dataset
Notes:
            
<param name="ds">legalNumCnfg is to used to set up the parameters used to generate legal numbers.</param>
   OperationID: VoidLegalNumCnfg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VoidLegalNumCnfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VoidLegalNumCnfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableFormatElements(epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableFormatElements
   Description: Load all Element available for the Legal Number format.
   OperationID: GetAvailableFormatElements
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableFormatElements_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetAvailableFormatElementsExclExceedSeparators(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetAvailableFormatElementsExclExceedSeparators
   Description: Load all Element available for the Legal Number format.
   OperationID: GetAvailableFormatElementsExclExceedSeparators
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetAvailableFormatElementsExclExceedSeparators_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAvailableFormatElementsExclExceedSeparators_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GenerateLegalNumberSample(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GenerateLegalNumberSample
   Description: Generate Legal Number Sample
   OperationID: GenerateLegalNumberSample
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GenerateLegalNumberSample_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GenerateLegalNumberSample_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetLegalNumberTypeList(epicorHeaders = None):
   """  
   Summary: Invoke method GetLegalNumberTypeList
   Description: Get list of Legal Number types
   OperationID: GetLegalNumberTypeList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetLegalNumberTypeList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetChangeLogDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetChangeLogDetails
   Description: Get Change Log for specific Legal Number
   OperationID: GetChangeLogDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetChangeLogDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetChangeLogDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLegalNumCnfg(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLegalNumCnfg
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumCnfg
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumCnfg_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumCnfg_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLegalNumDocType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLegalNumDocType
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumDocType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumDocType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumDocType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLegalNumPrefix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLegalNumPrefix
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLegalNumSeqPrefix(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLegalNumSeqPrefix
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumSeqPrefix
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumSeqPrefix_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumSeqPrefix_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewLegalNumSeq(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewLegalNumSeq
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewLegalNumSeq
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewLegalNumSeq_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewLegalNumSeq_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.LegalNumCnfgSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailableDocTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AvailableDocTypeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_AvailableLegalNumFormatRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_AvailableLegalNumFormatRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumCnfgListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumCnfgListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumCnfgRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumCnfgRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumDocTypeRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumDocTypeRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumPrefixRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumPrefixRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqPrefixRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumSeqPrefixRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_LegalNumSeqRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_LegalNumSeqRow] = obj["value"]
      pass

class Erp_Tablesets_AvailableDocTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Description:str = obj["Description"]
      self.SystemTranID:str = obj["SystemTranID"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AvailableLegalNumFormatRow:
   def __init__(self, obj):
      self.ElementCode:str = obj["ElementCode"]
      self.ElementDesc:str = obj["ElementDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumCnfgListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      """  The legal number identifier.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LegalNumberType:str = obj["LegalNumberType"]
      """  The type of legal number.  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  The legal number prefix.  """  
      self.GenerationType:str = obj["GenerationType"]
      """  Indicates how the number is generated.  Valid values are "system" and "manual".  """  
      self.DispAfterGen:bool = obj["DispAfterGen"]
      """  For system generated numbers, indicates if the number should be displayed to the user immediately after generation.  """  
      self.PrefixType:str = obj["PrefixType"]
      """  Indicates if the prefix is user defined or a selected journal code.  Valid values are "user" or "jrnlcode".  """  
      self.PrefixIsOverrideable:bool = obj["PrefixIsOverrideable"]
      """  For manual generation of legal numbers, indicates if the prefix can be overrided upon generation of the number.  """  
      self.NumberOption:str = obj["NumberOption"]
      """  Valid values are "Required" and "System".  """  
      self.LNCategory:str = obj["LNCategory"]
      """   The category of the legal number.  Valid options are:
DOC - Document legal number
TRAN - Transaction legal number  """  
      self.AllowPrefixesByPlant:bool = obj["AllowPrefixesByPlant"]
      """  Allow prefixes to be defined at the Site level.  """  
      self.UsePreNumberFmt:bool = obj["UsePreNumberFmt"]
      """  Indicates if pre-printed documents are used for printing.  """  
      self.AllowChangeAfterPrint:bool = obj["AllowChangeAfterPrint"]
      """  Indicates if changes can be made to a document after it has been printed.  """  
      self.NumLineDetails:int = obj["NumLineDetails"]
      """  Indicates the number of details lines that can be printed on a document per page.  """  
      self.ExcludeYrInNumber:bool = obj["ExcludeYrInNumber"]
      """  Indicates if the year should be excluded when generating a legal number.  """  
      self.Separator:str = obj["Separator"]
      """  The separator symbol fof the pieces that make up a legal number.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the legal number is active  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Reference to the fiscal calendar (Taiwan Localization field)  """  
      self.ExcludePerInNumber:bool = obj["ExcludePerInNumber"]
      """  Exclude Period (Taiwan Localization field)  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      """  The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  """  
      self.GenSSCC:bool = obj["GenSSCC"]
      """  Indicates if the Serial Shipment Container Code will be generated.  """  
      self.SeqLength:int = obj["SeqLength"]
      """  The length that the sequence can be, user will be able to set it from 1 to 10. And it will be filled with leading zeros if the sequence doesnt fit the defined seq length.  """  
      self.AllowPrefixesByWarehouse:bool = obj["AllowPrefixesByWarehouse"]
      """  Allow prefixes to be defined at Warehouse level.  """  
      self.AllowPrefixesByUser:bool = obj["AllowPrefixesByUser"]
      """  Allow prefixes to be defined at User level.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JournalCode:str = obj["JournalCode"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.LegalNumTypeDesc:str = obj["LegalNumTypeDesc"]
      """  The type of legal number.  """  
      self.OldDefaultPrefix:str = obj["OldDefaultPrefix"]
      """  The old default Prefix  """  
      self.VoidReason:str = obj["VoidReason"]
      """  The Reason of the void Legal Number Folios.  """  
      self.VoidYear:int = obj["VoidYear"]
      """  This field will be used to build Legal Number Folios.  """  
      self.FromFolio:str = obj["FromFolio"]
      """  Number of folios that start to be voided.  """  
      self.ToFolio:str = obj["ToFolio"]
      """  Last number of folios to be voided.  """  
      self.FromSeq:int = obj["FromSeq"]
      """  Inital sequence number from folio's number.  """  
      self.ToSeq:int = obj["ToSeq"]
      """  Last sequence number from folio's number.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumCnfgRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      """  The legal number identifier.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LegalNumberType:str = obj["LegalNumberType"]
      """  The type of legal number.  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  The legal number prefix.  """  
      self.GenerationType:str = obj["GenerationType"]
      """  Indicates how the number is generated.  Valid values are "system" and "manual".  """  
      self.DispAfterGen:bool = obj["DispAfterGen"]
      """  For system generated numbers, indicates if the number should be displayed to the user immediately after generation.  """  
      self.PrefixType:str = obj["PrefixType"]
      """  Indicates if the prefix is user defined or a selected journal code.  Valid values are "user" or "jrnlcode".  """  
      self.PrefixIsOverrideable:bool = obj["PrefixIsOverrideable"]
      """  For manual generation of legal numbers, indicates if the prefix can be overrided upon generation of the number.  """  
      self.NumberOption:str = obj["NumberOption"]
      """  Valid values are "Required" and "System".  """  
      self.LNCategory:str = obj["LNCategory"]
      """   The category of the legal number.  Valid options are:
DOC - Document legal number
TRAN - Transaction legal number  """  
      self.AllowPrefixesByPlant:bool = obj["AllowPrefixesByPlant"]
      """  Allow prefixes to be defined at the Site level.  """  
      self.UsePreNumberFmt:bool = obj["UsePreNumberFmt"]
      """  Indicates if pre-printed documents are used for printing.  """  
      self.AllowChangeAfterPrint:bool = obj["AllowChangeAfterPrint"]
      """  Indicates if changes can be made to a document after it has been printed.  """  
      self.NumLineDetails:int = obj["NumLineDetails"]
      """  Indicates the number of details lines that can be printed on a document per page.  """  
      self.ExcludeYrInNumber:bool = obj["ExcludeYrInNumber"]
      """  Indicates if the year should be excluded when generating a legal number.  """  
      self.Separator:str = obj["Separator"]
      """  The separator symbol fof the pieces that make up a legal number.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the legal number is active  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Reference to the fiscal calendar (Taiwan Localization field)  """  
      self.ExcludePerInNumber:bool = obj["ExcludePerInNumber"]
      """  Exclude Period (Taiwan Localization field)  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      """  The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  """  
      self.GenSSCC:bool = obj["GenSSCC"]
      """  Indicates if the Serial Shipment Container Code will be generated.  """  
      self.SeqLength:int = obj["SeqLength"]
      """  The length that the sequence can be, user will be able to set it from 1 to 10. And it will be filled with leading zeros if the sequence doesnt fit the defined seq length.  """  
      self.AllowPrefixesByWarehouse:bool = obj["AllowPrefixesByWarehouse"]
      """  Allow prefixes to be defined at Warehouse level.  """  
      self.AllowPrefixesByUser:bool = obj["AllowPrefixesByUser"]
      """  Allow prefixes to be defined at User level.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GenerationOption:str = obj["GenerationOption"]
      """  Indicates when the legal number should be generated. Available options depend on the combination of Number Type and Generation Type selected for the Legal Number.  """  
      self.AutomaticVoiding:bool = obj["AutomaticVoiding"]
      """  Automatically void the legal number when the document is deleted  """  
      self.AutomaticVoidingText:str = obj["AutomaticVoidingText"]
      """  The automatic voiding text  """  
      self.ChangeLog:bool = obj["ChangeLog"]
      """  Use Change Log to track changes.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Changed By  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.Format:str = obj["Format"]
      """  Stores the format defined to generate the Legal Number.  """  
      self.ConditionalSeparator:str = obj["ConditionalSeparator"]
      """  Separator is single character defined by user. It can be also used as Alternative Separator Character.  """  
      self.FreeText:str = obj["FreeText"]
      """  Free text defined by user to be used in Legal Numbers.  """  
      self.FiscalYearFormat:str = obj["FiscalYearFormat"]
      """  Defines whether the Fiscal Year is displayed with 4  or 2 digits .  """  
      self.FiscalPeriodLength:int = obj["FiscalPeriodLength"]
      """  Defines whether the FiscalPeriod is displayed with 1, 2, o 3 digits.  """  
      self.AddLeadingZero:bool = obj["AddLeadingZero"]
      """  Defines if Day is displayed with leading zeros or not.  """  
      self.EnableAutoGenerateOption:bool = obj["EnableAutoGenerateOption"]
      """  Determines if Automatic Generate Option is enabled.  """  
      self.EnableAutoVoidOption:bool = obj["EnableAutoVoidOption"]
      """  Determines if Automatic Voiding Option is enabled.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.FromFolio:str = obj["FromFolio"]
      """  Number of folios that start to be voided.  """  
      self.FromSeq:int = obj["FromSeq"]
      """  Inital sequence number from folio's number.  """  
      self.JournalCode:str = obj["JournalCode"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.LegalNumHistForeignKey:str = obj["LegalNumHistForeignKey"]
      """  Foreign Key from LegalNumHistory Table used on Peru CSF as reference to run LegalNumberVoiding process  """  
      self.LegalNumHistLegalNumber:str = obj["LegalNumHistLegalNumber"]
      """  Field for Peru CSF, Legal Number to be voided  """  
      self.LegalNumTypeDesc:str = obj["LegalNumTypeDesc"]
      self.MXTaxRcptType:str = obj["MXTaxRcptType"]
      """  This field will specify the working mode of the digital tax receipt functionality. Will have three possible values: "CFD", "CFDI" and "Disabled".  """  
      self.OldDefaultPrefix:str = obj["OldDefaultPrefix"]
      """  The old default Prefix  """  
      self.PayCheckNum:int = obj["PayCheckNum"]
      """  Check Number on payment, this field is used for Peru CSF  """  
      self.PayDocCheckAmt:int = obj["PayDocCheckAmt"]
      """  Document Check Amount on payment, this field is used for Peru CSF  """  
      self.PayDocTaxAmt:int = obj["PayDocTaxAmt"]
      """  Tax Amount on payment, this field is used for Peru CSF  """  
      self.PayVendorID:str = obj["PayVendorID"]
      """  Vendor ID on payment, this field is used for Peru CSF  """  
      self.PayVendorName:str = obj["PayVendorName"]
      """  Vendor Name on payment, this field is used for Peru CSF  """  
      self.ToFolio:str = obj["ToFolio"]
      """  Last number of folios to be voided.  """  
      self.ToSeq:int = obj["ToSeq"]
      """  Last sequence number from folio's number.  """  
      self.VoidReason:str = obj["VoidReason"]
      """  The Reason of the void Legal Number Folios.  """  
      self.VoidYear:int = obj["VoidYear"]
      """  This field will be used to build Legal Number Folios.  """  
      self.AutomaticGenerationList:str = obj["AutomaticGenerationList"]
      """  The list of automatic generation options  """  
      self.LegalNumberSample:str = obj["LegalNumberSample"]
      self.ExcludeYear:bool = obj["ExcludeYear"]
      """  Exclude Year in legal number format.  """  
      self.ExcludePeriod:bool = obj["ExcludePeriod"]
      """  Exclude period in legal number format.  """  
      self.INShippingPortCode:str = obj["INShippingPortCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumDocTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      """  The legal number identifier.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumPrefixRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      """  The legal number identifier.  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix value for a legal number.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.NumberOption:str = obj["NumberOption"]
      """  Valid values are "Required" and "System".  """  
      self.CnfgDefault:bool = obj["CnfgDefault"]
      """  Indicates if this is the default prefix for the legal number configuration.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse used for the prefix  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OldPrefix:str = obj["OldPrefix"]
      self.Description:str = obj["Description"]
      """  if Prefix is empty then [Blank Prefix] otherwise Prefix name.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.plantName:str = obj["plantName"]
      self.WarehseDescription:str = obj["WarehseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumSeqPrefixRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TransYear:int = obj["TransYear"]
      """  The transaction year the sequence applies to.  Based on a calendar year.  """  
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      """  The transaction year suffix.  """  
      self.Prefix:str = obj["Prefix"]
      """  The prefix used for this sequence when generating a legal number.  """  
      self.TransPeriod:int = obj["TransPeriod"]
      """  The transaction period.  """  
      self.NumberSeq:int = obj["NumberSeq"]
      """  The next available sequence number.  """  
      self.AvailFolios:int = obj["AvailFolios"]
      """  The number of pre-printed forms available for the sequence.  """  
      self.UsedFolios:int = obj["UsedFolios"]
      """  The number of folios used for this sequence.  """  
      self.StartSequence:int = obj["StartSequence"]
      """  Start Sequence (Taiwan Localization field)  """  
      self.EndSequence:int = obj["EndSequence"]
      """  End Sequence (Taiwan Localization field)  """  
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix used for the period. Available if TransPeriod > 0 (Taiwan Localization field)  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive (Taiwan Localization field)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGTableName:str = obj["AGTableName"]
      """  AGTableName  """  
      self.AGInvoiceNum:int = obj["AGInvoiceNum"]
      """  AGInvoiceNum  """  
      self.MXApprovalNum:int = obj["MXApprovalNum"]
      """  Approval Number (Mexico Localization field)  """  
      self.MXApprovalYear:int = obj["MXApprovalYear"]
      """  Approval Year (Mexico Localization field)  """  
      self.COExpirationDate:str = obj["COExpirationDate"]
      """  Expiration date for the sequence (Colombia Localization field)  """  
      self.CnfgDefault:bool = obj["CnfgDefault"]
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  Used as reference to LegalNumPrefix, because the Prefix field has Period symbol in the end.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.Plant:str = obj["Plant"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumSeqRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TransYear:int = obj["TransYear"]
      """  The transaction year the sequence applies to.  Based on a calendar year.  """  
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      """  The transaction year suffix.  """  
      self.Prefix:str = obj["Prefix"]
      """  The prefix used for this sequence when generating a legal number.  """  
      self.TransPeriod:int = obj["TransPeriod"]
      """  The transaction period.  """  
      self.NumberSeq:int = obj["NumberSeq"]
      """  The next available sequence number.  """  
      self.AvailFolios:int = obj["AvailFolios"]
      """  The number of pre-printed forms available for the sequence.  """  
      self.UsedFolios:int = obj["UsedFolios"]
      """  The number of folios used for this sequence.  """  
      self.StartSequence:int = obj["StartSequence"]
      """  Start Sequence (Taiwan Localization field)  """  
      self.EndSequence:int = obj["EndSequence"]
      """  End Sequence (Taiwan Localization field)  """  
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix used for the period. Available if TransPeriod > 0 (Taiwan Localization field)  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive (Taiwan Localization field)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGTableName:str = obj["AGTableName"]
      """  AGTableName  """  
      self.AGInvoiceNum:int = obj["AGInvoiceNum"]
      """  AGInvoiceNum  """  
      self.MXApprovalNum:int = obj["MXApprovalNum"]
      """  Approval Number (Mexico Localization field)  """  
      self.MXApprovalYear:int = obj["MXApprovalYear"]
      """  Approval Year (Mexico Localization field)  """  
      self.COExpirationDate:str = obj["COExpirationDate"]
      """  Expiration date for the sequence (Colombia Localization field)  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class AltPrefixValidations_input:
   """ Required : 
   ipLegalNumberID
   ovPrefix
   plPrefix
   whPrefix
   usPrefix
   ds
   """  
   def __init__(self, obj):
      self.ipLegalNumberID:str = obj["ipLegalNumberID"]
      self.ovPrefix:bool = obj["ovPrefix"]
      self.plPrefix:bool = obj["plPrefix"]
      self.whPrefix:bool = obj["whPrefix"]
      self.usPrefix:bool = obj["usPrefix"]
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class AltPrefixValidations_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      self.altPrefixExists:bool = obj["altPrefixExists"]
      self.opMsgText:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   legalNumberID
   """  
   def __init__(self, obj):
      self.legalNumberID:str = obj["legalNumberID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_AvailableDocTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.Description:str = obj["Description"]
      self.SystemTranID:str = obj["SystemTranID"]
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_AvailableLegalNumFormatRow:
   def __init__(self, obj):
      self.ElementCode:str = obj["ElementCode"]
      self.ElementDesc:str = obj["ElementDesc"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ChangeLogRow:
   def __init__(self, obj):
      self.ChangeLogID:int = obj["ChangeLogID"]
      self.Company:str = obj["Company"]
      self.SchemaName:str = obj["SchemaName"]
      self.TableName:str = obj["TableName"]
      self.CreatedBy:str = obj["CreatedBy"]
      self.Action:str = obj["Action"]
      self.Field:str = obj["Field"]
      self.OldValue:str = obj["OldValue"]
      self.NewValue:str = obj["NewValue"]
      self.CreatedOn:str = obj["CreatedOn"]
      self.FieldLabel:str = obj["FieldLabel"]
      self.ForeignKey:str = obj["ForeignKey"]
      self.SysRowID:str = obj["SysRowID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ChangeLogTableset:
   def __init__(self, obj):
      self.ChangeLog:list[Erp_Tablesets_ChangeLogRow] = obj["ChangeLog"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LegalNumCnfgListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      """  The legal number identifier.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LegalNumberType:str = obj["LegalNumberType"]
      """  The type of legal number.  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  The legal number prefix.  """  
      self.GenerationType:str = obj["GenerationType"]
      """  Indicates how the number is generated.  Valid values are "system" and "manual".  """  
      self.DispAfterGen:bool = obj["DispAfterGen"]
      """  For system generated numbers, indicates if the number should be displayed to the user immediately after generation.  """  
      self.PrefixType:str = obj["PrefixType"]
      """  Indicates if the prefix is user defined or a selected journal code.  Valid values are "user" or "jrnlcode".  """  
      self.PrefixIsOverrideable:bool = obj["PrefixIsOverrideable"]
      """  For manual generation of legal numbers, indicates if the prefix can be overrided upon generation of the number.  """  
      self.NumberOption:str = obj["NumberOption"]
      """  Valid values are "Required" and "System".  """  
      self.LNCategory:str = obj["LNCategory"]
      """   The category of the legal number.  Valid options are:
DOC - Document legal number
TRAN - Transaction legal number  """  
      self.AllowPrefixesByPlant:bool = obj["AllowPrefixesByPlant"]
      """  Allow prefixes to be defined at the Site level.  """  
      self.UsePreNumberFmt:bool = obj["UsePreNumberFmt"]
      """  Indicates if pre-printed documents are used for printing.  """  
      self.AllowChangeAfterPrint:bool = obj["AllowChangeAfterPrint"]
      """  Indicates if changes can be made to a document after it has been printed.  """  
      self.NumLineDetails:int = obj["NumLineDetails"]
      """  Indicates the number of details lines that can be printed on a document per page.  """  
      self.ExcludeYrInNumber:bool = obj["ExcludeYrInNumber"]
      """  Indicates if the year should be excluded when generating a legal number.  """  
      self.Separator:str = obj["Separator"]
      """  The separator symbol fof the pieces that make up a legal number.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the legal number is active  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Reference to the fiscal calendar (Taiwan Localization field)  """  
      self.ExcludePerInNumber:bool = obj["ExcludePerInNumber"]
      """  Exclude Period (Taiwan Localization field)  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      """  The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  """  
      self.GenSSCC:bool = obj["GenSSCC"]
      """  Indicates if the Serial Shipment Container Code will be generated.  """  
      self.SeqLength:int = obj["SeqLength"]
      """  The length that the sequence can be, user will be able to set it from 1 to 10. And it will be filled with leading zeros if the sequence doesnt fit the defined seq length.  """  
      self.AllowPrefixesByWarehouse:bool = obj["AllowPrefixesByWarehouse"]
      """  Allow prefixes to be defined at Warehouse level.  """  
      self.AllowPrefixesByUser:bool = obj["AllowPrefixesByUser"]
      """  Allow prefixes to be defined at User level.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.JournalCode:str = obj["JournalCode"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.LegalNumTypeDesc:str = obj["LegalNumTypeDesc"]
      """  The type of legal number.  """  
      self.OldDefaultPrefix:str = obj["OldDefaultPrefix"]
      """  The old default Prefix  """  
      self.VoidReason:str = obj["VoidReason"]
      """  The Reason of the void Legal Number Folios.  """  
      self.VoidYear:int = obj["VoidYear"]
      """  This field will be used to build Legal Number Folios.  """  
      self.FromFolio:str = obj["FromFolio"]
      """  Number of folios that start to be voided.  """  
      self.ToFolio:str = obj["ToFolio"]
      """  Last number of folios to be voided.  """  
      self.FromSeq:int = obj["FromSeq"]
      """  Inital sequence number from folio's number.  """  
      self.ToSeq:int = obj["ToSeq"]
      """  Last sequence number from folio's number.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumCnfgListTableset:
   def __init__(self, obj):
      self.LegalNumCnfgList:list[Erp_Tablesets_LegalNumCnfgListRow] = obj["LegalNumCnfgList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LegalNumCnfgRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      """  The legal number identifier.  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.LegalNumberType:str = obj["LegalNumberType"]
      """  The type of legal number.  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  The legal number prefix.  """  
      self.GenerationType:str = obj["GenerationType"]
      """  Indicates how the number is generated.  Valid values are "system" and "manual".  """  
      self.DispAfterGen:bool = obj["DispAfterGen"]
      """  For system generated numbers, indicates if the number should be displayed to the user immediately after generation.  """  
      self.PrefixType:str = obj["PrefixType"]
      """  Indicates if the prefix is user defined or a selected journal code.  Valid values are "user" or "jrnlcode".  """  
      self.PrefixIsOverrideable:bool = obj["PrefixIsOverrideable"]
      """  For manual generation of legal numbers, indicates if the prefix can be overrided upon generation of the number.  """  
      self.NumberOption:str = obj["NumberOption"]
      """  Valid values are "Required" and "System".  """  
      self.LNCategory:str = obj["LNCategory"]
      """   The category of the legal number.  Valid options are:
DOC - Document legal number
TRAN - Transaction legal number  """  
      self.AllowPrefixesByPlant:bool = obj["AllowPrefixesByPlant"]
      """  Allow prefixes to be defined at the Site level.  """  
      self.UsePreNumberFmt:bool = obj["UsePreNumberFmt"]
      """  Indicates if pre-printed documents are used for printing.  """  
      self.AllowChangeAfterPrint:bool = obj["AllowChangeAfterPrint"]
      """  Indicates if changes can be made to a document after it has been printed.  """  
      self.NumLineDetails:int = obj["NumLineDetails"]
      """  Indicates the number of details lines that can be printed on a document per page.  """  
      self.ExcludeYrInNumber:bool = obj["ExcludeYrInNumber"]
      """  Indicates if the year should be excluded when generating a legal number.  """  
      self.Separator:str = obj["Separator"]
      """  The separator symbol fof the pieces that make up a legal number.  """  
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if the legal number is active  """  
      self.FiscalCalendarID:str = obj["FiscalCalendarID"]
      """  Reference to the fiscal calendar (Taiwan Localization field)  """  
      self.ExcludePerInNumber:bool = obj["ExcludePerInNumber"]
      """  Exclude Period (Taiwan Localization field)  """  
      self.ExtensionDigit:int = obj["ExtensionDigit"]
      """  The extension digit is used to increase the capacity of the SSCC. It is assigned by the company that constructs the SSCC. Sometimes is used to identify the Package Type (P).  0=Case or carton. 1=Pallet (Larger than a case). 2=Container (larger than a pallet). 3=Undefined. 4=Internal company use. 5-8=Reserved. 9=Variable container.  """  
      self.GenSSCC:bool = obj["GenSSCC"]
      """  Indicates if the Serial Shipment Container Code will be generated.  """  
      self.SeqLength:int = obj["SeqLength"]
      """  The length that the sequence can be, user will be able to set it from 1 to 10. And it will be filled with leading zeros if the sequence doesnt fit the defined seq length.  """  
      self.AllowPrefixesByWarehouse:bool = obj["AllowPrefixesByWarehouse"]
      """  Allow prefixes to be defined at Warehouse level.  """  
      self.AllowPrefixesByUser:bool = obj["AllowPrefixesByUser"]
      """  Allow prefixes to be defined at User level.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GenerationOption:str = obj["GenerationOption"]
      """  Indicates when the legal number should be generated. Available options depend on the combination of Number Type and Generation Type selected for the Legal Number.  """  
      self.AutomaticVoiding:bool = obj["AutomaticVoiding"]
      """  Automatically void the legal number when the document is deleted  """  
      self.AutomaticVoidingText:str = obj["AutomaticVoidingText"]
      """  The automatic voiding text  """  
      self.ChangeLog:bool = obj["ChangeLog"]
      """  Use Change Log to track changes.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  Created By  """  
      self.CreatedOn:str = obj["CreatedOn"]
      """  Created On  """  
      self.ChangedBy:str = obj["ChangedBy"]
      """  Changed By  """  
      self.ChangedOn:str = obj["ChangedOn"]
      """  Changed On  """  
      self.Format:str = obj["Format"]
      """  Stores the format defined to generate the Legal Number.  """  
      self.ConditionalSeparator:str = obj["ConditionalSeparator"]
      """  Separator is single character defined by user. It can be also used as Alternative Separator Character.  """  
      self.FreeText:str = obj["FreeText"]
      """  Free text defined by user to be used in Legal Numbers.  """  
      self.FiscalYearFormat:str = obj["FiscalYearFormat"]
      """  Defines whether the Fiscal Year is displayed with 4  or 2 digits .  """  
      self.FiscalPeriodLength:int = obj["FiscalPeriodLength"]
      """  Defines whether the FiscalPeriod is displayed with 1, 2, o 3 digits.  """  
      self.AddLeadingZero:bool = obj["AddLeadingZero"]
      """  Defines if Day is displayed with leading zeros or not.  """  
      self.EnableAutoGenerateOption:bool = obj["EnableAutoGenerateOption"]
      """  Determines if Automatic Generate Option is enabled.  """  
      self.EnableAutoVoidOption:bool = obj["EnableAutoVoidOption"]
      """  Determines if Automatic Voiding Option is enabled.  """  
      self.FiscalCalDescription:str = obj["FiscalCalDescription"]
      self.FromFolio:str = obj["FromFolio"]
      """  Number of folios that start to be voided.  """  
      self.FromSeq:int = obj["FromSeq"]
      """  Inital sequence number from folio's number.  """  
      self.JournalCode:str = obj["JournalCode"]
      self.JrnlCodeJrnlDescription:str = obj["JrnlCodeJrnlDescription"]
      self.LegalNumHistForeignKey:str = obj["LegalNumHistForeignKey"]
      """  Foreign Key from LegalNumHistory Table used on Peru CSF as reference to run LegalNumberVoiding process  """  
      self.LegalNumHistLegalNumber:str = obj["LegalNumHistLegalNumber"]
      """  Field for Peru CSF, Legal Number to be voided  """  
      self.LegalNumTypeDesc:str = obj["LegalNumTypeDesc"]
      self.MXTaxRcptType:str = obj["MXTaxRcptType"]
      """  This field will specify the working mode of the digital tax receipt functionality. Will have three possible values: "CFD", "CFDI" and "Disabled".  """  
      self.OldDefaultPrefix:str = obj["OldDefaultPrefix"]
      """  The old default Prefix  """  
      self.PayCheckNum:int = obj["PayCheckNum"]
      """  Check Number on payment, this field is used for Peru CSF  """  
      self.PayDocCheckAmt:int = obj["PayDocCheckAmt"]
      """  Document Check Amount on payment, this field is used for Peru CSF  """  
      self.PayDocTaxAmt:int = obj["PayDocTaxAmt"]
      """  Tax Amount on payment, this field is used for Peru CSF  """  
      self.PayVendorID:str = obj["PayVendorID"]
      """  Vendor ID on payment, this field is used for Peru CSF  """  
      self.PayVendorName:str = obj["PayVendorName"]
      """  Vendor Name on payment, this field is used for Peru CSF  """  
      self.ToFolio:str = obj["ToFolio"]
      """  Last number of folios to be voided.  """  
      self.ToSeq:int = obj["ToSeq"]
      """  Last sequence number from folio's number.  """  
      self.VoidReason:str = obj["VoidReason"]
      """  The Reason of the void Legal Number Folios.  """  
      self.VoidYear:int = obj["VoidYear"]
      """  This field will be used to build Legal Number Folios.  """  
      self.AutomaticGenerationList:str = obj["AutomaticGenerationList"]
      """  The list of automatic generation options  """  
      self.LegalNumberSample:str = obj["LegalNumberSample"]
      self.ExcludeYear:bool = obj["ExcludeYear"]
      """  Exclude Year in legal number format.  """  
      self.ExcludePeriod:bool = obj["ExcludePeriod"]
      """  Exclude period in legal number format.  """  
      self.INShippingPortCode:str = obj["INShippingPortCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumCnfgTableset:
   def __init__(self, obj):
      self.LegalNumCnfg:list[Erp_Tablesets_LegalNumCnfgRow] = obj["LegalNumCnfg"]
      self.LegalNumDocType:list[Erp_Tablesets_LegalNumDocTypeRow] = obj["LegalNumDocType"]
      self.LegalNumPrefix:list[Erp_Tablesets_LegalNumPrefixRow] = obj["LegalNumPrefix"]
      self.LegalNumSeqPrefix:list[Erp_Tablesets_LegalNumSeqPrefixRow] = obj["LegalNumSeqPrefix"]
      self.LegalNumSeq:list[Erp_Tablesets_LegalNumSeqRow] = obj["LegalNumSeq"]
      self.AvailableDocType:list[Erp_Tablesets_AvailableDocTypeRow] = obj["AvailableDocType"]
      self.AvailableLegalNumFormat:list[Erp_Tablesets_AvailableLegalNumFormatRow] = obj["AvailableLegalNumFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_LegalNumDocTypeRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      """  The legal number identifier.  """  
      self.TranDocTypeID:str = obj["TranDocTypeID"]
      """  Transaction document type id.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumPrefixRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      """  The legal number identifier.  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix value for a legal number.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.NumberOption:str = obj["NumberOption"]
      """  Valid values are "Required" and "System".  """  
      self.CnfgDefault:bool = obj["CnfgDefault"]
      """  Indicates if this is the default prefix for the legal number configuration.  """  
      self.DcdUserID:str = obj["DcdUserID"]
      """  User ID  """  
      self.WarehouseCode:str = obj["WarehouseCode"]
      """  Warehouse used for the prefix  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.OldPrefix:str = obj["OldPrefix"]
      self.Description:str = obj["Description"]
      """  if Prefix is empty then [Blank Prefix] otherwise Prefix name.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.plantName:str = obj["plantName"]
      self.WarehseDescription:str = obj["WarehseDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumSeqPrefixRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TransYear:int = obj["TransYear"]
      """  The transaction year the sequence applies to.  Based on a calendar year.  """  
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      """  The transaction year suffix.  """  
      self.Prefix:str = obj["Prefix"]
      """  The prefix used for this sequence when generating a legal number.  """  
      self.TransPeriod:int = obj["TransPeriod"]
      """  The transaction period.  """  
      self.NumberSeq:int = obj["NumberSeq"]
      """  The next available sequence number.  """  
      self.AvailFolios:int = obj["AvailFolios"]
      """  The number of pre-printed forms available for the sequence.  """  
      self.UsedFolios:int = obj["UsedFolios"]
      """  The number of folios used for this sequence.  """  
      self.StartSequence:int = obj["StartSequence"]
      """  Start Sequence (Taiwan Localization field)  """  
      self.EndSequence:int = obj["EndSequence"]
      """  End Sequence (Taiwan Localization field)  """  
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix used for the period. Available if TransPeriod > 0 (Taiwan Localization field)  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive (Taiwan Localization field)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGTableName:str = obj["AGTableName"]
      """  AGTableName  """  
      self.AGInvoiceNum:int = obj["AGInvoiceNum"]
      """  AGInvoiceNum  """  
      self.MXApprovalNum:int = obj["MXApprovalNum"]
      """  Approval Number (Mexico Localization field)  """  
      self.MXApprovalYear:int = obj["MXApprovalYear"]
      """  Approval Year (Mexico Localization field)  """  
      self.COExpirationDate:str = obj["COExpirationDate"]
      """  Expiration date for the sequence (Colombia Localization field)  """  
      self.CnfgDefault:bool = obj["CnfgDefault"]
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      """  Used as reference to LegalNumPrefix, because the Prefix field has Period symbol in the end.  """  
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.Plant:str = obj["Plant"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_LegalNumSeqRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.TransYear:int = obj["TransYear"]
      """  The transaction year the sequence applies to.  Based on a calendar year.  """  
      self.TransYearSuffix:str = obj["TransYearSuffix"]
      """  The transaction year suffix.  """  
      self.Prefix:str = obj["Prefix"]
      """  The prefix used for this sequence when generating a legal number.  """  
      self.TransPeriod:int = obj["TransPeriod"]
      """  The transaction period.  """  
      self.NumberSeq:int = obj["NumberSeq"]
      """  The next available sequence number.  """  
      self.AvailFolios:int = obj["AvailFolios"]
      """  The number of pre-printed forms available for the sequence.  """  
      self.UsedFolios:int = obj["UsedFolios"]
      """  The number of folios used for this sequence.  """  
      self.StartSequence:int = obj["StartSequence"]
      """  Start Sequence (Taiwan Localization field)  """  
      self.EndSequence:int = obj["EndSequence"]
      """  End Sequence (Taiwan Localization field)  """  
      self.PeriodPrefix:str = obj["PeriodPrefix"]
      """  Prefix used for the period. Available if TransPeriod > 0 (Taiwan Localization field)  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive (Taiwan Localization field)  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AGTableName:str = obj["AGTableName"]
      """  AGTableName  """  
      self.AGInvoiceNum:int = obj["AGInvoiceNum"]
      """  AGInvoiceNum  """  
      self.MXApprovalNum:int = obj["MXApprovalNum"]
      """  Approval Number (Mexico Localization field)  """  
      self.MXApprovalYear:int = obj["MXApprovalYear"]
      """  Approval Year (Mexico Localization field)  """  
      self.COExpirationDate:str = obj["COExpirationDate"]
      """  Expiration date for the sequence (Colombia Localization field)  """  
      self.DefaultPrefix:str = obj["DefaultPrefix"]
      self.LegalNumberID:str = obj["LegalNumberID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtLegalNumCnfgTableset:
   def __init__(self, obj):
      self.LegalNumCnfg:list[Erp_Tablesets_LegalNumCnfgRow] = obj["LegalNumCnfg"]
      self.LegalNumDocType:list[Erp_Tablesets_LegalNumDocTypeRow] = obj["LegalNumDocType"]
      self.LegalNumPrefix:list[Erp_Tablesets_LegalNumPrefixRow] = obj["LegalNumPrefix"]
      self.LegalNumSeqPrefix:list[Erp_Tablesets_LegalNumSeqPrefixRow] = obj["LegalNumSeqPrefix"]
      self.LegalNumSeq:list[Erp_Tablesets_LegalNumSeqRow] = obj["LegalNumSeq"]
      self.AvailableDocType:list[Erp_Tablesets_AvailableDocTypeRow] = obj["AvailableDocType"]
      self.AvailableLegalNumFormat:list[Erp_Tablesets_AvailableLegalNumFormatRow] = obj["AvailableLegalNumFormat"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GenerateLegalNumberSample_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class GenerateLegalNumberSample_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetAvailableFormatElementsExclExceedSeparators_input:
   """ Required : 
   sSelectedFormatElemets
   """  
   def __init__(self, obj):
      self.sSelectedFormatElemets:str = obj["sSelectedFormatElemets"]
      pass

class GetAvailableFormatElementsExclExceedSeparators_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["returnObj"]
      pass

class GetAvailableFormatElements_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["returnObj"]
      pass

class GetByID_input:
   """ Required : 
   legalNumberID
   """  
   def __init__(self, obj):
      self.legalNumberID:str = obj["legalNumberID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["returnObj"]
      pass

class GetChangeLogDetails_input:
   """ Required : 
   LegalNumber
   """  
   def __init__(self, obj):
      self.LegalNumber:str = obj["LegalNumber"]
      pass

class GetChangeLogDetails_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_ChangeLogTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table Name  """  
      self.fieldName:str = obj["fieldName"]
      """  Field Name  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetLegalNumberTypeList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.sLegalNumberTypeList:str = obj["parameters"]
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
      self.returnObj:list[Erp_Tablesets_LegalNumCnfgListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetMXTaxRcptType_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetNewLegalNumCnfg_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class GetNewLegalNumCnfg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLegalNumDocType_input:
   """ Required : 
   ds
   legalNumberID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      self.legalNumberID:str = obj["legalNumberID"]
      pass

class GetNewLegalNumDocType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLegalNumPrefix_input:
   """ Required : 
   ds
   legalNumberID
   prefix
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      self.legalNumberID:str = obj["legalNumberID"]
      self.prefix:str = obj["prefix"]
      pass

class GetNewLegalNumPrefix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLegalNumSeqPrefix_input:
   """ Required : 
   ds
   legalNumberID
   prefix
   plant
   transYear
   transYearSuffix
   transPeriod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      self.legalNumberID:str = obj["legalNumberID"]
      self.prefix:str = obj["prefix"]
      self.plant:str = obj["plant"]
      self.transYear:int = obj["transYear"]
      self.transYearSuffix:str = obj["transYearSuffix"]
      self.transPeriod:int = obj["transPeriod"]
      pass

class GetNewLegalNumSeqPrefix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewLegalNumSeq_input:
   """ Required : 
   ds
   legalNumberID
   defaultPrefix
   transYear
   transYearSuffix
   transPeriod
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      self.legalNumberID:str = obj["legalNumberID"]
      self.defaultPrefix:str = obj["defaultPrefix"]
      self.transYear:int = obj["transYear"]
      self.transYearSuffix:str = obj["transYearSuffix"]
      self.transPeriod:int = obj["transPeriod"]
      pass

class GetNewLegalNumSeq_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseLegalNumCnfg
   whereClauseLegalNumDocType
   whereClauseLegalNumPrefix
   whereClauseLegalNumSeqPrefix
   whereClauseLegalNumSeq
   whereClauseAvailableDocType
   whereClauseAvailableLegalNumFormat
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseLegalNumCnfg:str = obj["whereClauseLegalNumCnfg"]
      self.whereClauseLegalNumDocType:str = obj["whereClauseLegalNumDocType"]
      self.whereClauseLegalNumPrefix:str = obj["whereClauseLegalNumPrefix"]
      self.whereClauseLegalNumSeqPrefix:str = obj["whereClauseLegalNumSeqPrefix"]
      self.whereClauseLegalNumSeq:str = obj["whereClauseLegalNumSeq"]
      self.whereClauseAvailableDocType:str = obj["whereClauseAvailableDocType"]
      self.whereClauseAvailableLegalNumFormat:str = obj["whereClauseAvailableLegalNumFormat"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetTranDocType_input:
   """ Required : 
   ipLegalNumberType
   ipLegalNumberID
   """  
   def __init__(self, obj):
      self.ipLegalNumberType:str = obj["ipLegalNumberType"]
      """  The current legalNumberType Number  """  
      self.ipLegalNumberID:str = obj["ipLegalNumberID"]
      """  The current legalNumberID Number  """  
      pass

class GetTranDocType_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["returnObj"]
      pass

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

class OnChangeFormat_input:
   """ Required : 
   sPreviousFormat
   sNewFormat
   """  
   def __init__(self, obj):
      self.sPreviousFormat:str = obj["sPreviousFormat"]
      """  Previous Legal Number format  """  
      self.sNewFormat:str = obj["sNewFormat"]
      """  New Legal Number format  """  
      pass

class OnChangeFormat_output:
   def __init__(self, obj):
      pass

class OnChangeGenSSCC_input:
   """ Required : 
   ipGenSSCC
   ds
   """  
   def __init__(self, obj):
      self.ipGenSSCC:bool = obj["ipGenSSCC"]
      """  The current Generate SSCC value  """  
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeGenSSCC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfGenerationOption_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfGenerationOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfGenerationType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfGenerationType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfLegalNumCnfgAutomaticVoiding_input:
   """ Required : 
   AutomaticVoiding
   ds
   """  
   def __init__(self, obj):
      self.AutomaticVoiding:bool = obj["AutomaticVoiding"]
      """  The Automatic Voiding Option  """  
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfLegalNumCnfgAutomaticVoiding_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfLegalNumPrefix_input:
   """ Required : 
   ColumnName
   ds
   """  
   def __init__(self, obj):
      self.ColumnName:str = obj["ColumnName"]
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfLegalNumPrefix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfLegalNumSeqEndSequence_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfLegalNumSeqEndSequence_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfLegalNumSeqPrefixEndSequence_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfLegalNumSeqPrefixEndSequence_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfLegalNumSeqPrefixStartSequence_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfLegalNumSeqPrefixStartSequence_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfLegalNumSeqStartSequence_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfLegalNumSeqStartSequence_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfLegalNumberType_input:
   """ Required : 
   ipLegalNumberType
   ds
   """  
   def __init__(self, obj):
      self.ipLegalNumberType:str = obj["ipLegalNumberType"]
      """  The current legalNumCnfg Number  """  
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfLegalNumberType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfNumberOption_input:
   """ Required : 
   ipNumberOption
   ds
   """  
   def __init__(self, obj):
      self.ipNumberOption:str = obj["ipNumberOption"]
      """  The Number Option  """  
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfNumberOption_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeOfPrefixType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class OnChangeOfPrefixType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ProcessPrefix_input:
   """ Required : 
   ipLegalNumberID
   proposedDefaultPrefix
   ds
   """  
   def __init__(self, obj):
      self.ipLegalNumberID:str = obj["ipLegalNumberID"]
      """  The current legalNumCnfg Number  """  
      self.proposedDefaultPrefix:str = obj["proposedDefaultPrefix"]
      """  Proposed default prefix  """  
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class ProcessPrefix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMsgText:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RemoveAltPrefix_input:
   """ Required : 
   ipLegalNumberID
   ovPrefix
   plPrefix
   whPrefix
   usPrefix
   ds
   """  
   def __init__(self, obj):
      self.ipLegalNumberID:str = obj["ipLegalNumberID"]
      self.ovPrefix:bool = obj["ovPrefix"]
      self.plPrefix:bool = obj["plPrefix"]
      self.whPrefix:bool = obj["whPrefix"]
      self.usPrefix:bool = obj["usPrefix"]
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class RemoveAltPrefix_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RemoveSequences_input:
   """ Required : 
   ipLegalNumberID
   ds
   """  
   def __init__(self, obj):
      self.ipLegalNumberID:str = obj["ipLegalNumberID"]
      """  Current legalNumCnfg Number  """  
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class RemoveSequences_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ResetTaxLegalNumber_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class ResetTaxLegalNumber_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RetrievePaymentInfo_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class RetrievePaymentInfo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLegalNumCnfgTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtLegalNumCnfgTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

class VoidLegalNumCnfg_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

class VoidLegalNumCnfg_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_LegalNumCnfgTableset] = obj["ds"]
      pass

      """  output parameters  """  

