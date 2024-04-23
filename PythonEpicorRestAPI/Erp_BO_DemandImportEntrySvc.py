import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.DemandImportEntrySvc
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_DemandImportEntries(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandImportEntries items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandImportEntries
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImportGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries",headers=creds) as resp:
           return await resp.json()

async def post_DemandImportEntries(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandImportEntries
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandImportEntries_Company_ImportID(Company, ImportID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandImportEntry item
   Description: Calls GetByID to retrieve the DemandImportEntry item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandImportEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries(" + Company + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandImportEntries_Company_ImportID(Company, ImportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandImportEntry for the service
   Description: Calls UpdateExt to update DemandImportEntry. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandImportEntry
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.ImportGrpRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries(" + Company + "," + ImportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandImportEntries_Company_ImportID(Company, ImportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandImportEntry item
   Description: Call UpdateExt to delete DemandImportEntry item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandImportEntry
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries(" + Company + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandImportEntries_Company_ImportID_DemandHeadImports(Company, ImportID, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemandHeadImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandHeadImports1
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandHeadImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries(" + Company + "," + ImportID + ")/DemandHeadImports",headers=creds) as resp:
           return await resp.json()

async def get_DemandImportEntries_Company_ImportID_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandHeadImport item
   Description: Calls GetByID to retrieve the DemandHeadImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandHeadImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandHeadImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandImportEntries(" + Company + "," + ImportID + ")/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandHeadImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandHeadImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandHeadImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandHeadImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports",headers=creds) as resp:
           return await resp.json()

async def post_DemandHeadImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandHeadImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandHeadImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandHeadImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandHeadImport item
   Description: Calls GetByID to retrieve the DemandHeadImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandHeadImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandHeadImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandHeadImport for the service
   Description: Calls UpdateExt to update DemandHeadImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandHeadImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandHeadImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandHeadImport item
   Description: Call UpdateExt to delete DemandHeadImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandHeadImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_PkgControlLabelValueImports(Company, ImportID, DemandContractNum, DemandHeadSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PkgControlLabelValueImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PkgControlLabelValueImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlLabelValueImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/PkgControlLabelValueImports",headers=creds) as resp:
           return await resp.json()

async def get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_PkgControlLabelValueImports_Company_Plant_ShipToCustID_ShipToNum_PartNum_DemandContractNum_DemandHeadSeq_ImportID(Company, ImportID, DemandContractNum, DemandHeadSeq, Plant, ShipToCustID, ShipToNum, PartNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlLabelValueImport item
   Description: Calls GetByID to retrieve the PkgControlLabelValueImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlLabelValueImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ShipToCustID: Desc: ShipToCustID   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/PkgControlLabelValueImports(" + Company + "," + Plant + "," + ShipToCustID + "," + ShipToNum + "," + PartNum + "," + DemandContractNum + "," + DemandHeadSeq + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDetailImports(Company, ImportID, DemandContractNum, DemandHeadSeq, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemandDetailImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandDetailImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandDetailImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandDetailImports",headers=creds) as resp:
           return await resp.json()

async def get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandDetailImport item
   Description: Calls GetByID to retrieve the DemandDetailImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandDetailImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandDetailImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandMiscChgImportDHs(Company, ImportID, DemandContractNum, DemandHeadSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemandMiscChgImportDHs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandMiscChgImportDHs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgImportDHRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandMiscChgImportDHs",headers=creds) as resp:
           return await resp.json()

async def get_DemandHeadImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandMiscChgImportDHs_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandMiscChgImportDH item
   Description: Calls GetByID to retrieve the DemandMiscChgImportDH item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgImportDH1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportDHRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandHeadImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + ")/DemandMiscChgImportDHs(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_PkgControlLabelValueImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PkgControlLabelValueImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PkgControlLabelValueImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PkgControlLabelValueImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/PkgControlLabelValueImports",headers=creds) as resp:
           return await resp.json()

async def post_PkgControlLabelValueImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PkgControlLabelValueImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/PkgControlLabelValueImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PkgControlLabelValueImports_Company_Plant_ShipToCustID_ShipToNum_PartNum_DemandContractNum_DemandHeadSeq_ImportID(Company, Plant, ShipToCustID, ShipToNum, PartNum, DemandContractNum, DemandHeadSeq, ImportID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PkgControlLabelValueImport item
   Description: Calls GetByID to retrieve the PkgControlLabelValueImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PkgControlLabelValueImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ShipToCustID: Desc: ShipToCustID   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/PkgControlLabelValueImports(" + Company + "," + Plant + "," + ShipToCustID + "," + ShipToNum + "," + PartNum + "," + DemandContractNum + "," + DemandHeadSeq + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PkgControlLabelValueImports_Company_Plant_ShipToCustID_ShipToNum_PartNum_DemandContractNum_DemandHeadSeq_ImportID(Company, Plant, ShipToCustID, ShipToNum, PartNum, DemandContractNum, DemandHeadSeq, ImportID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PkgControlLabelValueImport for the service
   Description: Calls UpdateExt to update PkgControlLabelValueImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PkgControlLabelValueImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ShipToCustID: Desc: ShipToCustID   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PkgControlLabelValueImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/PkgControlLabelValueImports(" + Company + "," + Plant + "," + ShipToCustID + "," + ShipToNum + "," + PartNum + "," + DemandContractNum + "," + DemandHeadSeq + "," + ImportID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PkgControlLabelValueImports_Company_Plant_ShipToCustID_ShipToNum_PartNum_DemandContractNum_DemandHeadSeq_ImportID(Company, Plant, ShipToCustID, ShipToNum, PartNum, DemandContractNum, DemandHeadSeq, ImportID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PkgControlLabelValueImport item
   Description: Call UpdateExt to delete PkgControlLabelValueImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PkgControlLabelValueImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param Plant: Desc: Plant   Required: True   Allow empty value : True
      :param ShipToCustID: Desc: ShipToCustID   Required: True   Allow empty value : True
      :param ShipToNum: Desc: ShipToNum   Required: True   Allow empty value : True
      :param PartNum: Desc: PartNum   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/PkgControlLabelValueImports(" + Company + "," + Plant + "," + ShipToCustID + "," + ShipToNum + "," + PartNum + "," + DemandContractNum + "," + DemandHeadSeq + "," + ImportID + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandDetailImports(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandDetailImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandDetailImports
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandDetailImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports",headers=creds) as resp:
           return await resp.json()

async def post_DemandDetailImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandDetailImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandDetailImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandDetailImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandDetailImport item
   Description: Calls GetByID to retrieve the DemandDetailImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandDetailImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandDetailImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandDetailImport for the service
   Description: Calls UpdateExt to update DemandDetailImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandDetailImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandDetailImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandDetailImport item
   Description: Call UpdateExt to delete DemandDetailImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandDetailImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandMiscChgImports(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemandMiscChgImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandMiscChgImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandMiscChgImports",headers=creds) as resp:
           return await resp.json()

async def get_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandMiscChgImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandMiscChgImport item
   Description: Calls GetByID to retrieve the DemandMiscChgImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandMiscChgImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleImports(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get DemandScheduleImports items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_DemandScheduleImports1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandScheduleImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandScheduleImports",headers=creds) as resp:
           return await resp.json()

async def get_DemandDetailImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, DemandScheduleSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandScheduleImport item
   Description: Calls GetByID to retrieve the DemandScheduleImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandScheduleImport1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param DemandScheduleSeq: Desc: DemandScheduleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandScheduleImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandDetailImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + ")/DemandScheduleImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandMiscChgImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandMiscChgImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandMiscChgImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImports",headers=creds) as resp:
           return await resp.json()

async def post_DemandMiscChgImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandMiscChgImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandMiscChgImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandMiscChgImport item
   Description: Calls GetByID to retrieve the DemandMiscChgImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandMiscChgImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandMiscChgImport for the service
   Description: Calls UpdateExt to update DemandMiscChgImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandMiscChgImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandMiscChgImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandMiscChgImport item
   Description: Call UpdateExt to delete DemandMiscChgImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandMiscChgImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandScheduleImports(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandScheduleImports items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandScheduleImports
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandScheduleImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandScheduleImports",headers=creds) as resp:
           return await resp.json()

async def post_DemandScheduleImports(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandScheduleImports
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandScheduleImportRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandScheduleImportRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandScheduleImports", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandScheduleImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, DemandScheduleSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandScheduleImport item
   Description: Calls GetByID to retrieve the DemandScheduleImport item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandScheduleImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param DemandScheduleSeq: Desc: DemandScheduleSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandScheduleImportRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandScheduleImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandScheduleImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, DemandScheduleSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandScheduleImport for the service
   Description: Calls UpdateExt to update DemandScheduleImport. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandScheduleImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param DemandScheduleSeq: Desc: DemandScheduleSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandScheduleImportRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandScheduleImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandScheduleImports_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_DemandScheduleSeq(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, DemandScheduleSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandScheduleImport item
   Description: Call UpdateExt to delete DemandScheduleImport item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandScheduleImport
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param DemandScheduleSeq: Desc: DemandScheduleSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandScheduleImports(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + DemandScheduleSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_DemandMiscChgImportDHs(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get DemandMiscChgImportDHs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_DemandMiscChgImportDHs
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.DemandMiscChgImportDHRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImportDHs",headers=creds) as resp:
           return await resp.json()

async def post_DemandMiscChgImportDHs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_DemandMiscChgImportDHs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportDHRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportDHRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImportDHs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_DemandMiscChgImportDHs_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the DemandMiscChgImportDH item
   Description: Calls GetByID to retrieve the DemandMiscChgImportDH item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_DemandMiscChgImportDH
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportDHRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImportDHs(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_DemandMiscChgImportDHs_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update DemandMiscChgImportDH for the service
   Description: Calls UpdateExt to update DemandMiscChgImportDH. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_DemandMiscChgImportDH
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.DemandMiscChgImportDHRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImportDHs(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_DemandMiscChgImportDHs_Company_ImportID_DemandContractNum_DemandHeadSeq_DemandDtlSeq_SeqNum(Company, ImportID, DemandContractNum, DemandHeadSeq, DemandDtlSeq, SeqNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete DemandMiscChgImportDH item
   Description: Call UpdateExt to delete DemandMiscChgImportDH item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_DemandMiscChgImportDH
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param ImportID: Desc: ImportID   Required: True   Allow empty value : True
      :param DemandContractNum: Desc: DemandContractNum   Required: True
      :param DemandHeadSeq: Desc: DemandHeadSeq   Required: True
      :param DemandDtlSeq: Desc: DemandDtlSeq   Required: True
      :param SeqNum: Desc: SeqNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/DemandMiscChgImportDHs(" + Company + "," + ImportID + "," + DemandContractNum + "," + DemandHeadSeq + "," + DemandDtlSeq + "," + SeqNum + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.ImportGrpListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseImportGrp, whereClauseDemandHeadImport, whereClausePkgControlLabelValueImport, whereClauseDemandDetailImport, whereClauseDemandMiscChgImport, whereClauseDemandScheduleImport, whereClauseDemandMiscChgImportDH, pageSize, absolutePage, epicorHeaders = None):
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
   params += "whereClauseImportGrp=" + whereClauseImportGrp
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemandHeadImport=" + whereClauseDemandHeadImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePkgControlLabelValueImport=" + whereClausePkgControlLabelValueImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemandDetailImport=" + whereClauseDemandDetailImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemandMiscChgImport=" + whereClauseDemandMiscChgImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemandScheduleImport=" + whereClauseDemandScheduleImport
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseDemandMiscChgImportDH=" + whereClauseDemandMiscChgImportDH
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(company, importID, epicorHeaders = None):
   """  
   Summary: Invoke method GetByID
   Description: Returns a DataSet given the primary key.
   OperationID: Get_GetByID
   Required: True   Allow empty value : True
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
   params += "company=" + company
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailDemandContractLine(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailDemandContractLine
   Description: Update Demand Detail information when the Demand Contract Line is changed.
   OperationID: ChangeDemandDetailDemandContractLine
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailDemandContractLine_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailDemandContractLine_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailMktgCamp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailMktgCamp
   Description: Update MktgCampaign on the DmdCntDtl.
   OperationID: ChangeDemandDetailMktgCamp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailMktgCamp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailMktgCamp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailPartNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailPartNum
   Description: Update partnum on the DmdCntDtl.
   OperationID: ChangeDemandDetailPartNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailPartNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailPartNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandDetailRevisionNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandDetailRevisionNum
   Description: Update Demand Detail information when the Part Revision Number is changed.
   OperationID: ChangeDemandDetailRevisionNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandDetailRevisionNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandDetailRevisionNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadCustID
   Description: Method to call when changing the Customer ID on the DemandHead record.
Validates the Customer ID and ressets the ShipTo to the Customer default.
   OperationID: ChangeDemandHeadCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadDemandContract(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadDemandContract
   Description: Update Demand Header information when the Demand Contract is changed.
   OperationID: ChangeDemandHeadDemandContract
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadDemandContract_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadDemandContract_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadERSOrder(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadERSOrder
   Description: Update Demand Header information when the ERS Order changes.
   OperationID: ChangeDemandHeadERSOrder
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadERSOrder_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadERSOrder_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadShipToCustID
   Description: Method to call when changing the ShipTo Customer ID on the DemandHead record.
Validates the ShipTo Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandHeadShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadShipToNum
   Description: Update Demand Header information when the Ship To Num changes.
   OperationID: ChangeDemandHeadShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandHeadUseOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandHeadUseOTS
   Description: Method to call when changing the UseOTS field the DemandHead record.
Refreshes the address list and contact info
   OperationID: ChangeDemandHeadUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandHeadUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandHeadUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleMarkForNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleMarkForNum
   Description: Update DemandSchedule information with values from the Mark For when the Mark For is changed.
   OperationID: ChangeDemandScheduleMarkForNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleMarkForNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleMarkForNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleMFCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleMFCustID
   Description: Method to call when changing the Mark For Customer ID on the DemandSchedule record.
Validates the Mark For Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandScheduleMFCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleMFCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleMFCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleOTSDetails(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleOTSDetails
   Description: Method to call when changing the OTS fields the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleOTSDetails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleOTSDetails_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleOTSDetails_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandSchedulePlant(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandSchedulePlant
   Description: Update DemandSchedule information with values from the Plant when the Plant is changed.
   OperationID: ChangeDemandSchedulePlant
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandSchedulePlant_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandSchedulePlant_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleSellingReqQty(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleSellingReqQty
   Description: Update Demand Schedule information when the Selling Req Qty is changed.
   OperationID: ChangeDemandScheduleSellingReqQty
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleSellingReqQty_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleSellingReqQty_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleShipToCustID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleShipToCustID
   Description: Method to call when changing the ShipTo Customer ID on the DemandSchedule record.
Validates the ShipTo Customer ID and ressets the ShipToNum to the Customer default.
   OperationID: ChangeDemandScheduleShipToCustID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleShipToCustID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleShipToCustID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleShipToNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleShipToNum
   Description: Update DemandSchedule information with values from the Ship To when the Ship To is changed.
   OperationID: ChangeDemandScheduleShipToNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleShipToNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleShipToNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleUseOTMF(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleUseOTMF
   Description: Method to call when changing the UseOTMF field the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleUseOTMF
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleUseOTMF_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleUseOTMF_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeDemandScheduleUseOTS(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeDemandScheduleUseOTS
   Description: Method to call when changing the UseOTS field the DemandSchedule record.
Refreshes the address list and contact info
   OperationID: ChangeDemandScheduleUseOTS
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeDemandScheduleUseOTS_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeDemandScheduleUseOTS_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeMiscCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeMiscCode
   Description: This method returns default information for the MiscChrg.  Method must use
parameters instead of the dataset due to the problem with changing the primary key field.
Also allows IMDemandMiscChgDH and IMDemandMiscChg to use the same code
   OperationID: ChangeMiscCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeMiscCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeMiscCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPartRevisionChange(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPartRevisionChange
   Description: The method is to be run on leave of the PartNum and Revision fields
before the ChangePart, ChangeRevision, or Update methods are run.
When run before CreateOrderFromQuote, the Part Number expected is the part number
from the quote.
This returns all the questions that need to be asked before a part can be changed.
   OperationID: CheckPartRevisionChange
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPartRevisionChange_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPartRevisionChange_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPriceDiscrepancy(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPriceDiscrepancy
   Description: Check if the differente between the UnitPrice and EDIUnitPrice is less than the value defd in
the PriceTolerance field of the ShipTo or Customer tables.
   OperationID: GetPriceDiscrepancy
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPriceDiscrepancy_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPriceDiscrepancy_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ReadyToProcess(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ReadyToProcess
   Description: Method to remove the Error Flag to the Demand PO records identified by the IntQueID.
   OperationID: ReadyToProcess
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ReadyToProcess_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ReadyToProcess_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportEDIb4Tran(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportEDIb4Tran
   Description: This method does nothing. It is defined exclusively to integrate BPMs with ImportEDI process.
   OperationID: ImportEDIb4Tran
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportEDIb4Tran_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportEDIb4Tran_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportEDIb4Val(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportEDIb4Val
   Description: This method does nothing. It is defined exclusively to integrate BPMs with ImportEDI process.
   OperationID: ImportEDIb4Val
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportEDIb4Val_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportEDIb4Val_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportEDIPreProcessDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportEDIPreProcessDemand
   Description: This method does nothing. It is defined exclusively to integrate BPMs with ImportEDI process.
   OperationID: ImportEDIPreProcessDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportEDIPreProcessDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportEDIPreProcessDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportEDIPostProcessDemand(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportEDIPostProcessDemand
   Description: This method does nothing. It is defined exclusively to integrate BPMs with ImportEDI process.
   OperationID: ImportEDIPostProcessDemand
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportEDIPostProcessDemand_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportEDIPostProcessDemand_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ImportEDIOnUDImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ImportEDIOnUDImport
   Description: This method does nothing. It is defined exclusively to integrate BPMs with ImportEDI process.
   OperationID: ImportEDIOnUDImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ImportEDIOnUDImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ImportEDIOnUDImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateOTSTaxID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateOTSTaxID
   Description: OTS Tax Id validation
   OperationID: ValidateOTSTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateOTSTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateOTSTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewImportGrp(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewImportGrp
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewImportGrp
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewImportGrp_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewImportGrp_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandHeadImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandHeadImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandHeadImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandHeadImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandHeadImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPkgControlLabelValueImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPkgControlLabelValueImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPkgControlLabelValueImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPkgControlLabelValueImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPkgControlLabelValueImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandDetailImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandDetailImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandDetailImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandDetailImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandDetailImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandMiscChgImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandMiscChgImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandMiscChgImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandMiscChgImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandMiscChgImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandScheduleImport(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandScheduleImport
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandScheduleImport
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandScheduleImport_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandScheduleImport_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewDemandMiscChgImportDH(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewDemandMiscChgImportDH
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewDemandMiscChgImportDH
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewDemandMiscChgImportDH_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewDemandMiscChgImportDH_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.DemandImportEntrySvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandDetailImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandDetailImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandHeadImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandHeadImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportDHRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandMiscChgImportDHRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandMiscChgImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandMiscChgImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_DemandScheduleImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_DemandScheduleImportRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ImportGrpListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_ImportGrpRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_ImportGrpRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PkgControlLabelValueImportRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PkgControlLabelValueImportRow] = obj["value"]
      pass

class Erp_Tablesets_DemandDetailImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  DemandContractNum  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  DemandDtlSeq  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  DemandContractLine  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  TestRecord  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.OrderLine:int = obj["OrderLine"]
      """  OrderLine  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  DoNotShipBeforeDate  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  DoNotShipAfterDate  """  
      self.DemandReference:str = obj["DemandReference"]
      """  DemandReference  """  
      self.LineDesc:str = obj["LineDesc"]
      """  LineDesc  """  
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.SalesUM:str = obj["SalesUM"]
      """  SalesUM  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  DiscountPercent  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  UnitPrice  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  PricePerCode  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  PriceGroupCode  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  QuoteNum  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  QuoteLine  """  
      self.POType:str = obj["POType"]
      """  POType  """  
      self.AcknowledgementType:str = obj["AcknowledgementType"]
      """  AcknowledgementType  """  
      self.ScheduleType:str = obj["ScheduleType"]
      """  ScheduleType  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """  SellingFactor  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  SellingFactorDirection  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.PONum:str = obj["PONum"]
      """  PONum  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  RejectedByUser  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.XPartNum:str = obj["XPartNum"]
      """  XPartNum  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  UsePriceList  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  RejectedBySystem  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  OverrideSystemReject  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  OpenLine  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  DemandCharacter01  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  DemandCharacter02  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  DemandCharacter03  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  DemandCharacter04  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  DemandNumber01  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  DemandNumber02  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  DemandNumber03  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  DemandNumber04  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  DemandDate01  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  DemandDate02  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  DemandDate03  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  DemandDate04  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  DemandLogical01  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  DemandLogical02  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  DemandLogical03  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  DemandLogical04  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  DeleteCurrentReleases  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  MktgCampaignID  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  MktgEvntSeq  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  XRefPartNum  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  XRefPartType  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  XRefCustNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  XRevisionNum  """  
      self.EDIUnitPrice:int = obj["EDIUnitPrice"]
      """  EDIUnitPrice  """  
      self.CumulativeQty:int = obj["CumulativeQty"]
      """  CumulativeQty  """  
      self.CumulativeDate:str = obj["CumulativeDate"]
      """  CumulativeDate  """  
      self.StartCumQty:int = obj["StartCumQty"]
      """  StartCumQty  """  
      self.StartCumDate:str = obj["StartCumDate"]
      """  StartCumDate  """  
      self.LastShipmentID:int = obj["LastShipmentID"]
      """  LastShipmentID  """  
      self.LastShipmentQty:int = obj["LastShipmentQty"]
      """  LastShipmentQty  """  
      self.LastShipmentDate:str = obj["LastShipmentDate"]
      """  LastShipmentDate  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  ScheduleNumber  """  
      self.LastMasterPack:int = obj["LastMasterPack"]
      """  LastMasterPack  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  DocUnitPrice  """  
      self.DocEDIUnitPrice:int = obj["DocEDIUnitPrice"]
      """  DocEDIUnitPrice  """  
      self.InternalPrice:int = obj["InternalPrice"]
      """  InternalPrice  """  
      self.DocInternalPrice:int = obj["DocInternalPrice"]
      """  DocInternalPrice  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  SmartStringProcessed  """  
      self.SmartString:str = obj["SmartString"]
      """  SmartString  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  BasePartNum  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  LastConfigDate  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  LastConfigTime  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  LastConfigUserID  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """  ConfigUnitPrice  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  ConfigBaseUnitPrice  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  BaseRevisionNum  """  
      self.TPQuoteNum:int = obj["TPQuoteNum"]
      """  TPQuoteNum  """  
      self.TPQuoteLine:int = obj["TPQuoteLine"]
      """  TPQuoteLine  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Rpt1UnitPrice  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Rpt2UnitPrice  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Rpt3UnitPrice  """  
      self.Rpt1InternalPrice:int = obj["Rpt1InternalPrice"]
      """  Rpt1InternalPrice  """  
      self.Rpt2InternalPrice:int = obj["Rpt2InternalPrice"]
      """  Rpt2InternalPrice  """  
      self.Rpt3InternalPrice:int = obj["Rpt3InternalPrice"]
      """  Rpt3InternalPrice  """  
      self.Rpt1EDIUnitPrice:int = obj["Rpt1EDIUnitPrice"]
      """  Rpt1EDIUnitPrice  """  
      self.Rpt2EDIUnitPrice:int = obj["Rpt2EDIUnitPrice"]
      """  Rpt2EDIUnitPrice  """  
      self.Rpt3EDIUnitPrice:int = obj["Rpt3EDIUnitPrice"]
      """  Rpt3EDIUnitPrice  """  
      self.ErrorList:str = obj["ErrorList"]
      """  ErrorList  """  
      self.EDICustom01:str = obj["EDICustom01"]
      """  EDICustom01  """  
      self.EDICustom02:str = obj["EDICustom02"]
      """  EDICustom02  """  
      self.EDICustom03:str = obj["EDICustom03"]
      """  EDICustom03  """  
      self.EDICustom04:str = obj["EDICustom04"]
      """  EDICustom04  """  
      self.EDICustom05:str = obj["EDICustom05"]
      """  EDICustom05  """  
      self.EDICustom06:str = obj["EDICustom06"]
      """  EDICustom06  """  
      self.EDICustom07:str = obj["EDICustom07"]
      """  EDICustom07  """  
      self.EDICustom08:str = obj["EDICustom08"]
      """  EDICustom08  """  
      self.EDICustom09:str = obj["EDICustom09"]
      """  EDICustom09  """  
      self.EDICustom10:str = obj["EDICustom10"]
      """  EDICustom10  """  
      self.BlockProcLine:bool = obj["BlockProcLine"]
      """  BlockProcLine  """  
      self.POLineRef:str = obj["POLineRef"]
      """  POLineRef  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.Configured:str = obj["Configured"]
      self.DmdContractNum:int = obj["DmdContractNum"]
      self.MultipleXRef:bool = obj["MultipleXRef"]
      self.PriceDiscrepancy:bool = obj["PriceDiscrepancy"]
      self.BitFlag:int = obj["BitFlag"]
      self.DemandContractDtlSalesUM:str = obj["DemandContractDtlSalesUM"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      self.PlantName:str = obj["PlantName"]
      self.PriceGroupDescription:str = obj["PriceGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandHeadImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  DemandContractNum  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.PONum:str = obj["PONum"]
      """  PONum  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  DoNotShipBeforeDate  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  DoNotShipAfterDate  """  
      self.CancelAfterDate:str = obj["CancelAfterDate"]
      """  CancelAfterDate  """  
      self.FOB:str = obj["FOB"]
      """  FOB  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipViaCode  """  
      self.TermsCode:str = obj["TermsCode"]
      """  TermsCode  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  AllocPriorityCode  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  ReservePriorityCode  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  ShipOrderComplete  """  
      self.OrderComment:str = obj["OrderComment"]
      """  OrderComment  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  InvoiceComment  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  AutoOrderBasedDisc  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  TestRecord  """  
      self.POType:str = obj["POType"]
      """  POType  """  
      self.AcknowledgementType:str = obj["AcknowledgementType"]
      """  AcknowledgementType  """  
      self.AcceptType:str = obj["AcceptType"]
      """  AcceptType  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  ScheduleNumber  """  
      self.ScheduleNumberSeq:int = obj["ScheduleNumberSeq"]
      """  ScheduleNumberSeq  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.LockRate:bool = obj["LockRate"]
      """  LockRate  """  
      self.Accepted:bool = obj["Accepted"]
      """  Accepted  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  RejectedByUser  """  
      self.OpenDemand:bool = obj["OpenDemand"]
      """  OpenDemand  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  RejectedBySystem  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  OverrideSystemReject  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  DemandCharacter01  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  DemandCharacter02  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  DemandCharacter03  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  DemandCharacter04  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  DemandNumber01  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  DemandNumber02  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  DemandNumber03  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  DemandNumber04  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  DemandDate01  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  DemandDate02  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  DemandDate03  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  DemandDate04  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  DemandLogical01  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  DemandLogical02  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  DemandLogical03  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  DemandLogical04  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  BTCustNum  """  
      self.EDIOrder:bool = obj["EDIOrder"]
      """  EDIOrder  """  
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  SelectedForProcessing  """  
      self.SCProcessing:bool = obj["SCProcessing"]
      """  SCProcessing  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  ReadyToProcess  """  
      self.ResetCums:bool = obj["ResetCums"]
      """  ResetCums  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  ERSOrder  """  
      self.CancelPO:bool = obj["CancelPO"]
      """  CancelPO  """  
      self.CreateNewOrder:bool = obj["CreateNewOrder"]
      """  CreateNewOrder  """  
      self.LinkedOrders:str = obj["LinkedOrders"]
      """  LinkedOrders  """  
      self.TCtrlNum:str = obj["TCtrlNum"]
      """  TCtrlNum  """  
      self.BatchNum:str = obj["BatchNum"]
      """  BatchNum  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  QuoteNum  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  DemandProcessDate  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  DemandProcessTime  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.CustomerTradingPartnerName:str = obj["CustomerTradingPartnerName"]
      """  CustomerTradingPartnerName  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.DemandContract:str = obj["DemandContract"]
      """  DemandContract  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  CustomerCustID  """  
      self.BTCustomerCustID:str = obj["BTCustomerCustID"]
      """  BTCustomerCustID  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  ShipToCustID  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  UseOTS  """  
      self.OTSName:str = obj["OTSName"]
      """  OTSName  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  OTSAddress1  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  OTSAddress2  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  OTSAddress3  """  
      self.OTSCity:str = obj["OTSCity"]
      """  OTSCity  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  OTSResaleID  """  
      self.OTSState:str = obj["OTSState"]
      """  OTSState  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  OTSZIP  """  
      self.EDIOTSCountry:str = obj["EDIOTSCountry"]
      """  EDIOTSCountry  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  OTSFaxNum  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  OTSPhoneNum  """  
      self.OTSContact:str = obj["OTSContact"]
      """  OTSContact  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  OTSSaveCustID  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  OTSSaveAs  """  
      self.ErrorList:str = obj["ErrorList"]
      """  ErrorList  """  
      self.EDICustom01:str = obj["EDICustom01"]
      """  EDICustom01  """  
      self.EDICustom02:str = obj["EDICustom02"]
      """  EDICustom02  """  
      self.EDICustom03:str = obj["EDICustom03"]
      """  EDICustom03  """  
      self.EDICustom04:str = obj["EDICustom04"]
      """  EDICustom04  """  
      self.EDICustom05:str = obj["EDICustom05"]
      """  EDICustom05  """  
      self.EDICustom06:str = obj["EDICustom06"]
      """  EDICustom06  """  
      self.EDICustom07:str = obj["EDICustom07"]
      """  EDICustom07  """  
      self.EDICustom08:str = obj["EDICustom08"]
      """  EDICustom08  """  
      self.EDICustom09:str = obj["EDICustom09"]
      """  EDICustom09  """  
      self.EDICustom10:str = obj["EDICustom10"]
      """  EDICustom10  """  
      self.ShipByTime:int = obj["ShipByTime"]
      """  ShipByTime  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  OTSCountryNum  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTSTaxRegionCode  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  OTSCustSaved  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      """  OTSSaved  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTSShipToNum  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  ShipToCustNum  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      self.EDI_OTSCountry:str = obj["EDI_OTSCountry"]
      self.ERSOverride:bool = obj["ERSOverride"]
      self.OpenContract:bool = obj["OpenContract"]
      self.OTSCountryDescription:str = obj["OTSCountryDescription"]
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.Tran_Type:str = obj["Tran_Type"]
      """  Tran_Type  """  
      self.CustAddrList:str = obj["CustAddrList"]
      self.DmdContractNum:int = obj["DmdContractNum"]
      self.DocumentName:str = obj["DocumentName"]
      self.CustAddrFormatted:str = obj["CustAddrFormatted"]
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustomerBTName:str = obj["BTCustomerBTName"]
      self.BTCustomerCustID_:str = obj["BTCustomerCustID_"]
      self.BTCustomerName:str = obj["BTCustomerName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerZip:str = obj["CustomerZip"]
      self.CustomerState:str = obj["CustomerState"]
      self.CustomerCountry:str = obj["CustomerCountry"]
      self.CustomerCity:str = obj["CustomerCity"]
      self.CustomerTradingPartnerName_:str = obj["CustomerTradingPartnerName_"]
      self.CustomerAddress1:str = obj["CustomerAddress1"]
      self.CustomerAddress2:str = obj["CustomerAddress2"]
      self.CustomerAddress3:str = obj["CustomerAddress3"]
      self.CustomerAllowShipTo3:bool = obj["CustomerAllowShipTo3"]
      self.CustomerAllowOTS:bool = obj["CustomerAllowOTS"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.OTSCountryEUMember:bool = obj["OTSCountryEUMember"]
      self.OTSCountryISOCode:str = obj["OTSCountryISOCode"]
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandMiscChgImportDHRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  DemandContractNum  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  DemandDtlSeq  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  MiscAmt  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  DocMiscAmt  """  
      self.FreqCode:str = obj["FreqCode"]
      """  FreqCode  """  
      self.Quoting:str = obj["Quoting"]
      """  Quoting  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Rpt1MiscAmt  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Rpt2MiscAmt  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Rpt3MiscAmt  """  
      self.Percentage:int = obj["Percentage"]
      """  Percentage  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorList:str = obj["ErrorList"]
      """  ErrorList  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandMiscChgImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  DemandContractNum  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  DemandDtlSeq  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  MiscAmt  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  DocMiscAmt  """  
      self.FreqCode:str = obj["FreqCode"]
      """  FreqCode  """  
      self.Quoting:str = obj["Quoting"]
      """  Quoting  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Rpt1MiscAmt  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Rpt2MiscAmt  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Rpt3MiscAmt  """  
      self.Percentage:int = obj["Percentage"]
      """  Percentage  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorList:str = obj["ErrorList"]
      """  ErrorList  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandScheduleImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  DemandContractNum  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  DemandDtlSeq  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  DemandScheduleSeq  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.OurReqQty:int = obj["OurReqQty"]
      """  OurReqQty  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipViaCode  """  
      self.SellingReqQty:int = obj["SellingReqQty"]
      """  SellingReqQty  """  
      self.ReqDate:str = obj["ReqDate"]
      """  ReqDate  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.MarkForNum:str = obj["MarkForNum"]
      """  MarkForNum  """  
      self.DeliveryDays:int = obj["DeliveryDays"]
      """  DeliveryDays  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  ScheduleNumber  """  
      self.DemandType:str = obj["DemandType"]
      """  DemandType  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.OrderLine:int = obj["OrderLine"]
      """  OrderLine  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  OrderRelNum  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  RejectedByUser  """  
      self.RAN:str = obj["RAN"]
      """  RAN  """  
      self.DemandReference:str = obj["DemandReference"]
      """  DemandReference  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  RejectedBySystem  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  OverrideSystemReject  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.OpenSchedule:bool = obj["OpenSchedule"]
      """  OpenSchedule  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  DemandCharacter01  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  DemandCharacter02  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  DemandCharacter03  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  DemandCharacter04  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  DemandNumber01  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  DemandNumber02  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  DemandNumber03  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  DemandNumber04  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  DemandDate01  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  DemandDate02  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  DemandDate03  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  DemandDate04  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  DemandLogical01  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  DemandLogical02  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  DemandLogical03  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  DemandLogical04  """  
      self.DocumentName:str = obj["DocumentName"]
      """  DocumentName  """  
      self.ForecastEndDate:str = obj["ForecastEndDate"]
      """  ForecastEndDate  """  
      self.DockingStation:str = obj["DockingStation"]
      """  DockingStation  """  
      self.Location:str = obj["Location"]
      """  Location  """  
      self.TransportID:str = obj["TransportID"]
      """  TransportID  """  
      self.ShipbyTime:int = obj["ShipbyTime"]
      """  ShipbyTime  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  UseOTS  """  
      self.OTSName:str = obj["OTSName"]
      """  OTSName  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  OTSAddress1  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  OTSAddress2  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  OTSAddress3  """  
      self.OTSCity:str = obj["OTSCity"]
      """  OTSCity  """  
      self.OTSState:str = obj["OTSState"]
      """  OTSState  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  OTSZIP  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  OTSResaleID  """  
      self.OTSContact:str = obj["OTSContact"]
      """  OTSContact  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  OTSFaxNum  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  OTSPhoneNum  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  OTSCountryNum  """  
      self.SubShipTo:str = obj["SubShipTo"]
      """  SubShipTo  """  
      self.ShipRouting:str = obj["ShipRouting"]
      """  ShipRouting  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  ShipToCustNum  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTSTaxRegionCode  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.ProcessDate:str = obj["ProcessDate"]
      """  ProcessDate  """  
      self.ProcessTime:int = obj["ProcessTime"]
      """  ProcessTime  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  MFCustNum  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  UseOTMF  """  
      self.OTMFName:str = obj["OTMFName"]
      """  OTMFName  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  OTMFAddress1  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  OTMFAddress2  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  OTMFAddress3  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  OTMFCity  """  
      self.OTMFState:str = obj["OTMFState"]
      """  OTMFState  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  OTMFZIP  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  OTMFContact  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  OTMFFaxNum  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  OTMFPhoneNum  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  OTMFCountryNum  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  QuoteNum  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  QuoteLine  """  
      self.QuoteRelNum:int = obj["QuoteRelNum"]
      """  QuoteRelNum  """  
      self.CTPNeedByDate:str = obj["CTPNeedByDate"]
      """  CTPNeedByDate  """  
      self.CTPShipDate:str = obj["CTPShipDate"]
      """  CTPShipDate  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SalesUM:str = obj["SalesUM"]
      """  SalesUM  """  
      self.ShipToCustomerCustID:str = obj["ShipToCustomerCustID"]
      """  ShipToCustomerCustID  """  
      self.MFCustomerCustID:str = obj["MFCustomerCustID"]
      """  MFCustomerCustID  """  
      self.OTSCountryDescription:str = obj["OTSCountryDescription"]
      """  OTSCountryDescription  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  OTSSaveCustID  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  OTSSaveAs  """  
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      """  OTMFCountryDescription  """  
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.ErrorList:str = obj["ErrorList"]
      """  ErrorList  """  
      self.EDICustom01:str = obj["EDICustom01"]
      """  EDICustom01  """  
      self.EDICustom02:str = obj["EDICustom02"]
      """  EDICustom02  """  
      self.EDICustom03:str = obj["EDICustom03"]
      """  EDICustom03  """  
      self.EDICustom04:str = obj["EDICustom04"]
      """  EDICustom04  """  
      self.EDICustom05:str = obj["EDICustom05"]
      """  EDICustom05  """  
      self.EDICustom06:str = obj["EDICustom06"]
      """  EDICustom06  """  
      self.EDICustom07:str = obj["EDICustom07"]
      """  EDICustom07  """  
      self.EDICustom08:str = obj["EDICustom08"]
      """  EDICustom08  """  
      self.EDICustom09:str = obj["EDICustom09"]
      """  EDICustom09  """  
      self.EDICustom10:str = obj["EDICustom10"]
      """  EDICustom10  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  OTSCustSaved  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      """  OTSSaved  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTSShipToNum  """  
      self.CTPManualConfirm:bool = obj["CTPManualConfirm"]
      """  The value will be set to true  if a manual CTP calculation was confirmed for this demand schedule. It will prevent auto CTP calculation for this demand schedule during process demand.  """  
      self.CTPSource:str = obj["CTPSource"]
      """  The value will be set to the calculated CapPromiseDtl  JobNum (Source)  if a manual CTP calculation was confirmed for this demand schedule.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.DmdContractNum:int = obj["DmdContractNum"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.MarkForAddrFormatted:str = obj["MarkForAddrFormatted"]
      self.ShipToAddrFormatted:str = obj["ShipToAddrFormatted"]
      self.BitFlag:int = obj["BitFlag"]
      self.MFCustomerBTName:str = obj["MFCustomerBTName"]
      self.MFCustomerCustID_:str = obj["MFCustomerCustID_"]
      self.MFCustomerName:str = obj["MFCustomerName"]
      self.OTMFCountryDescription_:str = obj["OTMFCountryDescription_"]
      self.OTSCountryEUMember:bool = obj["OTSCountryEUMember"]
      self.OTSCountryDescription_:str = obj["OTSCountryDescription_"]
      self.OTSCountryISOCode:str = obj["OTSCountryISOCode"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.ShipToCustomerName:str = obj["ShipToCustomerName"]
      self.ShipToCustomerCustID_:str = obj["ShipToCustomerCustID_"]
      self.ShipToCustomerBTName:str = obj["ShipToCustomerBTName"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.ImportType:str = obj["ImportType"]
      """  ImportType  """  
      self.ErrorFlag:bool = obj["ErrorFlag"]
      """  ErrorFlag  """  
      self.Status:str = obj["Status"]
      """  Status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DisplayImportID:str = obj["DisplayImportID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.ImportType:str = obj["ImportType"]
      """  ImportType  """  
      self.ErrorFlag:bool = obj["ErrorFlag"]
      """  ErrorFlag  """  
      self.Status:str = obj["Status"]
      """  Status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IntError:bool = obj["IntError"]
      self.DisplayImportID:str = obj["DisplayImportID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlLabelValueImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  The CustID associated with this Ship To.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship To number.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this DemandSchedule is related to.  """  
      self.ImportID:int = obj["ImportID"]
      """  The Import ID.  """  
      self.LabelValue01:str = obj["LabelValue01"]
      """  Value to display on package control label.  """  
      self.LabelValue02:str = obj["LabelValue02"]
      """  Value to display on package control label.  """  
      self.LabelValue03:str = obj["LabelValue03"]
      """  Value to display on package control label.  """  
      self.LabelValue04:str = obj["LabelValue04"]
      """  Value to display on package control label.  """  
      self.LabelValue05:str = obj["LabelValue05"]
      """  Value to display on package control label.  """  
      self.LabelValue06:str = obj["LabelValue06"]
      """  Value to display on package control label.  """  
      self.LabelValue07:str = obj["LabelValue07"]
      """  Value to display on package control label.  """  
      self.LabelValue08:str = obj["LabelValue08"]
      """  Value to display on package control label.  """  
      self.LabelValue09:str = obj["LabelValue09"]
      """  Value to display on package control label.  """  
      self.LabelValue10:str = obj["LabelValue10"]
      """  Value to display on package control label.  """  
      self.LabelValue11:str = obj["LabelValue11"]
      """  Value to display on package control label.  """  
      self.LabelValue12:str = obj["LabelValue12"]
      """  Value to display on package control label.  """  
      self.LabelValue13:str = obj["LabelValue13"]
      """  Value to display on package control label.  """  
      self.LabelValue14:str = obj["LabelValue14"]
      """  Value to display on package control label.  """  
      self.LabelValue15:str = obj["LabelValue15"]
      """  Value to display on package control label.  """  
      self.LabelValue16:str = obj["LabelValue16"]
      """  Value to display on package control label.  """  
      self.LabelValue17:str = obj["LabelValue17"]
      """  Value to display on package control label.  """  
      self.LabelValue18:str = obj["LabelValue18"]
      """  Value to display on package control label.  """  
      self.LabelValue19:str = obj["LabelValue19"]
      """  Value to display on package control label.  """  
      self.LabelValue20:str = obj["LabelValue20"]
      """  Value to display on package control label.  """  
      self.LabelValue21:str = obj["LabelValue21"]
      """  Value to display on package control label.  """  
      self.LabelValue22:str = obj["LabelValue22"]
      """  Value to display on package control label.  """  
      self.LabelValue23:str = obj["LabelValue23"]
      """  Value to display on package control label.  """  
      self.LabelValue24:str = obj["LabelValue24"]
      """  Value to display on package control label.  """  
      self.LabelValue25:str = obj["LabelValue25"]
      """  Value to display on package control label.  """  
      self.LabelValue26:str = obj["LabelValue26"]
      """  Value to display on package control label.  """  
      self.LabelValue27:str = obj["LabelValue27"]
      """  Value to display on package control label.  """  
      self.LabelValue28:str = obj["LabelValue28"]
      """  Value to display on package control label.  """  
      self.LabelValue29:str = obj["LabelValue29"]
      """  Value to display on package control label.  """  
      self.LabelValue30:str = obj["LabelValue30"]
      """  Value to display on package control label.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date that record was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID for the user who created this record.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  Date that record was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID for the user who last updated this record.  """  
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
class ChangeDemandDetailDemandContractLine_input:
   """ Required : 
   proposedDemandContractLine
   ds
   """  
   def __init__(self, obj):
      self.proposedDemandContractLine:int = obj["proposedDemandContractLine"]
      """  The proposed Demand Contract Line  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandDetailDemandContractLine_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandDetailMktgCamp_input:
   """ Required : 
   iMktgCampaignID
   ds
   """  
   def __init__(self, obj):
      self.iMktgCampaignID:str = obj["iMktgCampaignID"]
      """  The Marketing Campaign ID  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandDetailMktgCamp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandDetailPartNum_input:
   """ Required : 
   iPartNum
   ds
   sysRowID
   rowType
   """  
   def __init__(self, obj):
      self.iPartNum:str = obj["iPartNum"]
      """  The part  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.sysRowID:str = obj["sysRowID"]
      """  RowID of the selected record. Skips find part logic if this has a value.  """  
      self.rowType:str = obj["rowType"]
      """  RowType of the selected record. Only used with sysRowID.  """  
      pass

class ChangeDemandDetailPartNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.iPartNum:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.serialWarning:str = obj["parameters"]
      self.questionString:str = obj["parameters"]
      self.multipleMatch:bool = obj["multipleMatch"]
      pass

      """  output parameters  """  

class ChangeDemandDetailRevisionNum_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandDetailRevisionNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadCustID_input:
   """ Required : 
   ipCustID
   ds
   """  
   def __init__(self, obj):
      self.ipCustID:str = obj["ipCustID"]
      """  The proposed Customer ID  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadDemandContract_input:
   """ Required : 
   proposedDemandContract
   ds
   """  
   def __init__(self, obj):
      self.proposedDemandContract:str = obj["proposedDemandContract"]
      """  The proposed Demand Contract  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadDemandContract_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadERSOrder_input:
   """ Required : 
   proposedERSOrder
   ds
   """  
   def __init__(self, obj):
      self.proposedERSOrder:bool = obj["proposedERSOrder"]
      """  The proposed ERS Order  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadERSOrder_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadShipToCustID_input:
   """ Required : 
   ipShipToCustID
   ds
   """  
   def __init__(self, obj):
      self.ipShipToCustID:str = obj["ipShipToCustID"]
      """  The proposed ShipTo Customer ID  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadShipToNum_input:
   """ Required : 
   proposedShipToNum
   ds
   """  
   def __init__(self, obj):
      self.proposedShipToNum:str = obj["proposedShipToNum"]
      """  The proposed Ship To Num  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandHeadUseOTS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandHeadUseOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleMFCustID_input:
   """ Required : 
   ipMFCustID
   ds
   """  
   def __init__(self, obj):
      self.ipMFCustID:str = obj["ipMFCustID"]
      """  The proposed Mark For Customer ID  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleMFCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleMarkForNum_input:
   """ Required : 
   proposedMarkForNum
   ds
   """  
   def __init__(self, obj):
      self.proposedMarkForNum:str = obj["proposedMarkForNum"]
      """  The Proposed ShipToNum  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleMarkForNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleOTSDetails_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleOTSDetails_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandSchedulePlant_input:
   """ Required : 
   proposedPlant
   ds
   """  
   def __init__(self, obj):
      self.proposedPlant:str = obj["proposedPlant"]
      """  The Proposed Plant  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandSchedulePlant_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleSellingReqQty_input:
   """ Required : 
   proposedSellingReqQty
   ds
   """  
   def __init__(self, obj):
      self.proposedSellingReqQty:int = obj["proposedSellingReqQty"]
      """  The proposed Selling Req Quantity  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleSellingReqQty_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleShipToCustID_input:
   """ Required : 
   ipShipToCustID
   ds
   """  
   def __init__(self, obj):
      self.ipShipToCustID:str = obj["ipShipToCustID"]
      """  The proposed ShipTo Customer ID  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleShipToCustID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleShipToNum_input:
   """ Required : 
   proposedShipToNum
   ds
   """  
   def __init__(self, obj):
      self.proposedShipToNum:str = obj["proposedShipToNum"]
      """  The Proposed ShipToNum  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleShipToNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleUseOTMF_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleUseOTMF_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeDemandScheduleUseOTS_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeDemandScheduleUseOTS_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeMiscCode_input:
   """ Required : 
   tableName
   ds
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  name of table being passed in  """  
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ChangeMiscCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPartRevisionChange_input:
   """ Required : 
   iDemandContractNum
   iDemandHeadSeq
   iDemandDtlSeq
   cFieldName
   cPartNum
   """  
   def __init__(self, obj):
      self.iDemandContractNum:int = obj["iDemandContractNum"]
      """  The current IMDemandDetail.DemandContractNum field  """  
      self.iDemandHeadSeq:int = obj["iDemandHeadSeq"]
      """  The current IMDemandDetail.DemandHeadSeq field  """  
      self.iDemandDtlSeq:int = obj["iDemandDtlSeq"]
      """  The current IMDemandDetail.DemandDtlSeq field  """  
      self.cFieldName:str = obj["cFieldName"]
      """  The name of the field you are leaving  """  
      self.cPartNum:str = obj["cPartNum"]
      """  The new PartNum if a substitute part is found, partNum will be the substitute part  """  
      pass

class CheckPartRevisionChange_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.cPartNum:str = obj["parameters"]
      self.cConfigPartMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   company
   importID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.importID:int = obj["importID"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class Erp_Tablesets_DemandDetailImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  DemandContractNum  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  DemandDtlSeq  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.DemandContractLine:int = obj["DemandContractLine"]
      """  DemandContractLine  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  TestRecord  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.OrderLine:int = obj["OrderLine"]
      """  OrderLine  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  DoNotShipBeforeDate  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  DoNotShipAfterDate  """  
      self.DemandReference:str = obj["DemandReference"]
      """  DemandReference  """  
      self.LineDesc:str = obj["LineDesc"]
      """  LineDesc  """  
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.SalesUM:str = obj["SalesUM"]
      """  SalesUM  """  
      self.DiscountPercent:int = obj["DiscountPercent"]
      """  DiscountPercent  """  
      self.UnitPrice:int = obj["UnitPrice"]
      """  UnitPrice  """  
      self.PricePerCode:str = obj["PricePerCode"]
      """  PricePerCode  """  
      self.ProjectID:str = obj["ProjectID"]
      """  ProjectID  """  
      self.PriceGroupCode:str = obj["PriceGroupCode"]
      """  PriceGroupCode  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  QuoteNum  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  QuoteLine  """  
      self.POType:str = obj["POType"]
      """  POType  """  
      self.AcknowledgementType:str = obj["AcknowledgementType"]
      """  AcknowledgementType  """  
      self.ScheduleType:str = obj["ScheduleType"]
      """  ScheduleType  """  
      self.SellingFactor:int = obj["SellingFactor"]
      """  SellingFactor  """  
      self.SellingFactorDirection:str = obj["SellingFactorDirection"]
      """  SellingFactorDirection  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.PONum:str = obj["PONum"]
      """  PONum  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  RejectedByUser  """  
      self.PartNum:str = obj["PartNum"]
      """  PartNum  """  
      self.XPartNum:str = obj["XPartNum"]
      """  XPartNum  """  
      self.UsePriceList:bool = obj["UsePriceList"]
      """  UsePriceList  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  RejectedBySystem  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  OverrideSystemReject  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.OpenLine:bool = obj["OpenLine"]
      """  OpenLine  """  
      self.POLine:str = obj["POLine"]
      """  POLine  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  DemandCharacter01  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  DemandCharacter02  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  DemandCharacter03  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  DemandCharacter04  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  DemandNumber01  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  DemandNumber02  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  DemandNumber03  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  DemandNumber04  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  DemandDate01  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  DemandDate02  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  DemandDate03  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  DemandDate04  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  DemandLogical01  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  DemandLogical02  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  DemandLogical03  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  DemandLogical04  """  
      self.DeleteCurrentReleases:bool = obj["DeleteCurrentReleases"]
      """  DeleteCurrentReleases  """  
      self.MktgCampaignID:str = obj["MktgCampaignID"]
      """  MktgCampaignID  """  
      self.MktgEvntSeq:int = obj["MktgEvntSeq"]
      """  MktgEvntSeq  """  
      self.XRefPartNum:str = obj["XRefPartNum"]
      """  XRefPartNum  """  
      self.XRefPartType:str = obj["XRefPartType"]
      """  XRefPartType  """  
      self.XRefCustNum:int = obj["XRefCustNum"]
      """  XRefCustNum  """  
      self.RevisionNum:str = obj["RevisionNum"]
      """  RevisionNum  """  
      self.XRevisionNum:str = obj["XRevisionNum"]
      """  XRevisionNum  """  
      self.EDIUnitPrice:int = obj["EDIUnitPrice"]
      """  EDIUnitPrice  """  
      self.CumulativeQty:int = obj["CumulativeQty"]
      """  CumulativeQty  """  
      self.CumulativeDate:str = obj["CumulativeDate"]
      """  CumulativeDate  """  
      self.StartCumQty:int = obj["StartCumQty"]
      """  StartCumQty  """  
      self.StartCumDate:str = obj["StartCumDate"]
      """  StartCumDate  """  
      self.LastShipmentID:int = obj["LastShipmentID"]
      """  LastShipmentID  """  
      self.LastShipmentQty:int = obj["LastShipmentQty"]
      """  LastShipmentQty  """  
      self.LastShipmentDate:str = obj["LastShipmentDate"]
      """  LastShipmentDate  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  ScheduleNumber  """  
      self.LastMasterPack:int = obj["LastMasterPack"]
      """  LastMasterPack  """  
      self.DocUnitPrice:int = obj["DocUnitPrice"]
      """  DocUnitPrice  """  
      self.DocEDIUnitPrice:int = obj["DocEDIUnitPrice"]
      """  DocEDIUnitPrice  """  
      self.InternalPrice:int = obj["InternalPrice"]
      """  InternalPrice  """  
      self.DocInternalPrice:int = obj["DocInternalPrice"]
      """  DocInternalPrice  """  
      self.SmartStringProcessed:bool = obj["SmartStringProcessed"]
      """  SmartStringProcessed  """  
      self.SmartString:str = obj["SmartString"]
      """  SmartString  """  
      self.BasePartNum:str = obj["BasePartNum"]
      """  BasePartNum  """  
      self.LastConfigDate:str = obj["LastConfigDate"]
      """  LastConfigDate  """  
      self.LastConfigTime:int = obj["LastConfigTime"]
      """  LastConfigTime  """  
      self.LastConfigUserID:str = obj["LastConfigUserID"]
      """  LastConfigUserID  """  
      self.ConfigUnitPrice:int = obj["ConfigUnitPrice"]
      """  ConfigUnitPrice  """  
      self.ConfigBaseUnitPrice:int = obj["ConfigBaseUnitPrice"]
      """  ConfigBaseUnitPrice  """  
      self.BaseRevisionNum:str = obj["BaseRevisionNum"]
      """  BaseRevisionNum  """  
      self.TPQuoteNum:int = obj["TPQuoteNum"]
      """  TPQuoteNum  """  
      self.TPQuoteLine:int = obj["TPQuoteLine"]
      """  TPQuoteLine  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.Rpt1UnitPrice:int = obj["Rpt1UnitPrice"]
      """  Rpt1UnitPrice  """  
      self.Rpt2UnitPrice:int = obj["Rpt2UnitPrice"]
      """  Rpt2UnitPrice  """  
      self.Rpt3UnitPrice:int = obj["Rpt3UnitPrice"]
      """  Rpt3UnitPrice  """  
      self.Rpt1InternalPrice:int = obj["Rpt1InternalPrice"]
      """  Rpt1InternalPrice  """  
      self.Rpt2InternalPrice:int = obj["Rpt2InternalPrice"]
      """  Rpt2InternalPrice  """  
      self.Rpt3InternalPrice:int = obj["Rpt3InternalPrice"]
      """  Rpt3InternalPrice  """  
      self.Rpt1EDIUnitPrice:int = obj["Rpt1EDIUnitPrice"]
      """  Rpt1EDIUnitPrice  """  
      self.Rpt2EDIUnitPrice:int = obj["Rpt2EDIUnitPrice"]
      """  Rpt2EDIUnitPrice  """  
      self.Rpt3EDIUnitPrice:int = obj["Rpt3EDIUnitPrice"]
      """  Rpt3EDIUnitPrice  """  
      self.ErrorList:str = obj["ErrorList"]
      """  ErrorList  """  
      self.EDICustom01:str = obj["EDICustom01"]
      """  EDICustom01  """  
      self.EDICustom02:str = obj["EDICustom02"]
      """  EDICustom02  """  
      self.EDICustom03:str = obj["EDICustom03"]
      """  EDICustom03  """  
      self.EDICustom04:str = obj["EDICustom04"]
      """  EDICustom04  """  
      self.EDICustom05:str = obj["EDICustom05"]
      """  EDICustom05  """  
      self.EDICustom06:str = obj["EDICustom06"]
      """  EDICustom06  """  
      self.EDICustom07:str = obj["EDICustom07"]
      """  EDICustom07  """  
      self.EDICustom08:str = obj["EDICustom08"]
      """  EDICustom08  """  
      self.EDICustom09:str = obj["EDICustom09"]
      """  EDICustom09  """  
      self.EDICustom10:str = obj["EDICustom10"]
      """  EDICustom10  """  
      self.BlockProcLine:bool = obj["BlockProcLine"]
      """  BlockProcLine  """  
      self.POLineRef:str = obj["POLineRef"]
      """  POLineRef  """  
      self.PCLinkRemoved:bool = obj["PCLinkRemoved"]
      """  PCLinkRemoved  """  
      self.Configured:str = obj["Configured"]
      self.DmdContractNum:int = obj["DmdContractNum"]
      self.MultipleXRef:bool = obj["MultipleXRef"]
      self.PriceDiscrepancy:bool = obj["PriceDiscrepancy"]
      self.BitFlag:int = obj["BitFlag"]
      self.DemandContractDtlSalesUM:str = obj["DemandContractDtlSalesUM"]
      self.MktgCampaignIDCampDescription:str = obj["MktgCampaignIDCampDescription"]
      self.MktgEvntEvntDescription:str = obj["MktgEvntEvntDescription"]
      self.PlantName:str = obj["PlantName"]
      self.PriceGroupDescription:str = obj["PriceGroupDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandHeadImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  DemandContractNum  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.CustNum:int = obj["CustNum"]
      """  CustNum  """  
      self.PONum:str = obj["PONum"]
      """  PONum  """  
      self.DoNotShipBeforeDate:str = obj["DoNotShipBeforeDate"]
      """  DoNotShipBeforeDate  """  
      self.DoNotShipAfterDate:str = obj["DoNotShipAfterDate"]
      """  DoNotShipAfterDate  """  
      self.CancelAfterDate:str = obj["CancelAfterDate"]
      """  CancelAfterDate  """  
      self.FOB:str = obj["FOB"]
      """  FOB  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipViaCode  """  
      self.TermsCode:str = obj["TermsCode"]
      """  TermsCode  """  
      self.AllocPriorityCode:str = obj["AllocPriorityCode"]
      """  AllocPriorityCode  """  
      self.ReservePriorityCode:str = obj["ReservePriorityCode"]
      """  ReservePriorityCode  """  
      self.ShipOrderComplete:bool = obj["ShipOrderComplete"]
      """  ShipOrderComplete  """  
      self.OrderComment:str = obj["OrderComment"]
      """  OrderComment  """  
      self.InvoiceComment:str = obj["InvoiceComment"]
      """  InvoiceComment  """  
      self.AutoOrderBasedDisc:bool = obj["AutoOrderBasedDisc"]
      """  AutoOrderBasedDisc  """  
      self.TestRecord:bool = obj["TestRecord"]
      """  TestRecord  """  
      self.POType:str = obj["POType"]
      """  POType  """  
      self.AcknowledgementType:str = obj["AcknowledgementType"]
      """  AcknowledgementType  """  
      self.AcceptType:str = obj["AcceptType"]
      """  AcceptType  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  ScheduleNumber  """  
      self.ScheduleNumberSeq:int = obj["ScheduleNumberSeq"]
      """  ScheduleNumberSeq  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.LockRate:bool = obj["LockRate"]
      """  LockRate  """  
      self.Accepted:bool = obj["Accepted"]
      """  Accepted  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  RejectedByUser  """  
      self.OpenDemand:bool = obj["OpenDemand"]
      """  OpenDemand  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  RejectedBySystem  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  OverrideSystemReject  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  DemandCharacter01  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  DemandCharacter02  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  DemandCharacter03  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  DemandCharacter04  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  DemandNumber01  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  DemandNumber02  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  DemandNumber03  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  DemandNumber04  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  DemandDate01  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  DemandDate02  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  DemandDate03  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  DemandDate04  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  DemandLogical01  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  DemandLogical02  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  DemandLogical03  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  DemandLogical04  """  
      self.BTCustNum:int = obj["BTCustNum"]
      """  BTCustNum  """  
      self.EDIOrder:bool = obj["EDIOrder"]
      """  EDIOrder  """  
      self.SelectedForProcessing:bool = obj["SelectedForProcessing"]
      """  SelectedForProcessing  """  
      self.SCProcessing:bool = obj["SCProcessing"]
      """  SCProcessing  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ReadyToProcess:bool = obj["ReadyToProcess"]
      """  ReadyToProcess  """  
      self.ResetCums:bool = obj["ResetCums"]
      """  ResetCums  """  
      self.ERSOrder:bool = obj["ERSOrder"]
      """  ERSOrder  """  
      self.CancelPO:bool = obj["CancelPO"]
      """  CancelPO  """  
      self.CreateNewOrder:bool = obj["CreateNewOrder"]
      """  CreateNewOrder  """  
      self.LinkedOrders:str = obj["LinkedOrders"]
      """  LinkedOrders  """  
      self.TCtrlNum:str = obj["TCtrlNum"]
      """  TCtrlNum  """  
      self.BatchNum:str = obj["BatchNum"]
      """  BatchNum  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  QuoteNum  """  
      self.DemandProcessDate:str = obj["DemandProcessDate"]
      """  DemandProcessDate  """  
      self.DemandProcessTime:int = obj["DemandProcessTime"]
      """  DemandProcessTime  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.UserChar1:str = obj["UserChar1"]
      """  UserChar1  """  
      self.UserChar2:str = obj["UserChar2"]
      """  UserChar2  """  
      self.UserChar3:str = obj["UserChar3"]
      """  UserChar3  """  
      self.UserChar4:str = obj["UserChar4"]
      """  UserChar4  """  
      self.UserDate1:str = obj["UserDate1"]
      """  UserDate1  """  
      self.UserDate2:str = obj["UserDate2"]
      """  UserDate2  """  
      self.UserDate3:str = obj["UserDate3"]
      """  UserDate3  """  
      self.UserDate4:str = obj["UserDate4"]
      """  UserDate4  """  
      self.UserDecimal1:int = obj["UserDecimal1"]
      """  UserDecimal1  """  
      self.UserDecimal2:int = obj["UserDecimal2"]
      """  UserDecimal2  """  
      self.UserInteger1:int = obj["UserInteger1"]
      """  UserInteger1  """  
      self.UserInteger2:int = obj["UserInteger2"]
      """  UserInteger2  """  
      self.CustomerTradingPartnerName:str = obj["CustomerTradingPartnerName"]
      """  CustomerTradingPartnerName  """  
      self.TranType:str = obj["TranType"]
      """  TranType  """  
      self.DemandContract:str = obj["DemandContract"]
      """  DemandContract  """  
      self.CustomerCustID:str = obj["CustomerCustID"]
      """  CustomerCustID  """  
      self.BTCustomerCustID:str = obj["BTCustomerCustID"]
      """  BTCustomerCustID  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  ShipToCustID  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  UseOTS  """  
      self.OTSName:str = obj["OTSName"]
      """  OTSName  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  OTSAddress1  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  OTSAddress2  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  OTSAddress3  """  
      self.OTSCity:str = obj["OTSCity"]
      """  OTSCity  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  OTSResaleID  """  
      self.OTSState:str = obj["OTSState"]
      """  OTSState  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  OTSZIP  """  
      self.EDIOTSCountry:str = obj["EDIOTSCountry"]
      """  EDIOTSCountry  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  OTSFaxNum  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  OTSPhoneNum  """  
      self.OTSContact:str = obj["OTSContact"]
      """  OTSContact  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  OTSSaveCustID  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  OTSSaveAs  """  
      self.ErrorList:str = obj["ErrorList"]
      """  ErrorList  """  
      self.EDICustom01:str = obj["EDICustom01"]
      """  EDICustom01  """  
      self.EDICustom02:str = obj["EDICustom02"]
      """  EDICustom02  """  
      self.EDICustom03:str = obj["EDICustom03"]
      """  EDICustom03  """  
      self.EDICustom04:str = obj["EDICustom04"]
      """  EDICustom04  """  
      self.EDICustom05:str = obj["EDICustom05"]
      """  EDICustom05  """  
      self.EDICustom06:str = obj["EDICustom06"]
      """  EDICustom06  """  
      self.EDICustom07:str = obj["EDICustom07"]
      """  EDICustom07  """  
      self.EDICustom08:str = obj["EDICustom08"]
      """  EDICustom08  """  
      self.EDICustom09:str = obj["EDICustom09"]
      """  EDICustom09  """  
      self.EDICustom10:str = obj["EDICustom10"]
      """  EDICustom10  """  
      self.ShipByTime:int = obj["ShipByTime"]
      """  ShipByTime  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  OTSCountryNum  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTSTaxRegionCode  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  OTSCustSaved  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      """  OTSSaved  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTSShipToNum  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  ShipToCustNum  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.AvailBTCustList:str = obj["AvailBTCustList"]
      self.EDI_OTSCountry:str = obj["EDI_OTSCountry"]
      self.ERSOverride:bool = obj["ERSOverride"]
      self.OpenContract:bool = obj["OpenContract"]
      self.OTSCountryDescription:str = obj["OTSCountryDescription"]
      self.ShipToAddressList:str = obj["ShipToAddressList"]
      self.Tran_Type:str = obj["Tran_Type"]
      """  Tran_Type  """  
      self.CustAddrList:str = obj["CustAddrList"]
      self.DmdContractNum:int = obj["DmdContractNum"]
      self.DocumentName:str = obj["DocumentName"]
      self.CustAddrFormatted:str = obj["CustAddrFormatted"]
      self.ShipToAddressFormatted:str = obj["ShipToAddressFormatted"]
      self.BitFlag:int = obj["BitFlag"]
      self.BTCustomerBTName:str = obj["BTCustomerBTName"]
      self.BTCustomerCustID_:str = obj["BTCustomerCustID_"]
      self.BTCustomerName:str = obj["BTCustomerName"]
      self.CurrencyDocumentDesc:str = obj["CurrencyDocumentDesc"]
      self.CurrencyCurrSymbol:str = obj["CurrencyCurrSymbol"]
      self.CurrencyCurrencyID:str = obj["CurrencyCurrencyID"]
      self.CurrencyCurrName:str = obj["CurrencyCurrName"]
      self.CurrencyCurrDesc:str = obj["CurrencyCurrDesc"]
      self.CustomerBTName:str = obj["CustomerBTName"]
      self.CustomerName:str = obj["CustomerName"]
      self.CustomerZip:str = obj["CustomerZip"]
      self.CustomerState:str = obj["CustomerState"]
      self.CustomerCountry:str = obj["CustomerCountry"]
      self.CustomerCity:str = obj["CustomerCity"]
      self.CustomerTradingPartnerName_:str = obj["CustomerTradingPartnerName_"]
      self.CustomerAddress1:str = obj["CustomerAddress1"]
      self.CustomerAddress2:str = obj["CustomerAddress2"]
      self.CustomerAddress3:str = obj["CustomerAddress3"]
      self.CustomerAllowShipTo3:bool = obj["CustomerAllowShipTo3"]
      self.CustomerAllowOTS:bool = obj["CustomerAllowOTS"]
      self.FOBDescription:str = obj["FOBDescription"]
      self.OTSCountryEUMember:bool = obj["OTSCountryEUMember"]
      self.OTSCountryISOCode:str = obj["OTSCountryISOCode"]
      self.ReservePriDescription:str = obj["ReservePriDescription"]
      self.ShipViaCodeWebDesc:str = obj["ShipViaCodeWebDesc"]
      self.ShipViaCodeDescription:str = obj["ShipViaCodeDescription"]
      self.TermsDescription:str = obj["TermsDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandImportEntryTableset:
   def __init__(self, obj):
      self.ImportGrp:list[Erp_Tablesets_ImportGrpRow] = obj["ImportGrp"]
      self.DemandHeadImport:list[Erp_Tablesets_DemandHeadImportRow] = obj["DemandHeadImport"]
      self.PkgControlLabelValueImport:list[Erp_Tablesets_PkgControlLabelValueImportRow] = obj["PkgControlLabelValueImport"]
      self.DemandDetailImport:list[Erp_Tablesets_DemandDetailImportRow] = obj["DemandDetailImport"]
      self.DemandMiscChgImport:list[Erp_Tablesets_DemandMiscChgImportRow] = obj["DemandMiscChgImport"]
      self.DemandScheduleImport:list[Erp_Tablesets_DemandScheduleImportRow] = obj["DemandScheduleImport"]
      self.DemandMiscChgImportDH:list[Erp_Tablesets_DemandMiscChgImportDHRow] = obj["DemandMiscChgImportDH"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_DemandMiscChgImportDHRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  DemandContractNum  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  DemandDtlSeq  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  MiscAmt  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  DocMiscAmt  """  
      self.FreqCode:str = obj["FreqCode"]
      """  FreqCode  """  
      self.Quoting:str = obj["Quoting"]
      """  Quoting  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Rpt1MiscAmt  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Rpt2MiscAmt  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Rpt3MiscAmt  """  
      self.Percentage:int = obj["Percentage"]
      """  Percentage  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorList:str = obj["ErrorList"]
      """  ErrorList  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandMiscChgImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  DemandContractNum  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  DemandDtlSeq  """  
      self.SeqNum:int = obj["SeqNum"]
      """  SeqNum  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.MiscCode:str = obj["MiscCode"]
      """  MiscCode  """  
      self.Description:str = obj["Description"]
      """  Description  """  
      self.MiscAmt:int = obj["MiscAmt"]
      """  MiscAmt  """  
      self.DocMiscAmt:int = obj["DocMiscAmt"]
      """  DocMiscAmt  """  
      self.FreqCode:str = obj["FreqCode"]
      """  FreqCode  """  
      self.Quoting:str = obj["Quoting"]
      """  Quoting  """  
      self.Rpt1MiscAmt:int = obj["Rpt1MiscAmt"]
      """  Rpt1MiscAmt  """  
      self.Rpt2MiscAmt:int = obj["Rpt2MiscAmt"]
      """  Rpt2MiscAmt  """  
      self.Rpt3MiscAmt:int = obj["Rpt3MiscAmt"]
      """  Rpt3MiscAmt  """  
      self.Percentage:int = obj["Percentage"]
      """  Percentage  """  
      self.Type:str = obj["Type"]
      """  Type  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.ErrorList:str = obj["ErrorList"]
      """  ErrorList  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      self.BitFlag:int = obj["BitFlag"]
      self.MiscCodeDescription:str = obj["MiscCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_DemandScheduleImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  DemandContractNum  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  DemandHeadSeq  """  
      self.DemandDtlSeq:int = obj["DemandDtlSeq"]
      """  DemandDtlSeq  """  
      self.DemandScheduleSeq:int = obj["DemandScheduleSeq"]
      """  DemandScheduleSeq  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.GroupID:str = obj["GroupID"]
      """  GroupID  """  
      self.OurReqQty:int = obj["OurReqQty"]
      """  OurReqQty  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  ShipToNum  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipViaCode  """  
      self.SellingReqQty:int = obj["SellingReqQty"]
      """  SellingReqQty  """  
      self.ReqDate:str = obj["ReqDate"]
      """  ReqDate  """  
      self.NeedByDate:str = obj["NeedByDate"]
      """  NeedByDate  """  
      self.MarkForNum:str = obj["MarkForNum"]
      """  MarkForNum  """  
      self.DeliveryDays:int = obj["DeliveryDays"]
      """  DeliveryDays  """  
      self.ScheduleNumber:str = obj["ScheduleNumber"]
      """  ScheduleNumber  """  
      self.DemandType:str = obj["DemandType"]
      """  DemandType  """  
      self.OrderNum:int = obj["OrderNum"]
      """  OrderNum  """  
      self.OrderLine:int = obj["OrderLine"]
      """  OrderLine  """  
      self.OrderRelNum:int = obj["OrderRelNum"]
      """  OrderRelNum  """  
      self.RejectedByUser:bool = obj["RejectedByUser"]
      """  RejectedByUser  """  
      self.RAN:str = obj["RAN"]
      """  RAN  """  
      self.DemandReference:str = obj["DemandReference"]
      """  DemandReference  """  
      self.Posted:bool = obj["Posted"]
      """  Posted  """  
      self.RejectedBySystem:bool = obj["RejectedBySystem"]
      """  RejectedBySystem  """  
      self.OverrideSystemReject:bool = obj["OverrideSystemReject"]
      """  OverrideSystemReject  """  
      self.Plant:str = obj["Plant"]
      """  Plant  """  
      self.OpenSchedule:bool = obj["OpenSchedule"]
      """  OpenSchedule  """  
      self.DemandCharacter01:str = obj["DemandCharacter01"]
      """  DemandCharacter01  """  
      self.DemandCharacter02:str = obj["DemandCharacter02"]
      """  DemandCharacter02  """  
      self.DemandCharacter03:str = obj["DemandCharacter03"]
      """  DemandCharacter03  """  
      self.DemandCharacter04:str = obj["DemandCharacter04"]
      """  DemandCharacter04  """  
      self.DemandNumber01:int = obj["DemandNumber01"]
      """  DemandNumber01  """  
      self.DemandNumber02:int = obj["DemandNumber02"]
      """  DemandNumber02  """  
      self.DemandNumber03:int = obj["DemandNumber03"]
      """  DemandNumber03  """  
      self.DemandNumber04:int = obj["DemandNumber04"]
      """  DemandNumber04  """  
      self.DemandDate01:str = obj["DemandDate01"]
      """  DemandDate01  """  
      self.DemandDate02:str = obj["DemandDate02"]
      """  DemandDate02  """  
      self.DemandDate03:str = obj["DemandDate03"]
      """  DemandDate03  """  
      self.DemandDate04:str = obj["DemandDate04"]
      """  DemandDate04  """  
      self.DemandLogical01:bool = obj["DemandLogical01"]
      """  DemandLogical01  """  
      self.DemandLogical02:bool = obj["DemandLogical02"]
      """  DemandLogical02  """  
      self.DemandLogical03:bool = obj["DemandLogical03"]
      """  DemandLogical03  """  
      self.DemandLogical04:bool = obj["DemandLogical04"]
      """  DemandLogical04  """  
      self.DocumentName:str = obj["DocumentName"]
      """  DocumentName  """  
      self.ForecastEndDate:str = obj["ForecastEndDate"]
      """  ForecastEndDate  """  
      self.DockingStation:str = obj["DockingStation"]
      """  DockingStation  """  
      self.Location:str = obj["Location"]
      """  Location  """  
      self.TransportID:str = obj["TransportID"]
      """  TransportID  """  
      self.ShipbyTime:int = obj["ShipbyTime"]
      """  ShipbyTime  """  
      self.UseOTS:bool = obj["UseOTS"]
      """  UseOTS  """  
      self.OTSName:str = obj["OTSName"]
      """  OTSName  """  
      self.OTSAddress1:str = obj["OTSAddress1"]
      """  OTSAddress1  """  
      self.OTSAddress2:str = obj["OTSAddress2"]
      """  OTSAddress2  """  
      self.OTSAddress3:str = obj["OTSAddress3"]
      """  OTSAddress3  """  
      self.OTSCity:str = obj["OTSCity"]
      """  OTSCity  """  
      self.OTSState:str = obj["OTSState"]
      """  OTSState  """  
      self.OTSZIP:str = obj["OTSZIP"]
      """  OTSZIP  """  
      self.OTSResaleID:str = obj["OTSResaleID"]
      """  OTSResaleID  """  
      self.OTSContact:str = obj["OTSContact"]
      """  OTSContact  """  
      self.OTSFaxNum:str = obj["OTSFaxNum"]
      """  OTSFaxNum  """  
      self.OTSPhoneNum:str = obj["OTSPhoneNum"]
      """  OTSPhoneNum  """  
      self.OTSCountryNum:int = obj["OTSCountryNum"]
      """  OTSCountryNum  """  
      self.SubShipTo:str = obj["SubShipTo"]
      """  SubShipTo  """  
      self.ShipRouting:str = obj["ShipRouting"]
      """  ShipRouting  """  
      self.ShipToCustNum:int = obj["ShipToCustNum"]
      """  ShipToCustNum  """  
      self.OTSTaxRegionCode:str = obj["OTSTaxRegionCode"]
      """  OTSTaxRegionCode  """  
      self.CreateDate:str = obj["CreateDate"]
      """  CreateDate  """  
      self.ProcessDate:str = obj["ProcessDate"]
      """  ProcessDate  """  
      self.ProcessTime:int = obj["ProcessTime"]
      """  ProcessTime  """  
      self.MFCustNum:int = obj["MFCustNum"]
      """  MFCustNum  """  
      self.UseOTMF:bool = obj["UseOTMF"]
      """  UseOTMF  """  
      self.OTMFName:str = obj["OTMFName"]
      """  OTMFName  """  
      self.OTMFAddress1:str = obj["OTMFAddress1"]
      """  OTMFAddress1  """  
      self.OTMFAddress2:str = obj["OTMFAddress2"]
      """  OTMFAddress2  """  
      self.OTMFAddress3:str = obj["OTMFAddress3"]
      """  OTMFAddress3  """  
      self.OTMFCity:str = obj["OTMFCity"]
      """  OTMFCity  """  
      self.OTMFState:str = obj["OTMFState"]
      """  OTMFState  """  
      self.OTMFZIP:str = obj["OTMFZIP"]
      """  OTMFZIP  """  
      self.OTMFContact:str = obj["OTMFContact"]
      """  OTMFContact  """  
      self.OTMFFaxNum:str = obj["OTMFFaxNum"]
      """  OTMFFaxNum  """  
      self.OTMFPhoneNum:str = obj["OTMFPhoneNum"]
      """  OTMFPhoneNum  """  
      self.OTMFCountryNum:int = obj["OTMFCountryNum"]
      """  OTMFCountryNum  """  
      self.QuoteNum:int = obj["QuoteNum"]
      """  QuoteNum  """  
      self.QuoteLine:int = obj["QuoteLine"]
      """  QuoteLine  """  
      self.QuoteRelNum:int = obj["QuoteRelNum"]
      """  QuoteRelNum  """  
      self.CTPNeedByDate:str = obj["CTPNeedByDate"]
      """  CTPNeedByDate  """  
      self.CTPShipDate:str = obj["CTPShipDate"]
      """  CTPShipDate  """  
      self.IntError:bool = obj["IntError"]
      """  IntError  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.SalesUM:str = obj["SalesUM"]
      """  SalesUM  """  
      self.ShipToCustomerCustID:str = obj["ShipToCustomerCustID"]
      """  ShipToCustomerCustID  """  
      self.MFCustomerCustID:str = obj["MFCustomerCustID"]
      """  MFCustomerCustID  """  
      self.OTSCountryDescription:str = obj["OTSCountryDescription"]
      """  OTSCountryDescription  """  
      self.OTSSaveCustID:str = obj["OTSSaveCustID"]
      """  OTSSaveCustID  """  
      self.OTSSaveAs:str = obj["OTSSaveAs"]
      """  OTSSaveAs  """  
      self.OTMFCountryDescription:str = obj["OTMFCountryDescription"]
      """  OTMFCountryDescription  """  
      self.IUM:str = obj["IUM"]
      """  IUM  """  
      self.ErrorList:str = obj["ErrorList"]
      """  ErrorList  """  
      self.EDICustom01:str = obj["EDICustom01"]
      """  EDICustom01  """  
      self.EDICustom02:str = obj["EDICustom02"]
      """  EDICustom02  """  
      self.EDICustom03:str = obj["EDICustom03"]
      """  EDICustom03  """  
      self.EDICustom04:str = obj["EDICustom04"]
      """  EDICustom04  """  
      self.EDICustom05:str = obj["EDICustom05"]
      """  EDICustom05  """  
      self.EDICustom06:str = obj["EDICustom06"]
      """  EDICustom06  """  
      self.EDICustom07:str = obj["EDICustom07"]
      """  EDICustom07  """  
      self.EDICustom08:str = obj["EDICustom08"]
      """  EDICustom08  """  
      self.EDICustom09:str = obj["EDICustom09"]
      """  EDICustom09  """  
      self.EDICustom10:str = obj["EDICustom10"]
      """  EDICustom10  """  
      self.OTSCustSaved:bool = obj["OTSCustSaved"]
      """  OTSCustSaved  """  
      self.OTSSaved:bool = obj["OTSSaved"]
      """  OTSSaved  """  
      self.OTSShipToNum:str = obj["OTSShipToNum"]
      """  OTSShipToNum  """  
      self.CTPManualConfirm:bool = obj["CTPManualConfirm"]
      """  The value will be set to true  if a manual CTP calculation was confirmed for this demand schedule. It will prevent auto CTP calculation for this demand schedule during process demand.  """  
      self.CTPSource:str = obj["CTPSource"]
      """  The value will be set to the calculated CapPromiseDtl  JobNum (Source)  if a manual CTP calculation was confirmed for this demand schedule.  """  
      self.OTSTaxValidationStatus:int = obj["OTSTaxValidationStatus"]
      """  OTSTaxValidationStatus  """  
      self.OTSTaxValidationDate:str = obj["OTSTaxValidationDate"]
      """  OTSTaxValidationDate  """  
      self.DmdContractNum:int = obj["DmdContractNum"]
      self.MarkForAddrList:str = obj["MarkForAddrList"]
      self.ShipToAddrList:str = obj["ShipToAddrList"]
      self.MarkForAddrFormatted:str = obj["MarkForAddrFormatted"]
      self.ShipToAddrFormatted:str = obj["ShipToAddrFormatted"]
      self.BitFlag:int = obj["BitFlag"]
      self.MFCustomerBTName:str = obj["MFCustomerBTName"]
      self.MFCustomerCustID_:str = obj["MFCustomerCustID_"]
      self.MFCustomerName:str = obj["MFCustomerName"]
      self.OTMFCountryDescription_:str = obj["OTMFCountryDescription_"]
      self.OTSCountryEUMember:bool = obj["OTSCountryEUMember"]
      self.OTSCountryDescription_:str = obj["OTSCountryDescription_"]
      self.OTSCountryISOCode:str = obj["OTSCountryISOCode"]
      self.OTSTaxRegionCodeDescription:str = obj["OTSTaxRegionCodeDescription"]
      self.ShipToCustomerName:str = obj["ShipToCustomerName"]
      self.ShipToCustomerCustID_:str = obj["ShipToCustomerCustID_"]
      self.ShipToCustomerBTName:str = obj["ShipToCustomerBTName"]
      self.ShipViaWebDesc:str = obj["ShipViaWebDesc"]
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportGrpListRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.ImportType:str = obj["ImportType"]
      """  ImportType  """  
      self.ErrorFlag:bool = obj["ErrorFlag"]
      """  ErrorFlag  """  
      self.Status:str = obj["Status"]
      """  Status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.DisplayImportID:str = obj["DisplayImportID"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_ImportGrpListTableset:
   def __init__(self, obj):
      self.ImportGrpList:list[Erp_Tablesets_ImportGrpListRow] = obj["ImportGrpList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_ImportGrpRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.ImportID:int = obj["ImportID"]
      """  ImportID  """  
      self.ImportType:str = obj["ImportType"]
      """  ImportType  """  
      self.ErrorFlag:bool = obj["ErrorFlag"]
      """  ErrorFlag  """  
      self.Status:str = obj["Status"]
      """  Status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.IntError:bool = obj["IntError"]
      self.DisplayImportID:str = obj["DisplayImportID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PkgControlLabelValueImportRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.Plant:str = obj["Plant"]
      """  Site Identifier.  """  
      self.ShipToCustID:str = obj["ShipToCustID"]
      """  The CustID associated with this Ship To.  """  
      self.ShipToNum:str = obj["ShipToNum"]
      """  The Ship To number.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.DemandContractNum:int = obj["DemandContractNum"]
      """  The demand contract this demand is for.  """  
      self.DemandHeadSeq:int = obj["DemandHeadSeq"]
      """  The sequence from the DemandHead record this DemandSchedule is related to.  """  
      self.ImportID:int = obj["ImportID"]
      """  The Import ID.  """  
      self.LabelValue01:str = obj["LabelValue01"]
      """  Value to display on package control label.  """  
      self.LabelValue02:str = obj["LabelValue02"]
      """  Value to display on package control label.  """  
      self.LabelValue03:str = obj["LabelValue03"]
      """  Value to display on package control label.  """  
      self.LabelValue04:str = obj["LabelValue04"]
      """  Value to display on package control label.  """  
      self.LabelValue05:str = obj["LabelValue05"]
      """  Value to display on package control label.  """  
      self.LabelValue06:str = obj["LabelValue06"]
      """  Value to display on package control label.  """  
      self.LabelValue07:str = obj["LabelValue07"]
      """  Value to display on package control label.  """  
      self.LabelValue08:str = obj["LabelValue08"]
      """  Value to display on package control label.  """  
      self.LabelValue09:str = obj["LabelValue09"]
      """  Value to display on package control label.  """  
      self.LabelValue10:str = obj["LabelValue10"]
      """  Value to display on package control label.  """  
      self.LabelValue11:str = obj["LabelValue11"]
      """  Value to display on package control label.  """  
      self.LabelValue12:str = obj["LabelValue12"]
      """  Value to display on package control label.  """  
      self.LabelValue13:str = obj["LabelValue13"]
      """  Value to display on package control label.  """  
      self.LabelValue14:str = obj["LabelValue14"]
      """  Value to display on package control label.  """  
      self.LabelValue15:str = obj["LabelValue15"]
      """  Value to display on package control label.  """  
      self.LabelValue16:str = obj["LabelValue16"]
      """  Value to display on package control label.  """  
      self.LabelValue17:str = obj["LabelValue17"]
      """  Value to display on package control label.  """  
      self.LabelValue18:str = obj["LabelValue18"]
      """  Value to display on package control label.  """  
      self.LabelValue19:str = obj["LabelValue19"]
      """  Value to display on package control label.  """  
      self.LabelValue20:str = obj["LabelValue20"]
      """  Value to display on package control label.  """  
      self.LabelValue21:str = obj["LabelValue21"]
      """  Value to display on package control label.  """  
      self.LabelValue22:str = obj["LabelValue22"]
      """  Value to display on package control label.  """  
      self.LabelValue23:str = obj["LabelValue23"]
      """  Value to display on package control label.  """  
      self.LabelValue24:str = obj["LabelValue24"]
      """  Value to display on package control label.  """  
      self.LabelValue25:str = obj["LabelValue25"]
      """  Value to display on package control label.  """  
      self.LabelValue26:str = obj["LabelValue26"]
      """  Value to display on package control label.  """  
      self.LabelValue27:str = obj["LabelValue27"]
      """  Value to display on package control label.  """  
      self.LabelValue28:str = obj["LabelValue28"]
      """  Value to display on package control label.  """  
      self.LabelValue29:str = obj["LabelValue29"]
      """  Value to display on package control label.  """  
      self.LabelValue30:str = obj["LabelValue30"]
      """  Value to display on package control label.  """  
      self.CreatedDate:str = obj["CreatedDate"]
      """  Date that record was created.  """  
      self.CreatedBy:str = obj["CreatedBy"]
      """  The user ID for the user who created this record.  """  
      self.UpdatedDate:str = obj["UpdatedDate"]
      """  Date that record was last updated.  """  
      self.UpdatedBy:str = obj["UpdatedBy"]
      """  The user ID for the user who last updated this record.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtDemandImportEntryTableset:
   def __init__(self, obj):
      self.ImportGrp:list[Erp_Tablesets_ImportGrpRow] = obj["ImportGrp"]
      self.DemandHeadImport:list[Erp_Tablesets_DemandHeadImportRow] = obj["DemandHeadImport"]
      self.PkgControlLabelValueImport:list[Erp_Tablesets_PkgControlLabelValueImportRow] = obj["PkgControlLabelValueImport"]
      self.DemandDetailImport:list[Erp_Tablesets_DemandDetailImportRow] = obj["DemandDetailImport"]
      self.DemandMiscChgImport:list[Erp_Tablesets_DemandMiscChgImportRow] = obj["DemandMiscChgImport"]
      self.DemandScheduleImport:list[Erp_Tablesets_DemandScheduleImportRow] = obj["DemandScheduleImport"]
      self.DemandMiscChgImportDH:list[Erp_Tablesets_DemandMiscChgImportDHRow] = obj["DemandMiscChgImportDH"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetByID_input:
   """ Required : 
   company
   importID
   """  
   def __init__(self, obj):
      self.company:str = obj["company"]
      self.importID:int = obj["importID"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandImportEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandImportEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_DemandImportEntryTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_ImportGrpListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNewDemandDetailImport_input:
   """ Required : 
   ds
   company
   importID
   demandContractNum
   demandHeadSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.importID:int = obj["importID"]
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      pass

class GetNewDemandDetailImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDemandHeadImport_input:
   """ Required : 
   ds
   company
   importID
   demandContractNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.importID:int = obj["importID"]
      self.demandContractNum:int = obj["demandContractNum"]
      pass

class GetNewDemandHeadImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDemandMiscChgImportDH_input:
   """ Required : 
   ds
   company
   importID
   demandContractNum
   demandHeadSeq
   demandDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.importID:int = obj["importID"]
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      self.demandDtlSeq:int = obj["demandDtlSeq"]
      pass

class GetNewDemandMiscChgImportDH_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDemandMiscChgImport_input:
   """ Required : 
   ds
   company
   importID
   demandContractNum
   demandHeadSeq
   demandDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.importID:int = obj["importID"]
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      self.demandDtlSeq:int = obj["demandDtlSeq"]
      pass

class GetNewDemandMiscChgImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewDemandScheduleImport_input:
   """ Required : 
   ds
   company
   importID
   demandContractNum
   demandHeadSeq
   demandDtlSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.importID:int = obj["importID"]
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      self.demandDtlSeq:int = obj["demandDtlSeq"]
      pass

class GetNewDemandScheduleImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewImportGrp_input:
   """ Required : 
   ds
   company
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.company:str = obj["company"]
      pass

class GetNewImportGrp_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPkgControlLabelValueImport_input:
   """ Required : 
   ds
   company
   plant
   shipToCustID
   shipToNum
   partNum
   demandContractNum
   demandHeadSeq
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.company:str = obj["company"]
      self.plant:str = obj["plant"]
      self.shipToCustID:str = obj["shipToCustID"]
      self.shipToNum:str = obj["shipToNum"]
      self.partNum:str = obj["partNum"]
      self.demandContractNum:int = obj["demandContractNum"]
      self.demandHeadSeq:int = obj["demandHeadSeq"]
      pass

class GetNewPkgControlLabelValueImport_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPriceDiscrepancy_input:
   """ Required : 
   ipCustNum
   ipPONum
   ipUnitPrice
   ipEDIUnitPrice
   ipDemandDtlSeq
   """  
   def __init__(self, obj):
      self.ipCustNum:int = obj["ipCustNum"]
      """  CustNum  """  
      self.ipPONum:str = obj["ipPONum"]
      """  PONum  """  
      self.ipUnitPrice:int = obj["ipUnitPrice"]
      """  UnitPrice  """  
      self.ipEDIUnitPrice:int = obj["ipEDIUnitPrice"]
      """  EDIUnitPrice  """  
      self.ipDemandDtlSeq:int = obj["ipDemandDtlSeq"]
      """  DemandDtlSeq  """  
      pass

class GetPriceDiscrepancy_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opPriceDiscrepancy:bool = obj["opPriceDiscrepancy"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseImportGrp
   whereClauseDemandHeadImport
   whereClausePkgControlLabelValueImport
   whereClauseDemandDetailImport
   whereClauseDemandMiscChgImport
   whereClauseDemandScheduleImport
   whereClauseDemandMiscChgImportDH
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseImportGrp:str = obj["whereClauseImportGrp"]
      self.whereClauseDemandHeadImport:str = obj["whereClauseDemandHeadImport"]
      self.whereClausePkgControlLabelValueImport:str = obj["whereClausePkgControlLabelValueImport"]
      self.whereClauseDemandDetailImport:str = obj["whereClauseDemandDetailImport"]
      self.whereClauseDemandMiscChgImport:str = obj["whereClauseDemandMiscChgImport"]
      self.whereClauseDemandScheduleImport:str = obj["whereClauseDemandScheduleImport"]
      self.whereClauseDemandMiscChgImportDH:str = obj["whereClauseDemandMiscChgImportDH"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandImportEntryTableset] = obj["returnObj"]
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

class ImportEDIOnUDImport_input:
   """ Required : 
   udLine
   tableName
   SysRowID
   """  
   def __init__(self, obj):
      self.udLine:str = obj["udLine"]
      self.tableName:str = obj["tableName"]
      self.SysRowID:str = obj["SysRowID"]
      pass

class ImportEDIOnUDImport_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ImportEDIPostProcessDemand_input:
   """ Required : 
   DemandHeadRowid
   """  
   def __init__(self, obj):
      self.DemandHeadRowid:str = obj["DemandHeadRowid"]
      pass

class ImportEDIPostProcessDemand_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ImportEDIPreProcessDemand_input:
   """ Required : 
   DemandHeadRowid
   """  
   def __init__(self, obj):
      self.DemandHeadRowid:str = obj["DemandHeadRowid"]
      pass

class ImportEDIPreProcessDemand_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ImportEDIb4Tran_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ImportEDIb4Tran_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ImportEDIb4Val_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class ImportEDIb4Val_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class ReadyToProcess_input:
   """ Required : 
   importID
   """  
   def __init__(self, obj):
      self.importID:int = obj["importID"]
      """  The IntQueID of a Demand PO records  """  
      pass

class ReadyToProcess_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_DemandImportEntryTableset] = obj["returnObj"]
      pass

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDemandImportEntryTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtDemandImportEntryTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidateOTSTaxID_input:
   """ Required : 
   ds
   manualValidation
   hmrcFraudPrevHeader
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.manualValidation:bool = obj["manualValidation"]
      self.hmrcFraudPrevHeader:str = obj["hmrcFraudPrevHeader"]
      pass

class ValidateOTSTaxID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_DemandImportEntryTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

