import asyncio
import aiohttp
import configEpicorSchemas



# Title: Erp.BO.VendorSvc
# Description: Vendor BO
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/$metadata",headers=creds) as resp:
           return await resp.json()

async def get_Vendors(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Vendors items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Vendors
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors",headers=creds) as resp:
           return await resp.json()

async def post_Vendors(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Vendors
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendorRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendorRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum(Company, VendorNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Vendor item
   Description: Calls GetByID to retrieve the Vendor item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Vendor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendorRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Vendors_Company_VendorNum(Company, VendorNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Vendor for the service
   Description: Calls UpdateExt to update Vendor. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Vendor
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendorRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Vendors_Company_VendorNum(Company, VendorNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Vendor item
   Description: Call UpdateExt to delete Vendor item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Vendor
      :param Company: Desc: Company   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_EntityGLCs(Company, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get EntityGLCs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_EntityGLCs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/EntityGLCs",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_EntityGLCs_Company_RelatedToFile_Key1_Key2_Key3_Key4_Key5_Key6_GLControlType(Company, VendorNum, RelatedToFile, Key1, Key2, Key3, Key4, Key5, Key6, GLControlType, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the EntityGLC item
   Description: Calls GetByID to retrieve the EntityGLC item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_EntityGLC1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_TaxExempts(Company, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get TaxExempts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_TaxExempts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxExemptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/TaxExempts",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_TaxExempts_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company, VendorNum, RelatedToFile, Key1, Key2, TaxCode, RateCode, EffectiveFrom, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxExempt item
   Description: Calls GetByID to retrieve the TaxExempt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxExempt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/TaxExempts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_PEVendWhldHists(Company, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get PEVendWhldHists items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_PEVendWhldHists1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PEVendWhldHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/PEVendWhldHists",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_PEVendWhldHists_Company_VendorNum_RecordSeq(Company, VendorNum, RecordSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PEVendWhldHist item
   Description: Calls GetByID to retrieve the PEVendWhldHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PEVendWhldHist1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RecordSeq: Desc: RecordSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PEVendWhldHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/PEVendWhldHists(" + Company + "," + VendorNum + "," + RecordSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VendRestrictions(Company, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendRestrictions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendRestrictions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendRestrictions",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VendRestrictions_Company_VendorNum_RestrictionTypeID(Company, VendorNum, RestrictionTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendRestriction item
   Description: Calls GetByID to retrieve the VendRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendRestriction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendRestrictions(" + Company + "," + VendorNum + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VendBanks(Company, VendorNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendBanks items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendBanks1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendBanks",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VendBanks_Company_VendorNum_BankID(Company, VendorNum, BankID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendBank item
   Description: Calls GetByID to retrieve the VendBank item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendBank1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendBankRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VendCntMains(Company, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendCntMains items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendCntMains1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntMainRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendCntMains",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VendCntMains_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendCntMain item
   Description: Calls GetByID to retrieve the VendCntMain item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCntMain1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendCntMainRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendCntMains(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VenMFBills(Company, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VenMFBills items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VenMFBills1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VenMFBills",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VenMFBills_Company_VendorNum_PayBTFlag(Company, VendorNum, PayBTFlag, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VenMFBill item
   Description: Calls GetByID to retrieve the VenMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenMFBill1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VenMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VenMFBills(" + Company + "," + VendorNum + "," + PayBTFlag + ")",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VendorPPs(Company, VendorNum, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendorPPs items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendorPPs1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorPPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendorPPs",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VendorPPs_Company_VendorNum_PurPoint(Company, VendorNum, PurPoint, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendorPP item
   Description: Calls GetByID to retrieve the VendorPP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendorPP1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VenUPSEmails(Company, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VenUPSEmails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VenUPSEmails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VenUPSEmails",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VenUPSEmails_Company_VendorNum_UPSQVSeq(Company, VendorNum, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VenUPSEmail item
   Description: Calls GetByID to retrieve the VenUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenUPSEmail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VenUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VenUPSEmails(" + Company + "," + VendorNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VendorAttches(Company, VendorNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendorAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendorAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendorAttches",headers=creds) as resp:
           return await resp.json()

async def get_Vendors_Company_VendorNum_VendorAttches_Company_VendorNum_DrawingSeq(Company, VendorNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendorAttch item
   Description: Calls GetByID to retrieve the VendorAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendorAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendorAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Vendors(" + Company + "," + VendorNum + ")/VendorAttches(" + Company + "," + VendorNum + "," + DrawingSeq + ")",headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EntityGLCs",headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EntityGLCs", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
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
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")", json=requestBody,headers=creds) as resp:
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/EntityGLCs(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + Key3 + "," + Key4 + "," + Key5 + "," + Key6 + "," + GLControlType + ")",headers=creds) as resp:
           return await resp.json()

async def get_TaxExempts(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get TaxExempts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_TaxExempts
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.TaxExemptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TaxExempts",headers=creds) as resp:
           return await resp.json()

async def post_TaxExempts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_TaxExempts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TaxExempts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_TaxExempts_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company, RelatedToFile, Key1, Key2, TaxCode, RateCode, EffectiveFrom, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the TaxExempt item
   Description: Calls GetByID to retrieve the TaxExempt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_TaxExempt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TaxExempts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")",headers=creds) as resp:
           return await resp.json()

async def patch_TaxExempts_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company, RelatedToFile, Key1, Key2, TaxCode, RateCode, EffectiveFrom, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update TaxExempt for the service
   Description: Calls UpdateExt to update TaxExempt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_TaxExempt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.TaxExemptRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TaxExempts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_TaxExempts_Company_RelatedToFile_Key1_Key2_TaxCode_RateCode_EffectiveFrom(Company, RelatedToFile, Key1, Key2, TaxCode, RateCode, EffectiveFrom, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete TaxExempt item
   Description: Call UpdateExt to delete TaxExempt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_TaxExempt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param RelatedToFile: Desc: RelatedToFile   Required: True   Allow empty value : True
      :param Key1: Desc: Key1   Required: True   Allow empty value : True
      :param Key2: Desc: Key2   Required: True   Allow empty value : True
      :param TaxCode: Desc: TaxCode   Required: True   Allow empty value : True
      :param RateCode: Desc: RateCode   Required: True   Allow empty value : True
      :param EffectiveFrom: Desc: EffectiveFrom   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/TaxExempts(" + Company + "," + RelatedToFile + "," + Key1 + "," + Key2 + "," + TaxCode + "," + RateCode + "," + EffectiveFrom + ")",headers=creds) as resp:
           return await resp.json()

async def get_PEVendWhldHists(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get PEVendWhldHists items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_PEVendWhldHists
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PEVendWhldHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PEVendWhldHists",headers=creds) as resp:
           return await resp.json()

async def post_PEVendWhldHists(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_PEVendWhldHists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PEVendWhldHistRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PEVendWhldHistRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PEVendWhldHists", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_PEVendWhldHists_Company_VendorNum_RecordSeq(Company, VendorNum, RecordSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the PEVendWhldHist item
   Description: Calls GetByID to retrieve the PEVendWhldHist item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_PEVendWhldHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RecordSeq: Desc: RecordSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PEVendWhldHistRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PEVendWhldHists(" + Company + "," + VendorNum + "," + RecordSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_PEVendWhldHists_Company_VendorNum_RecordSeq(Company, VendorNum, RecordSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update PEVendWhldHist for the service
   Description: Calls UpdateExt to update PEVendWhldHist. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_PEVendWhldHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RecordSeq: Desc: RecordSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PEVendWhldHistRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PEVendWhldHists(" + Company + "," + VendorNum + "," + RecordSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_PEVendWhldHists_Company_VendorNum_RecordSeq(Company, VendorNum, RecordSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete PEVendWhldHist item
   Description: Call UpdateExt to delete PEVendWhldHist item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_PEVendWhldHist
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RecordSeq: Desc: RecordSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/PEVendWhldHists(" + Company + "," + VendorNum + "," + RecordSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendRestrictions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendRestrictions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRestrictions",headers=creds) as resp:
           return await resp.json()

async def post_VendRestrictions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendRestrictions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRestrictions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendRestrictions_Company_VendorNum_RestrictionTypeID(Company, VendorNum, RestrictionTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendRestriction item
   Description: Calls GetByID to retrieve the VendRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRestrictions(" + Company + "," + VendorNum + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendRestrictions_Company_VendorNum_RestrictionTypeID(Company, VendorNum, RestrictionTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendRestriction for the service
   Description: Calls UpdateExt to update VendRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRestrictions(" + Company + "," + VendorNum + "," + RestrictionTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendRestrictions_Company_VendorNum_RestrictionTypeID(Company, VendorNum, RestrictionTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendRestriction item
   Description: Call UpdateExt to delete VendRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRestrictions(" + Company + "," + VendorNum + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendBanks(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendBanks items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendBanks
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks",headers=creds) as resp:
           return await resp.json()

async def post_VendBanks(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendBanks
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendBankRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendBankRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendBanks_Company_VendorNum_BankID(Company, VendorNum, BankID, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendBank item
   Description: Calls GetByID to retrieve the VendBank item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendBank
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendBankRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendBanks_Company_VendorNum_BankID(Company, VendorNum, BankID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendBank for the service
   Description: Calls UpdateExt to update VendBank. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendBank
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendBankRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendBanks_Company_VendorNum_BankID(Company, VendorNum, BankID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendBank item
   Description: Call UpdateExt to delete VendBank item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendBank
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendBanks_Company_VendorNum_BankID_VendBankAttches(Company, VendorNum, BankID, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendBankAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendBankAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")/VendBankAttches",headers=creds) as resp:
           return await resp.json()

async def get_VendBanks_Company_VendorNum_BankID_VendBankAttches_Company_VendorNum_BankID_DrawingSeq(Company, VendorNum, BankID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendBankAttch item
   Description: Calls GetByID to retrieve the VendBankAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendBankAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendBankAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBanks(" + Company + "," + VendorNum + "," + BankID + ")/VendBankAttches(" + Company + "," + VendorNum + "," + BankID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendBankAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendBankAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendBankAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendBankAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBankAttches",headers=creds) as resp:
           return await resp.json()

async def post_VendBankAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendBankAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendBankAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendBankAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBankAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendBankAttches_Company_VendorNum_BankID_DrawingSeq(Company, VendorNum, BankID, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendBankAttch item
   Description: Calls GetByID to retrieve the VendBankAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendBankAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendBankAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBankAttches(" + Company + "," + VendorNum + "," + BankID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendBankAttches_Company_VendorNum_BankID_DrawingSeq(Company, VendorNum, BankID, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendBankAttch for the service
   Description: Calls UpdateExt to update VendBankAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendBankAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendBankAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBankAttches(" + Company + "," + VendorNum + "," + BankID + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendBankAttches_Company_VendorNum_BankID_DrawingSeq(Company, VendorNum, BankID, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendBankAttch item
   Description: Call UpdateExt to delete VendBankAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendBankAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param BankID: Desc: BankID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendBankAttches(" + Company + "," + VendorNum + "," + BankID + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendCntMains(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendCntMains items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendCntMains
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntMainRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntMains",headers=creds) as resp:
           return await resp.json()

async def post_VendCntMains(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendCntMains
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendCntMainRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendCntMainRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntMains", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendCntMains_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendCntMain item
   Description: Calls GetByID to retrieve the VendCntMain item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCntMain
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendCntMainRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntMains(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendCntMains_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendCntMain for the service
   Description: Calls UpdateExt to update VendCntMain. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendCntMain
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendCntMainRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntMains(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendCntMains_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendCntMain item
   Description: Call UpdateExt to delete VendCntMain item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendCntMain
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntMains(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_VenMFBills(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VenMFBills items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VenMFBills
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenMFBills",headers=creds) as resp:
           return await resp.json()

async def post_VenMFBills(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VenMFBills
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VenMFBillRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VenMFBillRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenMFBills", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VenMFBills_Company_VendorNum_PayBTFlag(Company, VendorNum, PayBTFlag, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VenMFBill item
   Description: Calls GetByID to retrieve the VenMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenMFBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VenMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenMFBills(" + Company + "," + VendorNum + "," + PayBTFlag + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VenMFBills_Company_VendorNum_PayBTFlag(Company, VendorNum, PayBTFlag, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VenMFBill for the service
   Description: Calls UpdateExt to update VenMFBill. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VenMFBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VenMFBillRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenMFBills(" + Company + "," + VendorNum + "," + PayBTFlag + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VenMFBills_Company_VendorNum_PayBTFlag(Company, VendorNum, PayBTFlag, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VenMFBill item
   Description: Call UpdateExt to delete VenMFBill item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VenMFBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenMFBills(" + Company + "," + VendorNum + "," + PayBTFlag + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendorPPs(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendorPPs items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendorPPs
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorPPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs",headers=creds) as resp:
           return await resp.json()

async def post_VendorPPs(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendorPPs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendorPPRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendorPPs_Company_VendorNum_PurPoint(Company, VendorNum, PurPoint, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendorPP item
   Description: Calls GetByID to retrieve the VendorPP item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendorPP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendorPPs_Company_VendorNum_PurPoint(Company, VendorNum, PurPoint, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendorPP for the service
   Description: Calls UpdateExt to update VendorPP. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendorPP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendorPPRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendorPPs_Company_VendorNum_PurPoint(Company, VendorNum, PurPoint, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendorPP item
   Description: Call UpdateExt to delete VendorPP item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendorPP
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendorPPs_Company_VendorNum_PurPoint_VenPPMFBills(Company, VendorNum, PurPoint, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VenPPMFBills items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VenPPMFBills1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenPPMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VenPPMFBills",headers=creds) as resp:
           return await resp.json()

async def get_VendorPPs_Company_VendorNum_PurPoint_VenPPMFBills_Company_VendorNum_PurPoint_PayBTFlag(Company, VendorNum, PurPoint, PayBTFlag, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VenPPMFBill item
   Description: Calls GetByID to retrieve the VenPPMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenPPMFBill1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VenPPMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VenPPMFBills(" + Company + "," + VendorNum + "," + PurPoint + "," + PayBTFlag + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendorPPs_Company_VendorNum_PurPoint_VenPPUPSEmails(Company, VendorNum, PurPoint, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VenPPUPSEmails items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VenPPUPSEmails1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenPPUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VenPPUPSEmails",headers=creds) as resp:
           return await resp.json()

async def get_VendorPPs_Company_VendorNum_PurPoint_VenPPUPSEmails_Company_VendorNum_PurPoint_UPSQVSeq(Company, VendorNum, PurPoint, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VenPPUPSEmail item
   Description: Calls GetByID to retrieve the VenPPUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenPPUPSEmail1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VenPPUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VenPPUPSEmails(" + Company + "," + VendorNum + "," + PurPoint + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendorPPs_Company_VendorNum_PurPoint_VendPPRestrictions(Company, VendorNum, PurPoint, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendPPRestrictions items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendPPRestrictions1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPPRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VendPPRestrictions",headers=creds) as resp:
           return await resp.json()

async def get_VendorPPs_Company_VendorNum_PurPoint_VendPPRestrictions_Company_VendorNum_PurPoint_RestrictionTypeID(Company, VendorNum, PurPoint, RestrictionTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendPPRestriction item
   Description: Calls GetByID to retrieve the VendPPRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPPRestriction1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPPRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VendPPRestrictions(" + Company + "," + VendorNum + "," + PurPoint + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendorPPs_Company_VendorNum_PurPoint_VendCnts(Company, VendorNum, PurPoint, select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendCnts items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendCnts1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VendCnts",headers=creds) as resp:
           return await resp.json()

async def get_VendorPPs_Company_VendorNum_PurPoint_VendCnts_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendCnt item
   Description: Calls GetByID to retrieve the VendCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCnt1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorPPs(" + Company + "," + VendorNum + "," + PurPoint + ")/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_VenPPMFBills(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VenPPMFBills items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VenPPMFBills
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenPPMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPMFBills",headers=creds) as resp:
           return await resp.json()

async def post_VenPPMFBills(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VenPPMFBills
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VenPPMFBillRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VenPPMFBillRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPMFBills", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VenPPMFBills_Company_VendorNum_PurPoint_PayBTFlag(Company, VendorNum, PurPoint, PayBTFlag, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VenPPMFBill item
   Description: Calls GetByID to retrieve the VenPPMFBill item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenPPMFBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VenPPMFBillRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPMFBills(" + Company + "," + VendorNum + "," + PurPoint + "," + PayBTFlag + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VenPPMFBills_Company_VendorNum_PurPoint_PayBTFlag(Company, VendorNum, PurPoint, PayBTFlag, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VenPPMFBill for the service
   Description: Calls UpdateExt to update VenPPMFBill. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VenPPMFBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VenPPMFBillRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPMFBills(" + Company + "," + VendorNum + "," + PurPoint + "," + PayBTFlag + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VenPPMFBills_Company_VendorNum_PurPoint_PayBTFlag(Company, VendorNum, PurPoint, PayBTFlag, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VenPPMFBill item
   Description: Call UpdateExt to delete VenPPMFBill item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VenPPMFBill
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param PayBTFlag: Desc: PayBTFlag   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPMFBills(" + Company + "," + VendorNum + "," + PurPoint + "," + PayBTFlag + ")",headers=creds) as resp:
           return await resp.json()

async def get_VenPPUPSEmails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VenPPUPSEmails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VenPPUPSEmails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenPPUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPUPSEmails",headers=creds) as resp:
           return await resp.json()

async def post_VenPPUPSEmails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VenPPUPSEmails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VenPPUPSEmailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VenPPUPSEmailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPUPSEmails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VenPPUPSEmails_Company_VendorNum_PurPoint_UPSQVSeq(Company, VendorNum, PurPoint, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VenPPUPSEmail item
   Description: Calls GetByID to retrieve the VenPPUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenPPUPSEmail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VenPPUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPUPSEmails(" + Company + "," + VendorNum + "," + PurPoint + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VenPPUPSEmails_Company_VendorNum_PurPoint_UPSQVSeq(Company, VendorNum, PurPoint, UPSQVSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VenPPUPSEmail for the service
   Description: Calls UpdateExt to update VenPPUPSEmail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VenPPUPSEmail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VenPPUPSEmailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPUPSEmails(" + Company + "," + VendorNum + "," + PurPoint + "," + UPSQVSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VenPPUPSEmails_Company_VendorNum_PurPoint_UPSQVSeq(Company, VendorNum, PurPoint, UPSQVSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VenPPUPSEmail item
   Description: Call UpdateExt to delete VenPPUPSEmail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VenPPUPSEmail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenPPUPSEmails(" + Company + "," + VendorNum + "," + PurPoint + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendPPRestrictions(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendPPRestrictions items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendPPRestrictions
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendPPRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendPPRestrictions",headers=creds) as resp:
           return await resp.json()

async def post_VendPPRestrictions(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendPPRestrictions
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendPPRestrictionRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendPPRestrictionRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendPPRestrictions", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendPPRestrictions_Company_VendorNum_PurPoint_RestrictionTypeID(Company, VendorNum, PurPoint, RestrictionTypeID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendPPRestriction item
   Description: Calls GetByID to retrieve the VendPPRestriction item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendPPRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendPPRestrictionRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendPPRestrictions(" + Company + "," + VendorNum + "," + PurPoint + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendPPRestrictions_Company_VendorNum_PurPoint_RestrictionTypeID(Company, VendorNum, PurPoint, RestrictionTypeID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendPPRestriction for the service
   Description: Calls UpdateExt to update VendPPRestriction. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendPPRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendPPRestrictionRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendPPRestrictions(" + Company + "," + VendorNum + "," + PurPoint + "," + RestrictionTypeID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendPPRestrictions_Company_VendorNum_PurPoint_RestrictionTypeID(Company, VendorNum, PurPoint, RestrictionTypeID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendPPRestriction item
   Description: Call UpdateExt to delete VendPPRestriction item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendPPRestriction
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param RestrictionTypeID: Desc: RestrictionTypeID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendPPRestrictions(" + Company + "," + VendorNum + "," + PurPoint + "," + RestrictionTypeID + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendCnts(select = None, expand = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendCnts items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendCnts
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts",headers=creds) as resp:
           return await resp.json()

async def post_VendCnts(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendCnts
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendCntRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendCntRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendCnts_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, select = None, expand = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendCnt item
   Description: Calls GetByID to retrieve the VendCnt item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param expand: Desc: Odata expand to child
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendCntRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendCnts_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendCnt for the service
   Description: Calls UpdateExt to update VendCnt. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendCntRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendCnts_Company_VendorNum_PurPoint_ConNum(Company, VendorNum, PurPoint, ConNum, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendCnt item
   Description: Call UpdateExt to delete VendCnt item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendCnt
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendCnts_Company_VendorNum_PurPoint_ConNum_VendCntAttches(Company, VendorNum, PurPoint, ConNum, select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID for the service
   Description: Get VendCntAttches items from the server using GetByID standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetByID_VendCntAttches1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")/VendCntAttches",headers=creds) as resp:
           return await resp.json()

async def get_VendCnts_Company_VendorNum_PurPoint_ConNum_VendCntAttches_Company_VendorNum_PurPoint_ConNum_DrawingSeq(Company, VendorNum, PurPoint, ConNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendCntAttch item
   Description: Calls GetByID to retrieve the VendCntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCntAttch1
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendCntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCnts(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + ")/VendCntAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendCntAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendCntAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendCntAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendCntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntAttches",headers=creds) as resp:
           return await resp.json()

async def post_VendCntAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendCntAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendCntAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendCntAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendCntAttches_Company_VendorNum_PurPoint_ConNum_DrawingSeq(Company, VendorNum, PurPoint, ConNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendCntAttch item
   Description: Calls GetByID to retrieve the VendCntAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendCntAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendCntAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendCntAttches_Company_VendorNum_PurPoint_ConNum_DrawingSeq(Company, VendorNum, PurPoint, ConNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendCntAttch for the service
   Description: Calls UpdateExt to update VendCntAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendCntAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendCntAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendCntAttches_Company_VendorNum_PurPoint_ConNum_DrawingSeq(Company, VendorNum, PurPoint, ConNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendCntAttch item
   Description: Call UpdateExt to delete VendCntAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendCntAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param PurPoint: Desc: PurPoint   Required: True   Allow empty value : True
      :param ConNum: Desc: ConNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendCntAttches(" + Company + "," + VendorNum + "," + PurPoint + "," + ConNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_VenUPSEmails(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VenUPSEmails items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VenUPSEmails
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VenUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenUPSEmails",headers=creds) as resp:
           return await resp.json()

async def post_VenUPSEmails(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VenUPSEmails
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VenUPSEmailRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VenUPSEmailRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenUPSEmails", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VenUPSEmails_Company_VendorNum_UPSQVSeq(Company, VendorNum, UPSQVSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VenUPSEmail item
   Description: Calls GetByID to retrieve the VenUPSEmail item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VenUPSEmail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VenUPSEmailRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenUPSEmails(" + Company + "," + VendorNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VenUPSEmails_Company_VendorNum_UPSQVSeq(Company, VendorNum, UPSQVSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VenUPSEmail for the service
   Description: Calls UpdateExt to update VenUPSEmail. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VenUPSEmail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VenUPSEmailRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenUPSEmails(" + Company + "," + VendorNum + "," + UPSQVSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VenUPSEmails_Company_VendorNum_UPSQVSeq(Company, VendorNum, UPSQVSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VenUPSEmail item
   Description: Call UpdateExt to delete VenUPSEmail item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VenUPSEmail
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param UPSQVSeq: Desc: UPSQVSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VenUPSEmails(" + Company + "," + VendorNum + "," + UPSQVSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendorAttches(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendorAttches items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendorAttches
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorAttches",headers=creds) as resp:
           return await resp.json()

async def post_VendorAttches(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendorAttches
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendorAttchRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendorAttchRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorAttches", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendorAttches_Company_VendorNum_DrawingSeq(Company, VendorNum, DrawingSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendorAttch item
   Description: Calls GetByID to retrieve the VendorAttch item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendorAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendorAttchRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorAttches(" + Company + "," + VendorNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendorAttches_Company_VendorNum_DrawingSeq(Company, VendorNum, DrawingSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendorAttch for the service
   Description: Calls UpdateExt to update VendorAttch. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendorAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param DrawingSeq: Desc: DrawingSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendorAttchRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorAttches(" + Company + "," + VendorNum + "," + DrawingSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendorAttches_Company_VendorNum_DrawingSeq(Company, VendorNum, DrawingSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendorAttch item
   Description: Call UpdateExt to delete VendorAttch item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendorAttch
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendorAttches(" + Company + "," + VendorNum + "," + DrawingSeq + ")",headers=creds) as resp:
           return await resp.json()

async def get_Partners(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get Partners items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_Partners
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.PartnerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Partners",headers=creds) as resp:
           return await resp.json()

async def post_Partners(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_Partners
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.PartnerRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Partners", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the Partner item
   Description: Calls GetByID to retrieve the Partner item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.PartnerRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")",headers=creds) as resp:
           return await resp.json()

async def patch_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update Partner for the service
   Description: Calls UpdateExt to update Partner. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.PartnerRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_Partners_Company_PartnerNum_PartnerType_PartnerID_SearchID(Company, PartnerNum, PartnerType, PartnerID, SearchID, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete Partner item
   Description: Call UpdateExt to delete Partner item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_Partner
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param PartnerNum: Desc: PartnerNum   Required: True
      :param PartnerType: Desc: PartnerType   Required: True
      :param PartnerID: Desc: PartnerID   Required: True   Allow empty value : True
      :param SearchID: Desc: SearchID   Required: True   Allow empty value : True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/Partners(" + Company + "," + PartnerNum + "," + PartnerType + "," + PartnerID + "," + SearchID + ")",headers=creds) as resp:
           return await resp.json()

async def get_VendRemitToes(select = None, filter = None, orderby = None, top = None, skip = None, inlinecount = None, epicorHeaders = None):
   """  
   Summary: Calls GetRows for the service
   Description: Get VendRemitToes items from the server using GetRows standard method. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: GetRows_VendRemitToes
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param orderby: Desc: Odata sort results
      :param top: Desc: Odata top results
      :param skip: Desc: Odata skip results
      :param inlinecount: Desc: Odata.count value
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendRemitToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRemitToes",headers=creds) as resp:
           return await resp.json()

async def post_VendRemitToes(requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to create new item for the service
   Description: Calls UpdateExt to create new item for the service. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li></ul></div>
   OperationID: NewUpdateExt_VendRemitToes
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/Erp.Tablesets.VendRemitToRow
   Returns: 
      201 Desc: Resource is created. Operation is successful.  => reference#/components/schemas/Erp.Tablesets.VendRemitToRow
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRemitToes", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def get_VendRemitToes_Company_VendorNum_RemitToSeq(Company, VendorNum, RemitToSeq, select = None, filter = None, epicorHeaders = None):
   """  
   Summary: Calls GetByID to retrieve the VendRemitTo item
   Description: Calls GetByID to retrieve the VendRemitTo item by specified keys. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: GetById_VendRemitTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RemitToSeq: Desc: RemitToSeq   Required: True
      :param select: Desc: Odata select comma delimited list of fields
      :param filter: Desc: Odata filter results
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/Erp.Tablesets.VendRemitToRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRemitToes(" + Company + "," + VendorNum + "," + RemitToSeq + ")",headers=creds) as resp:
           return await resp.json()

async def patch_VendRemitToes_Company_VendorNum_RemitToSeq(Company, VendorNum, RemitToSeq, requestBody, epicorHeaders = None):
   """  
   Summary: Calls UpdateExt to update VendRemitTo for the service
   Description: Calls UpdateExt to update VendRemitTo. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: UpdateExt_VendRemitTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RemitToSeq: Desc: RemitToSeq   Required: True
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: input params  => reference#/components/schemas/Erp.Tablesets.VendRemitToRow
   Returns: 
      204 Desc: No Content. Operation is successful.
      400 Desc: Unable to deserialize entity. Input data is not in correct format.
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.patch(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRemitToes(" + Company + "," + VendorNum + "," + RemitToSeq + ")", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def delete_VendRemitToes_Company_VendorNum_RemitToSeq(Company, VendorNum, RemitToSeq, epicorHeaders = None):
   """  
   Summary: Call UpdateExt to delete VendRemitTo item
   Description: Call UpdateExt to delete VendRemitTo item. <div>OData-specific rules:<ul><li>OData $-parameters data are case-sensitive</li><li>String parameters should be specified in single quotes</li></ul></div>
   OperationID: DeleteUpdateExt_VendRemitTo
      :param Company: Desc: Company   Required: True   Allow empty value : True
      :param VendorNum: Desc: VendorNum   Required: True
      :param RemitToSeq: Desc: RemitToSeq   Required: True
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
       async with session.delete(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/VendRemitToes(" + Company + "," + VendorNum + "," + RemitToSeq + ")",headers=creds) as resp:
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
      200 Desc: OK => reference#/components/schemas/Epicor.RESTApi.Help.ODataSetResponse_System.Collections.Generic.List_Erp.Tablesets.VendorListRow
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List",headers=creds) as resp:
           return await resp.json()




#########################################################################
# Custom methods:
#########################################################################
async def get_GetRows(whereClauseVendor, whereClauseVendorAttch, whereClauseEntityGLC, whereClauseTaxExempt, whereClausePartner, whereClausePEVendWhldHist, whereClauseVendRestriction, whereClauseVendBank, whereClauseVendBankAttch, whereClauseVendCntMain, whereClauseVenMFBill, whereClauseVendorPP, whereClauseVenPPMFBill, whereClauseVenPPUPSEmail, whereClauseVendPPRestriction, whereClauseVendCnt, whereClauseVendCntAttch, whereClauseVenUPSEmail, whereClauseVendRemitTo, pageSize, absolutePage, epicorHeaders = None):
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
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
   Required: True   Allow empty value : True
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
   params += "whereClauseVendor=" + whereClauseVendor
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendorAttch=" + whereClauseVendorAttch
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
   params += "whereClauseTaxExempt=" + whereClauseTaxExempt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePartner=" + whereClausePartner
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClausePEVendWhldHist=" + whereClausePEVendWhldHist
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendRestriction=" + whereClauseVendRestriction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendBank=" + whereClauseVendBank
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendBankAttch=" + whereClauseVendBankAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendCntMain=" + whereClauseVendCntMain
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVenMFBill=" + whereClauseVenMFBill
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendorPP=" + whereClauseVendorPP
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVenPPMFBill=" + whereClauseVenPPMFBill
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVenPPUPSEmail=" + whereClauseVenPPUPSEmail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendPPRestriction=" + whereClauseVendPPRestriction
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendCnt=" + whereClauseVendCnt
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendCntAttch=" + whereClauseVendCntAttch
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVenUPSEmail=" + whereClauseVenUPSEmail
   if(firstParam):
      params += "?"
      firstParam = False
   else:
      params += "&"
   params += "whereClauseVendRemitTo=" + whereClauseVendRemitTo
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def get_GetByID(vendorNum, epicorHeaders = None):
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
   params += "vendorNum=" + vendorNum

   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List" + params,headers=creds) as resp:
           return await resp.json()

async def post_GetNettingSupplierList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNettingSupplierList
   Description: Returns a list of Netting Suppliers only rows that satisfy the where clause.
   OperationID: GetNettingSupplierList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNettingSupplierList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNettingSupplierList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeBankBranchCode(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeBankBranchCode
   Description: Check if the Bank Branch code changed.
   OperationID: ChangeBankBranchCode
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeBankBranchCode_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeBankBranchCode_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeCalendar(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeCalendar
   Description: Change Calendar for new and updated vendors
   OperationID: ChangeCalendar
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeCalendar_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeCalendar_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeTaxRegion(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeTaxRegion
   Description: This method validates TaxRegionCode and populates description for supplier.
   OperationID: ChangeTaxRegion
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeTaxRegion_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeTaxRegion_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRemitToType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRemitToType
   Description: Future logic for scr 114469. Currently on hold. Check if the RemitToType changed.
   OperationID: ChangeRemitToType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRemitToType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRemitToType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeRemitToID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeRemitToID
   Description: Future logic for scr 114469. Currently on hold.  Check if the RemitToID changed.
   OperationID: ChangeRemitToID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeRemitToID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeRemitToID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendRemitToCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendRemitToCountry
   Description: Future logic for scr 114469. Currently on hold.  Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendRemitToCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendRemitToCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendRemitToCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CompareCountryTaxLiabality(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CompareCountryTaxLiabality
   Description: This method compares the Vendor TaxRegionCode with the Country TaxRegionCode
   OperationID: CompareCountryTaxLiabality
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CompareCountryTaxLiabality_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CompareCountryTaxLiabality_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendBankPayMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendBankPayMethod
   Description: Method to change the payment method.
   OperationID: ChangeVendBankPayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendBankPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendBankPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendPayMethod(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendPayMethod
   Description: Method to change the payment method.
   OperationID: ChangeVendPayMethod
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendPayMethod_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendPayMethod_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVenMFBillCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVenMFBillCountry
   Description: Method to change related fields to the county within Manifest Billing. Run when the country changes.
   OperationID: ChangeVenMFBillCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVenMFBillCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVenMFBillCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVenPPMFBillCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVenPPMFBillCountry
   Description: Method to change related fields to the county within Purchase Points Manifest Billing. Run when the country changes.
   OperationID: ChangeVenPPMFBillCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVenPPMFBillCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVenPPMFBillCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendGlobalVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendGlobalVendor
   Description: Method to call when changing the global vendor flag on a vendor.
Assigns the GlbFlag base on the new value.
   OperationID: ChangeVendGlobalVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendGlobalVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendGlobalVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendICTrader(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendICTrader
   Description: Method to call when changing the ICTrader flag on a vendor.
Assigns the EnableGlobalVendor based on the new value.
   OperationID: ChangeVendICTrader
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendICTrader_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendICTrader_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendPPCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendPPCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendPPCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendPPCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendPPCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendPPFFCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendPPFFCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendPPFFCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendPPFFCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendPPFFCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendBankCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendBankCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendBankCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendBankCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendBankCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendBankBCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendBankBCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendBankBCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendBankBCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendBankBCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ChangeVendFFCountry(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ChangeVendFFCountry
   Description: Method to change related fields to the county. Run when the country changes.
   OperationID: ChangeVendFFCountry
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ChangeVendFFCountry_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ChangeVendFFCountry_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckRUC(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckRUC
   Description: CSF Peru - This method test the validity of the Tax ID (RUC)
   OperationID: CheckRUC
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckRUC_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckRUC_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckVATFormat(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckVATFormat
   Description: This method test the validity of the VAT format
   OperationID: CheckVATFormat
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckVATFormat_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckVATFormat_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_DefaultName(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method DefaultName
   Description: If the Vendor Contact name is updated this method will parse the name into
firstname middlename and lastname fields.
If one of the name components is updated the components will be assembled into
the Vendor Contact name field
            
The contact must exist in the database before this method can be run. This means
that the update method must be run first.
            
The rowmod column must be set to 'U' in order for the method to process the record.
            
This procedure passes a dataset in and out,
   OperationID: DefaultName
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/DefaultName_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/DefaultName_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_EnablePriceList(epicorHeaders = None):
   """  
   Summary: Invoke method EnablePriceList
   Description: This method checks to see if the price list option should be enabled or not
based on security rights.
   OperationID: EnablePriceList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/EnablePriceList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetAddrElementList(epicorHeaders = None):
   """  
   Summary: Invoke method GetAddrElementList
   Description: This method calculates Address Element List
   OperationID: GetAddrElementList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetAddrElementList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_GetByVendID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetByVendID
   Description: Get vendor by ID
   OperationID: GetByVendID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetByVendID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetByVendID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetGlbVendorList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetGlbVendorList
   Description: This method returns the GlbVendor dataset based on a delimited list of
GlbVendorNum values passed in.
If GlbVendor.VendorNum = -1 that means the record has been skipped and should be shown
at the bottom of the browser. (GlbVendor only)
   OperationID: GetGlbVendorList
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetGlbVendorList_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetGlbVendorList_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetPerConData(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetPerConData
   Description: Gets the person contact information.
   OperationID: GetPerConData
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetPerConData_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetPerConData_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorForLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorForLink
   Description: This returns the Vendor dataset for linking.
   OperationID: GetVendorForLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorForLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorForLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorGlobalFieldsWithoutGlobalLock(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorGlobalFieldsWithoutGlobalLock
   Description: Returns the list of fields that are maintained by the "Master/Owner" of the global record without the GlobalLock field.
   OperationID: GetVendorGlobalFieldsWithoutGlobalLock
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorGlobalFieldsWithoutGlobalLock_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorGlobalFieldsWithoutGlobalLock_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetvendorGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetvendorGlobalFields
   Description: return the list of fields that are maintained by the "Master/Owner" of global record
   OperationID: GetvendorGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetvendorGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetvendorGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorPPGlobalFieldsWithPrimaryPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorPPGlobalFieldsWithPrimaryPP
   Description: Returns the list of fields that are maintained by the "Master/Owner" of the global record with the PrimaryPP field.
   OperationID: GetVendorPPGlobalFieldsWithPrimaryPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorPPGlobalFieldsWithPrimaryPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorPPGlobalFieldsWithPrimaryPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetvendorPPGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetvendorPPGlobalFields
   Description: return the list of fields that are maintained by the "Master/Owner" of global record
   OperationID: GetvendorPPGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetvendorPPGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetvendorPPGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendCntGlobalFieldsWithPrimaryContact(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendCntGlobalFieldsWithPrimaryContact
   Description: Returns the list of fields that are maintained by the "Master/Owner" of the global record with the PerConName and PrimaryContact fields.
   OperationID: GetVendCntGlobalFieldsWithPrimaryContact
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendCntGlobalFieldsWithPrimaryContact_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendCntGlobalFieldsWithPrimaryContact_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetvendCntGlobalFields(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetvendCntGlobalFields
   Description: return the list of fields that are maintained by the "Master/Owner" of global record
   OperationID: GetvendCntGlobalFields
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetvendCntGlobalFields_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetvendCntGlobalFields_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorPPForLink(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorPPForLink
   Description: This returns the VendorPP record in the Vendor dataset for linking.
   OperationID: GetVendorPPForLink
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorPPForLink_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorPPForLink_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GlbVendorsExist(epicorHeaders = None):
   """  
   Summary: Invoke method GlbVendorsExist
   Description: This method checks if GlbVendor records exists or not.  Can be used
to determine if the option to link/unlink vendors is available.
   OperationID: GlbVendorsExist
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
   Returns: 
      200 Desc: OK => reference#/components/schemas/GlbVendorsExist_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List",headers=creds) as resp:
           return await resp.json()

async def post_LinkGlbVendCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkGlbVendCnt
   Description: This method performs the actual logic to link VendCnt records for a linked vendor.
It will only allow VendCnt's of linked vendors to be processed, otherwise an exception
will be raised.  The ability to link VendCnt's for a linked Vendor should be offered
immediately after performing the update method on a Linked Vendor or a Linked Purchase Point
but it does not have to be limited to that time only.
If the Contact is for a VendCnt that already exists, the GlbVendCnt information is
translated and then copied to the VendorDataSet as an update.
If the Contact is for a new Vendor or Purchase Point, the GlbVendCnt information is translated
and then copied to the VendorDataSet as an Add.  Until the update method is run on the Contact
record the Link process is not completed.
If this link is for a contact on the Vendor, the contact data in the VendorDataSet
will be returned in the VendCntMain datatable.  If it is for a purchase point, the data will
returned in the VendCnt datatable.  This is determined by the value of glbPurPoint.  If it is
blank, it is processed as a contact for the vendor; otherwise it is process as a contact for
the purchase point.
   OperationID: LinkGlbVendCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LinkGlbVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkGlbVendor
   Description: This method performs the actual logic behind linking a Vendor.  It is run after
the PreLinkGlbVendor method which determines the Vendor ID to link to.
If the Vendor Id is for a Vendor that already exists, the GlbVendor information is
translated and then copied to the VendorDataSet as an update.
If the Vendor ID is for a new Vendor, the GlbVendor information is translated and then
copied to the VendorDataSet as an Add.  Until the update method is run on Vendor record
the Link process is not completed.
Once the Vendor record has been linked, the GlbVendorPP and GlbVendCnt records needs to
be offered up to be linked as well.
   OperationID: LinkGlbVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_LinkGlbVendorPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method LinkGlbVendorPP
   Description: This method performs the actual logic to link VendorPP records for a linked vendor.
It will only allow VendorPP's of linked vendors to be processed, otherwise an exception
will be raised.  The ability to link VendorPP's for a linked Vendor should be offered
immediately after performing the update method on a Linked Vendor but it does not have
to be limited to that time only.
It is run after the PreLinkGlbVendorPP method which determines the PurPoint to link to.
If the PurPoint is for a VendorPP that already exists, the GlbVendorPP information is
translated and then copied to the VendorDataSet as an update.
If the PurPoint is for a new VendorPP, the GlbVendorPP information is translated and then
copied to the VendorDataSet as an Add.  Until the update method is run on the VendorPP
record the Link process is not completed.
Once the VendorPP record has been linked, the GlbVendCnt records need to be offered up
to be linked as well.
   OperationID: LinkGlbVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/LinkGlbVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/LinkGlbVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshGlbVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshGlbVendor
   Description: Refresh global vendor row
   OperationID: RefreshGlbVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshGlbVendorPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshGlbVendorPP
   Description: Refresh global purchase point row
   OperationID: RefreshGlbVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshGlbVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshGlbVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_RefreshGlbVendCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method RefreshGlbVendCnt
   Description: Refresh global contact row
   OperationID: RefreshGlbVendCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/RefreshGlbVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/RefreshGlbVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkipGlbVendorPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkipGlbVendorPP
   Description: Mark unlinked GlbVendorPP records as skipped
   OperationID: SkipGlbVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipGlbVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkipSingleGlbVendorPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkipSingleGlbVendorPP
   Description: Mark a specific GlbVendorPP records as skipped
   OperationID: SkipSingleGlbVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipSingleGlbVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipSingleGlbVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkipGlbVendCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkipGlbVendCnt
   Description: Mark unlinked GlbVendCnt records as skipped
   OperationID: SkipGlbVendCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipGlbVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkipSingleGlbVendCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkipSingleGlbVendCnt
   Description: Mark a specific GlbVendCnt records as skipped
   OperationID: SkipSingleGlbVendCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipSingleGlbVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipSingleGlbVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ModifySearchIDs(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ModifySearchIDs
   Description: Modify Search ID.
   OperationID: ModifySearchIDs
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ModifySearchIDs_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ModifySearchIDs_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreLinkGlbVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreLinkGlbVendor
   Description: Linking a GlbVendor record ties a global record to a new or existing Vendor record so
that any changes made to the GlbVendor record in another company are automatically copied
to any linked Vendors.
This method performs the pre link logic to check of okay to link or get the new vendid
to create/link to.  Will be run before LinkGlbVendor which actually creates/updates a
Vendor record and will send the modified record back for update.  When the Link "button" is
originally selected, the LinkVendID will be defaulted to the GlbVendorId field.  It will then
check to see if this ID is available for Use.  If available for use the system will return a
question asking the user if they want to use this number.  If the answer is no, then the user
either needs to select an existing Vendor's ID to link to or enter a brand new ID.  You will
run this method until the user answer is yes.  Then the LinkGlbVendor method is called.
   OperationID: PreLinkGlbVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreLinkGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_PreLinkGlbVendorPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method PreLinkGlbVendorPP
   Description: Linking a GlbVendorPP record ties a global record to a new or existing Purchase Point record so
that any changes made to the GlbVendorPP record in another company are automatically copied
to any linked purchase points.
This method performs the pre link logic to check of okay to link or get the new PurPoint
to create/link to.  Will be run before LinkGlbVendorPP which actually creates/updates a
purchase point record and will send the modified record back for update.  When the Link "button" is
originally selected, the LinkPurPoint will be defaulted to the glbPurPoint field.
It will then check to see if this ID is available for use.  If available for use the system
will return a question asking the user if they want to use this number.  If the answer is no,
then the user either needs to select an existing PurPoint for the current customer to link
to or enter a brand new PurPoint for the vendor.  You will run this method until the
user's answer is yes.  Then the LinkGlbVendorPP method is called.
   OperationID: PreLinkGlbVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/PreLinkGlbVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/PreLinkGlbVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ResetPPIntl(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ResetPPIntl
   Description: Purpose:
Parameters:
<param name="ds">The Vendor data set</param>
Notes:
   OperationID: ResetPPIntl
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ResetPPIntl_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ResetPPIntl_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SetUPSQVEnable(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SetUPSQVEnable
   Description: Purpose:
Parameters:
<param name="ipQVEnable">logical indicating if the quantum view is to enabled/disabled</param><param name="ipUpdVenUPS">Yes, if the VenUPSEmail table is to be updated</param><param name="ipUPDVenPPUPS">Yes, if the VenUPSPPEmail talbe is to be updated</param><param name="ds">The Vendor data set</param>
Notes:
   OperationID: SetUPSQVEnable
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SetUPSQVEnable_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SetUPSQVEnable_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_SkipGlbVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method SkipGlbVendor
   Description: This method performs the logic behind the skip option for GlbVendor
Skip - marks the VendorNum field with a -1 to move the record to the bottom of the list
if the VendorNum field is not 0 will error out
   OperationID: SkipGlbVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/SkipGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/SkipGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_UnlinkGlbVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method UnlinkGlbVendor
   Description: This method performs the logic behind the unlink option for GlbVendor
Unlink - clears the VendorNum and VendorID field in GlbVendor.  Returns the Vendor DataSet
   OperationID: UnlinkGlbVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/UnlinkGlbVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/UnlinkGlbVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidatePayBTFlag(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidatePayBTFlag
   Description: Purpose:
Parameters:
<param name="ipPayBTFlag">requested pay bt flag to edit</param><param name="ipValVen"> logical indicating if the pay flag on the venMFBill is to be checked</param><param name="ipValVenPP">logical indicating if the pay flag on the venPPMFBill is to be checked</param><param name="ipVendorNum">Vendor Number</param><param name="ipPurPoint">Purchase Point</param>
Notes:
   OperationID: ValidatePayBTFlag
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidatePayBTFlag_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidatePayBTFlag_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_VendorBankExists(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method VendorBankExists
   Description: This method checks vendor bank existence.
   OperationID: VendorBankExists
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/VendorBankExists_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/VendorBankExists_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBankCustNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBankCustNum
   Description: Check Bank Customer Number
At this time this method is specific to Switzerland localization
   OperationID: CheckBankCustNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBankCustNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBankCustNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckBankCustNumSetup(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckBankCustNumSetup
   Description: Check Bank Customer Number Setup
At this time this method is specific to Switzerland localization
   OperationID: CheckBankCustNumSetup
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckBankCustNumSetup_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckBankCustNumSetup_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckISRPartyID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckISRPartyID
   Description: Check ISR Party ID
At this time this method is specific to Switzerland localization
   OperationID: CheckISRPartyID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckISRPartyID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckISRPartyID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_CheckPOBankAcctNum(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method CheckPOBankAcctNum
   Description: Check Postal Account
At this time this method is specific to Switzerland localization
   OperationID: CheckPOBankAcctNum
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/CheckPOBankAcctNum_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/CheckPOBankAcctNum_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetCodeDescList(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetCodeDescList
   Description: Retrieve Validation from Service designer
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_StorePartner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method StorePartner
   Description: Stores Partner
   OperationID: StorePartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/StorePartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/StorePartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeCode1099(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeCode1099
   Description: Call this method when the user enters the ttVendor.Code1099ID
   OperationID: OnChangeCode1099
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeCode1099_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeCode1099_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_OnChangeFormType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method OnChangeFormType
   Description: Call this method when the user enters the ttVendor.FormTypeID
   OperationID: OnChangeFormType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/OnChangeFormType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/OnChangeFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetDefaultFormType(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetDefaultFormType
   Description: Get Default 1099 Type.
   OperationID: GetDefaultFormType
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetDefaultFormType_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetDefaultFormType_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_TypeTINVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method TypeTINVendor
   Description: Return true if vendor TIN and TINType record exists
   OperationID: TypeTINVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/TypeTINVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/TypeTINVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_getPrimaryBankID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method getPrimaryBankID
   Description: Retrieve BankID from vendor returning true if found
   OperationID: getPrimaryBankID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/getPrimaryBankID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/getPrimaryBankID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorListRemmitance(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorListRemmitance
   Description: Returns a List Dataset for Remittance Advice report
   OperationID: GetVendorListRemmitance
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorListRemmitance_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorListRemmitance_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetVendorListSorted(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetVendorListSorted
   Description: Returns a List Dataset for advanced sorting
   OperationID: GetVendorListSorted
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetVendorListSorted_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetVendorListSorted_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_ValidateTaxID(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method ValidateTaxID
   Description: Supplier Tax Id validation
   OperationID: ValidateTaxID
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/ValidateTaxID_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/ValidateTaxID_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendor(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendor
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendor
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendor_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendor_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendorAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendorAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendorAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendorAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendorAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewTaxExempt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewTaxExempt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewTaxExempt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewTaxExempt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewTaxExempt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewPartner(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewPartner
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewPartner
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewPartner_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewPartner_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendRestriction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendBank(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendBank
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendBank
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendBank_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendBank_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendBankAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendBankAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendBankAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendBankAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendBankAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendCntMain(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendCntMain
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendCntMain
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendCntMain_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendCntMain_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVenMFBill(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVenMFBill
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVenMFBill
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVenMFBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVenMFBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendorPP(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendorPP
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendorPP
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendorPP_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendorPP_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVenPPMFBill(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVenPPMFBill
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVenPPMFBill
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVenPPMFBill_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVenPPMFBill_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVenPPUPSEmail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVenPPUPSEmail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVenPPUPSEmail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVenPPUPSEmail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVenPPUPSEmail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendPPRestriction(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendPPRestriction
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendPPRestriction
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendPPRestriction_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendPPRestriction_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendCnt(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendCnt
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendCnt
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendCnt_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendCnt_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendCntAttch(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendCntAttch
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendCntAttch
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendCntAttch_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendCntAttch_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVenUPSEmail(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVenUPSEmail
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVenUPSEmail
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVenUPSEmail_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVenUPSEmail_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()

async def post_GetNewVendRemitTo(requestBody, epicorHeaders = None):
   """  
   Summary: Invoke method GetNewVendRemitTo
   Description: Inserts a new row in the DataSet with defaults populated.
   OperationID: GetNewVendRemitTo
      :param epicorHeaders: A string representing the epicor log in information to be used, 
         already converted to base64 in the format username:password, defaults to the configEpicorSchemas creds
      :param requestBody: Desc: Input parameters  => reference#/components/schemas/GetNewVendRemitTo_input
   Returns: 
      200 Desc: OK => reference#/components/schemas/GetNewVendRemitTo_output
      500 Desc: Internal server error. Server is unable to process the request.
   """  


   creds = configEpicorSchemas.epicorCreds
   if(epicorHeaders != None):
         creds = epicorHeaders

   async with aiohttp.ClientSession() as session:
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List" + params,headers=creds) as resp:
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
       async with session.get(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List" + params,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
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
       async with session.post(configEpicorSchemas.epicorURL + "Erp.BO.VendorSvc/List", json=requestBody,headers=creds) as resp:
           return await resp.json()




#########################################################################
# OData Schemas:
#########################################################################
class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_EntityGLCRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_EntityGLCRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PEVendWhldHistRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PEVendWhldHistRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_PartnerRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_TaxExemptRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_TaxExemptRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenMFBillRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VenMFBillRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPMFBillRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VenPPMFBillRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenPPUPSEmailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VenPPUPSEmailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VenUPSEmailRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VenUPSEmailRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendBankAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendBankRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendBankRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendCntAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntMainRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendCntMainRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendCntRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendCntRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendPPRestrictionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendPPRestrictionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendRemitToRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendRemitToRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendRestrictionRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendRestrictionRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorAttchRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendorAttchRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorListRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendorListRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorPPRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendorPPRow] = obj["value"]
      pass

class Epicor_RESTApi_Help_ODataSetResponse_System_Collections_Generic_List_Erp_Tablesets_VendorRow:
   def __init__(self, obj):
      self.odatametadata:str = obj["odatametadata"]
      self.value:list[Erp_Tablesets_VendorRow] = obj["value"]
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

class Erp_Tablesets_PEVendWhldHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number  """  
      self.RecordSeq:int = obj["RecordSeq"]
      """  Record Sequence  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Create Date  """  
      self.UserID:str = obj["UserID"]
      """  User Identifier  """  
      self.IdentityDocType:str = obj["IdentityDocType"]
      """  Displays the Identity DocumentType  """  
      self.GoodContributor:bool = obj["GoodContributor"]
      """  Indicates if supplier has a Good Contributor status  """  
      self.WithholdingAgent:bool = obj["WithholdingAgent"]
      """  Indicates if supplier is a Withholding Agent  """  
      self.CollectionAgent:bool = obj["CollectionAgent"]
      """  Indicates the status of Collection Agent  """  
      self.NotFound:bool = obj["NotFound"]
      """  Not Found withholding status  """  
      self.NoAddress:bool = obj["NoAddress"]
      """  No Address Provided withholding status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.PartnerType:int = obj["PartnerType"]
      """  PartnerType  """  
      self.SearchID:str = obj["SearchID"]
      """  SearchID  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PartnerID:str = obj["PartnerID"]
      """  PartnerID  """  
      self.DspSearchID:str = obj["DspSearchID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxExemptRow:
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
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Exemption Effective Start Date  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Exemption Effective End Date  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.TextCode:str = obj["TextCode"]
      """  Tax Legal Text Code  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Tax Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Tax Resolution Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNum:int = obj["CustNum"]
      """  A unique Customer identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique Vendor identifier.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SalesTaxDescription:str = obj["SalesTaxDescription"]
      self.SalesTRCDescription:str = obj["SalesTRCDescription"]
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VenMFBillRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PayBTFlag:str = obj["PayBTFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayTypeDesc:str = obj["PayTypeDesc"]
      """   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Billing Address  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping biling address line 2  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping biling address line 3.  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping billing city  """  
      self.PayBTState:str = obj["PayBTState"]
      """  Shipping Billing state or province  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  Manifest Bililng postal code.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  Shipping biling country  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Internal field used to store the country number.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping billing phone number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PayBTCountryNumDescription:str = obj["PayBTCountryNumDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VenPPMFBillRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PayBTFlag:str = obj["PayBTFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayTypeDesc:str = obj["PayTypeDesc"]
      """   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Billing Address  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping biling address line 2  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping biling address line 3.  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping billing city  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  Pay manifest billing postal code.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  Shipping Billing state or province  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  Shipping biling country  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Internal field used to store the country number.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping billing phone number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PayBTCountryNumDescription:str = obj["PayBTCountryNumDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VenPPUPSEmailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantum View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email address to notify for a UPS shipment  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Logical indicating if the EmailAddress is to be updated at shipping.  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  Logical indicating if the ups quantum view fields are to be enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VenUPSEmailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantum View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email address to notify for a UPS shipment  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Logical indicating if the EmailAddress is to be updated at shipping.  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  logical indicating if the UPS quantum view fields are to be enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendBankAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.BankID:str = obj["BankID"]
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

class Erp_Tablesets_VendBankRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.BankName:str = obj["BankName"]
      """  Supplier Bank Name  """  
      self.Address1:str = obj["Address1"]
      """  First Address Line of the Supplier Bank  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line of the Supplier Bank  """  
      self.Address3:str = obj["Address3"]
      """  Third Address Line of the Supplier Bank  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Supplier Bank  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Postal Code or Zip code portion of the address of the Supplier Bank  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.NameOnAccount:str = obj["NameOnAccount"]
      """  Name on the Bank Account.  """  
      self.SwiftNum:str = obj["SwiftNum"]
      """  Swift number of the bank.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Bank Branch Code of the Supplier Bank  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code of the Supplier Bank  """  
      self.SECreditTransNum:str = obj["SECreditTransNum"]
      """  Sweden localization field, Credit Transfer Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account of the Supplier Bank  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC of the Supplier Bank  """  
      self.BankPersonCode:str = obj["BankPersonCode"]
      """  Free Form Bank Person Code. Used in localizations.  """  
      self.VendAccountType:str = obj["VendAccountType"]
      """  Supplier bank Account Type. Used in localizations.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BankRefCode:str = obj["BankRefCode"]
      """   Denmark Localization
Bank Reference code  """  
      self.AllowAsAltRemitToBank:bool = obj["AllowAsAltRemitToBank"]
      """  AllowAsAltRemitToBank  """  
      self.DFIIdentification:str = obj["DFIIdentification"]
      """  DFIIdentification  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHDTAID:str = obj["CHDTAID"]
      """  CHDTAID  """  
      self.CHISRPartyID:str = obj["CHISRPartyID"]
      """  CHISRPartyID  """  
      self.FeeOwnership:str = obj["FeeOwnership"]
      """  FeeOwnership  """  
      self.POBankAcctNum:str = obj["POBankAcctNum"]
      """  POBankAcctNum  """  
      self.BankCustNum:str = obj["BankCustNum"]
      """  BankCustNum  """  
      self.BankCustNumberStartPos:int = obj["BankCustNumberStartPos"]
      """  BankCustNumberStartPos  """  
      self.BankCustNumberLen:int = obj["BankCustNumberLen"]
      """  BankCustNumberLen  """  
      self.BAddress1:str = obj["BAddress1"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress2:str = obj["BAddress2"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress3:str = obj["BAddress3"]
      """  Specifies the supplier's bank address.  """  
      self.BankCharges:str = obj["BankCharges"]
      """  Bank Charges (Used for Czech Republic CSF)  """  
      self.BankCnstSymbol:str = obj["BankCnstSymbol"]
      """  Bank Constant Symbol (Used for Czech Republic CSF)  """  
      self.BankSpecSymbol:str = obj["BankSpecSymbol"]
      """  Bank Special Symbol (Used for Czech Republic CSF)  """  
      self.BankType:str = obj["BankType"]
      """  Bank type of electronic payment transactions  """  
      self.BCity:str = obj["BCity"]
      """  Specifies the supplier's bank city.  """  
      self.BCountryNum:int = obj["BCountryNum"]
      """  Specifies the supplier's bank country.  """  
      self.BPostalCode:str = obj["BPostalCode"]
      """  Specifies the supplier's postal code.  """  
      self.BState:str = obj["BState"]
      """  Specifies the supplier's bank state/province.  """  
      self.NOChequeCode:str = obj["NOChequeCode"]
      """  Norway CSF: Determines where bank cheque is sent.  """  
      self.NOFeeCostCode:str = obj["NOFeeCostCode"]
      """  Norway CSF: Determines how the bank fee cost will be settled between the company and supplier during the fund transfers between two entities.  """  
      self.ReceiverName:str = obj["ReceiverName"]
      """  Receiver Name.  Used in Japan localizations.  """  
      self.ReceivingBankName:str = obj["ReceivingBankName"]
      """  Receiving Bank Name.  Used in Japan localizations.  """  
      self.ReceivingBankNum:str = obj["ReceivingBankNum"]
      """  Receiving Bank Number.  Used in Japan localizations.  """  
      self.ReceivingBranchName:str = obj["ReceivingBranchName"]
      """  Receiving Branch Name.  Used in Japan localizations.  """  
      self.ReceivingBranchNum:str = obj["ReceivingBranchNum"]
      """  Receiving Branch Number.  Used in Japan localizations.  """  
      self.SEBankFeeCostOwner:str = obj["SEBankFeeCostOwner"]
      """  SEBankFeeCostOwner  """  
      self.PEDetractionsNBA:bool = obj["PEDetractionsNBA"]
      """  PEDetractionsNBA  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MX SAT Code  """  
      self.MXSATNameShort:str = obj["MXSATNameShort"]
      """  MX SAT Name Short  """  
      self.MXSATNameFull:str = obj["MXSATNameFull"]
      """  MX SAT Name Full  """  
      self.DKCreditorNum:str = obj["DKCreditorNum"]
      """  DKCreditorNum  """  
      self.PayID:str = obj["PayID"]
      """  A supplier alias used to make and receive payments.  """  
      self.ClearSystemIDCode:str = obj["ClearSystemIDCode"]
      """  ClearSystemIDCode  """  
      self.MemberID:str = obj["MemberID"]
      """  MemberID  """  
      self.BCountry:int = obj["BCountry"]
      self.CHScrPOBankAcctNum:str = obj["CHScrPOBankAcctNum"]
      """  Postal Account Number in format XX-#####V-P (CSF Switzerland)  """  
      self.PrimaryBank:bool = obj["PrimaryBank"]
      self.CHScrISRPartyID:str = obj["CHScrISRPartyID"]
      """  ISR Party Number in format XX-#####V-P (CSF Switzerland)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      self.BCountryNumDescription:str = obj["BCountryNumDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendCntAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.ConNum:int = obj["ConNum"]
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

class Erp_Tablesets_VendCntMainRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact number.  Unique identifier for the contact record.  """  
      self.Name:str = obj["Name"]
      """  Contact name.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Contact email address.  """  
      self.WebPassword:str = obj["WebPassword"]
      """  Password for SF/Portal, should not be easily editable from the Manufacturing System.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates if able to access the Supplier Workbench  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Link to the RoleCD table.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contacts Cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contacts Pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contacts Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contacts Alternate number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The Contacts Title  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name if the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is no longer contacted.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Inactive:bool = obj["Inactive"]
      """  This contact does not get used on new LOQs  """  
      self.FirstName:str = obj["FirstName"]
      """  First Name  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Middle Name  """  
      self.LastName:str = obj["LastName"]
      """  Last Name  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.Suffix:str = obj["Suffix"]
      """  Suffix  """  
      self.Initials:str = obj["Initials"]
      """  Initials  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      self.PrimaryContact:bool = obj["PrimaryContact"]
      self.VendCntAttrStrng:str = obj["VendCntAttrStrng"]
      self.GlbLink:str = obj["GlbLink"]
      """  GlbVendCnt fields in a linked list to find the linking record  """  
      self.PerConName:str = obj["PerConName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact number.  Unique identifier for the contact record.  """  
      self.Name:str = obj["Name"]
      """  Contact name.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Contact email address.  """  
      self.WebPassword:str = obj["WebPassword"]
      """  Password for SF/Portal, should not be easily editable from the Manufacturing System.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates if able to access the Supplier Workbench  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Link to the RoleCD table.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contacts Cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contacts Pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contacts Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contacts Alternate number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The Contacts Title  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name if the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is no longer contacted.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Inactive:bool = obj["Inactive"]
      """  This contact does not get used on new LOQs  """  
      self.FirstName:str = obj["FirstName"]
      """  First Name  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Middle Name  """  
      self.LastName:str = obj["LastName"]
      """  Last Name  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.Suffix:str = obj["Suffix"]
      """  Suffix  """  
      self.Initials:str = obj["Initials"]
      """  Initials  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimaryContact:bool = obj["PrimaryContact"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.VendCntAttrStrng:str = obj["VendCntAttrStrng"]
      self.GlbLink:str = obj["GlbLink"]
      """  GlbVendCnt fields in a linked list to find the linking record  """  
      self.PerConName:str = obj["PerConName"]
      """  The name of the person contact.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPPRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendRemitToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.RemitToSeq:int = obj["RemitToSeq"]
      """  RemitToSeq  """  
      self.RemitToType:str = obj["RemitToType"]
      """  RemitToType  """  
      self.RemitCustNum:int = obj["RemitCustNum"]
      """  RemitCustNum  """  
      self.RemitEmpID:str = obj["RemitEmpID"]
      """  RemitEmpID  """  
      self.RemitVendorNum:int = obj["RemitVendorNum"]
      """  RemitVendorNum  """  
      self.RemitToName:str = obj["RemitToName"]
      """  RemitToName  """  
      self.DefaultRemitTo:bool = obj["DefaultRemitTo"]
      """  DefaultRemitTo  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.OneCheck:bool = obj["OneCheck"]
      """  OneCheck  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.RemitToAddress1:str = obj["RemitToAddress1"]
      """  RemitToAddress1  """  
      self.RemitToAddress2:str = obj["RemitToAddress2"]
      """  RemitToAddress2  """  
      self.RemitToAddress3:str = obj["RemitToAddress3"]
      """  RemitToAddress3  """  
      self.RemitToCity:str = obj["RemitToCity"]
      """  RemitToCity  """  
      self.RemitToState:str = obj["RemitToState"]
      """  RemitToState  """  
      self.RemitToZip:str = obj["RemitToZip"]
      """  RemitToZip  """  
      self.RemitToCountry:int = obj["RemitToCountry"]
      """  RemitToCountry  """  
      self.RemitToPhoneNum:str = obj["RemitToPhoneNum"]
      """  RemitToPhoneNum  """  
      self.RemitToFaxNum:str = obj["RemitToFaxNum"]
      """  RemitToFaxNum  """  
      self.RemitToEmail:str = obj["RemitToEmail"]
      """  RemitToEmail  """  
      self.TermsCode:str = obj["TermsCode"]
      """  TermsCode  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RemitToID:str = obj["RemitToID"]
      """  This can either be a CustID, EmpID, or VendID depending on the RemitToType  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendorAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
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

class Erp_Tablesets_VendorListRow:
   def __init__(self, obj):
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the system, for linking other records to the Vendor.  """  
      self.Name:str = obj["Name"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.Address1:str = obj["Address1"]
      """  First address line of the Supplier  """  
      self.Address2:str = obj["Address2"]
      """  Second address line of the Supplier  """  
      self.Address3:str = obj["Address3"]
      """  Third address line of the Supplier  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Supplier  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Currency Code Description  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TIN:str = obj["TIN"]
      """  Taxpayer Identification Number  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendorPPRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.Name:str = obj["Name"]
      """  Purchase Point Name...can't be blank.  """  
      self.Address1:str = obj["Address1"]
      """  First address line  """  
      self.Address2:str = obj["Address2"]
      """  Second address line  """  
      self.Address3:str = obj["Address3"]
      """  Third address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  State portion of the address  """  
      self.Zip:str = obj["Zip"]
      """  Postal Code or Zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor purchase point.  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique Identifier from an external G/L interface  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Indicates if the shipment is international.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Certificate of Origin flag  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Commercial Invoice flag.  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Ship Export Declaration flag  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Letter of Instruction flag  """  
      self.FFID:str = obj["FFID"]
      """  Freight Forwarder ID  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Freight Forwarder Company Name  """  
      self.FFContact:str = obj["FFContact"]
      """  Freight Forwarder contact person  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  First address line of the Freight Forwarder  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Second address line of the Freight Forwarder  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Third address line of the Freight Forwarder  """  
      self.FFCity:str = obj["FFCity"]
      """  Freight Forwarder city portion of address.  """  
      self.FFState:str = obj["FFState"]
      """  Freight Forwarder state portion of address.  """  
      self.FFZip:str = obj["FFZip"]
      """  Freight Forwarder Zip code portion of the address  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Freight Forwarder Country portion of the address  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Freight Forwarder Phone Number  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Legal Name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.INExciseRegNumber:str = obj["INExciseRegNumber"]
      """  INExciseRegNumber  """  
      self.INExciseDivision:str = obj["INExciseDivision"]
      """  INExciseDivision  """  
      self.INExciseRange:str = obj["INExciseRange"]
      """  INExciseRange  """  
      self.INCommissionarate:str = obj["INCommissionarate"]
      """  INCommissionarate  """  
      self.INVATNumber:str = obj["INVATNumber"]
      """  INVATNumber  """  
      self.INServiceTaxRegNum:str = obj["INServiceTaxRegNum"]
      """  INServiceTaxRegNum  """  
      self.INTaxRegionCode:str = obj["INTaxRegionCode"]
      """  INTaxRegionCode  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  Municipio Code  """  
      self.GroupCode:str = obj["GroupCode"]
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.PrimaryPP:bool = obj["PrimaryPP"]
      self.VendAttrString:str = obj["VendAttrString"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is a global record  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  Sales Tax ID  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  Service Tax ID  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.MXISTMO:str = obj["MXISTMO"]
      """  Area of ISTMO de Tehuantepec (Polos de Desarrollo). Value is from MXLocISTMO User Code.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.INTaxRegionCodeDescription:str = obj["INTaxRegionCodeDescription"]
      self.TACodeTaxAuthorityDescription:str = obj["TACodeTaxAuthorityDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendorRow:
   def __init__(self, obj):
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the system, for linking other records to the Vendor.  """  
      self.Name:str = obj["Name"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.Address1:str = obj["Address1"]
      """  First address line of the Supplier  """  
      self.Address2:str = obj["Address2"]
      """  Second address line of the Supplier  """  
      self.Address3:str = obj["Address3"]
      """  Third address line of the Supplier  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Supplier  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  """  
      self.OneCheck:bool = obj["OneCheck"]
      """  Indicates that for this vendor all invoices must be paid on separate checks.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  """  
      self.AccountRef:str = obj["AccountRef"]
      """  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability of the Supplier  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payments to this vendors are made via electronic transfer.  """  
      self.PrimaryBankID:str = obj["PrimaryBankID"]
      """  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  """  
      self.Approved:bool = obj["Approved"]
      """   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  """  
      self.ICVend:bool = obj["ICVend"]
      """  This is an inter-company vendor.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor.  """  
      self.WebVendor:bool = obj["WebVendor"]
      """  This vendor is web enabled  """  
      self.VendURL:str = obj["VendURL"]
      """  Vendor URL.  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OnTimeRating:str = obj["OnTimeRating"]
      """  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.QualityRating:str = obj["QualityRating"]
      """  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  """  
      self.PriceRating:str = obj["PriceRating"]
      """  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ServiceRating:str = obj["ServiceRating"]
      """  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.VendPILimit:int = obj["VendPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalVendor:bool = obj["GlobalVendor"]
      """  Marks the vendor as a global vendor, available to be sent out to other companies  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this vendor participates in the Inter-Company Trading.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.MinOrderValue:int = obj["MinOrderValue"]
      """  MinOrderValue  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the production calendar for this Vendor.   If this equals "", then the ProdCal record is the Company Level production calendar.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      """  Should this Supplier be included in Consolidated Purchasing?  """  
      self.LocalPurchasing:bool = obj["LocalPurchasing"]
      """  If the Part Class being purchased is included in Consolidated Purchasing, should purchasing it from this Supplier override that so it will be purchased in this company?  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.CPay:bool = obj["CPay"]
      """  Flag to indicate if the Vendor participates in the Centralized Payment process.  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Indicates if the shipment is international.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Certificate of Origin flag  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Commercial Invoice flag.  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Ship Export Declaration flag  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Letter of Instruction flag  """  
      self.FFID:str = obj["FFID"]
      """  Freight Forwarder ID  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Freight Forwarder Company Name  """  
      self.FFContact:str = obj["FFContact"]
      """  Freight Forwarder contact person  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  First address line of the Freight Forwarder  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Second address line of the Freight Forwarder  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Third address line of the Freight Forwarder  """  
      self.FFCity:str = obj["FFCity"]
      """  Freight Forwarder city portion of address.  """  
      self.FFState:str = obj["FFState"]
      """  Freight Forwarder state portion of address.  """  
      self.FFZip:str = obj["FFZip"]
      """  Freight Forwarder Zip code portion of the address  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Freight Forwarder Country portion of the address  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Freight Forwarder Phone Number  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country Number  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this Supplier.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line for this Supplier.  """  
      self.ManagedCust:bool = obj["ManagedCust"]
      """  Flag indicating whether this vendor is associated with a 3PL customer.  """  
      self.ManagedCustID:str = obj["ManagedCustID"]
      """  CustID of the associated managed customer.  Only populated if ManagedCust flag = true.  """  
      self.ManagedCustNum:int = obj["ManagedCustNum"]
      """  CustNum associated with CustID of managed customer.  Only populated if ManagedCust flag = true.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.HasBank:bool = obj["HasBank"]
      """  If yes, indicates that Vendor has at least one assoicated VendBank record.  """  
      self.PmtAcctRef:str = obj["PmtAcctRef"]
      """  The Payment Banking Reference assigned by the supplier  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal Name  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      """   Indicates Advanced Tax invoice is expected from supplier
after prepayment is done. If this field is set to yes, prepayment
invoice is not crated automatically.  """  
      self.AllowAsAltRemitTo:bool = obj["AllowAsAltRemitTo"]
      """  AllowAsAltRemitTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.THBranchID:str = obj["THBranchID"]
      """  THBranchID  """  
      self.ParamCode:str = obj["ParamCode"]
      """  ParamCode  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGIDDocumentTypeCode:str = obj["AGIDDocumentTypeCode"]
      """  AGIDDocumentTypeCode  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  Colombia Loc Field. OneTimeCustVend new table ID  """  
      self.NoBankingReference:bool = obj["NoBankingReference"]
      """  No Banking Reference  """  
      self.PEGoodsContributor:bool = obj["PEGoodsContributor"]
      """  Peru Goods Contributor withholding status.  """  
      self.PEWithholdAgent:bool = obj["PEWithholdAgent"]
      """  Indicates the status of Peru Withholding Agent  """  
      self.PECollectionAgent:bool = obj["PECollectionAgent"]
      """  Indicates the status of Peru Collection Agent  """  
      self.PENotFound:bool = obj["PENotFound"]
      """  Peru Not Found withholding status.  """  
      self.PENoAddress:bool = obj["PENoAddress"]
      """  Peru No Address Provided withholding status.  """  
      self.PEIdentityDocType:str = obj["PEIdentityDocType"]
      """  Displays the Peru Identity Document Type.  """  
      self.COIsOneTimeVend:bool = obj["COIsOneTimeVend"]
      """  Colombia Loc Field.  """  
      self.PEDocumentID:str = obj["PEDocumentID"]
      """  Peru Document ID.  """  
      self.MaxLateDaysPORel:int = obj["MaxLateDaysPORel"]
      """  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code  """  
      self.TIN:str = obj["TIN"]
      """  Taxpayer Identification Number  """  
      self.TINType:str = obj["TINType"]
      """  TIN Type. Values are 1 for EIN, 2 for SSNs, ITINs, and ATINs and 0 if type of TIN is not terminable.  """  
      self.SecondTINNotice:bool = obj["SecondTINNotice"]
      """  Second TIN Notice  """  
      self.NameControl:str = obj["NameControl"]
      """  Name Control. Optional and used for electronic export.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Specifies the method of shipment. The Ship Via associated with this supplier appears by default, but you can select a different option from the list.  """  
      self.NonUS:bool = obj["NonUS"]
      """  Non US Supplier  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID for the 1099 Code  """  
      self.INSupplierType:str = obj["INSupplierType"]
      """  INSupplierType  """  
      self.INCSTNumber:str = obj["INCSTNumber"]
      """  INCSTNumber  """  
      self.INPANNumber:str = obj["INPANNumber"]
      """  INPANNumber  """  
      self.DEOrgType:str = obj["DEOrgType"]
      """  DEOrgType  """  
      self.PaymentReporting:bool = obj["PaymentReporting"]
      """  PaymentReporting  """  
      self.ExternalPurchasing:bool = obj["ExternalPurchasing"]
      """  This field indicates that this record should be sent over to an external system whenever it is changed/created/deleted, etc.  """  
      self.MXRetentionCode:str = obj["MXRetentionCode"]
      """  MXRetentionCode  """  
      self.Reporting1099Name:str = obj["Reporting1099Name"]
      """  Recipient's name for US 1099 reporting  """  
      self.Reporting1099Name2:str = obj["Reporting1099Name2"]
      """  Reporting1099Name2  """  
      self.FATCA:bool = obj["FATCA"]
      """  FATCA  """  
      self.AccountNum:str = obj["AccountNum"]
      """  AccountNum  """  
      self.TWGUIRegNum:str = obj["TWGUIRegNum"]
      """  TW GUI Code  """  
      self.MXTARCode:str = obj["MXTARCode"]
      """  MXTARCode  """  
      self.PEAddressID:str = obj["PEAddressID"]
      """  PEAddressID  """  
      self.PERetentionRegime:str = obj["PERetentionRegime"]
      """  PERetentionRegime  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  TaxEntityType  """  
      self.INGSTComplianceRate:int = obj["INGSTComplianceRate"]
      """  GST Compliance Rate for India  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.TINValidationStatus:int = obj["TINValidationStatus"]
      """  Validation Status of Taxpayer Identification Number  """  
      self.ImporterOfRecord:bool = obj["ImporterOfRecord"]
      """  Indicates whether this supplier is importer of records or not. Used for Avalara Tax Connect calculation.  """  
      self.PLAutomaticAPInvoiceNum:bool = obj["PLAutomaticAPInvoiceNum"]
      """  PLAutomaticAPInvoiceNum  """  
      self.SEC:str = obj["SEC"]
      """  Standard Entry Class Code  """  
      self.MXDIOTTranType:str = obj["MXDIOTTranType"]
      """  CSF Mexico DIOT Transaction Type  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  Form 1099-K Merchant Category Code  """  
      self.MXTaxpayerType:str = obj["MXTaxpayerType"]
      """  CSF Mexico Taxpayer Type  """  
      self.MXLegalRepRFC:str = obj["MXLegalRepRFC"]
      """  CSF Mexico Legal Representative RFC  """  
      self.MXLegalRepCURP:str = obj["MXLegalRepCURP"]
      """  CSF Mexico Legal Representative CURP  """  
      self.MXLegalRepName:str = obj["MXLegalRepName"]
      """  CSF Mexico Legal Representative Name  """  
      self.MXLegalRepTaxpayerType:str = obj["MXLegalRepTaxpayerType"]
      """  CSF Mexico Legal Representative Taxpayer Type  """  
      self.US1099State:str = obj["US1099State"]
      """  US 1099 State  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  Tax Validation Date  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  Supplier Scheme ID  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  Municipio Code  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.EDISupplier:bool = obj["EDISupplier"]
      """  Flag used to mark a Supplier as EDI.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.BusinessCatList:str = obj["BusinessCatList"]
      """  Delimited list of Business Categories  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.CountryDescription:str = obj["CountryDescription"]
      self.CurrDesc:str = obj["CurrDesc"]
      """  Currency Description.  """  
      self.DocumentMaskID:str = obj["DocumentMaskID"]
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      self.EnableGlobalVendor:bool = obj["EnableGlobalVendor"]
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Indicates if Reverse Charge Method should be enabled.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Vendor is a global vendor (either master or child)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbVendorNum that is linking to this vendor  """  
      self.Integrationflag:bool = obj["Integrationflag"]
      self.NettingCustID:str = obj["NettingCustID"]
      """  A user defined external Netting Customer ID.  This must be existing Customer ID within the file  """  
      self.NettingCustNum:int = obj["NettingCustNum"]
      """  A user defined external Netting Customer Number.  This must be existing Customer Number within the file  """  
      self.RevChargeMethodDesc:str = obj["RevChargeMethodDesc"]
      """  Reverse Charge Method description  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  Sales Tax ID  """  
      self.SearchIDs:str = obj["SearchIDs"]
      """  Automated Bank reconciliation.  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  Service Tax ID  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.VendAttrString:str = obj["VendAttrString"]
      """  Delimited string of vendor attributes  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.MXISTMO:str = obj["MXISTMO"]
      """  Area of ISTMO de Tehuantepec (Polos de Desarrollo). Value is from MXLocISTMO User Code.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGAFIPResponsibilityDescription:str = obj["AGAFIPResponsibilityDescription"]
      self.AGIDDocTypeDescription:str = obj["AGIDDocTypeDescription"]
      self.AGLocationDescription:str = obj["AGLocationDescription"]
      self.AGProvinceCodeDescription:str = obj["AGProvinceCodeDescription"]
      self.CalendarIDDescription:str = obj["CalendarIDDescription"]
      self.Code1099Description:str = obj["Code1099Description"]
      self.CountryNumEUMember:bool = obj["CountryNumEUMember"]
      self.CountryNumISOCode:str = obj["CountryNumISOCode"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      self.GroupCodeGroupDesc:str = obj["GroupCodeGroupDesc"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.TaxAuthCdTaxAuthorityDescription:str = obj["TaxAuthCdTaxAuthorityDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Week1Pymt_c:int = obj["Week1Pymt_c"]
      self.Week2Pymt_c:int = obj["Week2Pymt_c"]
      pass




#########################################################################
# Custom Schemas:
#########################################################################
class ChangeBankBranchCode_input:
   """ Required : 
   proposedBankBranchCode
   ds
   """  
   def __init__(self, obj):
      self.proposedBankBranchCode:str = obj["proposedBankBranchCode"]
      """  The proposed Bank Branch code  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeBankBranchCode_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeCalendar_input:
   """ Required : 
   ic_CalendarID
   ds
   """  
   def __init__(self, obj):
      self.ic_CalendarID:str = obj["ic_CalendarID"]
      """  Calendar Code  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeCalendar_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRemitToID_input:
   """ Required : 
   proposedRemitToID
   ds
   """  
   def __init__(self, obj):
      self.proposedRemitToID:str = obj["proposedRemitToID"]
      """  The proposed RemitTo ID  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeRemitToID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeRemitToType_input:
   """ Required : 
   proposedRemitToType
   ds
   """  
   def __init__(self, obj):
      self.proposedRemitToType:str = obj["proposedRemitToType"]
      """  The proposed RemitTo type  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeRemitToType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeTaxRegion_input:
   """ Required : 
   iProposedTaxRgnCode
   ds
   """  
   def __init__(self, obj):
      self.iProposedTaxRgnCode:str = obj["iProposedTaxRgnCode"]
      """  The proposed TaxCode value  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeTaxRegion_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVenMFBillCountry_input:
   """ Required : 
   i_CountryNum
   ds
   """  
   def __init__(self, obj):
      self.i_CountryNum:int = obj["i_CountryNum"]
      """  Country Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVenMFBillCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVenPPMFBillCountry_input:
   """ Required : 
   i_CountryNum
   ds
   """  
   def __init__(self, obj):
      self.i_CountryNum:int = obj["i_CountryNum"]
      """  Country Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVenPPMFBillCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendBankBCountry_input:
   """ Required : 
   i_CountryNum
   ds
   """  
   def __init__(self, obj):
      self.i_CountryNum:int = obj["i_CountryNum"]
      """  Country Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendBankBCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendBankCountry_input:
   """ Required : 
   i_CountryNum
   ds
   """  
   def __init__(self, obj):
      self.i_CountryNum:int = obj["i_CountryNum"]
      """  Country Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendBankCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendBankPayMethod_input:
   """ Required : 
   i_PayMethodNum
   ds
   """  
   def __init__(self, obj):
      self.i_PayMethodNum:int = obj["i_PayMethodNum"]
      """  Payment Method Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendBankPayMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendCountry_input:
   """ Required : 
   i_CountryNum
   ds
   """  
   def __init__(self, obj):
      self.i_CountryNum:int = obj["i_CountryNum"]
      """  Country Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendFFCountry_input:
   """ Required : 
   i_CountryNum
   ds
   """  
   def __init__(self, obj):
      self.i_CountryNum:int = obj["i_CountryNum"]
      """  FFCountry Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendFFCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendGlobalVendor_input:
   """ Required : 
   proposedGlobalVendor
   ds
   """  
   def __init__(self, obj):
      self.proposedGlobalVendor:bool = obj["proposedGlobalVendor"]
      """  The proposed global vendor value  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendGlobalVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendICTrader_input:
   """ Required : 
   proposedICTrader
   ds
   """  
   def __init__(self, obj):
      self.proposedICTrader:bool = obj["proposedICTrader"]
      """  The proposed ICTrader value  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendICTrader_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendPPCountry_input:
   """ Required : 
   i_CountryNum
   ds
   """  
   def __init__(self, obj):
      self.i_CountryNum:int = obj["i_CountryNum"]
      """  Country Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendPPCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendPPFFCountry_input:
   """ Required : 
   i_CountryNum
   ds
   """  
   def __init__(self, obj):
      self.i_CountryNum:int = obj["i_CountryNum"]
      """  Country Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendPPFFCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendPayMethod_input:
   """ Required : 
   i_PayMethodNum
   ds
   """  
   def __init__(self, obj):
      self.i_PayMethodNum:int = obj["i_PayMethodNum"]
      """  Payment Method Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendPayMethod_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ChangeVendRemitToCountry_input:
   """ Required : 
   i_CountryNum
   ds
   """  
   def __init__(self, obj):
      self.i_CountryNum:int = obj["i_CountryNum"]
      """  Country Number  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ChangeVendRemitToCountry_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBankCustNumSetup_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class CheckBankCustNumSetup_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.OpMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckBankCustNum_input:
   """ Required : 
   ipBankCustNum
   """  
   def __init__(self, obj):
      self.ipBankCustNum:str = obj["ipBankCustNum"]
      """  New value of Bank Customer Number.  """  
      pass

class CheckBankCustNum_output:
   def __init__(self, obj):
      pass

class CheckISRPartyID_input:
   """ Required : 
   ipISRPartyID
   ds
   """  
   def __init__(self, obj):
      self.ipISRPartyID:str = obj["ipISRPartyID"]
      """  New value of ISR Party ID.  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class CheckISRPartyID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckPOBankAcctNum_input:
   """ Required : 
   ipPOBankAcctNum
   ds
   """  
   def __init__(self, obj):
      self.ipPOBankAcctNum:str = obj["ipPOBankAcctNum"]
      """  New value of Postal Account.  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class CheckPOBankAcctNum_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckRUC_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class CheckRUC_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CheckVATFormat_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class CheckVATFormat_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class CompareCountryTaxLiabality_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class CompareCountryTaxLiabality_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.opMessage:str = obj["parameters"]
      self.countryTaxRegionCode:str = obj["parameters"]
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DefaultName_input:
   """ Required : 
   targetField
   ds
   """  
   def __init__(self, obj):
      self.targetField:str = obj["targetField"]
      """  Indicates which fields to populate either "Detail" or "Name"  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class DefaultName_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class DeleteByID_input:
   """ Required : 
   vendorNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      pass

class DeleteByID_output:
   def __init__(self, obj):
      pass

class EnablePriceList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.lEnablePriceList:bool = obj["lEnablePriceList"]
      pass

      """  output parameters  """  

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

class Erp_Tablesets_GlbVendCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact number.  Unique identifier for the contact record.  """  
      self.Name:str = obj["Name"]
      """  Contact name.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Contact email address.  """  
      self.WebPassword:str = obj["WebPassword"]
      """  Password for SF/Portal, should not be easily editable from the Manufacturing System.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates if able to access the Supplier Workbench  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Link to the RoleCD table.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contacts Cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contacts Pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contacts Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contacts Alternate number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The Contacts Title  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name if the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is no longer contacted.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Inactive:bool = obj["Inactive"]
      """  This contact does not get used on new LOQs  """  
      self.FirstName:str = obj["FirstName"]
      """  First Name  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Middle Name  """  
      self.LastName:str = obj["LastName"]
      """  Last Name  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.Suffix:str = obj["Suffix"]
      """  Suffix  """  
      self.Initials:str = obj["Initials"]
      """  Initials  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Owner's Purchase Point  """  
      self.GlbConNum:int = obj["GlbConNum"]
      """  Global Contact number.  Unique identifier for the contact record.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldVendorNum:int = obj["OldVendorNum"]
      """  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  """  
      self.OldPurPoint:str = obj["OldPurPoint"]
      """  Original Owner's Purchase Point - NOT CURRENTLY IN USE  """  
      self.OldConNum:int = obj["OldConNum"]
      """  Original owner's Contact number.  Unique identifier for the contact record. - NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global vendor contacts.  The user can come back at a later time and choose to link a skipped vendor contact if they need to.  """  
      self.FaceBook:str = obj["FaceBook"]
      self.IM:str = obj["IM"]
      self.LinkedIn:str = obj["LinkedIn"]
      self.PerConID:int = obj["PerConID"]
      self.SyncAddressToPerCon:bool = obj["SyncAddressToPerCon"]
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      self.Twitter:str = obj["Twitter"]
      self.WebLink1:str = obj["WebLink1"]
      self.WebLink2:str = obj["WebLink2"]
      self.WebLink3:str = obj["WebLink3"]
      self.WebLink4:str = obj["WebLink4"]
      self.WebLink5:str = obj["WebLink5"]
      self.WebSite:str = obj["WebSite"]
      self.GlbSysRowID:str = obj["GlbSysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.LinkConNum:int = obj["LinkConNum"]
      self.IsLinked:bool = obj["IsLinked"]
      """  Indicates the record is linked  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbVendorPPRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PurPoint:str = obj["PurPoint"]
      self.Name:str = obj["Name"]
      """  Purchase Point Name...can't be blank.  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      self.Zip:str = obj["Zip"]
      self.Country:str = obj["Country"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor purchase point.  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique Identifier from an external G/L interface  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.EDICode:str = obj["EDICode"]
      self.GlbPurPoint:str = obj["GlbPurPoint"]
      """  Owner's Purchase Point  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldVendorNum:int = obj["OldVendorNum"]
      """  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  """  
      self.OldPurPoint:str = obj["OldPurPoint"]
      """  Original Owner's Purchase Point - NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global vendor purchse points.  The user can come back at a later time and choose to link a skipped purchase point if they need to.  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODAmount:int = obj["CODAmount"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODFreight:bool = obj["CODFreight"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DocOnly:bool = obj["DocOnly"]
      self.GroundType:str = obj["GroundType"]
      self.Hazmat:bool = obj["Hazmat"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.RefNotes:str = obj["RefNotes"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.VerbalConf:bool = obj["VerbalConf"]
      self.DeliveryType:str = obj["DeliveryType"]
      self.ServAlert:bool = obj["ServAlert"]
      self.ServAOD:bool = obj["ServAOD"]
      self.ServAuthNum:str = obj["ServAuthNum"]
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      self.ServHomeDel:bool = obj["ServHomeDel"]
      self.ServInstruct:str = obj["ServInstruct"]
      self.ServPhone:str = obj["ServPhone"]
      self.ServPOD:bool = obj["ServPOD"]
      self.ServRef1:str = obj["ServRef1"]
      self.ServRef2:str = obj["ServRef2"]
      self.ServRef3:str = obj["ServRef3"]
      self.ServRef4:str = obj["ServRef4"]
      self.ServRef5:str = obj["ServRef5"]
      self.ServRelease:bool = obj["ServRelease"]
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      self.ServSatPickup:bool = obj["ServSatPickup"]
      self.ServSignature:bool = obj["ServSignature"]
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      self.OverrideService:bool = obj["OverrideService"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.DeliveryConf:int = obj["DeliveryConf"]
      self.FFAddress1:str = obj["FFAddress1"]
      self.FFAddress2:str = obj["FFAddress2"]
      self.FFAddress3:str = obj["FFAddress3"]
      self.FFCity:str = obj["FFCity"]
      self.FFCompName:str = obj["FFCompName"]
      self.FFContact:str = obj["FFContact"]
      self.FFCountry:str = obj["FFCountry"]
      self.FFCountryNum:int = obj["FFCountryNum"]
      self.FFID:str = obj["FFID"]
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      self.FFState:str = obj["FFState"]
      self.FFZip:str = obj["FFZip"]
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      self.IntrntlShip:bool = obj["IntrntlShip"]
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      self.NonStdPkg:bool = obj["NonStdPkg"]
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      self.UPSQVEmailType:str = obj["UPSQVEmailType"]
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      self.LegalName:str = obj["LegalName"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.INExciseRegNumber:str = obj["INExciseRegNumber"]
      """  INExciseRegNumber  """  
      self.INExciseDivision:str = obj["INExciseDivision"]
      """  INExciseDivision  """  
      self.INExciseRange:str = obj["INExciseRange"]
      """  INExciseRange  """  
      self.INCommissionarate:str = obj["INCommissionarate"]
      """  INCommissionarate  """  
      self.INVATNumber:str = obj["INVATNumber"]
      """  INVATNumber  """  
      self.INServiceTaxRegNum:str = obj["INServiceTaxRegNum"]
      """  INServiceTaxRegNum  """  
      self.INTaxRegionCode:str = obj["INTaxRegionCode"]
      """  INTaxRegionCode  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  Municipio Code  """  
      self.LinkPurPoint:str = obj["LinkPurPoint"]
      self.IsLinked:bool = obj["IsLinked"]
      """  Indicates the record is linked  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbVendorRow:
   def __init__(self, obj):
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive Code assigned by the user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  """  
      self.Name:str = obj["Name"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.Address1:str = obj["Address1"]
      self.Address2:str = obj["Address2"]
      self.Address3:str = obj["Address3"]
      self.City:str = obj["City"]
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  """  
      self.Box1099:int = obj["Box1099"]
      """  A user definable field which controls in which box on the 1099 that the amount should be printed.  """  
      self.OneCheck:bool = obj["OneCheck"]
      """  Indicates that for this vendor all invoices must be paid on separate checks.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  """  
      self.AccountRef:str = obj["AccountRef"]
      """  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payments to this vendors are made via electronic transfer.  """  
      self.PrimaryBankID:str = obj["PrimaryBankID"]
      """  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  """  
      self.Approved:bool = obj["Approved"]
      """   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  """  
      self.ICVend:bool = obj["ICVend"]
      """  This is an inter-company vendor.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor.  """  
      self.WebVendor:bool = obj["WebVendor"]
      """  This vendor is web enabled  """  
      self.VendURL:str = obj["VendURL"]
      """  Vendor URL.  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OnTimeRating:str = obj["OnTimeRating"]
      """  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.QualityRating:str = obj["QualityRating"]
      """  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  """  
      self.PriceRating:str = obj["PriceRating"]
      """  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ServiceRating:str = obj["ServiceRating"]
      """  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.VendPILimit:int = obj["VendPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalVendor:bool = obj["GlobalVendor"]
      """  Marks the vendor as a global vendor, available to be sent out to other companies  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this vendor participates in the Inter-Company Trading.  """  
      self.GlbCompany:str = obj["GlbCompany"]
      """  Owner Company Identifier.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlbVendorNum:int = obj["GlbVendorNum"]
      """  A  unique integer assigned by the parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.GlbVendorID:str = obj["GlbVendorID"]
      """  A descriptive Code assigned by the parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor.  """  
      self.MinOrderValue:int = obj["MinOrderValue"]
      """  MinOrderValue  """  
      self.CurrencyBaseCurrCode:str = obj["CurrencyBaseCurrCode"]
      """  A unique code that identifies the currency.  """  
      self.CalendarID:str = obj["CalendarID"]
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      self.OldCompany:str = obj["OldCompany"]
      """  Original Owner Company Identifier. - NOT CURRENTLY IN USE  """  
      self.OldVendorNum:int = obj["OldVendorNum"]
      """  A  unique integer assigned by the original parent system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  - NOT CURRENTLY IN USE  """  
      self.OldVendorID:str = obj["OldVendorID"]
      """  A descriptive Code assigned by the original parent company user to uniquely identify the vendor record. This code must be unique within the file. It should be descriptive as possible. This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This Master key is a little different in that the user can change it. This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses the unchangeable, VendNum field  assigned by the system for linking other records to the Vendor. - NOT CURRENTLY IN USE  """  
      self.Skipped:bool = obj["Skipped"]
      """  Indicates if the user chose to skip this record when linking global vendors.  The user can come back at a later time and choose to link a skipped vendor if they need to.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      self.LocalPurchasing:bool = obj["LocalPurchasing"]
      self.ApplyChrg:bool = obj["ApplyChrg"]
      self.ChrgAmount:int = obj["ChrgAmount"]
      self.COD:bool = obj["COD"]
      self.CODAmount:int = obj["CODAmount"]
      self.CODCheck:bool = obj["CODCheck"]
      self.CODFreight:bool = obj["CODFreight"]
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      self.DeclaredIns:bool = obj["DeclaredIns"]
      self.DocOnly:bool = obj["DocOnly"]
      self.GroundType:str = obj["GroundType"]
      self.Hazmat:bool = obj["Hazmat"]
      self.NotifyEMail:str = obj["NotifyEMail"]
      self.NotifyFlag:bool = obj["NotifyFlag"]
      self.RefNotes:str = obj["RefNotes"]
      self.ResDelivery:bool = obj["ResDelivery"]
      self.SatDelivery:bool = obj["SatDelivery"]
      self.SatPickup:bool = obj["SatPickup"]
      self.VerbalConf:bool = obj["VerbalConf"]
      self.DeliveryType:str = obj["DeliveryType"]
      self.ServAlert:bool = obj["ServAlert"]
      self.ServAOD:bool = obj["ServAOD"]
      self.ServAuthNum:str = obj["ServAuthNum"]
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      self.ServHomeDel:bool = obj["ServHomeDel"]
      self.ServInstruct:str = obj["ServInstruct"]
      self.ServPhone:str = obj["ServPhone"]
      self.ServPOD:bool = obj["ServPOD"]
      self.ServRef1:str = obj["ServRef1"]
      self.ServRef2:str = obj["ServRef2"]
      self.ServRef3:str = obj["ServRef3"]
      self.ServRef4:str = obj["ServRef4"]
      self.ServRef5:str = obj["ServRef5"]
      self.ServRelease:bool = obj["ServRelease"]
      self.ServSatDelivery:bool = obj["ServSatDelivery"]
      self.ServSatPickup:bool = obj["ServSatPickup"]
      self.ServSignature:bool = obj["ServSignature"]
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      self.OverrideService:bool = obj["OverrideService"]
      self.CPay:bool = obj["CPay"]
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      self.DeliveryConf:int = obj["DeliveryConf"]
      self.FFAddress1:str = obj["FFAddress1"]
      self.FFAddress2:str = obj["FFAddress2"]
      self.FFAddress3:str = obj["FFAddress3"]
      self.FFCity:str = obj["FFCity"]
      self.FFCompName:str = obj["FFCompName"]
      self.FFContact:str = obj["FFContact"]
      self.FFCountry:str = obj["FFCountry"]
      self.FFCountryNum:int = obj["FFCountryNum"]
      self.FFID:str = obj["FFID"]
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      self.FFState:str = obj["FFState"]
      self.FFZip:str = obj["FFZip"]
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      self.IntrntlShip:bool = obj["IntrntlShip"]
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      self.NonStdPkg:bool = obj["NonStdPkg"]
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      self.UPSQVEmailType:str = obj["UPSQVEmailType"]
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      self.ManagedCust:bool = obj["ManagedCust"]
      self.ManagedCustID:str = obj["ManagedCustID"]
      self.ManagedCustNum:int = obj["ManagedCustNum"]
      self.PartPayment:bool = obj["PartPayment"]
      self.PMUID:int = obj["PMUID"]
      self.HasBank:bool = obj["HasBank"]
      self.PmtAcctRef:str = obj["PmtAcctRef"]
      self.LegalName:str = obj["LegalName"]
      self.OrgRegCode:str = obj["OrgRegCode"]
      self.TaxRegReason:str = obj["TaxRegReason"]
      self.VendAccountType:str = obj["VendAccountType"]
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.AllowAsAltRemitTo:bool = obj["AllowAsAltRemitTo"]
      """  AllowAsAltRemitTo  """  
      self.THBranchID:str = obj["THBranchID"]
      """  THBranchID  """  
      self.ParamCode:str = obj["ParamCode"]
      """  ParamCode  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGIDDocumentTypeCode:str = obj["AGIDDocumentTypeCode"]
      """  AGIDDocumentTypeCode  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  COOneTimeID  """  
      self.NoBankingReference:bool = obj["NoBankingReference"]
      """  NoBankingReference  """  
      self.PEGoodsContributor:bool = obj["PEGoodsContributor"]
      """  PEGoodsContributor  """  
      self.PEWithholdAgent:bool = obj["PEWithholdAgent"]
      """  PEWithholdAgent  """  
      self.PECollectionAgent:bool = obj["PECollectionAgent"]
      """  PECollectionAgent  """  
      self.PENotFound:bool = obj["PENotFound"]
      """  PENotFound  """  
      self.PENoAddress:bool = obj["PENoAddress"]
      """  PENoAddress  """  
      self.PEIdentityDocType:str = obj["PEIdentityDocType"]
      """  PEIdentityDocType  """  
      self.COIsOneTimeVend:bool = obj["COIsOneTimeVend"]
      """  COIsOneTimeVend  """  
      self.PEDocumentID:str = obj["PEDocumentID"]
      """  PEDocumentID  """  
      self.MaxLateDaysPORel:int = obj["MaxLateDaysPORel"]
      """  MaxLateDaysPORel  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code  """  
      self.TIN:str = obj["TIN"]
      """  TIN  """  
      self.TINType:str = obj["TINType"]
      """  TINType  """  
      self.SecondTINNotice:bool = obj["SecondTINNotice"]
      """  SecondTINNotice  """  
      self.NameControl:str = obj["NameControl"]
      """  NameControl  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  ShipViaCode  """  
      self.NonUS:bool = obj["NonUS"]
      """  NonUS  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  FormTypeID  """  
      self.INSupplierType:str = obj["INSupplierType"]
      """  INSupplierType  """  
      self.INCSTNumber:str = obj["INCSTNumber"]
      """  INCSTNumber  """  
      self.INPANNumber:str = obj["INPANNumber"]
      """  INPANNumber  """  
      self.DEOrgType:str = obj["DEOrgType"]
      """  DEOrgType  """  
      self.PaymentReporting:bool = obj["PaymentReporting"]
      """  PaymentReporting  """  
      self.ExternalPurchasing:bool = obj["ExternalPurchasing"]
      """  ExternalPurchasing  """  
      self.MXRetentionCode:str = obj["MXRetentionCode"]
      """  MXRetentionCode  """  
      self.Reporting1099Name:str = obj["Reporting1099Name"]
      """  Reporting1099Name  """  
      self.Reporting1099Name2:str = obj["Reporting1099Name2"]
      """  Reporting1099Name2  """  
      self.FATCA:bool = obj["FATCA"]
      """  FATCA  """  
      self.AccountNum:str = obj["AccountNum"]
      """  AccountNum  """  
      self.TWGUIRegNum:str = obj["TWGUIRegNum"]
      """  TWGUIRegNum  """  
      self.MXTARCode:str = obj["MXTARCode"]
      """  MXTARCode  """  
      self.PEAddressID:str = obj["PEAddressID"]
      """  PEAddressID  """  
      self.PERetentionRegime:str = obj["PERetentionRegime"]
      """  PERetentionRegime  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  TaxEntityType  """  
      self.INGSTComplianceRate:int = obj["INGSTComplianceRate"]
      """  INGSTComplianceRate  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.TINValidationStatus:int = obj["TINValidationStatus"]
      """  TINValidationStatus  """  
      self.ImporterOfRecord:bool = obj["ImporterOfRecord"]
      """  ImporterOfRecord  """  
      self.PLAutomaticAPInvoiceNum:bool = obj["PLAutomaticAPInvoiceNum"]
      """  PLAutomaticAPInvoiceNum  """  
      self.SEC:str = obj["SEC"]
      """  SEC  """  
      self.MXDIOTTranType:str = obj["MXDIOTTranType"]
      """  MXDIOTTranType  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  US1099KMerchCatCode  """  
      self.MXTaxpayerType:str = obj["MXTaxpayerType"]
      """  MXTaxpayerType  """  
      self.MXLegalRepRFC:str = obj["MXLegalRepRFC"]
      """  MXLegalRepRFC  """  
      self.MXLegalRepCURP:str = obj["MXLegalRepCURP"]
      """  MXLegalRepCURP  """  
      self.MXLegalRepName:str = obj["MXLegalRepName"]
      """  MXLegalRepName  """  
      self.MXLegalRepTaxpayerType:str = obj["MXLegalRepTaxpayerType"]
      """  MXLegalRepTaxpayerType  """  
      self.US1099State:str = obj["US1099State"]
      """  US1099State  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  TaxValidationStatus  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  TaxValidationDate  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  ExternalSchemeID  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  Municipio Code  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.EDISupplier:bool = obj["EDISupplier"]
      """  Flag used to mark a Supplier as EDI.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.DispVendorID:str = obj["DispVendorID"]
      self.LinkVendorID:str = obj["LinkVendorID"]
      """  The VendorId to link to (new or existing)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_GlbVendorTableset:
   def __init__(self, obj):
      self.GlbVendor:list[Erp_Tablesets_GlbVendorRow] = obj["GlbVendor"]
      self.GlbVendCnt:list[Erp_Tablesets_GlbVendCntRow] = obj["GlbVendCnt"]
      self.GlbVendorPP:list[Erp_Tablesets_GlbVendorPPRow] = obj["GlbVendorPP"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_PEVendWhldHistRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number  """  
      self.RecordSeq:int = obj["RecordSeq"]
      """  Record Sequence  """  
      self.CreateDate:str = obj["CreateDate"]
      """  Create Date  """  
      self.UserID:str = obj["UserID"]
      """  User Identifier  """  
      self.IdentityDocType:str = obj["IdentityDocType"]
      """  Displays the Identity DocumentType  """  
      self.GoodContributor:bool = obj["GoodContributor"]
      """  Indicates if supplier has a Good Contributor status  """  
      self.WithholdingAgent:bool = obj["WithholdingAgent"]
      """  Indicates if supplier is a Withholding Agent  """  
      self.CollectionAgent:bool = obj["CollectionAgent"]
      """  Indicates the status of Collection Agent  """  
      self.NotFound:bool = obj["NotFound"]
      """  Not Found withholding status  """  
      self.NoAddress:bool = obj["NoAddress"]
      """  No Address Provided withholding status  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_PartnerRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.PartnerNum:int = obj["PartnerNum"]
      """  PartnerNum  """  
      self.PartnerType:int = obj["PartnerType"]
      """  PartnerType  """  
      self.SearchID:str = obj["SearchID"]
      """  SearchID  """  
      self.IsActive:bool = obj["IsActive"]
      """  IsActive  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.PartnerID:str = obj["PartnerID"]
      """  PartnerID  """  
      self.DspSearchID:str = obj["DspSearchID"]
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_TaxExemptRow:
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
      self.TaxCode:str = obj["TaxCode"]
      """  Descriptive code assigned by user which uniquely identifies a Sales Tax master record.  Can't be blank. This is used as a foreign key in other files and may be used in displays/reports where space for the full description is limited.  """  
      self.RateCode:str = obj["RateCode"]
      """  Tax Rate Code  """  
      self.EffectiveFrom:str = obj["EffectiveFrom"]
      """  Exemption Effective Start Date  """  
      self.EffectiveTo:str = obj["EffectiveTo"]
      """  Exemption Effective End Date  """  
      self.ExemptType:int = obj["ExemptType"]
      """  Exemption Type  """  
      self.ExemptPercent:int = obj["ExemptPercent"]
      """  Exemption Percent  """  
      self.TextCode:str = obj["TextCode"]
      """  Tax Legal Text Code  """  
      self.ResolutionNum:str = obj["ResolutionNum"]
      """  Tax Resolution Number  """  
      self.ResolutionDate:str = obj["ResolutionDate"]
      """  Tax Resolution Date  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CustNum:int = obj["CustNum"]
      """  A unique Customer identifier.  """  
      self.PartNum:str = obj["PartNum"]
      """  The PartNum field identifies the Part.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A unique Vendor identifier.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.SalesTaxDescription:str = obj["SalesTaxDescription"]
      self.SalesTRCDescription:str = obj["SalesTRCDescription"]
      self.TaxTextDescription:str = obj["TaxTextDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_UpdExtVendorTableset:
   def __init__(self, obj):
      self.Vendor:list[Erp_Tablesets_VendorRow] = obj["Vendor"]
      self.VendorAttch:list[Erp_Tablesets_VendorAttchRow] = obj["VendorAttch"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.TaxExempt:list[Erp_Tablesets_TaxExemptRow] = obj["TaxExempt"]
      self.Partner:list[Erp_Tablesets_PartnerRow] = obj["Partner"]
      self.PEVendWhldHist:list[Erp_Tablesets_PEVendWhldHistRow] = obj["PEVendWhldHist"]
      self.VendRestriction:list[Erp_Tablesets_VendRestrictionRow] = obj["VendRestriction"]
      self.VendBank:list[Erp_Tablesets_VendBankRow] = obj["VendBank"]
      self.VendBankAttch:list[Erp_Tablesets_VendBankAttchRow] = obj["VendBankAttch"]
      self.VendCntMain:list[Erp_Tablesets_VendCntMainRow] = obj["VendCntMain"]
      self.VenMFBill:list[Erp_Tablesets_VenMFBillRow] = obj["VenMFBill"]
      self.VendorPP:list[Erp_Tablesets_VendorPPRow] = obj["VendorPP"]
      self.VenPPMFBill:list[Erp_Tablesets_VenPPMFBillRow] = obj["VenPPMFBill"]
      self.VenPPUPSEmail:list[Erp_Tablesets_VenPPUPSEmailRow] = obj["VenPPUPSEmail"]
      self.VendPPRestriction:list[Erp_Tablesets_VendPPRestrictionRow] = obj["VendPPRestriction"]
      self.VendCnt:list[Erp_Tablesets_VendCntRow] = obj["VendCnt"]
      self.VendCntAttch:list[Erp_Tablesets_VendCntAttchRow] = obj["VendCntAttch"]
      self.VenUPSEmail:list[Erp_Tablesets_VenUPSEmailRow] = obj["VenUPSEmail"]
      self.VendRemitTo:list[Erp_Tablesets_VendRemitToRow] = obj["VendRemitTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VenMFBillRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PayBTFlag:str = obj["PayBTFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayTypeDesc:str = obj["PayTypeDesc"]
      """   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Billing Address  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping biling address line 2  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping biling address line 3.  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping billing city  """  
      self.PayBTState:str = obj["PayBTState"]
      """  Shipping Billing state or province  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  Manifest Bililng postal code.  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  Shipping biling country  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Internal field used to store the country number.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping billing phone number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PayBTCountryNumDescription:str = obj["PayBTCountryNumDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VenPPMFBillRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.PayBTFlag:str = obj["PayBTFlag"]
      """  For Shipping; Bill Shipper, Bill Recipient, Bill Third Party, Bill Consignee  """  
      self.PayTypeDesc:str = obj["PayTypeDesc"]
      """   Describes the billing type.  Valid values and their description are:
1 - Shipper
2 - FedEx  Collect
3 - Third Party
4 - UPS Prepaid
5 - FedEx Recipient
6 - UPS Consignee
7 - UPS Freight Collect
8 - UPS Free On Board
9 - UPS Cost and Freight
10 - UPS Delivery Duty Paid
11 - UPS Shpping Duty and Tax Consignee  """  
      self.PayAccount:str = obj["PayAccount"]
      """  Shipping Pay Flag Account Number. Required when Pag Flag is collect or Third party  """  
      self.PayBTAddress1:str = obj["PayBTAddress1"]
      """  Shipping Billing Address  """  
      self.PayBTAddress2:str = obj["PayBTAddress2"]
      """  Shipping biling address line 2  """  
      self.PayBTAddress3:str = obj["PayBTAddress3"]
      """  Shipping biling address line 3.  """  
      self.PayBTCity:str = obj["PayBTCity"]
      """  Shipping billing city  """  
      self.PayBTZip:str = obj["PayBTZip"]
      """  Pay manifest billing postal code.  """  
      self.PayBTState:str = obj["PayBTState"]
      """  Shipping Billing state or province  """  
      self.PayBTCountry:str = obj["PayBTCountry"]
      """  Shipping biling country  """  
      self.PayBTCountryNum:int = obj["PayBTCountryNum"]
      """  Internal field used to store the country number.  """  
      self.PayBTPhone:str = obj["PayBTPhone"]
      """  Shipping billing phone number  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PayBTCountryNumDescription:str = obj["PayBTCountryNumDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VenPPUPSEmailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantum View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email address to notify for a UPS shipment  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Logical indicating if the EmailAddress is to be updated at shipping.  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  Logical indicating if the ups quantum view fields are to be enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VenUPSEmailRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.UPSQVSeq:int = obj["UPSQVSeq"]
      """  UPS Quantum View Sequence  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Email address to notify for a UPS shipment  """  
      self.ShipmentNotify:bool = obj["ShipmentNotify"]
      """  Logical indicating if the EmailAddress is to be updated at shipping.  """  
      self.FailureNotify:bool = obj["FailureNotify"]
      """  Logical indicating if the Email Address is to be notified of a failed shipment.  """  
      self.DeliveryNotify:bool = obj["DeliveryNotify"]
      """  Logical indicating if the Email Address is to be notified of delivery.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.EnableQuantumView:bool = obj["EnableQuantumView"]
      """  logical indicating if the UPS quantum view fields are to be enabled.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendBankAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.BankID:str = obj["BankID"]
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

class Erp_Tablesets_VendBankRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  Supplier Number  """  
      self.BankID:str = obj["BankID"]
      """  Unique ID of the vendor's bank.  """  
      self.BankName:str = obj["BankName"]
      """  Supplier Bank Name  """  
      self.Address1:str = obj["Address1"]
      """  First Address Line of the Supplier Bank  """  
      self.Address2:str = obj["Address2"]
      """  Second Address Line of the Supplier Bank  """  
      self.Address3:str = obj["Address3"]
      """  Third Address Line of the Supplier Bank  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Supplier Bank  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.PostalCode:str = obj["PostalCode"]
      """  Postal Code or Zip code portion of the address of the Supplier Bank  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.BankAcctNumber:str = obj["BankAcctNumber"]
      """  The Bank account number for the Vendor.  Used with Electronic payments.  """  
      self.NameOnAccount:str = obj["NameOnAccount"]
      """  Name on the Bank Account.  """  
      self.SwiftNum:str = obj["SwiftNum"]
      """  Swift number of the bank.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.BankBranchCode:str = obj["BankBranchCode"]
      """  Bank Branch Code of the Supplier Bank  """  
      self.IBANCode:str = obj["IBANCode"]
      """  IBAN Code of the Supplier Bank  """  
      self.SECreditTransNum:str = obj["SECreditTransNum"]
      """  Sweden localization field, Credit Transfer Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal name  """  
      self.CorrespAccount:str = obj["CorrespAccount"]
      """  Correspondence Account of the Supplier Bank  """  
      self.LocalBIC:str = obj["LocalBIC"]
      """  Local BIC of the Supplier Bank  """  
      self.BankPersonCode:str = obj["BankPersonCode"]
      """  Free Form Bank Person Code. Used in localizations.  """  
      self.VendAccountType:str = obj["VendAccountType"]
      """  Supplier bank Account Type. Used in localizations.  """  
      self.CardCode:str = obj["CardCode"]
      """   Denmark Localization
Card (payment) code  """  
      self.BankGiroAcctNbr:str = obj["BankGiroAcctNbr"]
      """   Denmark Localization
Account Number  """  
      self.BankRefCode:str = obj["BankRefCode"]
      """   Denmark Localization
Bank Reference code  """  
      self.AllowAsAltRemitToBank:bool = obj["AllowAsAltRemitToBank"]
      """  AllowAsAltRemitToBank  """  
      self.DFIIdentification:str = obj["DFIIdentification"]
      """  DFIIdentification  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.CHDTAID:str = obj["CHDTAID"]
      """  CHDTAID  """  
      self.CHISRPartyID:str = obj["CHISRPartyID"]
      """  CHISRPartyID  """  
      self.FeeOwnership:str = obj["FeeOwnership"]
      """  FeeOwnership  """  
      self.POBankAcctNum:str = obj["POBankAcctNum"]
      """  POBankAcctNum  """  
      self.BankCustNum:str = obj["BankCustNum"]
      """  BankCustNum  """  
      self.BankCustNumberStartPos:int = obj["BankCustNumberStartPos"]
      """  BankCustNumberStartPos  """  
      self.BankCustNumberLen:int = obj["BankCustNumberLen"]
      """  BankCustNumberLen  """  
      self.BAddress1:str = obj["BAddress1"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress2:str = obj["BAddress2"]
      """  Specifies the supplier's bank address.  """  
      self.BAddress3:str = obj["BAddress3"]
      """  Specifies the supplier's bank address.  """  
      self.BankCharges:str = obj["BankCharges"]
      """  Bank Charges (Used for Czech Republic CSF)  """  
      self.BankCnstSymbol:str = obj["BankCnstSymbol"]
      """  Bank Constant Symbol (Used for Czech Republic CSF)  """  
      self.BankSpecSymbol:str = obj["BankSpecSymbol"]
      """  Bank Special Symbol (Used for Czech Republic CSF)  """  
      self.BankType:str = obj["BankType"]
      """  Bank type of electronic payment transactions  """  
      self.BCity:str = obj["BCity"]
      """  Specifies the supplier's bank city.  """  
      self.BCountryNum:int = obj["BCountryNum"]
      """  Specifies the supplier's bank country.  """  
      self.BPostalCode:str = obj["BPostalCode"]
      """  Specifies the supplier's postal code.  """  
      self.BState:str = obj["BState"]
      """  Specifies the supplier's bank state/province.  """  
      self.NOChequeCode:str = obj["NOChequeCode"]
      """  Norway CSF: Determines where bank cheque is sent.  """  
      self.NOFeeCostCode:str = obj["NOFeeCostCode"]
      """  Norway CSF: Determines how the bank fee cost will be settled between the company and supplier during the fund transfers between two entities.  """  
      self.ReceiverName:str = obj["ReceiverName"]
      """  Receiver Name.  Used in Japan localizations.  """  
      self.ReceivingBankName:str = obj["ReceivingBankName"]
      """  Receiving Bank Name.  Used in Japan localizations.  """  
      self.ReceivingBankNum:str = obj["ReceivingBankNum"]
      """  Receiving Bank Number.  Used in Japan localizations.  """  
      self.ReceivingBranchName:str = obj["ReceivingBranchName"]
      """  Receiving Branch Name.  Used in Japan localizations.  """  
      self.ReceivingBranchNum:str = obj["ReceivingBranchNum"]
      """  Receiving Branch Number.  Used in Japan localizations.  """  
      self.SEBankFeeCostOwner:str = obj["SEBankFeeCostOwner"]
      """  SEBankFeeCostOwner  """  
      self.PEDetractionsNBA:bool = obj["PEDetractionsNBA"]
      """  PEDetractionsNBA  """  
      self.MXSATCode:str = obj["MXSATCode"]
      """  MX SAT Code  """  
      self.MXSATNameShort:str = obj["MXSATNameShort"]
      """  MX SAT Name Short  """  
      self.MXSATNameFull:str = obj["MXSATNameFull"]
      """  MX SAT Name Full  """  
      self.DKCreditorNum:str = obj["DKCreditorNum"]
      """  DKCreditorNum  """  
      self.PayID:str = obj["PayID"]
      """  A supplier alias used to make and receive payments.  """  
      self.ClearSystemIDCode:str = obj["ClearSystemIDCode"]
      """  ClearSystemIDCode  """  
      self.MemberID:str = obj["MemberID"]
      """  MemberID  """  
      self.BCountry:int = obj["BCountry"]
      self.CHScrPOBankAcctNum:str = obj["CHScrPOBankAcctNum"]
      """  Postal Account Number in format XX-#####V-P (CSF Switzerland)  """  
      self.PrimaryBank:bool = obj["PrimaryBank"]
      self.CHScrISRPartyID:str = obj["CHScrISRPartyID"]
      """  ISR Party Number in format XX-#####V-P (CSF Switzerland)  """  
      self.BitFlag:int = obj["BitFlag"]
      self.BankBranchCodeDescDescription:str = obj["BankBranchCodeDescDescription"]
      self.BankBranchCodeDescBankBranchCode:str = obj["BankBranchCodeDescBankBranchCode"]
      self.BCountryNumDescription:str = obj["BCountryNumDescription"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendCntAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
      self.PurPoint:str = obj["PurPoint"]
      self.ConNum:int = obj["ConNum"]
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

class Erp_Tablesets_VendCntMainRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact number.  Unique identifier for the contact record.  """  
      self.Name:str = obj["Name"]
      """  Contact name.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Contact email address.  """  
      self.WebPassword:str = obj["WebPassword"]
      """  Password for SF/Portal, should not be easily editable from the Manufacturing System.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates if able to access the Supplier Workbench  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Link to the RoleCD table.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contacts Cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contacts Pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contacts Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contacts Alternate number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The Contacts Title  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name if the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is no longer contacted.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Inactive:bool = obj["Inactive"]
      """  This contact does not get used on new LOQs  """  
      self.FirstName:str = obj["FirstName"]
      """  First Name  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Middle Name  """  
      self.LastName:str = obj["LastName"]
      """  Last Name  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.Suffix:str = obj["Suffix"]
      """  Suffix  """  
      self.Initials:str = obj["Initials"]
      """  Initials  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.GlbFlag:bool = obj["GlbFlag"]
      self.PrimaryContact:bool = obj["PrimaryContact"]
      self.VendCntAttrStrng:str = obj["VendCntAttrStrng"]
      self.GlbLink:str = obj["GlbLink"]
      """  GlbVendCnt fields in a linked list to find the linking record  """  
      self.PerConName:str = obj["PerConName"]
      self.BitFlag:int = obj["BitFlag"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendCntRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  This key links the record to the Vendor file.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase point from Vendor.  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact number.  Unique identifier for the contact record.  """  
      self.Name:str = obj["Name"]
      """  Contact name.  """  
      self.Func:str = obj["Func"]
      """  Used to enter a short description that should indicate what the contacts main function is. Ex: Shipping, Buyer, Engineer. This is an optional field.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Specific Fax telephone number for the contact. Optional field.  The user should only enter a Fax number for the contact if it is different than the fax number for the vendor. When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point file if the contacts number is blank.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  Specific Business telephone number for the contact. Optional field.  The user should only enter this when the contact has a phone number different than the Vendor.  When displaying phone numbers of contacts the system will use the phone number found in the Vendor or Purchase Point  file if the contacts number is blank.  """  
      self.EmailAddress:str = obj["EmailAddress"]
      """  Contact email address.  """  
      self.WebPassword:str = obj["WebPassword"]
      """  Password for SF/Portal, should not be easily editable from the Manufacturing System.  """  
      self.WebUser:bool = obj["WebUser"]
      """  Indicates if able to access the Supplier Workbench  """  
      self.RoleCode:str = obj["RoleCode"]
      """  Code that identifies the role of this person. Link to the RoleCD table.  """  
      self.CellPhoneNum:str = obj["CellPhoneNum"]
      """  The contacts Cell phone number.  """  
      self.PagerNum:str = obj["PagerNum"]
      """  The contacts Pager number.  """  
      self.HomeNum:str = obj["HomeNum"]
      """  The contacts Home number.  """  
      self.AltNum:str = obj["AltNum"]
      """  The contacts Alternate number.  """  
      self.ContactTitle:str = obj["ContactTitle"]
      """  The Contacts Title  """  
      self.ReportsTo:str = obj["ReportsTo"]
      """  The name if the person this contact reports to.  """  
      self.Comment:str = obj["Comment"]
      """  Comments are intended to be internal comments about a specific contact.  """  
      self.NoContact:bool = obj["NoContact"]
      """  Indicates that this contact is no longer contacted.  """  
      self.CreateDate:str = obj["CreateDate"]
      """  The date the task was created.  """  
      self.CreateDcdUserID:str = obj["CreateDcdUserID"]
      """  The UserID that created the task  """  
      self.ChangeDate:str = obj["ChangeDate"]
      """  The date the task was last changed.  """  
      self.ChangeDcdUserID:str = obj["ChangeDcdUserID"]
      """  The UserID that last changed the task  """  
      self.Inactive:bool = obj["Inactive"]
      """  This contact does not get used on new LOQs  """  
      self.FirstName:str = obj["FirstName"]
      """  First Name  """  
      self.MiddleName:str = obj["MiddleName"]
      """  Middle Name  """  
      self.LastName:str = obj["LastName"]
      """  Last Name  """  
      self.Prefix:str = obj["Prefix"]
      """  Prefix  """  
      self.Suffix:str = obj["Suffix"]
      """  Suffix  """  
      self.Initials:str = obj["Initials"]
      """  Initials  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.PerConID:int = obj["PerConID"]
      """  Unique identifier for a PerCon record.  """  
      self.SyncEmailToPerCon:bool = obj["SyncEmailToPerCon"]
      """  Default to True. If unchecked then changes to the email fields on PerCon won't affect this record and vice versa.  """  
      self.SyncLinksToPerCon:bool = obj["SyncLinksToPerCon"]
      """  Default to True. If unchecked then changes to the Web link fields on PerCon won't affect this record and vice versa.  """  
      self.SyncNameToPerCon:bool = obj["SyncNameToPerCon"]
      """  Default to True. If unchecked then changes to the Name fields on PerCon won't affect this record and vice versa.  """  
      self.SyncPhoneToPerCon:bool = obj["SyncPhoneToPerCon"]
      """  Default to True. If unchecked then changes to the Phone fields on PerCon won't affect this record and vice versa.  """  
      self.WebSite:str = obj["WebSite"]
      """  Contact's website.  """  
      self.IM:str = obj["IM"]
      """  Contact's IM.  """  
      self.Twitter:str = obj["Twitter"]
      """  Contact's Twitter.  """  
      self.LinkedIn:str = obj["LinkedIn"]
      """  Contact's LinkedIn.  """  
      self.FaceBook:str = obj["FaceBook"]
      """  Contact's FaceBook.  """  
      self.WebLink1:str = obj["WebLink1"]
      """  User defined Link 1.  """  
      self.WebLink2:str = obj["WebLink2"]
      """  User defined Link 2.  """  
      self.WebLink3:str = obj["WebLink3"]
      """  User defined Link 3.  """  
      self.WebLink4:str = obj["WebLink4"]
      """  User defined Link 4.  """  
      self.WebLink5:str = obj["WebLink5"]
      """  User defined Link 5.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.PrimaryContact:bool = obj["PrimaryContact"]
      self.GlbFlag:bool = obj["GlbFlag"]
      self.VendCntAttrStrng:str = obj["VendCntAttrStrng"]
      self.GlbLink:str = obj["GlbLink"]
      """  GlbVendCnt fields in a linked list to find the linking record  """  
      self.PerConName:str = obj["PerConName"]
      """  The name of the person contact.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.RoleCodeRoleDescription:str = obj["RoleCodeRoleDescription"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendPPRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendRemitToRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company  """  
      self.VendorNum:int = obj["VendorNum"]
      """  VendorNum  """  
      self.RemitToSeq:int = obj["RemitToSeq"]
      """  RemitToSeq  """  
      self.RemitToType:str = obj["RemitToType"]
      """  RemitToType  """  
      self.RemitCustNum:int = obj["RemitCustNum"]
      """  RemitCustNum  """  
      self.RemitEmpID:str = obj["RemitEmpID"]
      """  RemitEmpID  """  
      self.RemitVendorNum:int = obj["RemitVendorNum"]
      """  RemitVendorNum  """  
      self.RemitToName:str = obj["RemitToName"]
      """  RemitToName  """  
      self.DefaultRemitTo:bool = obj["DefaultRemitTo"]
      """  DefaultRemitTo  """  
      self.Inactive:bool = obj["Inactive"]
      """  Inactive  """  
      self.OneCheck:bool = obj["OneCheck"]
      """  OneCheck  """  
      self.Comments:str = obj["Comments"]
      """  Comments  """  
      self.RemitToAddress1:str = obj["RemitToAddress1"]
      """  RemitToAddress1  """  
      self.RemitToAddress2:str = obj["RemitToAddress2"]
      """  RemitToAddress2  """  
      self.RemitToAddress3:str = obj["RemitToAddress3"]
      """  RemitToAddress3  """  
      self.RemitToCity:str = obj["RemitToCity"]
      """  RemitToCity  """  
      self.RemitToState:str = obj["RemitToState"]
      """  RemitToState  """  
      self.RemitToZip:str = obj["RemitToZip"]
      """  RemitToZip  """  
      self.RemitToCountry:int = obj["RemitToCountry"]
      """  RemitToCountry  """  
      self.RemitToPhoneNum:str = obj["RemitToPhoneNum"]
      """  RemitToPhoneNum  """  
      self.RemitToFaxNum:str = obj["RemitToFaxNum"]
      """  RemitToFaxNum  """  
      self.RemitToEmail:str = obj["RemitToEmail"]
      """  RemitToEmail  """  
      self.TermsCode:str = obj["TermsCode"]
      """  TermsCode  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  CurrencyCode  """  
      self.PMUID:int = obj["PMUID"]
      """  PMUID  """  
      self.SysRevID:int = obj["SysRevID"]
      """  SysRevID  """  
      self.SysRowID:str = obj["SysRowID"]
      """  SysRowID  """  
      self.RemitToID:str = obj["RemitToID"]
      """  This can either be a CustID, EmpID, or VendID depending on the RemitToType  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendRestrictionRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.RestrictionTypeID:str = obj["RestrictionTypeID"]
      """  Restriction Type identification.  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.RestrictionTypeDescription:str = obj["RestrictionTypeDescription"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendorAttchRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      self.VendorNum:int = obj["VendorNum"]
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

class Erp_Tablesets_VendorListRow:
   def __init__(self, obj):
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the system, for linking other records to the Vendor.  """  
      self.Name:str = obj["Name"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.Address1:str = obj["Address1"]
      """  First address line of the Supplier  """  
      self.Address2:str = obj["Address2"]
      """  Second address line of the Supplier  """  
      self.Address3:str = obj["Address3"]
      """  Third address line of the Supplier  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Supplier  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.CurrDesc:str = obj["CurrDesc"]
      """  Currency Code Description  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.TIN:str = obj["TIN"]
      """  Taxpayer Identification Number  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendorListTableset:
   def __init__(self, obj):
      self.VendorList:list[Erp_Tablesets_VendorListRow] = obj["VendorList"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class Erp_Tablesets_VendorPPRow:
   def __init__(self, obj):
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.Name:str = obj["Name"]
      """  Purchase Point Name...can't be blank.  """  
      self.Address1:str = obj["Address1"]
      """  First address line  """  
      self.Address2:str = obj["Address2"]
      """  Second address line  """  
      self.Address3:str = obj["Address3"]
      """  Third address line  """  
      self.City:str = obj["City"]
      """  City portion of the address  """  
      self.State:str = obj["State"]
      """  State portion of the address  """  
      self.Zip:str = obj["Zip"]
      """  Postal Code or Zip code portion of the address  """  
      self.Country:str = obj["Country"]
      """  Country. Can be blank. Printed as last line of mailing name and address.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  The internal key used to tie back to the Vendor master file.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when a  purchase point is referenced.  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Vendor.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor purchase point.  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique Identifier from an external G/L interface  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor purchase point.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.OverrideCarrier:bool = obj["OverrideCarrier"]
      """  Override Carrier Defaults.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.OverrideService:bool = obj["OverrideService"]
      """  Override Service Options.  If not checked then the vendor values will be used if overriden else the Site values  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Indicates if the shipment is international.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Certificate of Origin flag  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Commercial Invoice flag.  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Ship Export Declaration flag  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Letter of Instruction flag  """  
      self.FFID:str = obj["FFID"]
      """  Freight Forwarder ID  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Freight Forwarder Company Name  """  
      self.FFContact:str = obj["FFContact"]
      """  Freight Forwarder contact person  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  First address line of the Freight Forwarder  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Second address line of the Freight Forwarder  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Third address line of the Freight Forwarder  """  
      self.FFCity:str = obj["FFCity"]
      """  Freight Forwarder city portion of address.  """  
      self.FFState:str = obj["FFState"]
      """  Freight Forwarder state portion of address.  """  
      self.FFZip:str = obj["FFZip"]
      """  Freight Forwarder Zip code portion of the address  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Freight Forwarder Country portion of the address  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Freight Forwarder Phone Number  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country Number  """  
      self.LegalName:str = obj["LegalName"]
      """  Legal Name  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.INExciseRegNumber:str = obj["INExciseRegNumber"]
      """  INExciseRegNumber  """  
      self.INExciseDivision:str = obj["INExciseDivision"]
      """  INExciseDivision  """  
      self.INExciseRange:str = obj["INExciseRange"]
      """  INExciseRange  """  
      self.INCommissionarate:str = obj["INCommissionarate"]
      """  INCommissionarate  """  
      self.INVATNumber:str = obj["INVATNumber"]
      """  INVATNumber  """  
      self.INServiceTaxRegNum:str = obj["INServiceTaxRegNum"]
      """  INServiceTaxRegNum  """  
      self.INTaxRegionCode:str = obj["INTaxRegionCode"]
      """  INTaxRegionCode  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  Municipio Code  """  
      self.GroupCode:str = obj["GroupCode"]
      self.IntegrationFlag:bool = obj["IntegrationFlag"]
      self.PhoneNum:str = obj["PhoneNum"]
      self.PrimaryPP:bool = obj["PrimaryPP"]
      self.VendAttrString:str = obj["VendAttrString"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if ShipTo is a global record  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany, GlbVendorNum and GlbPurPoint that is linking to this purchase point  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  Sales Tax ID  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  Service Tax ID  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.MXISTMO:str = obj["MXISTMO"]
      """  Area of ISTMO de Tehuantepec (Polos de Desarrollo). Value is from MXLocISTMO User Code.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.INTaxRegionCodeDescription:str = obj["INTaxRegionCodeDescription"]
      self.TACodeTaxAuthorityDescription:str = obj["TACodeTaxAuthorityDescription"]
      self.VendorNumState:str = obj["VendorNumState"]
      self.VendorNumAddress3:str = obj["VendorNumAddress3"]
      self.VendorNumAddress2:str = obj["VendorNumAddress2"]
      self.VendorNumDefaultFOB:str = obj["VendorNumDefaultFOB"]
      self.VendorNumCurrencyCode:str = obj["VendorNumCurrencyCode"]
      self.VendorNumAddress1:str = obj["VendorNumAddress1"]
      self.VendorNumCity:str = obj["VendorNumCity"]
      self.VendorNumVendorID:str = obj["VendorNumVendorID"]
      self.VendorNumZIP:str = obj["VendorNumZIP"]
      self.VendorNumCountry:str = obj["VendorNumCountry"]
      self.VendorNumTermsCode:str = obj["VendorNumTermsCode"]
      self.VendorNumName:str = obj["VendorNumName"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      pass

class Erp_Tablesets_VendorRow:
   def __init__(self, obj):
      self.Inactive:bool = obj["Inactive"]
      """  Indicates if vendor is inactive.  Inactive vendors are suppressed from data entry browses/selection lists and reports.  No new POs may be entered for the vendor, but the vendor may still be appear on existing POs.  """  
      self.Company:str = obj["Company"]
      """  Company Identifier.  """  
      self.VendorID:str = obj["VendorID"]
      """  A descriptive code assigned by the user to uniquely identify the vendor record.  This code must be unique within the file.  This ID may be used on displays/reports where space for full name is not available or may be inappropriate. This master key is a little different in that the user can change it.  This change is allowed because the system is not using the VendID as a foreign key in any other file. Instead it uses an internal value, VendNum, which cannot be changed, and is assigned by the system, for linking other records to the Vendor.  """  
      self.Name:str = obj["Name"]
      """  Vendor's name.  This field has a format length of 50. Normally the maintenance will be done in a left/right scrollable field of 30. Printing may not always print all 50. This also applies to the address lines.  """  
      self.VendorNum:int = obj["VendorNum"]
      """  A  unique integer assigned by the system to new vendors by the  maintenance program. This field is used as the foreign key to identify the vendor in other files such as CheckHed, or POHeader. The end user should never need to know about the value of this field.  """  
      self.Address1:str = obj["Address1"]
      """  First address line of the Supplier  """  
      self.Address2:str = obj["Address2"]
      """  Second address line of the Supplier  """  
      self.Address3:str = obj["Address3"]
      """  Third address line of the Supplier  """  
      self.City:str = obj["City"]
      """  City portion of the address of the Supplier  """  
      self.State:str = obj["State"]
      """  Can be blank.  """  
      self.ZIP:str = obj["ZIP"]
      """  Postal Code or Zip code portion of the address of the Supplier  """  
      self.Country:str = obj["Country"]
      """  Country Name. Printed as last line of mailing address. Can be blank.  """  
      self.TaxPayerID:str = obj["TaxPayerID"]
      """  The Tax Payer ID. Used in 1099 processing.  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Contains the key of the Purchase Point (VendorPP) record that should be used as a default for the vendor. Purchase points are used in Purchase Orders like Customer Shipto are used in Sales Orders. A blank value signifies that the default should be the vendor itself. This field is updated via a toggle box in purchase point maintenance. When the user checks this box the key of the Purchase Point record (PurPoint) is placed into this field. This method insures that only one Purchase point can exist as the default. Also if the toggle box is cleared then this field should be updated to blanks.  """  
      self.TermsCode:str = obj["TermsCode"]
      """  Establishes the default Purchasing terms for this vendor. This can be blank or must be valid in the Terms file. It supplies Purchase Order and A/P Invoice entry with defaults.  """  
      self.GroupCode:str = obj["GroupCode"]
      """  Vendors Group Code. Can be blank or must be valid in the VendGrup master file.  """  
      self.Print1099:bool = obj["Print1099"]
      """  Only vendors where Print 1099 = Yes will be selected in the 1099 processing.  """  
      self.OneCheck:bool = obj["OneCheck"]
      """  Indicates that for this vendor all invoices must be paid on separate checks.  """  
      self.PrintLabels:bool = obj["PrintLabels"]
      """  Only vendors that are PrintLabel = Yes will be selected for printing of mailing labels.  """  
      self.FaxNum:str = obj["FaxNum"]
      """  Fax telephone number for the vendor. Optional field. This field is used as the general Fax # for the vendor.  It will be displayed as PO entry/Inquiry when no specific contact is given for the purchase order or the contact record has a blank Fax #.  """  
      self.PhoneNum:str = obj["PhoneNum"]
      """  The general Business Phone Number for the vendor. Displayed in PO  entry and inquires when no contact is given or when contact has a blank phone number.  """  
      self.Comment:str = obj["Comment"]
      """   Comments are intended to be internal comments about a specific vendor. These do get pulled into other programs. They are mainly intended as an online storage facility.
To be view-as EDITOR widget.  """  
      self.PayHold:bool = obj["PayHold"]
      """  Indicates if payments to vendor should be held. If "yes" then vendor can't be selected in check processing. Also individual invoices can be put on hold.  """  
      self.PrimPCon:int = obj["PrimPCon"]
      """  Contains the key of the Primary Purchasing contact for the customer. This field is not directly maintainable. Instead it is set during contact maintenance by having the user mark a check box indicating primary Purchaser.  This is the contact that is used as a default in Purchase Order Entry when no purchase point is referenced  """  
      self.AccountRef:str = obj["AccountRef"]
      """  Identifies your account with the specific vendor. This is an optional field which is printed on any checks the system generates to this vendor.  """  
      self.DefaultFOB:str = obj["DefaultFOB"]
      """  Default FOB policy for Purchase Orders to this vendor.  Used as a default to POHeader.FOB.  """  
      self.RcvInspectionReq:bool = obj["RcvInspectionReq"]
      """  Indicates if  Inspection is required for items received from this vendor.  Inspection will also be enforced if the related PartClass, Podetail, JobMtl or JobOper have their "RcvInspectionReq" fields set to Yes.  """  
      self.CurrencyCode:str = obj["CurrencyCode"]
      """  A unique code that identifies the currency.  """  
      self.TaxRegionCode:str = obj["TaxRegionCode"]
      """  Tax Liability of the Supplier  """  
      self.CountryNum:int = obj["CountryNum"]
      """  Country part of address. This field is in sync with the Country field. It must be a valid entry in the Country table.  """  
      self.LangNameID:str = obj["LangNameID"]
      """  Indicates the language to be used.  This controls which language will be selected when extracting part descriptions from PartLangDesc table.  """  
      self.BorderCrossing:str = obj["BorderCrossing"]
      """  Area/city code from where goods cross the border. This field is intended for Intrastat reporting. The field can be blank to indicate the value from the Country table.  This field is only visible if ISSyst.EnableHarbour is set.  """  
      self.FormatStr:str = obj["FormatStr"]
      """  Optional Custom address format.  Controls the address format used on crystal forms.  """  
      self.ElecPayment:bool = obj["ElecPayment"]
      """  Payments to this vendors are made via electronic transfer.  """  
      self.PrimaryBankID:str = obj["PrimaryBankID"]
      """  ID of the vendor's primary bank.  Relates to the VendBank record, NOT the BankAcct record.  """  
      self.Approved:bool = obj["Approved"]
      """   Indicates if the Vendor is approved for Purchasing.
Purchases can only be made from vendors that are approved.  """  
      self.ICVend:bool = obj["ICVend"]
      """  This is an inter-company vendor.  """  
      self.EMailAddress:str = obj["EMailAddress"]
      """  Email address of the vendor.  """  
      self.WebVendor:bool = obj["WebVendor"]
      """  This vendor is web enabled  """  
      self.VendURL:str = obj["VendURL"]
      """  Vendor URL.  """  
      self.EarlyBuffer:int = obj["EarlyBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.LateBuffer:int = obj["LateBuffer"]
      """  Used to calculate on-time delivery performance rating  """  
      self.OnTimeRating:str = obj["OnTimeRating"]
      """  Freeform field for rating On-time delivery performance.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.QualityRating:str = obj["QualityRating"]
      """  Freeform field for rating QA performance.  This field is used as a criteria in selecting vendors in RFQ responses.  """  
      self.PriceRating:str = obj["PriceRating"]
      """  Freeform field for rating Price Accuracy.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ServiceRating:str = obj["ServiceRating"]
      """  Freeform field for rating this vendors service.  This field is used as a criteria in selecting vendors in RFQ responses  """  
      self.ExternalId:str = obj["ExternalId"]
      """  Unique identifier from an external G/L interface  """  
      self.VendPILimit:int = obj["VendPILimit"]
      """  An optional field that allows user to enter a monetary value to be used as a Credit limit for payment instruments such as post dated checks or bank drafts.  Credit limit of zero is considered as having unlimited credit.  """  
      self.GlobalVendor:bool = obj["GlobalVendor"]
      """  Marks the vendor as a global vendor, available to be sent out to other companies  """  
      self.ICTrader:bool = obj["ICTrader"]
      """  Indicates if this vendor participates in the Inter-Company Trading.  """  
      self.TaxAuthorityCode:str = obj["TaxAuthorityCode"]
      """  Establishes the tax authority for this vendor.  This field can be blank, but if entered, it must be valid in the TaxAuthorityCd file.  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  Disable this record from receiving global updates  """  
      self.MinOrderValue:int = obj["MinOrderValue"]
      """  MinOrderValue  """  
      self.CalendarID:str = obj["CalendarID"]
      """  Identifies the production calendar for this Vendor.   If this equals "", then the ProdCal record is the Company Level production calendar.  """  
      self.EDICode:str = obj["EDICode"]
      """  The Trading Partner ID that is used for incoming and outgoing EDI transactions.  """  
      self.ConsolidatedPurchasing:bool = obj["ConsolidatedPurchasing"]
      """  Should this Supplier be included in Consolidated Purchasing?  """  
      self.LocalPurchasing:bool = obj["LocalPurchasing"]
      """  If the Part Class being purchased is included in Consolidated Purchasing, should purchasing it from this Supplier override that so it will be purchased in this company?  """  
      self.ResDelivery:bool = obj["ResDelivery"]
      """  Is this a residential delivery  """  
      self.SatDelivery:bool = obj["SatDelivery"]
      """  Is a Saturday delivery acceptable  """  
      self.SatPickup:bool = obj["SatPickup"]
      """  Is a Saturday pickup available  """  
      self.Hazmat:bool = obj["Hazmat"]
      """  Hazmat or Dangerous Goods delivery  """  
      self.DocOnly:bool = obj["DocOnly"]
      """  Documents Only delivery  """  
      self.RefNotes:str = obj["RefNotes"]
      """  Reference Notes for the delivery  """  
      self.ApplyChrg:bool = obj["ApplyChrg"]
      """  Apply Handling Charge to shipment  """  
      self.ChrgAmount:int = obj["ChrgAmount"]
      """  Handling Charge Amount  """  
      self.COD:bool = obj["COD"]
      """  Prefer COD delivery  """  
      self.CODFreight:bool = obj["CODFreight"]
      """  Add Freight COD Amount owed  """  
      self.CODCheck:bool = obj["CODCheck"]
      """  Cashier's Check or Money order is required on COD Delivery  """  
      self.CODAmount:int = obj["CODAmount"]
      """  Amount due on Cashier's check or money order  """  
      self.GroundType:str = obj["GroundType"]
      """  Valid Values are blank, "Any" (Any Payment), "GF" (Guaranteed Funds), or "Cash" (Currency)  """  
      self.NotifyFlag:bool = obj["NotifyFlag"]
      """  Indicates whether to send an email notification of delivery  """  
      self.NotifyEMail:str = obj["NotifyEMail"]
      """  The list of email address to notify about a delivery  """  
      self.DeclaredIns:bool = obj["DeclaredIns"]
      """  Flag to indicate that an insurance value was declared on delivery  """  
      self.DeclaredAmt:int = obj["DeclaredAmt"]
      """  Declared Insurance Amount  """  
      self.ServSignature:bool = obj["ServSignature"]
      """  Service delivery requires signature  """  
      self.ServAlert:bool = obj["ServAlert"]
      """  Service Priority Alert flag  """  
      self.ServHomeDel:bool = obj["ServHomeDel"]
      """  Service Home Delivery allowed  """  
      self.DeliveryType:str = obj["DeliveryType"]
      """  Service Home Delivery Type Code  """  
      self.ServDeliveryDate:str = obj["ServDeliveryDate"]
      """  Service Home Delivery date  """  
      self.ServPhone:str = obj["ServPhone"]
      """  Home delivery phone number  """  
      self.ServInstruct:str = obj["ServInstruct"]
      """  Service Delivery Instructions  """  
      self.ServRelease:bool = obj["ServRelease"]
      """  Service Signature release is on file  """  
      self.ServAuthNum:str = obj["ServAuthNum"]
      """  Service Signature Release authorization number  """  
      self.ServRef1:str = obj["ServRef1"]
      """  Service Reference 1  """  
      self.ServRef2:str = obj["ServRef2"]
      """  Service Reference 2  """  
      self.ServRef3:str = obj["ServRef3"]
      """  Service Reference 3  """  
      self.ServRef4:str = obj["ServRef4"]
      """  Service Reference 4  """  
      self.ServRef5:str = obj["ServRef5"]
      """  Service Reference 5  """  
      self.CPay:bool = obj["CPay"]
      """  Flag to indicate if the Vendor participates in the Centralized Payment process.  """  
      self.IndividualPackIDs:bool = obj["IndividualPackIDs"]
      """  Indicates whether or not all freight charges sent or received are for individual pack DIs or the master pack.  """  
      self.IntrntlShip:bool = obj["IntrntlShip"]
      """  Indicates if the shipment is international.  """  
      self.CertOfOrigin:bool = obj["CertOfOrigin"]
      """  Certificate of Origin flag  """  
      self.CommercialInvoice:bool = obj["CommercialInvoice"]
      """  Commercial Invoice flag.  """  
      self.ShipExprtDeclartn:bool = obj["ShipExprtDeclartn"]
      """  Ship Export Declaration flag  """  
      self.LetterOfInstr:bool = obj["LetterOfInstr"]
      """  Letter of Instruction flag  """  
      self.FFID:str = obj["FFID"]
      """  Freight Forwarder ID  """  
      self.FFCompName:str = obj["FFCompName"]
      """  Freight Forwarder Company Name  """  
      self.FFContact:str = obj["FFContact"]
      """  Freight Forwarder contact person  """  
      self.FFAddress1:str = obj["FFAddress1"]
      """  First address line of the Freight Forwarder  """  
      self.FFAddress2:str = obj["FFAddress2"]
      """  Second address line of the Freight Forwarder  """  
      self.FFAddress3:str = obj["FFAddress3"]
      """  Third address line of the Freight Forwarder  """  
      self.FFCity:str = obj["FFCity"]
      """  Freight Forwarder city portion of address.  """  
      self.FFState:str = obj["FFState"]
      """  Freight Forwarder state portion of address.  """  
      self.FFZip:str = obj["FFZip"]
      """  Freight Forwarder Zip code portion of the address  """  
      self.FFCountry:str = obj["FFCountry"]
      """  Freight Forwarder Country portion of the address  """  
      self.NonStdPkg:bool = obj["NonStdPkg"]
      """  Non Standard Packaging  """  
      self.DeliveryConf:int = obj["DeliveryConf"]
      """   Determines the level of delivery confirmation.
1 - No Signature Required
2 - Adult Signature Required
3 - Confirmation Required
4 - Verbal Confirmation Required  """  
      self.AddlHdlgFlag:bool = obj["AddlHdlgFlag"]
      """  Additional Handling flag  """  
      self.UPSQuantumView:bool = obj["UPSQuantumView"]
      """  UPS Quantum View  """  
      self.UPSQVShipFromName:str = obj["UPSQVShipFromName"]
      """  UPS Quantum View Ship from Name  """  
      self.UPSQVMemo:str = obj["UPSQVMemo"]
      """  UPS Quantum View Memo  """  
      self.FFPhoneNum:str = obj["FFPhoneNum"]
      """  Freight Forwarder Phone Number  """  
      self.FFCountryNum:int = obj["FFCountryNum"]
      """  Freight Forwarder Country Number  """  
      self.RevChargeMethod:str = obj["RevChargeMethod"]
      """   Indicates what VAT Reverse Charge method needs to be applied for this Supplier.  The possible values are:
   "RCT"  -  "Reverse Charge with Threshold";
   "RCN"  -  "Reverse Charge with No Threshold"
Leave this field blank if no Reverse Charge should be applied in the AP invoice line for this Supplier.  """  
      self.ManagedCust:bool = obj["ManagedCust"]
      """  Flag indicating whether this vendor is associated with a 3PL customer.  """  
      self.ManagedCustID:str = obj["ManagedCustID"]
      """  CustID of the associated managed customer.  Only populated if ManagedCust flag = true.  """  
      self.ManagedCustNum:int = obj["ManagedCustNum"]
      """  CustNum associated with CustID of managed customer.  Only populated if ManagedCust flag = true.  """  
      self.PMUID:int = obj["PMUID"]
      """  Unique identifier of the payment method  """  
      self.HasBank:bool = obj["HasBank"]
      """  If yes, indicates that Vendor has at least one assoicated VendBank record.  """  
      self.PmtAcctRef:str = obj["PmtAcctRef"]
      """  The Payment Banking Reference assigned by the supplier  """  
      self.LegalName:str = obj["LegalName"]
      """  Full Legal Name  """  
      self.TaxRegReason:str = obj["TaxRegReason"]
      """  Tax Payer Registration Reason Code  """  
      self.OrgRegCode:str = obj["OrgRegCode"]
      """  Organization Registration Code  """  
      self.AdvTaxInv:bool = obj["AdvTaxInv"]
      """   Indicates Advanced Tax invoice is expected from supplier
after prepayment is done. If this field is set to yes, prepayment
invoice is not crated automatically.  """  
      self.AllowAsAltRemitTo:bool = obj["AllowAsAltRemitTo"]
      """  AllowAsAltRemitTo  """  
      self.SysRevID:int = obj["SysRevID"]
      """  Revision identifier for this row. It is incremented upon each write.  """  
      self.SysRowID:str = obj["SysRowID"]
      """  Unique identifier for this row. The value is a GUID.  """  
      self.THBranchID:str = obj["THBranchID"]
      """  THBranchID  """  
      self.ParamCode:str = obj["ParamCode"]
      """  ParamCode  """  
      self.AGAFIPResponsibilityCode:str = obj["AGAFIPResponsibilityCode"]
      """  AGAFIPResponsibilityCode  """  
      self.AGGrossIncomeTaxID:str = obj["AGGrossIncomeTaxID"]
      """  AGGrossIncomeTaxID  """  
      self.AGIDDocumentTypeCode:str = obj["AGIDDocumentTypeCode"]
      """  AGIDDocumentTypeCode  """  
      self.AGProvinceCode:str = obj["AGProvinceCode"]
      """  AGProvinceCode  """  
      self.AGUseGoodDefaultMark:bool = obj["AGUseGoodDefaultMark"]
      """  AGUseGoodDefaultMark  """  
      self.AGApartment:str = obj["AGApartment"]
      """  AGApartment  """  
      self.AGExtraStreetNumber:str = obj["AGExtraStreetNumber"]
      """  AGExtraStreetNumber  """  
      self.AGFloor:str = obj["AGFloor"]
      """  AGFloor  """  
      self.AGLocationCode:str = obj["AGLocationCode"]
      """  AGLocationCode  """  
      self.AGNeighborhood:str = obj["AGNeighborhood"]
      """  AGNeighborhood  """  
      self.AGStreet:str = obj["AGStreet"]
      """  AGStreet  """  
      self.AGStreetNumber:str = obj["AGStreetNumber"]
      """  AGStreetNumber  """  
      self.COOneTimeID:str = obj["COOneTimeID"]
      """  Colombia Loc Field. OneTimeCustVend new table ID  """  
      self.NoBankingReference:bool = obj["NoBankingReference"]
      """  No Banking Reference  """  
      self.PEGoodsContributor:bool = obj["PEGoodsContributor"]
      """  Peru Goods Contributor withholding status.  """  
      self.PEWithholdAgent:bool = obj["PEWithholdAgent"]
      """  Indicates the status of Peru Withholding Agent  """  
      self.PECollectionAgent:bool = obj["PECollectionAgent"]
      """  Indicates the status of Peru Collection Agent  """  
      self.PENotFound:bool = obj["PENotFound"]
      """  Peru Not Found withholding status.  """  
      self.PENoAddress:bool = obj["PENoAddress"]
      """  Peru No Address Provided withholding status.  """  
      self.PEIdentityDocType:str = obj["PEIdentityDocType"]
      """  Displays the Peru Identity Document Type.  """  
      self.COIsOneTimeVend:bool = obj["COIsOneTimeVend"]
      """  Colombia Loc Field.  """  
      self.PEDocumentID:str = obj["PEDocumentID"]
      """  Peru Document ID.  """  
      self.MaxLateDaysPORel:int = obj["MaxLateDaysPORel"]
      """  Defines the Number of Days from the PO release date the schedule engine considers a late PO Release or discard it. If the PO release date plus the supplier due date horizon is before today then the PO Release is discarded. If the PO release date plus the supplier due date horizon is today or later then the PO Release is considered late.  """  
      self.Code1099ID:str = obj["Code1099ID"]
      """  1099 Code  """  
      self.TIN:str = obj["TIN"]
      """  Taxpayer Identification Number  """  
      self.TINType:str = obj["TINType"]
      """  TIN Type. Values are 1 for EIN, 2 for SSNs, ITINs, and ATINs and 0 if type of TIN is not terminable.  """  
      self.SecondTINNotice:bool = obj["SecondTINNotice"]
      """  Second TIN Notice  """  
      self.NameControl:str = obj["NameControl"]
      """  Name Control. Optional and used for electronic export.  """  
      self.ShipViaCode:str = obj["ShipViaCode"]
      """  Specifies the method of shipment. The Ship Via associated with this supplier appears by default, but you can select a different option from the list.  """  
      self.NonUS:bool = obj["NonUS"]
      """  Non US Supplier  """  
      self.FormTypeID:str = obj["FormTypeID"]
      """  Form Type ID for the 1099 Code  """  
      self.INSupplierType:str = obj["INSupplierType"]
      """  INSupplierType  """  
      self.INCSTNumber:str = obj["INCSTNumber"]
      """  INCSTNumber  """  
      self.INPANNumber:str = obj["INPANNumber"]
      """  INPANNumber  """  
      self.DEOrgType:str = obj["DEOrgType"]
      """  DEOrgType  """  
      self.PaymentReporting:bool = obj["PaymentReporting"]
      """  PaymentReporting  """  
      self.ExternalPurchasing:bool = obj["ExternalPurchasing"]
      """  This field indicates that this record should be sent over to an external system whenever it is changed/created/deleted, etc.  """  
      self.MXRetentionCode:str = obj["MXRetentionCode"]
      """  MXRetentionCode  """  
      self.Reporting1099Name:str = obj["Reporting1099Name"]
      """  Recipient's name for US 1099 reporting  """  
      self.Reporting1099Name2:str = obj["Reporting1099Name2"]
      """  Reporting1099Name2  """  
      self.FATCA:bool = obj["FATCA"]
      """  FATCA  """  
      self.AccountNum:str = obj["AccountNum"]
      """  AccountNum  """  
      self.TWGUIRegNum:str = obj["TWGUIRegNum"]
      """  TW GUI Code  """  
      self.MXTARCode:str = obj["MXTARCode"]
      """  MXTARCode  """  
      self.PEAddressID:str = obj["PEAddressID"]
      """  PEAddressID  """  
      self.PERetentionRegime:str = obj["PERetentionRegime"]
      """  PERetentionRegime  """  
      self.TaxEntityType:str = obj["TaxEntityType"]
      """  TaxEntityType  """  
      self.INGSTComplianceRate:int = obj["INGSTComplianceRate"]
      """  GST Compliance Rate for India  """  
      self.INTaxRegistrationID:str = obj["INTaxRegistrationID"]
      """  INTaxRegistrationID  """  
      self.TINValidationStatus:int = obj["TINValidationStatus"]
      """  Validation Status of Taxpayer Identification Number  """  
      self.ImporterOfRecord:bool = obj["ImporterOfRecord"]
      """  Indicates whether this supplier is importer of records or not. Used for Avalara Tax Connect calculation.  """  
      self.PLAutomaticAPInvoiceNum:bool = obj["PLAutomaticAPInvoiceNum"]
      """  PLAutomaticAPInvoiceNum  """  
      self.SEC:str = obj["SEC"]
      """  Standard Entry Class Code  """  
      self.MXDIOTTranType:str = obj["MXDIOTTranType"]
      """  CSF Mexico DIOT Transaction Type  """  
      self.US1099KMerchCatCode:str = obj["US1099KMerchCatCode"]
      """  Form 1099-K Merchant Category Code  """  
      self.MXTaxpayerType:str = obj["MXTaxpayerType"]
      """  CSF Mexico Taxpayer Type  """  
      self.MXLegalRepRFC:str = obj["MXLegalRepRFC"]
      """  CSF Mexico Legal Representative RFC  """  
      self.MXLegalRepCURP:str = obj["MXLegalRepCURP"]
      """  CSF Mexico Legal Representative CURP  """  
      self.MXLegalRepName:str = obj["MXLegalRepName"]
      """  CSF Mexico Legal Representative Name  """  
      self.MXLegalRepTaxpayerType:str = obj["MXLegalRepTaxpayerType"]
      """  CSF Mexico Legal Representative Taxpayer Type  """  
      self.US1099State:str = obj["US1099State"]
      """  US 1099 State  """  
      self.TaxValidationStatus:int = obj["TaxValidationStatus"]
      """  Tax ID Validation Status: Not Validated – 0, Valid – 1, Invalid – 2.  """  
      self.TaxValidationDate:str = obj["TaxValidationDate"]
      """  Tax Validation Date  """  
      self.HMRCTaxValidationLog:str = obj["HMRCTaxValidationLog"]
      """  HMRCTaxValidationLog  """  
      self.ExternalSchemeID:str = obj["ExternalSchemeID"]
      """  Supplier Scheme ID  """  
      self.MXMunicipio:str = obj["MXMunicipio"]
      """  Municipio Code  """  
      self.EInvoice:bool = obj["EInvoice"]
      """  EInvoice  """  
      self.EDISupplier:bool = obj["EDISupplier"]
      """  Flag used to mark a Supplier as EDI.  """  
      self.FSMSendTo:bool = obj["FSMSendTo"]
      """  FSMSendTo  """  
      self.BusinessCatList:str = obj["BusinessCatList"]
      """  Delimited list of Business Categories  """  
      self.COASegReferences:str = obj["COASegReferences"]
      """  List of fields which are referenced by COA segments.  """  
      self.CountryDescription:str = obj["CountryDescription"]
      self.CurrDesc:str = obj["CurrDesc"]
      """  Currency Description.  """  
      self.DocumentMaskID:str = obj["DocumentMaskID"]
      self.EnableGlobalLock:bool = obj["EnableGlobalLock"]
      self.EnableGlobalVendor:bool = obj["EnableGlobalVendor"]
      self.EnableMultiCompany:bool = obj["EnableMultiCompany"]
      self.EnableRevCharge:bool = obj["EnableRevCharge"]
      """  Indicates if Reverse Charge Method should be enabled.  """  
      self.FOBDescription:str = obj["FOBDescription"]
      self.GlbFlag:bool = obj["GlbFlag"]
      """  Indicates if the Vendor is a global vendor (either master or child)  """  
      self.GlbLink:str = obj["GlbLink"]
      """  Delimited list of GlbCompany and GlbVendorNum that is linking to this vendor  """  
      self.Integrationflag:bool = obj["Integrationflag"]
      self.NettingCustID:str = obj["NettingCustID"]
      """  A user defined external Netting Customer ID.  This must be existing Customer ID within the file  """  
      self.NettingCustNum:int = obj["NettingCustNum"]
      """  A user defined external Netting Customer Number.  This must be existing Customer Number within the file  """  
      self.RevChargeMethodDesc:str = obj["RevChargeMethodDesc"]
      """  Reverse Charge Method description  """  
      self.SalesTaxID:str = obj["SalesTaxID"]
      """  Sales Tax ID  """  
      self.SearchIDs:str = obj["SearchIDs"]
      """  Automated Bank reconciliation.  """  
      self.ServiceTaxID:str = obj["ServiceTaxID"]
      """  Service Tax ID  """  
      self.ShipViaDescription:str = obj["ShipViaDescription"]
      self.VendAttrString:str = obj["VendAttrString"]
      """  Delimited string of vendor attributes  """  
      self.LangNameIDDescription:str = obj["LangNameIDDescription"]
      self.MXISTMO:str = obj["MXISTMO"]
      """  Area of ISTMO de Tehuantepec (Polos de Desarrollo). Value is from MXLocISTMO User Code.  """  
      self.BitFlag:int = obj["BitFlag"]
      self.AGAFIPResponsibilityDescription:str = obj["AGAFIPResponsibilityDescription"]
      self.AGIDDocTypeDescription:str = obj["AGIDDocTypeDescription"]
      self.AGLocationDescription:str = obj["AGLocationDescription"]
      self.AGProvinceCodeDescription:str = obj["AGProvinceCodeDescription"]
      self.CalendarIDDescription:str = obj["CalendarIDDescription"]
      self.Code1099Description:str = obj["Code1099Description"]
      self.CountryNumEUMember:bool = obj["CountryNumEUMember"]
      self.CountryNumISOCode:str = obj["CountryNumISOCode"]
      self.CountryNumDescription:str = obj["CountryNumDescription"]
      self.CurrencyCodeCurrSymbol:str = obj["CurrencyCodeCurrSymbol"]
      self.CurrencyCodeDocumentDesc:str = obj["CurrencyCodeDocumentDesc"]
      self.CurrencyCodeCurrencyID:str = obj["CurrencyCodeCurrencyID"]
      self.CurrencyCodeCurrName:str = obj["CurrencyCodeCurrName"]
      self.CurrencyCodeCurrDesc:str = obj["CurrencyCodeCurrDesc"]
      self.DeliveryTypeDescription:str = obj["DeliveryTypeDescription"]
      self.FormTypeDescription:str = obj["FormTypeDescription"]
      self.GroupCodeGroupDesc:str = obj["GroupCodeGroupDesc"]
      self.PayMethodType:int = obj["PayMethodType"]
      self.PayMethodName:str = obj["PayMethodName"]
      self.PayMethodSummarizePerCustomer:bool = obj["PayMethodSummarizePerCustomer"]
      self.PurPointAddress3:str = obj["PurPointAddress3"]
      self.PurPointAddress1:str = obj["PurPointAddress1"]
      self.PurPointPrimPCon:int = obj["PurPointPrimPCon"]
      self.PurPointName:str = obj["PurPointName"]
      self.PurPointZip:str = obj["PurPointZip"]
      self.PurPointCountry:str = obj["PurPointCountry"]
      self.PurPointCity:str = obj["PurPointCity"]
      self.PurPointState:str = obj["PurPointState"]
      self.PurPointAddress2:str = obj["PurPointAddress2"]
      self.TaxAuthCdTaxAuthorityDescription:str = obj["TaxAuthCdTaxAuthorityDescription"]
      self.TaxRegionCodeDescription:str = obj["TaxRegionCodeDescription"]
      self.TermsCodeDescription:str = obj["TermsCodeDescription"]
      self.RowMod:str = obj["RowMod"]
      """  RowMod  """  
      self.UD_SysRevID:str = obj["UD_SysRevID"]
      self.Week1Pymt_c:int = obj["Week1Pymt_c"]
      self.Week2Pymt_c:int = obj["Week2Pymt_c"]
      pass

class Erp_Tablesets_VendorTableset:
   def __init__(self, obj):
      self.Vendor:list[Erp_Tablesets_VendorRow] = obj["Vendor"]
      self.VendorAttch:list[Erp_Tablesets_VendorAttchRow] = obj["VendorAttch"]
      self.EntityGLC:list[Erp_Tablesets_EntityGLCRow] = obj["EntityGLC"]
      self.TaxExempt:list[Erp_Tablesets_TaxExemptRow] = obj["TaxExempt"]
      self.Partner:list[Erp_Tablesets_PartnerRow] = obj["Partner"]
      self.PEVendWhldHist:list[Erp_Tablesets_PEVendWhldHistRow] = obj["PEVendWhldHist"]
      self.VendRestriction:list[Erp_Tablesets_VendRestrictionRow] = obj["VendRestriction"]
      self.VendBank:list[Erp_Tablesets_VendBankRow] = obj["VendBank"]
      self.VendBankAttch:list[Erp_Tablesets_VendBankAttchRow] = obj["VendBankAttch"]
      self.VendCntMain:list[Erp_Tablesets_VendCntMainRow] = obj["VendCntMain"]
      self.VenMFBill:list[Erp_Tablesets_VenMFBillRow] = obj["VenMFBill"]
      self.VendorPP:list[Erp_Tablesets_VendorPPRow] = obj["VendorPP"]
      self.VenPPMFBill:list[Erp_Tablesets_VenPPMFBillRow] = obj["VenPPMFBill"]
      self.VenPPUPSEmail:list[Erp_Tablesets_VenPPUPSEmailRow] = obj["VenPPUPSEmail"]
      self.VendPPRestriction:list[Erp_Tablesets_VendPPRestrictionRow] = obj["VendPPRestriction"]
      self.VendCnt:list[Erp_Tablesets_VendCntRow] = obj["VendCnt"]
      self.VendCntAttch:list[Erp_Tablesets_VendCntAttchRow] = obj["VendCntAttch"]
      self.VenUPSEmail:list[Erp_Tablesets_VenUPSEmailRow] = obj["VenUPSEmail"]
      self.VendRemitTo:list[Erp_Tablesets_VendRemitToRow] = obj["VendRemitTo"]
      self.ExtensionTables:list[Ice_Extensions_ExtensionTableData] = obj["ExtensionTables"]
      pass

class GetAddrElementList_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.addrElementList:str = obj["parameters"]
      pass

      """  output parameters  """  

class GetByID_input:
   """ Required : 
   vendorNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetByID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendorTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendorTableset] = obj["returnObj"]
      pass

class GetByVendID_input:
   """ Required : 
   vendorID
   """  
   def __init__(self, obj):
      self.vendorID:str = obj["vendorID"]
      """  Vendor ID  """  
      pass

class GetByVendID_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorTableset] = obj["returnObj"]
      pass

class GetCodeDescList_input:
   """ Required : 
   tableName
   fieldName
   """  
   def __init__(self, obj):
      self.tableName:str = obj["tableName"]
      """  Table to search  """  
      self.fieldName:str = obj["fieldName"]
      """  Field to search  """  
      pass

class GetCodeDescList_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetDefaultFormType_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class GetDefaultFormType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetGlbVendorList_input:
   """ Required : 
   glbVendorNumList
   """  
   def __init__(self, obj):
      self.glbVendorNumList:str = obj["glbVendorNumList"]
      """  Delimited list of GlbVendorNum values  """  
      pass

class GetGlbVendorList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_GlbVendorTableset] = obj["returnObj"]
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
      self.returnObj:list[Erp_Tablesets_VendorListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetNettingSupplierList_input:
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

class GetNettingSupplierList_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorListTableset] = obj["returnObj"]
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
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
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
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewPartner_input:
   """ Required : 
   ds
   partnerNum
   partnerType
   partnerID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.partnerNum:int = obj["partnerNum"]
      self.partnerType:int = obj["partnerType"]
      self.partnerID:str = obj["partnerID"]
      pass

class GetNewPartner_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewTaxExempt_input:
   """ Required : 
   ds
   relatedToFile
   key1
   key2
   taxCode
   rateCode
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.relatedToFile:str = obj["relatedToFile"]
      self.key1:str = obj["key1"]
      self.key2:str = obj["key2"]
      self.taxCode:str = obj["taxCode"]
      self.rateCode:str = obj["rateCode"]
      pass

class GetNewTaxExempt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVenMFBill_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVenMFBill_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVenPPMFBill_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class GetNewVenPPMFBill_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVenPPUPSEmail_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class GetNewVenPPUPSEmail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVenUPSEmail_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVenUPSEmail_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendBankAttch_input:
   """ Required : 
   ds
   vendorNum
   bankID
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.bankID:str = obj["bankID"]
      pass

class GetNewVendBankAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendBank_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVendBank_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendCntAttch_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   conNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      self.conNum:int = obj["conNum"]
      pass

class GetNewVendCntAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendCntMain_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class GetNewVendCntMain_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendCnt_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class GetNewVendCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendPPRestriction_input:
   """ Required : 
   ds
   vendorNum
   purPoint
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      self.purPoint:str = obj["purPoint"]
      pass

class GetNewVendPPRestriction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendRemitTo_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVendRemitTo_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendRestriction_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVendRestriction_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendorAttch_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVendorAttch_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendorPP_input:
   """ Required : 
   ds
   vendorNum
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.vendorNum:int = obj["vendorNum"]
      pass

class GetNewVendorPP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetNewVendor_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class GetNewVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetPerConData_input:
   """ Required : 
   targetTable
   perConID
   ds
   """  
   def __init__(self, obj):
      self.targetTable:str = obj["targetTable"]
      """  The table to fill with the PerCon data.
            Use empty string to fill all contact tables.  """  
      self.perConID:int = obj["perConID"]
      """  Person Contact ID  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class GetPerConData_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class GetRows_input:
   """ Required : 
   whereClauseVendor
   whereClauseVendorAttch
   whereClauseEntityGLC
   whereClauseTaxExempt
   whereClausePartner
   whereClausePEVendWhldHist
   whereClauseVendRestriction
   whereClauseVendBank
   whereClauseVendBankAttch
   whereClauseVendCntMain
   whereClauseVenMFBill
   whereClauseVendorPP
   whereClauseVenPPMFBill
   whereClauseVenPPUPSEmail
   whereClauseVendPPRestriction
   whereClauseVendCnt
   whereClauseVendCntAttch
   whereClauseVenUPSEmail
   whereClauseVendRemitTo
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClauseVendor:str = obj["whereClauseVendor"]
      self.whereClauseVendorAttch:str = obj["whereClauseVendorAttch"]
      self.whereClauseEntityGLC:str = obj["whereClauseEntityGLC"]
      self.whereClauseTaxExempt:str = obj["whereClauseTaxExempt"]
      self.whereClausePartner:str = obj["whereClausePartner"]
      self.whereClausePEVendWhldHist:str = obj["whereClausePEVendWhldHist"]
      self.whereClauseVendRestriction:str = obj["whereClauseVendRestriction"]
      self.whereClauseVendBank:str = obj["whereClauseVendBank"]
      self.whereClauseVendBankAttch:str = obj["whereClauseVendBankAttch"]
      self.whereClauseVendCntMain:str = obj["whereClauseVendCntMain"]
      self.whereClauseVenMFBill:str = obj["whereClauseVenMFBill"]
      self.whereClauseVendorPP:str = obj["whereClauseVendorPP"]
      self.whereClauseVenPPMFBill:str = obj["whereClauseVenPPMFBill"]
      self.whereClauseVenPPUPSEmail:str = obj["whereClauseVenPPUPSEmail"]
      self.whereClauseVendPPRestriction:str = obj["whereClauseVendPPRestriction"]
      self.whereClauseVendCnt:str = obj["whereClauseVendCnt"]
      self.whereClauseVendCntAttch:str = obj["whereClauseVendCntAttch"]
      self.whereClauseVenUPSEmail:str = obj["whereClauseVenUPSEmail"]
      self.whereClauseVendRemitTo:str = obj["whereClauseVendRemitTo"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetRows_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVendCntGlobalFieldsWithPrimaryContact_input:
   """ Required : 
   VendorNum
   PurPoint
   ConNum
   """  
   def __init__(self, obj):
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact Number  """  
      pass

class GetVendCntGlobalFieldsWithPrimaryContact_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetVendorForLink_input:
   """ Required : 
   vendorID
   """  
   def __init__(self, obj):
      self.vendorID:str = obj["vendorID"]
      """  LinkVendorID field on the GlbVendor record to link  """  
      pass

class GetVendorForLink_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorTableset] = obj["returnObj"]
      pass

class GetVendorGlobalFieldsWithoutGlobalLock_input:
   """ Required : 
   VendorNum
   GlobalLock
   """  
   def __init__(self, obj):
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  If vendor is locked from receiving global updates  """  
      pass

class GetVendorGlobalFieldsWithoutGlobalLock_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetVendorListRemmitance_input:
   """ Required : 
   whereClause
   groupID
   vendorID
   vendorNums
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      """  whereClause  """  
      self.groupID:str = obj["groupID"]
      """  ID of the group that contains the vendor looking for.  """  
      self.vendorID:str = obj["vendorID"]
      """  specific VendorID to search  """  
      self.vendorNums:str = obj["vendorNums"]
      """  optional parameter to indicates a separate string of vendorNums, only used if vendorID is empty  """  
      self.pageSize:int = obj["pageSize"]
      """  Maximum number of rows to return. Leave as zero for no maximum  """  
      self.absolutePage:int = obj["absolutePage"]
      """  Page of rows to return  """  
      pass

class GetVendorListRemmitance_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVendorListSorted_input:
   """ Required : 
   whereClause
   pageSize
   absolutePage
   """  
   def __init__(self, obj):
      self.whereClause:str = obj["whereClause"]
      self.pageSize:int = obj["pageSize"]
      self.absolutePage:int = obj["absolutePage"]
      pass

class GetVendorListSorted_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorListTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.morePages:bool = obj["morePages"]
      pass

      """  output parameters  """  

class GetVendorPPForLink_input:
   """ Required : 
   vendorID
   purPoint
   """  
   def __init__(self, obj):
      self.vendorID:str = obj["vendorID"]
      """  vendorID field on the GlbVendor record  """  
      self.purPoint:str = obj["purPoint"]
      """  LinkPurPoint field on the GlbVendorPP record  """  
      pass

class GetVendorPPForLink_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorTableset] = obj["returnObj"]
      pass

class GetVendorPPGlobalFieldsWithPrimaryPP_input:
   """ Required : 
   VendorNum
   PurPoint
   """  
   def __init__(self, obj):
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      pass

class GetVendorPPGlobalFieldsWithPrimaryPP_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetvendCntGlobalFields_input:
   """ Required : 
   VendorNum
   PurPoint
   ConNum
   """  
   def __init__(self, obj):
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      self.ConNum:int = obj["ConNum"]
      """  Contact Number  """  
      pass

class GetvendCntGlobalFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetvendorGlobalFields_input:
   """ Required : 
   VendorNum
   GlobalLock
   """  
   def __init__(self, obj):
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number  """  
      self.GlobalLock:bool = obj["GlobalLock"]
      """  If vendor is locked from receiving global updates  """  
      pass

class GetvendorGlobalFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GetvendorPPGlobalFields_input:
   """ Required : 
   VendorNum
   PurPoint
   """  
   def __init__(self, obj):
      self.VendorNum:int = obj["VendorNum"]
      """  Vendor Number  """  
      self.PurPoint:str = obj["PurPoint"]
      """  Purchase Point  """  
      pass

class GetvendorPPGlobalFields_output:
   def __init__(self, obj):
      self.returnObj:str = obj["returnObj"]
      pass

class GlbVendorsExist_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.glbVendorsExist:bool = obj["glbVendorsExist"]
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

class LinkGlbVendCnt_input:
   """ Required : 
   glbCompany
   glbVendorNum
   glbPurPoint
   glbConNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbVendorPP record to link  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global VendorNum field on the GlbVendCnt record to link  """  
      self.glbPurPoint:str = obj["glbPurPoint"]
      """  Global PurPoint field on the GlbVendCnt record to link  """  
      self.glbConNum:int = obj["glbConNum"]
      """  Global Contact Number field on the GlbVendCnt record to link  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class LinkGlbVendCnt_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorTableset] = obj["returnObj"]
      pass

class LinkGlbVendorPP_input:
   """ Required : 
   glbCompany
   glbVendorNum
   glbPurPoint
   ds
   ds1
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbVendorPP record to link  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global VendorNum field on the GlbVendorPP record to link  """  
      self.glbPurPoint:str = obj["glbPurPoint"]
      """  Global PurPoint field on the GlbVendorPP record to link  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_VendorTableset] = obj["ds1"]
      pass

class LinkGlbVendorPP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds1:list[Erp_Tablesets_VendorTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class LinkGlbVendor_input:
   """ Required : 
   glbCompany
   glbVendorNum
   ds
   ds1
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbVendor record to link  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global VendorNum field on the GlbVendor record to link  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_VendorTableset] = obj["ds1"]
      pass

class LinkGlbVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      self.ds1:list[Erp_Tablesets_VendorTableset] = obj["ds1"]
      pass

      """  output parameters  """  

class ModifySearchIDs_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ModifySearchIDs_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeCode1099_input:
   """ Required : 
   ipFormType
   code1099ID
   ds
   """  
   def __init__(self, obj):
      self.ipFormType:str = obj["ipFormType"]
      """  1099 Form Type  """  
      self.code1099ID:str = obj["code1099ID"]
      """  1099 Code ID  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class OnChangeCode1099_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class OnChangeFormType_input:
   """ Required : 
   ipFormType
   ds
   """  
   def __init__(self, obj):
      self.ipFormType:str = obj["ipFormType"]
      """  1099 Form Type  """  
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class OnChangeFormType_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class PreLinkGlbVendorPP_input:
   """ Required : 
   glbCompany
   glbVendorNum
   glbPurPoint
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbVendorPP record to link  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global VendorNum field on the GlbVendorPP record to link  """  
      self.glbPurPoint:str = obj["glbPurPoint"]
      """  Global PurPoint field on the GlbVendorPP record to link  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class PreLinkGlbVendorPP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      self.askQuestion:bool = obj["askQuestion"]
      pass

      """  output parameters  """  

class PreLinkGlbVendor_input:
   """ Required : 
   glbCompany
   glbVendorNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbVendor record to link  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global VendorNum field on the GlbVendor record to link  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class PreLinkGlbVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      self.vMessage:str = obj["parameters"]
      self.askQuestion:bool = obj["askQuestion"]
      pass

      """  output parameters  """  

class RefreshGlbVendCnt_input:
   """ Required : 
   glbCompany
   glbVendorNum
   glbPurPoint
   glbConNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global vendor number  """  
      self.glbPurPoint:str = obj["glbPurPoint"]
      """  Global purchase point  """  
      self.glbConNum:int = obj["glbConNum"]
      """  Global contact number  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class RefreshGlbVendCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshGlbVendorPP_input:
   """ Required : 
   glbCompany
   glbVendorNum
   glbPurPoint
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global Vendor Number  """  
      self.glbPurPoint:str = obj["glbPurPoint"]
      """  Global purchase point  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class RefreshGlbVendorPP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class RefreshGlbVendor_input:
   """ Required : 
   glbCompany
   glbVendorNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global company  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global Vendor Number  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class RefreshGlbVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ResetPPIntl_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class ResetPPIntl_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SetUPSQVEnable_input:
   """ Required : 
   ipQVEnable
   ipUpdVenUPS
   ipUPDVenPPUPS
   ds
   """  
   def __init__(self, obj):
      self.ipQVEnable:bool = obj["ipQVEnable"]
      self.ipUpdVenUPS:bool = obj["ipUpdVenUPS"]
      self.ipUPDVenPPUPS:bool = obj["ipUPDVenPPUPS"]
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class SetUPSQVEnable_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SkipGlbVendCnt_input:
   """ Required : 
   glbCompany
   glbVendorNum
   glbPurPoint
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global Vendor Number  """  
      self.glbPurPoint:str = obj["glbPurPoint"]
      """  Global Purchase Point  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class SkipGlbVendCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SkipGlbVendorPP_input:
   """ Required : 
   glbCompany
   glbVendorNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global Vendor Number  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class SkipGlbVendorPP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SkipGlbVendor_input:
   """ Required : 
   glbCompany
   glbVendorNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbVendor record to skip  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global VendorNum field on the GlbVendor record to skip  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class SkipGlbVendor_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SkipSingleGlbVendCnt_input:
   """ Required : 
   glbLink
   ds
   """  
   def __init__(self, obj):
      self.glbLink:str = obj["glbLink"]
      """  Delimited list of global values containing global company, supplier number, purchase point, and contact num  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class SkipSingleGlbVendCnt_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class SkipSingleGlbVendorPP_input:
   """ Required : 
   glbLink
   ds
   """  
   def __init__(self, obj):
      self.glbLink:str = obj["glbLink"]
      """  Delimited list of global values containing global company, supplier number, and purchase point  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class SkipSingleGlbVendorPP_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class StorePartner_input:
   """ Required : 
   ipPartnerNum
   ipSearchID
   """  
   def __init__(self, obj):
      self.ipPartnerNum:int = obj["ipPartnerNum"]
      """  Partner Num  """  
      self.ipSearchID:str = obj["ipSearchID"]
      """  Search ID  """  
      pass

class StorePartner_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      """  boolean  """  
      pass

class TypeTINVendor_input:
   """ Required : 
   vendorNum
   TIN
   TINType
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      self.TIN:str = obj["TIN"]
      """  Taxpayer identification Number  """  
      self.TINType:str = obj["TINType"]
      """  TIN Type  """  
      pass

class TypeTINVendor_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

class UnlinkGlbVendor_input:
   """ Required : 
   glbCompany
   glbVendorNum
   ds
   """  
   def __init__(self, obj):
      self.glbCompany:str = obj["glbCompany"]
      """  Global Company field on the GlbVendor record to unlink  """  
      self.glbVendorNum:int = obj["glbVendorNum"]
      """  Global VendorNum field on the GlbVendor record to unlink  """  
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

class UnlinkGlbVendor_output:
   def __init__(self, obj):
      self.returnObj:list[Erp_Tablesets_VendorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_GlbVendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class UpdateExt_input:
   """ Required : 
   ds
   continueProcessingOnError
   rollbackParentOnChildError
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVendorTableset] = obj["ds"]
      self.continueProcessingOnError:bool = obj["continueProcessingOnError"]
      self.rollbackParentOnChildError:bool = obj["rollbackParentOnChildError"]
      pass

class UpdateExt_output:
   def __init__(self, obj):
      self.returnObj:list[Ice_BOUpdErrorTableset] = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_UpdExtVendorTableset] = obj["ds"]
      self.errorsOccurred:bool = obj["errorsOccurred"]
      pass

      """  output parameters  """  

class Update_input:
   """ Required : 
   ds
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

class Update_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      pass

      """  output parameters  """  

class ValidatePayBTFlag_input:
   """ Required : 
   ipPayBTFlag
   ipValVen
   ipValVenPP
   ipVendorNum
   ipPurPoint
   """  
   def __init__(self, obj):
      self.ipPayBTFlag:str = obj["ipPayBTFlag"]
      self.ipValVen:bool = obj["ipValVen"]
      self.ipValVenPP:bool = obj["ipValVenPP"]
      self.ipVendorNum:int = obj["ipVendorNum"]
      self.ipPurPoint:str = obj["ipPurPoint"]
      pass

class ValidatePayBTFlag_output:
   def __init__(self, obj):
      pass

class ValidateTaxID_input:
   """ Required : 
   ds
   manualValidation
   hmrcFraudPrevHeader
   """  
   def __init__(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.manualValidation:bool = obj["manualValidation"]
      self.hmrcFraudPrevHeader:str = obj["hmrcFraudPrevHeader"]
      pass

class ValidateTaxID_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.ds:list[Erp_Tablesets_VendorTableset] = obj["ds"]
      self.opMessage:str = obj["parameters"]
      pass

      """  output parameters  """  

class VendorBankExists_input:
   """ Required : 
   vendorNum
   """  
   def __init__(self, obj):
      self.vendorNum:int = obj["vendorNum"]
      """  Vendor Number  """  
      pass

class VendorBankExists_output:
   def __init__(self, obj):
      pass

   def parameters(self, obj):
      self.vendBankExists:bool = obj["vendBankExists"]
      pass

      """  output parameters  """  

class getPrimaryBankID_input:
   """ Required : 
   vendorID
   """  
   def __init__(self, obj):
      self.vendorID:str = obj["vendorID"]
      """  Vendor ID  """  
      pass

class getPrimaryBankID_output:
   def __init__(self, obj):
      self.returnObj:bool = obj["returnObj"]
      pass

   def parameters(self, obj):
      self.bankID:str = obj["parameters"]
      pass

      """  output parameters  """  

